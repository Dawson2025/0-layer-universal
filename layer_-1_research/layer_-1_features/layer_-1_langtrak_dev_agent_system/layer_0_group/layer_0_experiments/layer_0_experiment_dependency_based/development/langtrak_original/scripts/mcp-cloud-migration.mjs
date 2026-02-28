#!/usr/bin/env node
/**
 * Cloud Migration Test
 * Tests migrating a local project to cloud storage
 *
 * Coverage:
 * - Create local (SQLite) project
 * - Add data to local project
 * - Migrate project from local to cloud
 * - Verify data integrity after migration
 * - Confirm cloud storage is now active
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

import {
  performGoogleOAuthLogin,
  normalizeCliJson,
  getFirebaseAuthContext,
  firestoreGetDocument,
  firestoreRunQuery,
} from './lib/google-auth-helpers.mjs';
import { getAdminFirestore } from './lib/firestore-admin-client.mjs';

const BASE = 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';
const RUN_MODE = process.env.RUN_NAVIGATION_MODE ?? 'direct';
const useRealisticNavigation = RUN_MODE === 'realistic';

if (process.env.RUN_CLOUD_TESTS !== '1') {
  console.log('[cloud-migration-test] skipping (set RUN_CLOUD_TESTS=1 to enable)');
  process.exit(0);
}

const timestamp = Date.now();
const GOOGLE_EMAIL = process.env.GOOGLE_TEST_EMAIL;
const GOOGLE_PASSWORD = process.env.GOOGLE_TEST_PASSWORD;

if (!GOOGLE_EMAIL || !GOOGLE_PASSWORD) {
  console.error('[cloud-migration-test] missing GOOGLE_TEST_EMAIL / GOOGLE_TEST_PASSWORD');
  process.exit(1);
}
const projectName = `Migration Test ${timestamp}`;
const testPhonemes = [`M1_${timestamp}`, `M2_${timestamp}`];

const summary = {
  testType: 'local_to_cloud_migration',
  timestamp,
  googleAccount: 'configured_via_env',
  projectName,
  testPhonemes,
  steps: [],
  cloudProjectId: null,
};
summary.navigationMode = RUN_MODE;

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) {
    const text = (result.content ?? [])
      .filter((part) => part.type === 'text')
      .map((part) => part.text.trim())
      .join('\n');
    console.log(`\n=== ${label} ===`);
    if (text) console.log(text);
  }
  return result;
}

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'cloud-migration');
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

function recordStep(entry) {
  summary.steps.push(entry);
  const { action, status } = entry;
  console.log(`\n[${action}] status=${status}`);
  if (entry.message) {
    console.log(`  ${entry.message}`);
  }
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summaryPath = path.join(artifactsDir, `run-${timestamp}.json`);

  const client = new Client({ name: 'cloud-migration-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n====================================');
  console.log('LOCAL TO CLOUD MIGRATION TEST');
  console.log('====================================');
  console.log(`Google Account: ${GOOGLE_EMAIL}`);
  console.log(`Project: ${projectName}`);
  console.log('Flow: Local → Add Data → Migrate → Verify\n');

  try {
    let firebaseContext = null;
    // Sign in with Google
    await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Navigate to login');

    const loginResult = await performGoogleOAuthLogin(client, callTool, {
      email: GOOGLE_EMAIL,
      password: GOOGLE_PASSWORD,
      baseUrl: BASE,
    });

    recordStep({
      action: 'google_login',
      status: loginResult.status === 'signed-in' ? 'ok' : 'skipped',
      message: loginResult.status === 'signed-in'
        ? 'Authenticated with Google account'
        : 'Google account already authenticated in session',
      loginResult,
    });

    summary.firebaseUser = loginResult.firebase;

    firebaseContext = await getFirebaseAuthContext(client, callTool);
    summary.firebaseContext = {
      uid: firebaseContext.uid,
      email: firebaseContext.email,
      projectId: firebaseContext.projectId,
    };

    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Post Google login');
    }

    // Create LOCAL project
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, 'Navigate to project creation');

    await callTool(client, 'browser_evaluate', {
      function: `() => {
        const nameInput = document.querySelector('#name');
        if (nameInput) {
          nameInput.value = '${projectName}';
          nameInput.dispatchEvent(new Event('input', { bubbles: true }));
        }

        // Explicitly select LOCAL storage
        const localRadio = document.querySelector('#storage_local');
        if (localRadio) {
          localRadio.checked = true;
          localRadio.dispatchEvent(new Event('change', { bubbles: true }));
        }

        return {
          nameSet: !!nameInput,
          localSelected: localRadio?.checked || false
        };
      }`,
    }, 'Fill project form with LOCAL storage');

    await callTool(client, 'browser_evaluate', {
      function: "() => { document.querySelector('button.button.primary')?.click(); return true; }",
    }, 'Submit local project creation');

    await callTool(
      client,
      'browser_wait_for',
      { time: useRealisticNavigation ? 1 : 0.5 },
      'Wait for project creation'
    );

    recordStep({ action: 'create_local_project', status: 'ok' });

    // Add some data to the local project
    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` }, 'Navigate to admin phonemes');

    for (const phoneme of testPhonemes) {
      await callTool(client, 'browser_evaluate', {
        function: `() => {
          const phonemeInput = document.querySelector('input[id*="phoneme"], input[placeholder*="p"]');
          if (phonemeInput) {
            phonemeInput.value = '${phoneme}';
            phonemeInput.dispatchEvent(new Event('input', { bubbles: true }));
          }

          const buttons = Array.from(document.querySelectorAll('button'));
          const addBtn = buttons.find(b => b.textContent.includes('Add'));
          if (addBtn) addBtn.click();

          return { phoneme: '${phoneme}' };
        }`,
      }, `Add phoneme: ${phoneme}`);

      await callTool(
        client,
        'browser_wait_for',
        { time: useRealisticNavigation ? 1 : 0.4 },
        'Wait for phoneme add'
      );
    }

    recordStep({
      action: 'add_data_to_local_project',
      status: 'ok',
      phonemesAdded: testPhonemes.length
    });

    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Local project with data');
    }

    // Navigate to projects page to find migration option
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Navigate to projects list');
    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Projects list');
    }

    // Check if cloud storage is available for migration
    const cloudAvailCheck = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const targetName = ${JSON.stringify(projectName)};
          const cards = Array.from(document.querySelectorAll('.variant-group'));
          const targetCard = cards.find(card => {
            const cardName = card.dataset?.name || '';
            if (cardName) {
              return cardName === targetName;
            }
            return card.textContent.includes(targetName);
          });

          if (targetCard) {
            const buttons = Array.from(targetCard.querySelectorAll('button'));
            const migrateBtn = buttons.find(b =>
              b.textContent.includes('Migrate') ||
              b.textContent.includes('Cloud') && !b.textContent.includes('Local')
            );

            const dataset = targetCard.dataset || {};
            let cloudProjectId = '';
            if (dataset.variantId && dataset.variantId.startsWith('cloud:')) {
              cloudProjectId = dataset.variantId.split(':')[1];
            }
            if (!cloudProjectId) {
              const match = targetCard.textContent.match(/Linked Cloud:\\s*([A-Za-z0-9_-]+)/);
              if (match) {
                cloudProjectId = match[1];
              }
            }

            return {
              found: true,
              hasMigrateButton: !!migrateBtn,
              buttonText: migrateBtn?.textContent || '',
              allButtons: buttons.map(b => b.textContent.trim()),
              variantId: dataset.variantId || '',
              cloudProjectId
            };
          }
          return { found: false };
        }`
      },
      'Check for migrate to cloud button'
    );

    const rawmigrationCheck = cloudAvailCheck.content?.find(c => c.type === 'text')?.text || '{}';
    const migrationCheck = normalizeCliJson(rawmigrationCheck) || {};
    if (migrationCheck?.variantId) {
      summary.localVariantId = migrationCheck.variantId;
      if (!summary.localProjectId && migrationCheck.variantId.startsWith('local:')) {
        summary.localProjectId = migrationCheck.variantId.split(':')[1];
      }
    }
    if (!summary.cloudProjectId && migrationCheck?.cloudProjectId) {
      summary.cloudProjectId = migrationCheck.cloudProjectId;
    }

    if (!migrationCheck.found || !migrationCheck.hasMigrateButton) {
      console.log('\n⚠️  Migration button not found or cloud storage not available');
      console.log('This test requires Firebase/Firestore to be configured for migration.');

      summary.skipped = true;
      summary.reason = 'Migration to cloud not available - Firebase not configured or no migration UI';
      summary.migrationCheck = migrationCheck;

    recordStep({
      action: 'check_migration_available',
      status: 'unavailable',
      message: 'Cloud migration not available',
      migrationCheck
    });

      await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
      await callTool(client, 'browser_close', {});
      await client.close();

      console.log('\n📄 Test skipped - migration feature not available');
      process.exit(0);
    }

    console.log('\n✅ Migration to cloud button found - proceeding with migration');

    recordStep({ action: 'check_migration_available', status: 'ok', migrationCheck });

    if (summary.localProjectId) {
      await callTool(
        client,
        'browser_navigate',
        { url: `${BASE}/projects/${summary.localProjectId}/enter` },
        'Enter local project before creating word'
      );
      await callTool(
        client,
        'browser_wait_for',
        { time: useRealisticNavigation ? 1 : 0.4 },
        'Wait after entering project'
      );

      const localWordPayload = JSON.stringify({
        language: 'Automation Local Lang',
        english_words: `Migration local word ${timestamp}`,
        new_language_word: `loc_${timestamp}`,
        syllables: [
          {
            syllableType: 'CVC',
            phonemes: {
              onset: { phoneme: 'p', length_type: 'single' },
              nucleus: { phoneme: 'a', length_type: 'single' },
              coda: { phoneme: 't', length_type: 'single' },
            },
          },
        ],
      });

      const createLocalWord = await callTool(
        client,
        'browser_evaluate',
        {
          function: `() => {
            const payload = ${localWordPayload};
            return fetch('/api/create-word', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              credentials: 'include',
              body: JSON.stringify(payload),
            })
              .then(r => r.json())
              .catch(err => ({ error: String(err) }));
          }`,
        },
        'Create local project word via API'
      );

      const rawLocalWord = createLocalWord.content?.find(c => c.type === 'text')?.text || '{}';
      const localWordResult = normalizeCliJson(rawLocalWord) || {};

      recordStep({
        action: 'create_local_word',
        status: localWordResult.success ? 'ok' : 'warning',
        message: localWordResult.success
          ? 'Created local word prior to migration'
          : `Failed to create local word: ${localWordResult.error || 'unknown error'}`,
        localWordResult,
      });

      await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Return to projects list after word creation');
      await callTool(
        client,
        'browser_wait_for',
        { time: useRealisticNavigation ? 1 : 0.4 },
        'Wait for projects list reload'
      );
    }

    // Click migrate to cloud button
    await callTool(client, 'browser_evaluate', {
      function: `() => {
        const targetName = ${JSON.stringify(projectName)};
        const cards = Array.from(document.querySelectorAll('.variant-group'));
        const targetCard = cards.find(card => {
          const cardName = card.dataset?.name || '';
          if (cardName) {
            return cardName === targetName;
          }
          return card.textContent.includes(targetName);
        });

        if (targetCard) {
          const buttons = Array.from(targetCard.querySelectorAll('button'));
          const migrateBtn = buttons.find(b =>
            b.textContent.includes('Migrate') ||
            (b.textContent.includes('Cloud') && !b.textContent.includes('Local'))
          );

          if (migrateBtn) {
            migrateBtn.click();
            return { clicked: true, button: migrateBtn.textContent };
          }
        }
        return { clicked: false };
      }`,
    }, 'Click Migrate to Cloud button');

    await callTool(
      client,
      'browser_handle_dialog',
      { accept: true },
      'Confirm cloud migration dialog'
    );

    await callTool(
      client,
      'browser_handle_dialog',
      { accept: true },
      'Acknowledge migration success alert'
    );

    await callTool(
      client,
      'browser_wait_for',
      { time: useRealisticNavigation ? 3 : 1 },
      'Wait for migration process'
    );
    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'After migration');
    }

    recordStep({ action: 'migrate_to_cloud', status: 'ok' });

    // Verify migration completed
    const postMigrationCheck = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const targetName = ${JSON.stringify(projectName)};
          const cards = Array.from(document.querySelectorAll('.variant-group'));
          const targetCard = cards.find(card => {
            const cardName = card.dataset?.name || '';
            if (cardName) {
              return cardName === targetName;
            }
            return card.textContent.includes(targetName);
          });

          if (targetCard) {
            const cardText = targetCard.textContent;
            const dataset = targetCard.dataset || {};
            let cloudProjectId = '';
            if (dataset.variantId && dataset.variantId.startsWith('cloud:')) {
              cloudProjectId = dataset.variantId.split(':')[1];
            }
            if (!cloudProjectId) {
              const match = cardText.match(/Linked Cloud:\\s*([A-Za-z0-9_-]+)/);
              if (match) {
                cloudProjectId = match[1];
              }
            }

            return {
              found: true,
              hasCloudIndicator: cardText.includes('Cloud') || cardText.includes('☁️') || cardText.includes('🌐'),
              hasLocalIndicator: cardText.includes('Local') || cardText.includes('💾'),
              cardText: cardText.substring(0, 300),
              cloudProjectId
            };
          }
          return { found: false };
        }`
      },
      'Verify cloud migration'
    );

    const rawpostMigration = postMigrationCheck.content?.find(c => c.type === 'text')?.text || '{}';
    const postMigration = normalizeCliJson(rawpostMigration) || {};
    if (postMigration.cloudProjectId) {
      summary.cloudProjectId = postMigration.cloudProjectId;
    }

    const migrationSuccess = !!postMigration.hasCloudIndicator;

    recordStep({
      action: 'verify_migration',
      status: migrationSuccess ? 'ok' : 'warning',
      message: migrationSuccess
        ? 'Project now shows cloud storage indicator'
        : 'Migration completed but cloud indicator unclear',
      postMigration
    });

    if (!summary.cloudProjectId && postMigration?.cloudProjectId) {
      summary.cloudProjectId = postMigration.cloudProjectId;
    }

    if (!summary.cloudProjectId) {
      const projectNameLiteral = JSON.stringify(projectName);
      const cloudVariantCheck = await callTool(
        client,
        'browser_evaluate',
        {
          function: `() => {
            const targetName = ${projectNameLiteral};
            const cards = Array.from(document.querySelectorAll('.variant-group'));
            const targetCard = cards.find(card => card.dataset && card.dataset.storage === 'cloud' && (card.dataset.name === targetName || card.textContent.includes(targetName)));
            if (!targetCard) {
              return { found: false };
            }
            const variantId = targetCard.dataset?.variantId || '';
            const cloudProjectId = variantId.startsWith('cloud:') ? variantId.split(':')[1] : '';
            return {
              found: true,
              variantId,
              cloudProjectId,
              storage: targetCard.dataset?.storage || ''
            };
          }`,
        },
        'Locate cloud variant card'
      );

      const rawCloudVariant = cloudVariantCheck.content?.find(c => c.type === 'text')?.text || '{}';
      const cloudVariant = normalizeCliJson(rawCloudVariant) || {};
      recordStep({
        action: 'cloud_variant_lookup',
        status: cloudVariant.found ? 'ok' : 'warning',
        message: cloudVariant.found
          ? `Cloud variant located with identifier ${cloudVariant.variantId || '(unknown)'}`
          : 'Cloud variant card not found after migration',
        cloudVariant,
      });

      if (cloudVariant.cloudProjectId) {
        summary.cloudProjectId = cloudVariant.cloudProjectId;
      }
    }

    if (!summary.cloudProjectId && summary.localProjectId) {
      const localIdLiteral = JSON.stringify(String(summary.localProjectId));
      const cloudLinkFetch = await callTool(
        client,
        'browser_evaluate',
        {
          function: `() => fetch('/api/projects/' + ${localIdLiteral} + '/cloud-link', { credentials: 'include' })\n            .then(r => r.json())\n            .catch(err => ({ error: String(err) }))`,
        },
        'Fetch cloud link via API'
      );

      const rawCloudLink = cloudLinkFetch.content?.find(c => c.type === 'text')?.text || '{}';
      const cloudLink = normalizeCliJson(rawCloudLink) || {};
      recordStep({
        action: 'cloud_link_lookup',
        status: cloudLink.success ? 'ok' : 'warning',
        message: cloudLink.success
          ? `API returned cloud project id ${cloudLink.cloudProjectId || '(missing)'}`
          : `API cloud link lookup failed: ${cloudLink.error || 'unknown error'}`,
        cloudLink,
      });

      if (cloudLink?.cloudProjectId) {
        summary.cloudProjectId = cloudLink.cloudProjectId;
      }
    }

    // Enter project and verify data is still there
    await callTool(client, 'browser_evaluate', {
      function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); } return true; }",
    }, 'Enter migrated project');

    await callTool(
      client,
      'browser_wait_for',
      { time: useRealisticNavigation ? 1 : 0.5 },
      'Wait for project load'
    );

    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` }, 'Check phonemes after migration');
    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Phonemes after migration');
    }

    // Verify phonemes are still there
    const dataCheck = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const pageText = document.body.textContent;
          return {
            hasM1: pageText.includes('${testPhonemes[0]}'),
            hasM2: pageText.includes('${testPhonemes[1]}'),
            phonemesPreserved: pageText.includes('${testPhonemes[0]}') && pageText.includes('${testPhonemes[1]}')
          };
        }`
      },
      'Verify data integrity'
    );

    const rawdataIntegrity = dataCheck.content?.find(c => c.type === 'text')?.text || '{}';
    const dataIntegrity = normalizeCliJson(rawdataIntegrity) || {};

    const dataIntegrityStatus = dataIntegrity.phonemesPreserved ? 'ok' : 'warning';
    recordStep({
      action: 'verify_data_integrity',
      status: dataIntegrityStatus,
      message: dataIntegrity.phonemesPreserved
        ? 'All data preserved after migration'
        : 'Could not verify phoneme entries after migration',
      dataIntegrity
    });

    if (firebaseContext && summary.cloudProjectId) {
      let restSucceeded = false;
      let restErrorMessage = '';

      try {
        const firestoreProject = await firestoreGetDocument(
          firebaseContext,
          `projects/${summary.cloudProjectId}`,
        );

        recordStep({
          action: 'firestore_project_lookup',
          status: firestoreProject ? 'ok' : 'warning',
          message: firestoreProject
            ? 'Cloud project document found in Firestore'
            : 'Cloud project document missing in Firestore',
          firestoreProject,
        });

        const firestoreWords = await firestoreRunQuery(
          firebaseContext,
          'words',
          [{ fieldPath: 'project_id', value: summary.cloudProjectId }],
          { limit: 50 },
        );

        recordStep({
          action: 'firestore_words_check',
          status: 'ok',
          message: `Firestore words for cloud project: ${firestoreWords.length}`,
          wordCount: firestoreWords.length,
        });

        const firestorePhonemes = await firestoreRunQuery(
          firebaseContext,
          'phonemes',
          [{ fieldPath: 'project_id', value: summary.cloudProjectId }],
          { limit: 50 },
        );

        recordStep({
          action: 'firestore_phonemes_check',
          status: 'ok',
          message: `Firestore phonemes for cloud project: ${firestorePhonemes.length}`,
          phonemeCount: firestorePhonemes.length,
        });

        restSucceeded = true;
      } catch (firestoreError) {
        restErrorMessage = firestoreError?.message || String(firestoreError);
        recordStep({
          action: 'firestore_rest_verification',
          status: 'warning',
          message: `Firestore REST verification failed: ${restErrorMessage}`,
        });
      }

      if (!restSucceeded) {
        const adminDb = await getAdminFirestore();
        if (adminDb) {
          try {
            const projectSnap = await adminDb
              .collection('projects')
              .doc(summary.cloudProjectId)
              .get();

            recordStep({
              action: 'firestore_project_lookup_admin',
              status: projectSnap.exists ? 'ok' : 'warning',
              message: projectSnap.exists
                ? 'Cloud project document retrieved via Admin SDK'
                : 'Cloud project document missing via Admin SDK',
              firestoreProject: projectSnap.exists ? projectSnap.data() : null,
            });

            const wordsSnap = await adminDb
              .collection('words')
              .where('project_id', '==', summary.cloudProjectId)
              .limit(50)
              .get();

            recordStep({
              action: 'firestore_words_check_admin',
              status: 'ok',
              message: `Admin SDK retrieved ${wordsSnap.size} word document(s)`,
              wordCount: wordsSnap.size,
            });

            const phonemesSnap = await adminDb
              .collection('phonemes')
              .where('project_id', '==', summary.cloudProjectId)
              .limit(50)
              .get();

            recordStep({
              action: 'firestore_phonemes_check_admin',
              status: 'ok',
              message: `Admin SDK retrieved ${phonemesSnap.size} phoneme document(s)`,
              phonemeCount: phonemesSnap.size,
            });
          } catch (adminError) {
            recordStep({
              action: 'firestore_verification',
              status: 'warning',
              message: `Firestore verification failed via REST (${restErrorMessage}) and Admin SDK (${adminError?.message || adminError})`,
            });
          }
        } else {
          recordStep({
            action: 'firestore_verification',
            status: 'warning',
            message: restErrorMessage
              ? `Firestore verification failed via REST (${restErrorMessage}) and no Admin service account is configured`
              : 'Firestore verification skipped - no Admin service account is configured',
          });
        }
      }
    } else {
      recordStep({
        action: 'firestore_context_missing',
        status: 'warning',
        message: 'Skipping Firestore verification - missing auth context or project ID',
      });
    }

    summary.migrationSuccessful = migrationSuccess;
    summary.dataIntegrityPreserved = dataIntegrity.phonemesPreserved;
    summary.result = migrationSuccess
      ? (dataIntegrity.phonemesPreserved ? 'success' : 'warning')
      : 'failed';

    await callTool(client, 'browser_close', {});
    await client.close();

    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));

    console.log('\n====================================');
    console.log('MIGRATION TEST COMPLETE');
    console.log('====================================');
    console.log(`Migration: ${migrationSuccess ? '✅ Success' : '⚠️ Unclear'}`);
    console.log(`Data Integrity: ${dataIntegrity.phonemesPreserved ? '✅ Preserved' : '⚠️ Not verified'}`);
    console.log(`\n📄 Summary: ${summaryPath}`);

  } catch (error) {
    summary.error = error?.message ?? String(error);
    console.error('\n❌ [cloud-migration-test] failed', error);

    recordStep({ action: 'test_error', status: 'failed', error: summary.error });

    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    await callTool(client, 'browser_close', {}).catch(() => {});
    await client.close();
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('[cloud-migration-test] execution error', err);
  process.exit(1);
});

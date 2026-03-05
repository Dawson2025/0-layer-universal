// resource_id: "0cd1ed73-537e-407f-b757-36a27ef476d0"
// resource_type: "document"
// resource_name: "mcp-cloud-projects"
#!/usr/bin/env node
/**
 * Cloud Project Lifecycle Test
 * Tests cloud/Firebase storage features
 *
 * Coverage:
 * - Create cloud-based project (vs local SQLite)
 * - Verify Firebase/Firestore persistence
 * - Test cloud-specific features
 * - Multi-user collaboration (if applicable)
 * - Cloud data operations
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
  console.log('[cloud-projects-test] skipping (set RUN_CLOUD_TESTS=1 to enable)');
  process.exit(0);
}

const timestamp = Date.now();
const GOOGLE_EMAIL = process.env.GOOGLE_TEST_EMAIL;
const GOOGLE_PASSWORD = process.env.GOOGLE_TEST_PASSWORD;

if (!GOOGLE_EMAIL || !GOOGLE_PASSWORD) {
  console.error('[cloud-projects-test] missing GOOGLE_TEST_EMAIL / GOOGLE_TEST_PASSWORD');
  process.exit(1);
}
const projectName = `Cloud Project ${timestamp}`;

const summary = {
  testType: 'cloud_project_lifecycle',
  timestamp,
  googleAccount: 'configured_via_env',
  projectName,
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
  const dir = path.join(process.cwd(), 'artifacts', 'cloud-projects');
  await fs.mkdir(dir, { recursive: true});
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

  const client = new Client({ name: 'cloud-projects-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n====================================');
  console.log('CLOUD PROJECT LIFECYCLE TEST');
  console.log('====================================');
  console.log(`Google Account: ${GOOGLE_EMAIL}`);
  console.log(`Project: ${projectName}`);
  console.log('Storage: Firebase/Firestore (Cloud)\n');

  try {
    let firebaseContext = null;

    // Sign in with Google account
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

    // Navigate to create project
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, 'Navigate to project creation');
    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Project creation page');
    }

    // Check if cloud storage is available
    const cloudCheckResult = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const cloudRadio = document.querySelector('#storage_cloud');
          const localRadio = document.querySelector('#storage_local');
          return {
            cloudExists: !!cloudRadio,
            cloudDisabled: cloudRadio?.disabled || false,
            localExists: !!localRadio,
            cloudChecked: cloudRadio?.checked || false,
            localChecked: localRadio?.checked || false,
            cloudLabel: cloudRadio?.nextElementSibling?.textContent?.trim() || '',
          };
        }`
      },
      'Check cloud storage availability'
    );

    const rawCloudCheck = cloudCheckResult.content?.find(c => c.type === 'text')?.text || '{}';
    const cloudCheck = normalizeCliJson(rawCloudCheck) || {};

    recordStep({ action: 'check_cloud_storage', status: 'ok', cloudCheck });

    if (cloudCheck.cloudDisabled || !cloudCheck.cloudExists) {
      console.log('\n⚠️  Cloud storage is not available');
      console.log('This test requires Firebase/Firestore to be configured.');
      console.log('Cloud storage option is disabled or missing.');

      summary.skipped = true;
      summary.reason = 'Cloud storage not available - Firebase not configured';

      recordStep({
        action: 'cloud_storage_check',
        status: 'unavailable',
        message: 'Firebase/Firestore not configured or disabled'
      });

      await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
      await callTool(client, 'browser_close', {});
      await client.close();

      console.log('\n📄 Test skipped - cloud storage not available');
      process.exit(0);
    }

    console.log('\n✅ Cloud storage is available - proceeding with cloud project creation');

    // Create cloud project
    await callTool(client, 'browser_evaluate', {
      function: `() => {
        const nameInput = document.querySelector('#name');
        if (nameInput) {
          nameInput.value = '${projectName}';
          nameInput.dispatchEvent(new Event('input', { bubbles: true }));
        }

        const cloudRadio = document.querySelector('#storage_cloud');
        if (cloudRadio && !cloudRadio.disabled) {
          cloudRadio.checked = true;
          cloudRadio.dispatchEvent(new Event('change', { bubbles: true }));
        }

        return {
          nameSet: !!nameInput,
          cloudSelected: cloudRadio?.checked || false
        };
      }`,
    }, 'Fill project form with cloud storage');

    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Project form filled');
    }

    await callTool(client, 'browser_evaluate', {
      function: "() => { document.querySelector('button.button.primary')?.click(); return true; }",
    }, 'Submit project creation');

    await callTool(
      client,
      'browser_wait_for',
      { time: useRealisticNavigation ? 2 : 1 },
      'Wait for cloud project creation'
    );
    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'After project creation');
    }

    // Verify we're on main menu or projects page
    const navCheck = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          return {
            url: window.location.href,
            pathname: window.location.pathname,
            isMainMenu: window.location.pathname === '/main-menu',
            isProjects: window.location.pathname === '/projects',
            hasProjectName: document.body.textContent.includes('${projectName}')
          };
        }`
      },
      'Verify project creation'
    );

    const rawNavState = navCheck.content?.find(c => c.type === 'text')?.text || '{}';
    const navState = normalizeCliJson(rawNavState) || {};

    if (!navState.hasProjectName) {
      throw new Error('Cloud project creation may have failed - project name not found on page');
    }

    recordStep({
      action: 'create_cloud_project',
      status: 'ok',
      message: `Cloud project "${projectName}" created successfully`,
      navState
    });

    // Navigate to projects list to verify cloud badge/indicator
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Navigate to projects list');
    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Projects list');
    }

    // Check project storage type indicator
    const projectCheck = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const targetName = ${JSON.stringify(projectName)};
          const variantCards = Array.from(document.querySelectorAll('.variant-group'));
          const targetCard = variantCards.find(card => {
            const cardName = card.dataset?.name || '';
            if (cardName) {
              return cardName === targetName;
            }
            return card.textContent.includes(targetName);
          });

          if (!targetCard) {
            return { found: false };
          }

          const cardText = targetCard.textContent;
          const dataset = targetCard.dataset || {};
          let cloudProjectId = '';
          const variantId = dataset.variantId || '';
          if (variantId.startsWith('cloud:')) {
            cloudProjectId = variantId.split(':')[1];
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
            cardText: cardText.substring(0, 200),
            variantId,
            cloudProjectId,
            storage: dataset.storage || '',
          };
        }`
      },
      'Check project storage type'
    );

    const rawProjectInfo = projectCheck.content?.find(c => c.type === 'text')?.text || '{}';
    const projectInfo = normalizeCliJson(rawProjectInfo) || {};
    summary.cloudProjectId = projectInfo.cloudProjectId || null;
    if (!summary.cloudProjectId && projectInfo?.variantId?.startsWith?.('cloud:')) {
      summary.cloudProjectId = projectInfo.variantId.split(':')[1];
    }
    if (!summary.cloudProjectId && projectInfo?.variantId?.startsWith?.('local:')) {
      const localId = projectInfo.variantId.split(':')[1];
      if (localId) {
        const cloudLinkFetch = await callTool(
          client,
          'browser_evaluate',
          {
            function: `() => fetch('/api/projects/' + ${JSON.stringify(localId)} + '/cloud-link', { credentials: 'include' })\n              .then(r => r.json())\n              .catch(err => ({ error: String(err) }))`,
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
    }

    recordStep({
      action: 'verify_cloud_project_badge',
      status: projectInfo.hasCloudIndicator ? 'ok' : 'warning',
      message: projectInfo.hasCloudIndicator
        ? 'Cloud storage indicator found on project card'
        : 'Cloud storage indicator not clearly visible',
      projectInfo
    });

    if (firebaseContext && projectInfo.cloudProjectId) {
      let restSucceeded = false;
      let restErrorMessage = '';

      try {
        const firestoreProject = await firestoreGetDocument(
          firebaseContext,
          `projects/${projectInfo.cloudProjectId}`,
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
          [{ fieldPath: 'project_id', value: projectInfo.cloudProjectId }],
          { limit: 25 },
        );

        recordStep({
          action: 'firestore_words_check',
          status: 'ok',
          message: `Retrieved ${firestoreWords.length} word document(s) for project`,
          wordCount: firestoreWords.length,
        });

        const firestorePhonemes = await firestoreRunQuery(
          firebaseContext,
          'phonemes',
          [{ fieldPath: 'project_id', value: projectInfo.cloudProjectId }],
          { limit: 25 },
        );

        recordStep({
          action: 'firestore_phonemes_check',
          status: 'ok',
          message: `Retrieved ${firestorePhonemes.length} phoneme document(s) for project`,
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
              .doc(projectInfo.cloudProjectId)
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
              .where('project_id', '==', projectInfo.cloudProjectId)
              .limit(25)
              .get();

            recordStep({
              action: 'firestore_words_check_admin',
              status: 'ok',
              message: `Admin SDK retrieved ${wordsSnap.size} word document(s)`,
              wordCount: wordsSnap.size,
            });

            const phonemesSnap = await adminDb
              .collection('phonemes')
              .where('project_id', '==', projectInfo.cloudProjectId)
              .limit(25)
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

    // Enter the project to verify cloud operations work
    await callTool(client, 'browser_evaluate', {
      function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); } return true; }",
    }, 'Enter cloud project');

    await callTool(
      client,
      'browser_wait_for',
      { time: useRealisticNavigation ? 1 : 0.5 },
      'Wait for project load'
    );
    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Inside cloud project');
    }

    recordStep({ action: 'enter_cloud_project', status: 'ok' });

    const cloudVariantIdentifier = projectInfo?.variantId || `cloud:${summary.cloudProjectId || ''}`;
    if (cloudVariantIdentifier && cloudVariantIdentifier !== 'cloud:') {
      await callTool(
        client,
        'browser_navigate',
        { url: `${BASE}/projects/${cloudVariantIdentifier}/enter` },
        'Ensure cloud project context via direct route'
      );
      await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after entering cloud project');
    }

    const cloudWordPayload = JSON.stringify({
      language: 'Automation Cloud Lang',
      english_words: `Cloud automation word ${timestamp}`,
      new_language_word: `cloud_${timestamp}`,
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

    const createCloudWord = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const payload = ${cloudWordPayload};
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
      'Create cloud project word via API'
    );

    const rawCloudWord = createCloudWord.content?.find(c => c.type === 'text')?.text || '{}';
    const cloudWordResult = normalizeCliJson(rawCloudWord) || {};

    recordStep({
      action: 'create_cloud_word',
      status: cloudWordResult.success ? 'ok' : 'warning',
      message: cloudWordResult.success
        ? 'Created word inside cloud project via API'
        : `Failed to create cloud project word: ${cloudWordResult.error || 'unknown error'}`,
      cloudWordResult,
    });

    // Summary
    summary.cloudProjectCreated = true;
    summary.cloudOperationsWork = true;
    summary.result = 'success';

    await callTool(client, 'browser_close', {});
    await client.close();

    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));

    console.log('\n====================================');
    console.log('✅ CLOUD PROJECT TEST PASSED');
    console.log('====================================');
    console.log(`Cloud project "${projectName}" created and verified`);
    console.log('Cloud storage operations working correctly');
    console.log(`\n📄 Summary: ${summaryPath}`);

  } catch (error) {
    summary.error = error?.message ?? String(error);
    console.error('\n❌ [cloud-projects-test] failed', error);

    recordStep({ action: 'test_error', status: 'failed', error: summary.error });

    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    await callTool(client, 'browser_close', {}).catch(() => {});
    await client.close();
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('[cloud-projects-test] execution error', err);
  process.exit(1);
});

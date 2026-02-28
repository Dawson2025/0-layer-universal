#!/usr/bin/env node
/**
 * USER-REALISTIC Storage Resilience Test (US-057-059)
 *
 * Tests storage options using realistic UI navigation:
 * - Creates projects with both local and cloud storage via UI
 * - Navigates through project creation form using UI buttons
 * - Validates storage options are accessible through normal navigation
 * - Tests Firebase availability detection
 *
 * NOTE: This test will expose navigation gaps - if storage options
 * are only accessible via URL changes, that's a UX bug!
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

import {
  switchTab,
  fillField,
  clickButtonWithText,
  clickElement,
  waitForElement,
  navigateFromDashboard,
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `storage${timestamp}`,
  email: `storage${timestamp}@example.com`,
  password: 'Test123!',
};

function resultText(result) {
  return (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text)
    .join('\n');
}

function normalizeCliJson(raw) {
  if (!raw) return null;
  let text = raw.trim();
  text = text.replace(/^### Result\s*/i, '').trim();
  if (text.startsWith('```')) {
    text = text.replace(/^```(?:json)?/i, '').replace(/```$/i, '').trim();
  }
  const nextSection = text.indexOf('\n###');
  if (nextSection !== -1) {
    text = text.slice(0, nextSection).trim();
  }

  const tryParse = (candidate) => {
    if (!candidate) return null;
    try {
      return JSON.parse(candidate);
    } catch {
      return null;
    }
  };

  let parsed = tryParse(text);

  if (parsed === null && (text.includes('{') || text.includes('['))) {
    const braceIdx = text.indexOf('{');
    const bracketIdx = text.indexOf('[');
    const startIdx = (() => {
      if (braceIdx === -1) return bracketIdx;
      if (bracketIdx === -1) return braceIdx;
      return Math.min(braceIdx, bracketIdx);
    })();
    if (startIdx !== -1) {
      const trimmed = text.slice(startIdx);
      const endBrace = trimmed.lastIndexOf('}');
      const endBracket = trimmed.lastIndexOf(']');
      const endIdx = Math.max(endBrace, endBracket);
      if (endIdx !== -1) {
        parsed = tryParse(trimmed.slice(0, endIdx + 1));
      }
    }
  }

  if (typeof parsed === 'string') {
    const inner = tryParse(parsed);
    if (inner !== null) parsed = inner;
  }

  if (parsed === null) {
    throw new Error(`Unable to parse CLI JSON payload: ${raw}`);
  }
  return parsed;
}

async function callTool(client, name, args, label, summary) {
  const result = await client.callTool({ name, arguments: args });
  if (label) {
    console.log(`\n=== ${label} ===`);
    const text = resultText(result);
    if (text) console.log(text.trim());
  }
  if (summary) {
    summary.steps.push({
      action: label || name,
      args,
      output: resultText(result),
    });
  }
  return result;
}

async function browserEvalJSON(client, expression) {
  await client.callTool({
    name: 'browser_evaluate',
    arguments: { function: `async () => { window.__mcpPayload = await (${expression}); return true; }` },
  });
  const raw = await client.callTool({
    name: 'browser_evaluate',
    arguments: { function: "() => JSON.stringify(window.__mcpPayload ?? null)" },
  });
  const text = resultText(raw);
  if (!text) return null;
  return normalizeCliJson(text);
}

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'storage-resilience', `realistic-${timestamp}`);
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

function analyzeSnapshot(snapshot, output) {
  if (!snapshot || !snapshot.projects) return;
  output.firebaseAvailable = snapshot.firebaseAvailable;
  output.projectCount = snapshot.projects.length;
  output.localProjects = snapshot.projects
    .map((project) => ({
      name: project.name,
      groupId: project.groupId,
      variants: project.variants.filter((variant) => variant.storage === 'local'),
    }))
    .filter((project) => project.variants.length > 0);
  output.cloudProjects = snapshot.projects
    .map((project) => ({
      name: project.name,
      groupId: project.groupId,
      variants: project.variants.filter((variant) => variant.storage === 'cloud'),
    }))
    .filter((project) => project.variants.length > 0);
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summary = {
    user,
    steps: [],
    formStates: [],
    storageSnapshots: [],
    createFormStates: [],
    analysis: {},
    navigationGaps: [],
    artifactsDir,
  };

  const client = new Client({ name: 'realistic-storage-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n=¾ USER-REALISTIC STORAGE RESILIENCE TEST');
  console.log('========================================');
  console.log('Flow: Register ’ Create Projects (Local & Cloud) ’ Validate Storage Options\n');
  console.log('   This test will expose navigation gaps in storage options UI\n');

  try {
    // ------------------------------------------------------------
    // Phase 1: Registration via UI
    // ------------------------------------------------------------
    console.log('\n=Ý Phase 1: User registration via UI');
    await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/login` }, 'Load login page', summary);
    await waitForElement(client, callTool, '.tab-button', 5000);

    await switchTab(client, callTool, 1, 'Open Sign Up tab');
    await fillField(client, callTool, '#reg-username', user.username, `Enter username ${user.username}`);
    await fillField(client, callTool, '#reg-email', user.email, `Enter email ${user.email}`);
    await fillField(client, callTool, '#reg-password', user.password, 'Enter password');
    await fillField(client, callTool, '#confirm-password', user.password, 'Confirm password');
    await clickButtonWithText(client, callTool, 'Create Account', 'Submit registration form');

    await waitForElement(client, callTool, '.logout-link', 5000);
    await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration', summary);

    // ------------------------------------------------------------
    // Phase 2: Navigate to projects list via UI
    // ------------------------------------------------------------
    console.log('\n=Â Phase 2: Navigate to projects via dashboard UI');
    await clickElement(
      client,
      callTool,
      'a[href="/projects"]',
      'My Projects button',
      'Click "My Projects" from dashboard'
    );
    await waitForElement(client, callTool, '.projects-container, .project-card, a[href="/projects/create"]', 5000);
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait for projects page load', summary);

    const initialSnapshot = await browserEvalJSON(client, 'window.collectStorageSummary ? window.collectStorageSummary() : window.__storageSummary');
    summary.storageSnapshots.push({ label: 'initial', data: initialSnapshot });

    // ------------------------------------------------------------
    // Phase 3: Create local storage project via UI
    // ------------------------------------------------------------
    console.log('\n=¿ Phase 3: Create local storage project via UI navigation');
    await clickElement(
      client,
      callTool,
      'a[href="/projects/create"]',
      'Create New Project button',
      'Click "Create New Project" from projects list'
    );
    await waitForElement(client, callTool, '#name', 5000);

    const localProjectName = `Local Project ${timestamp}`;
    await fillField(client, callTool, '#name', localProjectName, `Enter local project name ${localProjectName}`);

    // Select local storage option
    const localSelectionResult = await browserEvalJSON(
      client,
      `(() => {
        const localRadio = document.querySelector('#storage_local');
        if (localRadio) {
          localRadio.checked = true;
          localRadio.dispatchEvent(new Event('change', { bubbles: true }));
        }
        return {
          localChecked: localRadio ? localRadio.checked : null,
        };
      })()`,
    );
    summary.formStates.push({
      projectName: localProjectName,
      storage: 'local',
      radioState: localSelectionResult,
    });

    await clickButtonWithText(client, callTool, 'Create Project', 'Submit local project creation');
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after local project creation', summary);

    // Navigate back to projects list via UI
    await clickElement(
      client,
      callTool,
      'a[href="/projects"]',
      'Back to Projects button',
      'Return to projects list via UI'
    );
    await waitForElement(client, callTool, '.project-card', 5000);
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait on projects list (after local)', summary);

    const afterLocalSnapshot = await browserEvalJSON(client, 'window.collectStorageSummary ? window.collectStorageSummary() : window.__storageSummary');
    summary.storageSnapshots.push({ label: 'after_local_creation', data: afterLocalSnapshot });

    const analysis = {};
    analyzeSnapshot(afterLocalSnapshot, analysis);

    // ------------------------------------------------------------
    // Phase 4: Test cloud storage (if available)
    // ------------------------------------------------------------
    console.log('\n  Phase 4: Test cloud storage option');
    if (analysis.firebaseAvailable) {
      console.log('Firebase is available - testing cloud project creation');

      await clickElement(
        client,
        callTool,
        'a[href="/projects/create"]',
        'Create New Project button',
        'Click "Create New Project" for cloud project'
      );
      await waitForElement(client, callTool, '#name', 5000);

      // Inspect form state before creating cloud project
      const beforeCloudState = await browserEvalJSON(
        client,
        `(() => {
          const cloudInput = document.querySelector('#storage_cloud');
          const localInput = document.querySelector('#storage_local');
          const cloudDesc = cloudInput
            ? (cloudInput.closest('.storage-option')?.querySelector('.storage-option-desc')?.textContent || '').trim()
            : '';
          return {
            cloudDisabled: !!(cloudInput && cloudInput.disabled),
            cloudChecked: !!(cloudInput && cloudInput.checked),
            localChecked: !!(localInput && localInput.checked),
            cloudDesc,
            firebaseBodyFlag: document.body.dataset.firebaseAvailable,
          };
        })()`,
      );
      summary.createFormStates.push({ label: 'before_cloud_creation', state: beforeCloudState });

      const cloudProjectName = `Cloud Project ${timestamp}`;
      await fillField(client, callTool, '#name', cloudProjectName, `Enter cloud project name ${cloudProjectName}`);

      // Select cloud storage option
      const cloudSelectionResult = await browserEvalJSON(
        client,
        `(() => {
          const cloudRadio = document.querySelector('#storage_cloud');
          if (cloudRadio && !cloudRadio.disabled) {
            cloudRadio.checked = true;
            cloudRadio.dispatchEvent(new Event('change', { bubbles: true }));
            return { cloudChecked: true, cloudDisabled: false };
          }
          return { cloudChecked: false, cloudDisabled: cloudRadio ? cloudRadio.disabled : null };
        })()`,
      );
      summary.formStates.push({
        projectName: cloudProjectName,
        storage: 'cloud',
        radioState: cloudSelectionResult,
      });

      await clickButtonWithText(client, callTool, 'Create Project', 'Submit cloud project creation');
      await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after cloud project creation', summary);

      // Navigate back to projects list
      await clickElement(
        client,
        callTool,
        'a[href="/projects"]',
        'Back to Projects button',
        'Return to projects list via UI (after cloud)'
      );
      await waitForElement(client, callTool, '.project-card', 5000);
      await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait on projects list (after cloud)', summary);

      const afterCloudSnapshot = await browserEvalJSON(client, 'window.collectStorageSummary ? window.collectStorageSummary() : window.__storageSummary');
      summary.storageSnapshots.push({ label: 'after_cloud_creation', data: afterCloudSnapshot });
      analyzeSnapshot(afterCloudSnapshot, analysis);
    } else {
      console.log('   Firebase unavailable - cloud project creation skipped');

      // Still inspect the form to document the disabled state
      await clickElement(
        client,
        callTool,
        'a[href="/projects/create"]',
        'Create New Project button',
        'Open create form to inspect Firebase unavailable state'
      );
      await waitForElement(client, callTool, '#name', 5000);

      const unavailableState = await browserEvalJSON(
        client,
        `(() => {
          const cloudInput = document.querySelector('#storage_cloud');
          const localInput = document.querySelector('#storage_local');
          return {
            cloudDisabled: !!(cloudInput && cloudInput.disabled),
            cloudChecked: !!(cloudInput && cloudInput.checked),
            localChecked: !!(localInput && localInput.checked),
            firebaseBodyFlag: document.body.dataset.firebaseAvailable,
          };
        })()`,
      );
      summary.createFormStates.push({ label: 'firebase_unavailable_state', state: unavailableState });
      summary.analysis.notes = 'Firebase unavailable; cloud project creation skipped.';

      // Navigate back
      await clickElement(
        client,
        callTool,
        'a[href="/projects"]',
        'Back to Projects button',
        'Return to projects list'
      );
    }

    summary.analysis = analysis;

    await callTool(client, 'browser_close', {}, 'Close browser', summary);
    await client.close();

    console.log('\n Storage resilience test completed successfully!');
    console.log(`=Ê Analysis: ${JSON.stringify(analysis, null, 2)}`);
  } catch (error) {
    summary.error = error?.message || String(error);
    console.error('[mcp-storage-resilience-realistic] failure', error);

    // Document if error was due to navigation gap
    if (error.message && error.message.includes('not found')) {
      summary.navigationGaps.push({
        error: error.message,
        context: 'Potential UI navigation gap detected',
      });
    }

    await callTool(client, 'browser_close', {}, 'Close browser after failure', summary).catch(() => {});
    await client.close();
    throw error;
  } finally {
    const summaryPath = path.join(artifactsDir, 'summary.json');
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`\n=Ä Summary saved to ${summaryPath}\n`);
  }
}

main().catch((err) => {
  console.error('[mcp-storage-resilience-realistic] execution error', err);
  process.exit(1);
});

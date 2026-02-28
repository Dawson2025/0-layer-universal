#!/usr/bin/env node
/**
 * USER-REALISTIC Project Variant Flow (US-016 → US-024)
 *
 * Exercises branching, renaming, and variant navigation exclusively through UI interactions.
 * Initial page load uses a direct URL, all subsequent navigation relies on clickable elements.
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

import {
  switchTab,
  fillField,
  clickButtonWithText,
  waitForElement,
  navigateFromDashboard,
  selectOption,
  clickElement,
  clickProjectCardAction,
  enterProjectByName,
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `variants${timestamp}`,
  email: `variants${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Variant Project ${timestamp}`;
const branchName = `${projectName} Branch`;
const renamedProject = `${projectName} Renamed`;

const steps = [];

function record(label, result) {
  const text = (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text.trim())
    .filter(Boolean)
    .join('\n\n');
  steps.push({ label, text });
  if (label) {
    console.log(`\n=== ${label} ===`);
    console.log(text || '(no text result)');
  }
}

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) record(label, result);
  return result;
}

async function ensure(condition, message) {
  if (!condition) throw new Error(message);
}

async function main() {
  const client = new Client({ name: 'realistic-project-variants', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n🧬 USER-REALISTIC PROJECT VARIANT TEST');
  console.log('======================================');

  // ------------------------------------------------------------
  // Phase 1: Register via UI
  // ------------------------------------------------------------
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/login` }, 'Load login page');
  await ensure(
    await waitForElement(client, callTool, '#login-tab', 5000),
    'Login page did not render'
  );
  await switchTab(client, callTool, 1, 'Open Sign Up tab');

  await fillField(client, callTool, '#reg-username', user.username, `Enter username ${user.username}`);
  await fillField(client, callTool, '#reg-email', user.email, `Enter email ${user.email}`);
  await fillField(client, callTool, '#reg-password', user.password, 'Enter password');
  await fillField(client, callTool, '#confirm-password', user.password, 'Confirm password');
  await clickButtonWithText(client, callTool, 'Create Account', 'Submit registration form');

  await ensure(
    await waitForElement(client, callTool, '.logout-link', 5000),
    'Dashboard did not load after registration'
  );
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration');

  // ------------------------------------------------------------
  // Phase 2: Create project via dashboard buttons
  // ------------------------------------------------------------
  console.log('\n🛠️ Creating initial project through dashboard flow');
  await navigateFromDashboard(client, callTool, 'create-project');
  await ensure(
    await waitForElement(client, callTool, '#name', 5000),
    'Project creation form did not open'
  );
  await callTool(client, 'browser_snapshot', {}, 'Project creation form');

  await fillField(client, callTool, '#name', projectName, `Type project name ${projectName}`);
  await selectOption(client, callTool, '#storage_local', 'Select local storage option');
  await clickButtonWithText(client, callTool, 'Create Project', 'Submit project creation');

  await ensure(
    await waitForElement(client, callTool, 'a[href="/projects"]', 5000),
    'Variant menu did not load after project creation'
  );
  await callTool(client, 'browser_snapshot', {}, 'Variant menu after creation');

  // ------------------------------------------------------------
  // Phase 3: Branch project using projects list UI
  // ------------------------------------------------------------
  console.log('\n🌿 Branching project from My Projects list');
  await clickElement(client, callTool, 'a[href="/projects"]', 'Projects breadcrumb', 'Return to projects list via breadcrumb');
  await ensure(
    await waitForElement(client, callTool, '.project-card', 5000),
    'Projects list did not render'
  );
  await callTool(client, 'browser_snapshot', {}, 'Projects list before branch');

  await clickProjectCardAction(client, callTool, projectName, 'Branch Project', 'Click "Branch Project" button');
  await callTool(
    client,
    'browser_handle_dialog',
    { accept: true, promptText: branchName },
    'Provide branch name'
  );
  await callTool(client, 'browser_handle_dialog', { accept: true }, 'Confirm branch success dialog');
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait for branch completion');
  await callTool(client, 'browser_snapshot', {}, 'Projects list after branching');

  // ------------------------------------------------------------
  // Phase 4: Rename original project through UI
  // ------------------------------------------------------------
  console.log('\n✏️ Renaming original project via project card action');
  await clickProjectCardAction(client, callTool, projectName, 'Rename Project', 'Click "Rename Project" button');
  await callTool(
    client,
    'browser_handle_dialog',
    { accept: true, promptText: renamedProject },
    'Provide rename value'
  );
  await callTool(client, 'browser_handle_dialog', { accept: true }, 'Confirm rename success dialog');
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait for rename completion');
  await callTool(client, 'browser_snapshot', {}, 'Projects list after rename');

  // ------------------------------------------------------------
  // Phase 5: Enter renamed project and capture variant menu
  // ------------------------------------------------------------
  console.log('\n🎯 Entering renamed project to verify variant dashboard');
  await enterProjectByName(client, callTool, renamedProject, 'Enter renamed project');
  await ensure(
    await waitForElement(client, callTool, 'a[href="/projects"]', 5000),
    'Variant menu did not load after entering project'
  );
  await callTool(client, 'browser_snapshot', {}, 'Variant menu for renamed project');

  await clickElement(client, callTool, 'a[href="/projects"]', 'Projects breadcrumb', 'Return to projects list');
  await callTool(client, 'browser_snapshot', {}, 'Projects list final state');

  // ------------------------------------------------------------
  // Cleanup
  // ------------------------------------------------------------
  await callTool(client, 'browser_close', {}, 'Close browser session');
  await client.close();

  console.log('\n✅ Project variants realistic flow completed successfully!');
  console.log(
    JSON.stringify(
      {
        user,
        projectName,
        branchName,
        renamedProject,
        steps,
      },
      null,
      2
    )
  );
}

main().catch((err) => {
  console.error('[mcp-project-variants-realistic] failed', err);
  process.exit(1);
});


// resource_id: "082e8a0d-d867-4027-83eb-d18999fd06e9"
// resource_type: "document"
// resource_name: "mcp-project-share-delete-realistic"
#!/usr/bin/env node
/**
 * USER-REALISTIC Project Sharing & Deletion Flow (US-018 → US-023)
 *
 * Covers:
 * - Creating a collaboration group through dashboard controls
 * - Creating a project via UI forms
 * - Sharing project with group using modal interactions
 * - Deleting project via confirmation dialogs
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
  selectDropdownOption,
  clickElement,
  clickProjectCardAction,
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `sharedelete${timestamp}`,
  email: `sharedelete${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `ShareDelete Project ${timestamp}`;
const groupName = `Automation Group ${timestamp}`;

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

async function verifyProjectRemoved(client) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const cards = Array.from(document.querySelectorAll('.project-card .project-name, .item-card .item-name'));
        return cards.some((node) => node.textContent?.trim() === ${JSON.stringify(projectName)}) ? 'present' : 'absent';
      }`,
    },
    'Check project removal'
  );
  const textOutput = result.content?.find((part) => part.type === 'text')?.text ?? '';
  if (!textOutput.includes('absent')) {
    throw new Error(`Project "${projectName}" still visible after deletion`);
  }
}

async function main() {
  const client = new Client({ name: 'realistic-project-share-delete', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n🤝 USER-REALISTIC PROJECT SHARE & DELETE TEST');
  console.log('=============================================');

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
  // Phase 2: Create collaboration group via UI navigation
  // ------------------------------------------------------------
  console.log('\n👥 Creating collaboration group');
  await navigateFromDashboard(client, callTool, 'groups');
  await ensure(
    await waitForElement(client, callTool, 'input[name="name"]', 5000),
    'Create Group form not visible'
  );
  await callTool(client, 'browser_snapshot', {}, 'Create Group form');

  await fillField(client, callTool, 'input[name="name"]', groupName, `Enter group name ${groupName}`);
  await fillField(
    client,
    callTool,
    'textarea[name="description"]',
    'Automation test group created via realistic navigation',
    'Enter group description'
  );
  await clickButtonWithText(client, callTool, 'Create Group', 'Submit group creation');

  await ensure(
    await waitForElement(client, callTool, '.group-card', 5000),
    'Groups list did not show new group'
  );
  await callTool(client, 'browser_snapshot', {}, 'Groups list after creation');

  await clickElement(client, callTool, 'a.back-button', 'Back to Dashboard', 'Return to dashboard');
  await ensure(
    await waitForElement(client, callTool, '.logout-link', 5000),
    'Dashboard did not reload after returning from groups'
  );

  // ------------------------------------------------------------
  // Phase 3: Create project through dashboard path
  // ------------------------------------------------------------
  console.log('\n🚀 Creating project for sharing/deletion tests');
  await navigateFromDashboard(client, callTool, 'create-project');
  await ensure(
    await waitForElement(client, callTool, '#name', 5000),
    'Project creation form not visible'
  );
  await callTool(client, 'browser_snapshot', {}, 'Project creation form');

  await fillField(client, callTool, '#name', projectName, `Enter project name ${projectName}`);
  await selectOption(client, callTool, '#storage_local', 'Select local storage');
  await clickButtonWithText(client, callTool, 'Create Project', 'Submit project creation');

  await ensure(
    await waitForElement(client, callTool, 'a[href="/projects"]', 5000),
    'Project menu did not appear after creation'
  );
  await callTool(client, 'browser_snapshot', {}, 'Project menu after creation');

  // ------------------------------------------------------------
  // Phase 4: Share project with group via modal
  // ------------------------------------------------------------
  console.log('\n🔗 Sharing project with created group');
  await clickElement(client, callTool, 'a[href="/projects"]', 'Projects breadcrumb', 'Return to projects list');
  await ensure(
    await waitForElement(client, callTool, '.project-card', 5000),
    'Projects list did not render'
  );
  await callTool(client, 'browser_snapshot', {}, 'Projects list before sharing');

  await clickProjectCardAction(client, callTool, projectName, 'Share Project', 'Open share modal');
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait for share modal animation');

  await selectDropdownOption(client, callTool, '#shareWithGroup', groupName, 'Select target group in share modal');
  await clickButtonWithText(client, callTool, 'Share with Group', 'Trigger share action');
  await callTool(client, 'browser_handle_dialog', { accept: true }, 'Confirm share success alert');
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after sharing');
  await callTool(client, 'browser_snapshot', {}, 'Projects list after sharing');

  // ------------------------------------------------------------
  // Phase 5: Delete project via confirmation dialogs
  // ------------------------------------------------------------
  console.log('\n🗑️ Deleting shared project using UI controls');
  await clickProjectCardAction(client, callTool, projectName, 'Delete Project', 'Initiate deletion');
  await callTool(client, 'browser_handle_dialog', { accept: true }, 'Confirm deletion prompt');
  await callTool(client, 'browser_handle_dialog', { accept: true }, 'Acknowledge deletion success alert');
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after deletion');
  await callTool(client, 'browser_snapshot', {}, 'Projects list after deletion');

  await verifyProjectRemoved(client);

  // ------------------------------------------------------------
  // Cleanup
  // ------------------------------------------------------------
  await callTool(client, 'browser_close', {}, 'Close browser session');
  await client.close();

  console.log('\n✅ Project share & delete realistic flow completed successfully!');
  console.log(
    JSON.stringify(
      {
        user,
        projectName,
        groupName,
        steps,
      },
      null,
      2
    )
  );
}

main().catch((err) => {
  console.error('[mcp-project-share-delete-realistic] failed', err);
  process.exit(1);
});

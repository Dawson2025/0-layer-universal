// resource_id: "91683b26-9cd6-47e9-af1b-aa74fe3dcae7"
// resource_type: "document"
// resource_name: "mcp-phonemes-flat-realistic"
#!/usr/bin/env node
/**
 * USER-REALISTIC Phoneme Views Flow (US-025 → US-028)
 *
 * Ensures the phoneme navigation cards work by clicking through Flat, Nested, and Full hierarchy
 * views using only UI interactions.
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
  navigateFromProjectMenu,
  clickElement,
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `phonemes${timestamp}`,
  email: `phonemes${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Phoneme Project ${timestamp}`;

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

async function visitPhonemeView(client, label, destination) {
  await navigateFromProjectMenu(client, callTool, destination);
  await ensure(
    await waitForElement(client, callTool, 'a.back-button', 5000),
    `${label} page did not load`
  );
  await callTool(client, 'browser_snapshot', {}, `${label} view`);
  await clickElement(client, callTool, 'a[href="/main-menu"]', 'Variant menu breadcrumb', `Return from ${label}`);
  await ensure(
    await waitForElement(client, callTool, 'a[href="/phonemes/full"]', 5000),
    'Project main menu did not reappear after returning'
  );
}

async function main() {
  const client = new Client({ name: 'realistic-phonemes', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n🔤 USER-REALISTIC PHONEME VIEW TEST');
  console.log('===================================');

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
  // Phase 2: Create project via dashboard controls
  // ------------------------------------------------------------
  console.log('\n🛠️ Creating project before viewing phonemes');
  await navigateFromDashboard(client, callTool, 'create-project');
  await ensure(
    await waitForElement(client, callTool, '#name', 5000),
    'Project creation form not visible'
  );
  await callTool(client, 'browser_snapshot', {}, 'Project creation form');

  await fillField(client, callTool, '#name', projectName, `Enter project name ${projectName}`);
  await selectOption(client, callTool, '#storage_local', 'Select local storage option');
  await clickButtonWithText(client, callTool, 'Create Project', 'Submit project creation');

  await ensure(
    await waitForElement(client, callTool, 'a[href="/phonemes/full"]', 5000),
    'Project main menu did not appear after creation'
  );
  await callTool(client, 'browser_snapshot', {}, 'Project main menu after creation');

  // ------------------------------------------------------------
  // Phase 3: Visit phoneme views via navigation cards
  // ------------------------------------------------------------
  console.log('\n📂 Navigating through phoneme views');
  await visitPhonemeView(client, 'Flat phoneme list', 'phonemes-flat');
  await visitPhonemeView(client, 'Nested phoneme view', 'phonemes-nested');
  await visitPhonemeView(client, 'Full phoneme hierarchy', 'phonemes-full');

  // ------------------------------------------------------------
  // Cleanup
  // ------------------------------------------------------------
  await callTool(client, 'browser_close', {}, 'Close browser session');
  await client.close();

  console.log('\n✅ Phoneme navigation realistic flow completed successfully!');
  console.log(
    JSON.stringify(
      {
        user,
        projectName,
        steps,
      },
      null,
      2
    )
  );
}

main().catch((err) => {
  console.error('[mcp-phonemes-flat-realistic] failed', err);
  process.exit(1);
});

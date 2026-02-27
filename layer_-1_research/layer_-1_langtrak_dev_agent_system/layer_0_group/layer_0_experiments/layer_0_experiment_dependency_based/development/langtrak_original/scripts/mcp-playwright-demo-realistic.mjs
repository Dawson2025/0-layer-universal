#!/usr/bin/env node
/**
 * USER-REALISTIC Authentication Flow Test (US-001-005)
 *
 * Simulates a complete registration and login journey using ONLY UI interactions.
 * No direct URL jumps after the initial load – every transition happens through
 * the same buttons and links a real user would click.
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

import {
  switchTab,
  fillField,
  clickButtonWithText,
  clickElement,
  waitForElement,
  navigateFromDashboard,
  submitFormWithNavigation,
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `realisticUser${timestamp}`,
  email: `realistic${timestamp}@example.com`,
  password: 'Test123!',
};

const steps = [];

function record(label, result) {
  const textParts = (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text.trim())
    .filter(Boolean);
  steps.push({ label, text: textParts.join('\n\n') });

  if (label) {
    console.log(`\n=== ${label} ===`);
    console.log(textParts.join('\n\n') || '(no text result)');
  }
}

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) record(label, result);
  return result;
}

async function ensure(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

async function main() {
  const client = new Client({ name: 'realistic-auth-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n🔐 USER-REALISTIC AUTHENTICATION TEST');
  console.log('=====================================');
  console.log('Journey: Register → Sign Out → Sign In → Projects → Sign Out (UI only)\n');

  // ----------------------------------------
  // Visit login page (initial direct navigation)
  // ----------------------------------------
  await callTool(
    client,
    'browser_navigate',
    { url: `${APP_BASE_URL}/login` },
    'Load login page'
  );
  await ensure(
    await waitForElement(client, callTool, '.tab-button', 5000),
    'Login navigation tabs did not load'
  );

  // ----------------------------------------
  // Register new account using Sign Up tab
  // ----------------------------------------
  console.log('\n📝 Phase 1: Registering via Sign Up tab');
  await switchTab(client, callTool, 1, 'Open Sign Up tab');

  await fillField(client, callTool, '#reg-username', user.username, `Enter username ${user.username}`);
  await fillField(client, callTool, '#reg-email', user.email, `Enter email ${user.email}`);
  await fillField(client, callTool, '#reg-password', user.password, 'Enter registration password');
  await fillField(client, callTool, '#confirm-password', user.password, 'Confirm registration password');

  await submitFormWithNavigation(client, callTool, 'Create Account', 'Submit registration form');

  await ensure(
    await waitForElement(client, callTool, '.logout-link', 8000),
    'Did not land on dashboard after registration'
  );
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration');

  // ----------------------------------------
  // Sign out from dashboard via UI
  // ----------------------------------------
  console.log('\n🚪 Phase 2: Signing out from dashboard');
  await clickElement(client, callTool, 'a.logout-link', 'Sign Out link', 'Sign out via header link');
  await ensure(
    await waitForElement(client, callTool, '.tab-button', 5000),
    'Login page did not reappear after logout'
  );
  await callTool(client, 'browser_snapshot', {}, 'Login page after sign out');

  // ----------------------------------------
  // Sign back in using Sign In tab
  // ----------------------------------------
  console.log('\n🔁 Phase 3: Signing back in');
  await switchTab(client, callTool, 0, 'Ensure Sign In tab is active');

  await fillField(client, callTool, '#email', user.email, `Enter login email ${user.email}`);
  await fillField(client, callTool, '#password', user.password, 'Enter login password');
  await clickButtonWithText(client, callTool, 'Sign In with Email', 'Submit login form');

  await ensure(
    await waitForElement(client, callTool, 'a[href="/projects"]', 5000),
    'Dashboard did not load after logging back in'
  );
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after login');

  // ----------------------------------------
  // Navigate to projects using dashboard UI
  // ----------------------------------------
  console.log('\n📂 Phase 4: Navigating to Projects via dashboard controls');
  await navigateFromDashboard(client, callTool, 'projects');
  await ensure(
    await waitForElement(client, callTool, 'a[href="/projects/create"]', 5000),
    'Projects list did not load'
  );
  await callTool(client, 'browser_snapshot', {}, 'Projects screen via UI navigation');

  // ----------------------------------------
  // Sign out from projects page (UI navigation back to login)
  // ----------------------------------------
  console.log('\n✅ Phase 5: Signing out from projects page');
  await clickElement(client, callTool, 'a[href="/dashboard"]', 'Dashboard breadcrumb', 'Return to dashboard from projects view');
  await ensure(
    await waitForElement(client, callTool, '.logout-link', 5000),
    'Dashboard did not appear before final logout'
  );
  await clickElement(client, callTool, 'a.logout-link', 'Sign Out link', 'Sign out from dashboard view');
  await ensure(
    await waitForElement(client, callTool, '.tab-button', 5000),
    'Login page did not appear after final logout'
  );
  await callTool(client, 'browser_snapshot', {}, 'Login page after final sign out');

  // Close the browser session
  await callTool(client, 'browser_close', {}, 'Close browser session');
  await client.close();

  console.log('\n🎉 Realistic authentication journey completed successfully!\n');
}

main().catch((err) => {
  console.error('[mcp-playwright-demo-realistic] failed', err);
  process.exit(1);
});

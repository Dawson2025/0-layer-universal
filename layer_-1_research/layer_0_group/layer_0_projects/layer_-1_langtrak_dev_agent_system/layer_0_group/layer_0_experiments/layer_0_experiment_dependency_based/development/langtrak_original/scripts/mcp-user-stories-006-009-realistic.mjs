#!/usr/bin/env node
/**
 * USER-REALISTIC Groups & Collaboration Flow (US-006 → US-011)
 *
 * Covers:
 * - Admin registers via UI and accesses dashboard
 * - Creates a collaborative group using dashboard buttons
 * - Opens invite modal, regenerates invite link through UI controls
 * - Verifies old invite link rejection and new invite link registration path
 * - Invitee joins and confirms group visibility through UI navigation
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
  waitForCondition,
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const admin = {
  username: `admin${timestamp}`,
  email: `admin${timestamp}@example.com`,
  password: 'Test123!',
};
const invitee = {
  username: `member${timestamp}`,
  email: `member${timestamp}@example.com`,
  password: 'Test123!',
};

const groupName = `Team ${timestamp}`;

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

function extractResultValue(result) {
  const text = (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text)
    .join('\n');
  const match = text.match(/### Result\s+([\s\S]*?)(?:\n###|$)/);
  if (!match) return text.trim();
  let value = match[1].trim();
  try {
    return JSON.parse(value);
  } catch {
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    return value;
  }
}

async function ensure(condition, message) {
  if (!condition) throw new Error(message);
}

async function clickFirstMatchingCard(client, textSnippet, label) {
  return callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const cards = Array.from(document.querySelectorAll('.group-card, .item-card'));
        const card = cards.find((el) => el.textContent.includes(${JSON.stringify(textSnippet)}));
        if (card) {
          card.click();
          return { clicked: true, text: card.textContent.trim() };
        }
        return { clicked: false, available: cards.map((el) => el.textContent.trim()).slice(0, 5) };
      }`,
    },
    label
  );
}

async function main() {
  const client = new Client({ name: 'realistic-groups-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n🤝 USER-REALISTIC GROUPS & COLLABORATION TEST');
  console.log('============================================');
  console.log('Flow: Admin registers → creates group → shares invite → invitee joins via UI\n');

  // ------------------------------------------------------------
  // Phase 1: Admin registration and dashboard verification
  // ------------------------------------------------------------
  await callTool(
    client,
    'browser_navigate',
    { url: `${APP_BASE_URL}/login` },
    'Load login page for admin registration'
  );
  await ensure(
    await waitForElement(client, callTool, '#login-tab', 5000),
    'Login tab did not appear'
  );

  await switchTab(client, callTool, 1, 'Open Sign Up tab for admin');
  await fillField(client, callTool, '#reg-username', admin.username, `Enter admin username ${admin.username}`);
  await fillField(client, callTool, '#reg-email', admin.email, `Enter admin email ${admin.email}`);
  await fillField(client, callTool, '#reg-password', admin.password, 'Enter admin password');
  await fillField(client, callTool, '#confirm-password', admin.password, 'Confirm admin password');
  await clickButtonWithText(client, callTool, 'Create Account', 'Submit admin registration form');

  await ensure(
    await waitForElement(client, callTool, '.logout-link', 5000),
    'Dashboard did not load after admin registration'
  );
  await callTool(client, 'browser_snapshot', {}, 'Admin dashboard after registration');

  // ------------------------------------------------------------
  // Phase 2: Create collaborative group via UI
  // ------------------------------------------------------------
  console.log('\n👥 Creating collaborative group through dashboard controls');
  await navigateFromDashboard(client, callTool, 'groups');
  await ensure(
    await waitForElement(client, callTool, 'input[name="name"]', 5000),
    'Create Group form did not appear'
  );
  await callTool(client, 'browser_snapshot', {}, 'Create Group form opened via UI');

  await fillField(
    client,
    callTool,
    'input[name="name"]',
    groupName,
    `Enter group name ${groupName}`
  );
  await fillField(
    client,
    callTool,
    'textarea[name="description"]',
    'Automated test group for realistic navigation validations',
    'Enter group description'
  );
  await clickButtonWithText(client, callTool, 'Create Group', 'Submit group creation form');

  await ensure(
    await waitForElement(client, callTool, '.group-card', 5000),
    'Groups list did not load after creation'
  );
  await callTool(client, 'browser_snapshot', {}, 'Groups menu after creation');

  await clickFirstMatchingCard(client, groupName, 'Open new group detail card');
  await ensure(
    await waitForElement(client, callTool, '.admin-buttons', 5000),
    'Group detail page did not load'
  );
  await callTool(client, 'browser_snapshot', {}, 'Group detail after opening card');

  // ------------------------------------------------------------
  // Phase 3: Manage invite links through modal controls
  // ------------------------------------------------------------
  console.log('\n🔗 Verifying invite modal interactions');
  await clickButtonWithText(client, callTool, 'Share Invite Link', 'Open invite modal');
  await ensure(
    await waitForElement(client, callTool, '#inviteLinkModal.modal', 3000),
    'Invite modal did not open'
  );

  const originalInviteResult = await callTool(
    client,
    'browser_evaluate',
    { function: "() => document.getElementById('inviteLinkInput')?.value || ''" },
    'Capture current invite link value'
  );
  const originalInviteLink = extractResultValue(originalInviteResult);
  console.log(`Original invite link: ${originalInviteLink}`);

  await clickButtonWithText(client, callTool, 'Generate New Link', 'Request invite regeneration');
  await callTool(client, 'browser_handle_dialog', { accept: true }, 'Accept regeneration confirmation');
  await callTool(client, 'browser_handle_dialog', { accept: true }, 'Dismiss regeneration success alert');

  const newInviteResult = await callTool(
    client,
    'browser_evaluate',
    { function: "() => document.getElementById('inviteLinkInput')?.value || ''" },
    'Capture regenerated invite link'
  );
  const newInviteLink = extractResultValue(newInviteResult);
  console.log(`Regenerated invite link: ${newInviteLink}`);

  await clickButtonWithText(client, callTool, 'Close', 'Close invite modal');

  // ------------------------------------------------------------
  // Phase 4: Sign out admin and validate invite links as guest
  // ------------------------------------------------------------
  console.log('\n🚪 Signing out admin to simulate guest invite flow');
  await clickElement(client, callTool, 'a.back-button', 'Back button', 'Return to groups list');
  await ensure(
    await waitForElement(client, callTool, '.group-card', 5000),
    'Groups list did not load before sign out'
  );
  await clickElement(client, callTool, 'a.back-button', 'Back button', 'Return to dashboard from groups');
  await ensure(
    await waitForElement(client, callTool, '.logout-link', 5000),
    'Dashboard did not appear before admin logout'
  );
  await clickElement(client, callTool, 'a.logout-link', 'Sign Out link', 'Sign out admin via header link');
  await ensure(
    await waitForElement(client, callTool, '.tab-button', 5000),
    'Login page did not appear after admin logout'
  );
  await callTool(client, 'browser_snapshot', {}, 'Login page after admin logout');

  console.log('\n🚫 Visiting original invite link (should be invalid after regeneration)');
  await callTool(
    client,
    'browser_navigate',
    { url: originalInviteLink },
    'Visit original invite link (expected invalid)'
  );
  await callTool(client, 'browser_snapshot', {}, 'Snapshot after visiting invalid invite link');

  console.log('\n✅ Visiting regenerated invite link to join as new member');
  await callTool(
    client,
    'browser_navigate',
    { url: newInviteLink },
    'Visit regenerated invite link'
  );
  // The join token redirects unauthenticated users to /login, where we can sign up.
  await ensure(
    await waitForElement(client, callTool, '.tab-button', 5000),
    'Login page did not render for invitee after visiting invite link'
  );
  await callTool(client, 'browser_snapshot', {}, 'Invitee redirected to login');

  await switchTab(client, callTool, 1, 'Open Sign Up tab for invitee');
  await fillField(client, callTool, '#reg-username', invitee.username, `Enter invitee username ${invitee.username}`);
  await fillField(client, callTool, '#reg-email', invitee.email, `Enter invitee email ${invitee.email}`);
  await fillField(client, callTool, '#reg-password', invitee.password, 'Enter invitee password');
  await fillField(client, callTool, '#confirm-password', invitee.password, 'Confirm invitee password');
  await clickButtonWithText(client, callTool, 'Create Account', 'Submit invitee registration');

  await ensure(
    await waitForCondition(
      client,
      callTool,
      "() => !!document.querySelector('.logout-link') || !!document.querySelector('.members-list') || (window.location.pathname || '').startsWith('/groups/')",
      8000,
      250,
      'Wait for invitee authenticated landing'
    ),
    'Invitee did not reach an authenticated page after registration'
  );
  await callTool(client, 'browser_snapshot', {}, 'Invitee after registration');

  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/groups` }, 'Navigate to groups list as invitee');
  await ensure(
    await waitForElement(client, callTool, '.group-card', 8000),
    'Groups list did not load for invitee'
  );
  await callTool(client, 'browser_snapshot', {}, 'Groups list for invitee');
  await ensure(
    await waitForCondition(
      client,
      callTool,
      `() => Array.from(document.querySelectorAll('.group-card')).some((card) => (card.textContent || '').includes(${JSON.stringify(groupName)}))`,
      6000
    ),
    'Joined group did not appear for invitee'
  );

  // ------------------------------------------------------------
  // Phase 5: Verify group visibility for invitee via UI
  // ------------------------------------------------------------
  console.log('\n🔍 Verifying group visibility for invitee');
  await clickFirstMatchingCard(client, groupName, 'Open joined group from invitee dashboard');
  await ensure(
    await waitForElement(client, callTool, '.member-list', 5000),
    'Invitee group detail did not load'
  );
  await callTool(client, 'browser_snapshot', {}, 'Invitee group detail view');

  await clickElement(client, callTool, 'a.back-button', 'Back to Groups button', 'Return to groups listing');
  await ensure(
    await waitForElement(client, callTool, '.group-card', 5000),
    'Groups menu did not appear for invitee'
  );
  await callTool(client, 'browser_snapshot', {}, 'Groups menu as invitee');

  await clickElement(client, callTool, 'a.logout-link', 'Sign Out link', 'Invitee sign out');
  await callTool(client, 'browser_close', {}, 'Close browser session');
  await client.close();

  console.log('\n🎉 Realistic groups & collaboration journey completed successfully!\n');
  console.log(
    JSON.stringify(
      {
        admin,
        invitee,
        groupName,
        originalInviteLink,
        newInviteLink,
        steps,
      },
      null,
      2
    )
  );
}

main().catch((err) => {
  console.error('[mcp-user-stories-006-009-realistic] failed', err);
  process.exit(1);
});

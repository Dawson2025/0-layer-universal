// resource_id: "93c16ce0-f52b-4efa-867b-00dde5d9ad77"
// resource_type: "document"
// resource_name: "mcp-user-stories-006-009"
#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE = 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

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

const steps = [];

function record(step, result) {
  const textParts = (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text.trim());
  steps.push({ step, text: textParts.join('\n\n') });
  console.log(`\n=== ${step} ===`);
  console.log(textParts.join('\n\n') || '(no text result)');
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
    const parsed = JSON.parse(value);
    return parsed;
  } catch {
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    return value;
  }
}

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) record(label, result);
  return result;
}

async function main() {
  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  // Register admin user (US-001, reused for US-006+)
  await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Go to login');
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return document.getElementById('register-tab')?.classList.contains('active'); }" },
    'Switch to Sign Up tab (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: `() => { const el = document.querySelector('#reg-username'); if (el) { el.value = '${admin.username}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }` },
    'Fill username (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: `() => { const el = document.querySelector('#reg-email'); if (el) { el.value = '${admin.email}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }` },
    'Fill email (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: `() => { const el = document.querySelector('#reg-password'); if (el) { el.value = '${admin.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }` },
    'Fill password (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: `() => { const el = document.querySelector('#confirm-password'); if (el) { el.value = '${admin.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }` },
    'Confirm password (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = document.querySelector('#register-tab .form-button'); if (btn) { btn.click(); return 'submitted'; } return 'button-missing'; }",
    },
    'Submit registration (JS)',
  );
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration');

  // US-006: Verify dashboard layout
  await callTool(client, 'browser_navigate', { url: `${BASE}/dashboard` }, 'Navigate to dashboard');
  await callTool(client, 'browser_snapshot', {}, 'Dashboard snapshot');

  // US-007: Create new group
  const groupName = `Team ${timestamp}`;
  await callTool(client, 'browser_navigate', { url: `${BASE}/groups/create` }, 'Open create group');
  await callTool(
    client,
    'browser_evaluate',
    { function: `() => { const el = document.querySelector('input[placeholder=\"Enter a name for your group\"]'); if (el) { el.value = '${groupName}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }` },
    'Enter group name (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const el = document.querySelector('textarea[placeholder=\"Describe what this group is for (optional)\"]'); if (el) { el.value = 'Automated test group'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }",
    },
    'Enter group description (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = Array.from(document.querySelectorAll('button')).find((b) => b.textContent.includes('Create Group')); if (btn) { btn.click(); return 'submitted'; } return 'button-missing'; }",
    },
    'Submit group creation (JS)',
  );
  await callTool(client, 'browser_snapshot', {}, 'Groups list after creation');

  // Navigate to group detail via DOM click
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelector('.group-card')?.click(); return 'clicked'; }" },
    'Click group card (JS)',
  );
  await callTool(client, 'browser_snapshot', {}, 'Group detail snapshot');

  // US-008: Fetch invite link
  const inviteLinkResult = await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { if (window.showInviteLinkModal) { window.showInviteLinkModal(); } return document.getElementById('inviteLinkInput')?.value || ''; }",
    },
    'Open invite modal via JS',
  );
  const originalInviteLink = extractResultValue(inviteLinkResult);
  console.log(`Original invite link: ${originalInviteLink}`);

  const regenRequest = await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { if (window.regenerateInviteLink) { window.regenerateInviteLink(); return 'requested'; } return 'missing'; }",
    },
    'Trigger invite regeneration (JS)',
  );
  const regenResponse = await callTool(
    client,
    'browser_handle_dialog',
    { accept: true },
    'Accept regeneration alert',
  );
  const newInviteLinkResult = await callTool(
    client,
    'browser_evaluate',
    {
      function: "() => document.getElementById('inviteLinkInput')?.value || ''",
    },
    'Read regenerated invite link (JS)',
  );
  const newInviteLink = extractResultValue(newInviteLinkResult);
  console.log(`New invite link: ${newInviteLink}`);

  // Sign out admin
  await callTool(client, 'browser_navigate', { url: `${BASE}/logout` }, 'Sign out admin');
  await callTool(client, 'browser_snapshot', {}, 'Login snapshot after admin logout');

  // Visit invite link (US-009)
  await callTool(client, 'browser_navigate', { url: originalInviteLink }, 'Visit old invite link');
  await callTool(client, 'browser_snapshot', {}, 'Old invite link snapshot');
  await callTool(client, 'browser_navigate', { url: newInviteLink }, 'Visit regenerated invite link');
  await callTool(client, 'browser_snapshot', {}, 'Invite redirect snapshot');

  // Register invitee on /register page
  await callTool(
    client,
    'browser_evaluate',
    { function: `() => { const el = document.querySelector('#username'); if (el) { el.value = '${invitee.username}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }` },
    'Fill invitee username (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: `() => { const el = document.querySelector('#email'); if (el) { el.value = '${invitee.email}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }` },
    'Fill invitee email (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: `() => { const el = document.querySelector('#password'); if (el) { el.value = '${invitee.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }` },
    'Fill invitee password (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#confirm_password'); if (el) { el.value = '${invitee.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Confirm invitee password (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = document.querySelector('button.form-button'); if (btn) { btn.click(); return 'submitted'; } return 'button-missing'; }",
    },
    'Submit invitee registration (JS)',
  );
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after invitee join');

  // Verify group membership
  await callTool(client, 'browser_navigate', { url: `${BASE}/groups` }, 'Invitee groups list');
  await callTool(client, 'browser_snapshot', {}, 'Groups snapshot (invitee)');
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelector('.group-card')?.click(); return 'clicked'; }" },
    'Invitee open group detail (JS)',
  );
  await callTool(client, 'browser_snapshot', {}, 'Group detail (invitee)');

  await callTool(client, 'browser_close', {}, 'Close browser');
  await client.close();

  console.log('\n=== Summary ===');
  console.log(
    JSON.stringify(
      {
        admin,
        invitee,
        originalInviteLink,
        newInviteLink,
        steps,
      },
      null,
      2,
    ),
  );
}

main().catch((err) => {
  console.error('[mcp-user-stories-006-009] failed', err);
  process.exit(1);
});

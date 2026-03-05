// resource_id: "52d438ee-1705-47c1-8206-541f9301f130"
// resource_type: "document"
// resource_name: "mcp-project-share-delete"
#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE = 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `sharedelete${timestamp}`,
  email: `sharedelete${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `ShareDelete Project ${timestamp}`;
const groupName = `Automation Group ${timestamp}`;

const steps = [];

function record(step, result) {
  const text = (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text.trim())
    .join('\n\n');
  steps.push({ step, text });
  console.log(`\n=== ${step} ===`);
  console.log(text || '(no text result)');
}

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) record(label, result);
  return result;
}

async function main() {
  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  // Register user
  await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Open login page');
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const tab = document.querySelectorAll('.tab-button')[1]; if (tab) { tab.click(); return true; } return false; }",
    },
    'Switch to Sign Up tab',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#reg-username'); if (el) { el.value = '${user.username}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Fill username',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#reg-email'); if (el) { el.value = '${user.email}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Fill email',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#reg-password'); if (el) { el.value = '${user.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Fill password',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#confirm-password'); if (el) { el.value = '${user.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Confirm password',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = document.querySelector('#register-tab .form-button'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
    },
    'Submit registration',
  );
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration');

  // Create group for sharing
  await callTool(client, 'browser_navigate', { url: `${BASE}/groups/create` }, 'Open create group form');
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('input[placeholder=\"Enter a name for your group\"]'); if (el) { el.value = '${groupName}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Fill group name',
  );
  await callTool(client, 'browser_evaluate', { function: "() => { const el = document.querySelector('textarea'); if (el) { el.value = 'Automation test group'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }" }, 'Fill group description');
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = Array.from(document.querySelectorAll('button')).find((b) => b.textContent.includes('Create Group')); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
    },
    'Submit group creation',
  );
  await callTool(client, 'browser_snapshot', {}, 'Groups list after group creation');

  // Create project
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, 'Open create project form');
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#name'); if (el) { el.value = '${projectName}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Fill project name',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const radio = document.querySelector('#storage_local'); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change', { bubbles: true })); } return !!radio?.checked; }",
    },
    'Select local storage',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = document.querySelector('button.button.primary'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
    },
    'Submit project creation',
  );
  await callTool(client, 'browser_snapshot', {}, 'Variant menu after project creation');

  // Navigate to projects list
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Open projects list');
  await callTool(client, 'browser_snapshot', {}, 'Projects list before sharing');

  // Share project with created group
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = Array.from(document.querySelectorAll('button')).find((b) => b.textContent.includes('Share Project')); if (btn) { btn.click(); return 'clicked'; } return 'not-found'; }",
    },
    'Open share modal',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const select = document.getElementById('shareWithGroup'); if (select && select.options.length > 1) { select.value = select.options[1].value; select.dispatchEvent(new Event('change', { bubbles: true })); return select.value; } return null; }",
    },
    'Select group in share modal',
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { if (typeof shareProject === 'function') { shareProject(); return 'invoked'; } return 'missing'; }" },
    'Invoke shareProject()',
  );
  await callTool(
    client,
    'browser_handle_dialog',
    { accept: true },
    'Acknowledge share success alert',
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after share');
  await callTool(client, 'browser_snapshot', {}, 'Projects list after sharing');

  // Delete project
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = Array.from(document.querySelectorAll('button')).find((b) => b.textContent.includes('Delete Project')); if (btn) { btn.click(); return 'clicked'; } return 'not-found'; }",
    },
    'Initiate project deletion',
  );
  await callTool(
    client,
    'browser_handle_dialog',
    { accept: true },
    'Confirm deletion prompt',
  );
  await callTool(
    client,
    'browser_handle_dialog',
    { accept: true },
    'Acknowledge deletion success alert',
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after deletion');
  await callTool(client, 'browser_snapshot', {}, 'Projects list after deletion');

  // Verify project removed
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { return Array.from(document.querySelectorAll('.project-card .project-name')).some(node => node.textContent.trim() === '${projectName}') ? 'still-present' : 'absent'; }`,
    },
    'Verify project card removed',
  );

  await callTool(client, 'browser_close', {}, 'Close browser');
  await client.close();

  console.log(
    JSON.stringify(
      {
        user,
        projectName,
        groupName,
        steps,
      },
      null,
      2,
    ),
  );
}

main().catch((err) => {
  console.error('[mcp-project-share-delete] failed', err);
  process.exit(1);
});

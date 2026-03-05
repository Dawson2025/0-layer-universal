// resource_id: "48f46315-b66c-47e7-9034-49906731c75d"
// resource_type: "document"
// resource_name: "mcp-project-variants"
#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE = 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `variants${timestamp}`,
  email: `variants${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Variant Project ${timestamp}`;
const renamedProject = `${projectName} Renamed`;
const branchName = `${projectName} Branch`;

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

  // Register a fresh user (US-001)
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
    'Fill registration username',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#reg-email'); if (el) { el.value = '${user.email}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Fill registration email',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#reg-password'); if (el) { el.value = '${user.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Fill registration password',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const el = document.querySelector('#confirm-password'); if (el) { el.value = '${user.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
    'Confirm registration password',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = document.querySelector('#register-tab .form-button'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
    },
    'Submit registration form',
  );
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration');

  // Create a local project (US-014)
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
  await callTool(client, 'browser_snapshot', {}, 'Variant menu after project creation (US-024)');

  // Go to projects list
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Open projects list');
  await callTool(client, 'browser_snapshot', {}, 'Projects list before branch');

  // Branch the project (US-016)
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = Array.from(document.querySelectorAll('button')).find((b) => b.textContent.includes('Branch Project') || b.textContent.includes(' Branch')); if (btn) { btn.click(); return 'clicked'; } return 'not-found'; }",
    },
    'Click branch project button',
  );
  await callTool(
    client,
    'browser_handle_dialog',
    {
      accept: true,
      promptText: branchName,
    },
    'Provide branch name prompt',
  );
  await callTool(
    client,
    'browser_handle_dialog',
    { accept: true },
    'Acknowledge branch success alert',
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after branch reload');
  await callTool(client, 'browser_snapshot', {}, 'Projects list after branch');

  // Rename the project group (US-017)
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = Array.from(document.querySelectorAll('button')).find((b) => b.textContent.includes('Rename Project')); if (btn) { btn.click(); return 'clicked'; } return 'not-found'; }",
    },
    'Click rename project button',
  );
  await callTool(
    client,
    'browser_handle_dialog',
    {
      accept: true,
      promptText: renamedProject,
    },
    'Provide rename prompt',
  );
  await callTool(
    client,
    'browser_handle_dialog',
    { accept: true },
    'Acknowledge rename success alert',
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after rename reload');
  await callTool(client, 'browser_snapshot', {}, 'Projects list after rename');

  // Enter the renamed project (US-015 reused, US-024 view)
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = Array.from(document.querySelectorAll('a.action-button.enter')).find((b) => b.textContent.includes('Enter')); if (btn) { btn.click(); return btn.href || 'clicked'; } return 'not-found'; }",
    },
    'Enter project via variant action',
  );
  await callTool(client, 'browser_snapshot', {}, 'Variant menu after entering renamed project');

  await callTool(client, 'browser_close', {}, 'Close browser');
  await client.close();

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
      2,
    ),
  );
}

main().catch((err) => {
  console.error('[mcp-project-variants] failed', err);
  process.exit(1);
});

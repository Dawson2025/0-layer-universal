// resource_id: "4116c075-c20a-49ff-88e9-60c96fbb8290"
// resource_type: "document"
// resource_name: "mcp-projects-flow"
#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE = 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  email: `admin1760727222266@example.com`,
  password: 'Test123!',
};
const projects = [
  `Project Alpha ${timestamp}`,
  `Project Beta ${timestamp}`,
];

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

  // Login
  await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Navigate to login');
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const email = document.querySelector('#email'); if (email) { email.value = '${user.email}'; email.dispatchEvent(new Event('input', { bubbles: true })); } return email?.value || ''; }`,
    },
    'Fill login email (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const password = document.querySelector('#password'); if (password) { password.value = '${user.password}'; password.dispatchEvent(new Event('input', { bubbles: true })); } return password?.value || ''; }`,
    },
    'Fill login password (JS)',
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const btn = Array.from(document.querySelectorAll('button')).find((b) => b.textContent.includes('Sign In with Email')); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
    },
    'Submit login (JS)',
  );
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after login');

  // US-012 initial view
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'View projects list (initial)');
  await callTool(client, 'browser_snapshot', {}, 'Projects list snapshot (initial)');

  for (const [index, projectName] of projects.entries()) {
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, `Open create project form #${index + 1}`);
    await callTool(
      client,
      'browser_evaluate',
      {
        function:
          `() => { const nameInput = document.querySelector('#name'); if (nameInput) { nameInput.value = '${projectName}'; nameInput.dispatchEvent(new Event('input', { bubbles: true })); } return nameInput?.value || ''; }`,
      },
      `Fill project name ${index + 1}`,
    );
    await callTool(
      client,
      'browser_evaluate',
      {
        function:
          "() => { const local = document.querySelector('#storage_local'); if (local) { local.checked = true; local.dispatchEvent(new Event('change', { bubbles: true })); } return !!local?.checked; }",
      },
      `Select local storage ${index + 1}`,
    );
    await callTool(
      client,
      'browser_evaluate',
      {
        function:
          "() => { const btn = document.querySelector('button.button.primary'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
      },
      `Submit project creation ${index + 1}`,
    );
    await callTool(client, 'browser_snapshot', {}, `Post-creation snapshot ${index + 1}`);
  }

  // US-012 verify projects list populated
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'View projects list (populated)');
  await callTool(client, 'browser_snapshot', {}, 'Projects list snapshot (populated)');

  // US-013 search projects
  const searchTerm = 'Beta';
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        `() => { const input = document.querySelector('#projectSearchInput'); if (input) { input.value = '${searchTerm}'; input.dispatchEvent(new Event('input', { bubbles: true })); } return input?.value || ''; }`,
    },
    'Filter projects via search (JS)',
  );
  await callTool(client, 'browser_snapshot', {}, 'Projects list after search filter');
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const input = document.querySelector('#projectSearchInput'); if (input) { input.value = ''; input.dispatchEvent(new Event('input', { bubbles: true })); } return input?.value || ''; }",
    },
    'Clear project search (JS)',
  );

  // US-015 enter project
  await callTool(
    client,
    'browser_evaluate',
    {
      function:
        "() => { const enterButton = Array.from(document.querySelectorAll('a.action-button.enter')).find((btn) => btn.textContent.includes('🎯') || btn.textContent.includes('Enter')); if (enterButton) { enterButton.click(); return enterButton.href || 'clicked'; } return 'missing'; }",
    },
    'Click Enter on project (JS)',
  );
  await callTool(client, 'browser_snapshot', {}, 'Main menu after entering project');

  await callTool(client, 'browser_close', {}, 'Close browser');
  await client.close();

  console.log('\n=== Summary ===');
  console.log(
    JSON.stringify(
      {
        user,
        projects,
        searchTerm,
        steps,
      },
      null,
      2,
    ),
  );
}

main().catch((err) => {
  console.error('[mcp-projects-flow] failed', err);
  process.exit(1);
});

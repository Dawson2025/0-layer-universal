#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE = 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `phonemes${timestamp}`,
  email: `phonemes${timestamp}@example.com`,
  password: 'Test123!',
};

async function main() {
  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  await client.callTool({ name: 'browser_navigate', arguments: { url: `${BASE}/login` } });
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: "() => { const tab = document.querySelectorAll('.tab-button')[1]; if (tab) { tab.click(); return true; } return false; }",
    },
  });
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: `() => { const el = document.querySelector('#reg-username'); if (el) { el.value = '${user.username}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
  });
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: `() => { const el = document.querySelector('#reg-email'); if (el) { el.value = '${user.email}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
  });
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: `() => { const el = document.querySelector('#reg-password'); if (el) { el.value = '${user.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
  });
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: `() => { const el = document.querySelector('#confirm-password'); if (el) { el.value = '${user.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
  });
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: "() => { const btn = document.querySelector('#register-tab .form-button'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
    },
  });
  await client.callTool({ name: 'browser_snapshot', arguments: {} });

  await client.callTool({ name: 'browser_navigate', arguments: { url: `${BASE}/projects/create` } });
  const projectName = `Phoneme Project ${timestamp}`;
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: `() => { const el = document.querySelector('#name'); if (el) { el.value = '${projectName}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    },
  });
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: "() => { const radio = document.querySelector('#storage_local'); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change', { bubbles: true })); } return !!radio?.checked; }",
    },
  });
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: "() => { const btn = document.querySelector('button.button.primary'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
    },
  });
  await client.callTool({ name: 'browser_snapshot', arguments: {} });

  await client.callTool({ name: 'browser_navigate', arguments: { url: `${BASE}/phonemes/flat` } });
  await client.callTool({ name: 'browser_snapshot', arguments: {} });
  await client.callTool({ name: 'browser_navigate', arguments: { url: `${BASE}/phonemes/nested` } });
  await client.callTool({ name: 'browser_snapshot', arguments: {} });
  await client.callTool({ name: 'browser_navigate', arguments: { url: `${BASE}/phonemes/full` } });
  await client.callTool({ name: 'browser_snapshot', arguments: {} });

  await client.callTool({ name: 'browser_close', arguments: {} });
  await client.close();
}

main().catch((err) => {
  console.error('[mcp-phonemes-flat] failed', err);
  process.exit(1);
});

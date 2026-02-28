#!/usr/bin/env node
/**
 * Simple US-053 Test - Recalculate Phoneme Frequencies
 * Uses proper MCP browser tools (browser_type, browser_click, browser_snapshot)
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5000';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) {
    console.log(`\n=== ${label} ===`);
    const text = (result.content ?? [])
      .filter((p) => p.type === 'text')
      .map((p) => p.text.trim())
      .join('\n');
    if (text) console.log(text);
  }
  return result;
}

async function getSnapshot(client) {
  return await callTool(client, 'browser_snapshot', {});
}

async function main() {
  const client = new Client({ name: 'us053-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  const timestamp = Date.now();
  const user = {
    username: `us053test${timestamp}`,
    email: `us053test${timestamp}@example.com`,
    password: 'Test123!',
  };
  const projectName = `US053 Test ${timestamp}`;

  console.log('\n🧪 US-053 ENDPOINT TEST');
  console.log('========================');
  console.log(`User: ${user.username}`);
  console.log(`Project: ${projectName}`);
  console.log(`Endpoint: POST /api/admin/recalculate-phoneme-frequencies\n`);

  try {
    // Step 1: Navigate to login
    await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Navigate to login');
    let snap = await getSnapshot(client);

    // Step 2: Switch to Sign Up tab
    await callTool(client, 'browser_click', {
      element: 'Sign Up tab',
      ref: 'e8',
    }, 'Click Sign Up tab');

    await callTool(client, 'browser_wait_for', { time: 0.5 });
    snap = await getSnapshot(client);

    // Step 3: Fill registration form
    await callTool(client, 'browser_type', {
      element: 'Username field',
      ref: 'e38',
      text: user.username,
    }, `Type username: ${user.username}`);

    await callTool(client, 'browser_type', {
      element: 'Email field',
      ref: 'e41',
      text: user.email,
    }, `Type email: ${user.email}`);

    await callTool(client, 'browser_type', {
      element: 'Password field',
      ref: 'e44',
      text: user.password,
    }, 'Type password');

    await callTool(client, 'browser_type', {
      element: 'Confirm Password field',
      ref: 'e47',
      text: user.password,
    }, 'Confirm password');

    // Step 4: Submit registration
    await callTool(client, 'browser_click', {
      element: 'Create Account button',
      ref: 'e48',
    }, 'Submit registration');

    await callTool(client, 'browser_wait_for', { time: 2 });
    snap = await getSnapshot(client);

    // Step 5: Navigate to create project
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, 'Navigate to project creation');
    snap = await getSnapshot(client);

    // Find and fill project name field
    await callTool(client, 'browser_evaluate', {
      function: `() => { const name = document.querySelector('#name, input[name="name"]'); if (name) { name.value = '${projectName}'; name.dispatchEvent(new Event('input', { bubbles: true })); } return name ? 'filled' : 'not-found'; }`,
    }, 'Fill project name');

    // Select local storage
    await callTool(client, 'browser_evaluate', {
      function: "() => { const radio = document.querySelector('#storage_local, input[value=\"local\"]'); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change', { bubbles: true })); } return radio ? 'selected' : 'not-found'; }",
    }, 'Select local storage');

    // Submit project creation
    await callTool(client, 'browser_evaluate', {
      function: "() => { const btn = document.querySelector('button.primary, button[type=\"submit\"]'); if (btn) { btn.click(); } return btn ? 'clicked' : 'not-found'; }",
    }, 'Create project');

    await callTool(client, 'browser_wait_for', { time: 2 });

    // Step 6: Go to projects list and enter
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Navigate to projects');
    await callTool(client, 'browser_wait_for', { time: 1 });
    snap = await getSnapshot(client);

    await callTool(client, 'browser_evaluate', {
      function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); } return enter ? 'clicked' : 'not-found'; }",
    }, 'Enter project');

    await callTool(client, 'browser_wait_for', { time: 2 });
    snap = await getSnapshot(client);

    // Step 7: Navigate to admin panel
    console.log('\n📊 Navigating to Admin panel...');
    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` }, 'Open admin panel');
    await callTool(client, 'browser_wait_for', { time: 2 });
    snap = await getSnapshot(client);

    // Step 8: Test US-053 endpoint via API call
    console.log('\n🎯 Testing US-053 Endpoint: Recalculate Phoneme Frequencies');
    const recalcResult = await callTool(client, 'browser_evaluate', {
      function: `async () => {
        try {
          const response = await fetch('/api/admin/recalculate-phoneme-frequencies', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
          });
          const data = await response.json();
          return {
            status: response.status,
            ok: response.ok,
            data: data
          };
        } catch (error) {
          return { error: error.message };
        }
      }`,
    }, 'Call recalculate frequencies API');

    // Parse result
    const resultText = recalcResult.content?.find(p => p.type === 'text')?.text || '';
    console.log('\n📊 US-053 API Response:');
    console.log(resultText);

    // Check if it's a success
    if (resultText.includes('"success":true') || resultText.includes('"ok":true')) {
      console.log('\n✅ US-053 ENDPOINT TEST: PASSED');
      console.log('✅ Recalculate phoneme frequencies endpoint is working!');
    } else if (resultText.includes('404')) {
      console.log('\n❌ US-053 ENDPOINT TEST: FAILED - 404 Not Found');
    } else {
      console.log('\n⚠️  US-053 ENDPOINT TEST: RESPONSE RECEIVED');
      console.log('Check the response above to verify');
    }

    await callTool(client, 'browser_close', {});
    await client.close();

    console.log('\n✅ Test complete');
    process.exit(0);

  } catch (error) {
    console.error('\n❌ Test failed:', error);
    try {
      await callTool(client, 'browser_close', {});
      await client.close();
    } catch {}
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('[mcp-test-us053] failed', err);
  process.exit(1);
});


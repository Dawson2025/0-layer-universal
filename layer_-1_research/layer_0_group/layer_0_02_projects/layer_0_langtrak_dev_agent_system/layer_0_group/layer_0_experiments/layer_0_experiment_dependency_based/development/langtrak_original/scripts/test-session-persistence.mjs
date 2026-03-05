// resource_id: "6559405e-5bd6-4441-bd8b-4e293ec3d15b"
// resource_type: "document"
// resource_name: "test-session-persistence"
/**
 * Test if Playwright MCP maintains session cookies across navigations
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const MCP_URL = 'http://localhost:3000/mcp/playwright';
const BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5000';
const testUser = {
  username: `sessiontest${Date.now()}`,
  email: `sessiontest${Date.now()}@test.com`,
  password: 'Test123!',
};

async function callTool(client, name, args, label) {
  console.log(`\n=== ${label || name} ===`);
  const result = await client.request({ method: 'tools/call', params: { name, arguments: args } }, null);
  if (result && result.content && result.content[0]) {
    const content = result.content[0].text || JSON.stringify(result.content[0]);
    console.log(content.substring(0, 500));
  }
  return result;
}

async function main() {
  const client = new Client({ name: 'session-test', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    // Step 1: Navigate to login page
    await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, '1. Navigate to login');

    // Step 2: Register via evaluate (stays in same context)
    await callTool(
      client,
      'browser_evaluate',
      {
        function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return 'clicked'; }",
      },
      '2. Switch to register tab',
    );

    await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const setValue = (sel, val) => { const el = document.querySelector(sel); if (el) { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); } };
          setValue('#reg-username', '${testUser.username}');
          setValue('#reg-email', '${testUser.email}');
          setValue('#reg-password', '${testUser.password}');
          setValue('#confirm-password', '${testUser.password}');
          return 'filled';
        }`,
      },
      '3. Fill registration form',
    );

    await callTool(
      client,
      'browser_evaluate',
      {
        function: "() => { document.querySelector('#register-tab .form-button')?.click(); return 'submitted'; }",
      },
      '4. Submit registration',
    );

    await callTool(client, 'browser_wait_for', { time: 2 }, '5. Wait for redirect');

    // Step 3: Check if we're logged in by looking at page URL
    const snapshotResult = await callTool(client, 'browser_snapshot', {}, '6. Check current page');
    const snapshotText = snapshotResult.content?.[0]?.text || '';
    const currentUrl = snapshotText.match(/Page URL: ([^\n]+)/)?.[1] || '';
    
    console.log(`\n📍 Current URL: ${currentUrl}`);
    
    if (currentUrl.includes('/login')) {
      console.log('❌ STILL ON LOGIN PAGE - Session not working!');
    } else {
      console.log('✅ REDIRECTED AWAY FROM LOGIN - Session might be working!');
    }

    // Step 4: Try navigating to admin page (requires auth)
    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` }, '7. Navigate to admin page');
    await callTool(client, 'browser_wait_for', { time: 1 }, '8. Wait');

    const finalSnapshot = await callTool(client, 'browser_snapshot', {}, '9. Check final page');
    const finalText = finalSnapshot.content?.[0]?.text || '';
    const finalUrl = finalText.match(/Page URL: ([^\n]+)/)?.[1] || '';

    console.log(`\n📍 Final URL: ${finalUrl}`);

    if (finalUrl.includes('/login')) {
      console.log('❌ REDIRECTED TO LOGIN - Session NOT maintained across browser_navigate!');
    } else if (finalUrl.includes('/admin/phonemes')) {
      console.log('✅ SUCCESS - Session maintained!');
    }

    await callTool(client, 'browser_close', {}, 'Close browser');
    await client.close();
  } catch (error) {
    console.error('❌ Test failed:', error.message);
    await callTool(client, 'browser_close', {}, 'Close browser on error').catch(() => {});
    await client.close();
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});


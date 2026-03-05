// resource_id: "2ff7775d-ee51-4072-b8cb-33702505de1f"
// resource_type: "document"
// resource_name: "mcp-admin-us053-test"
#!/usr/bin/env node
/**
 * US-050-053 Admin Database Tools Test - Proper MCP Tools Version
 * Uses browser_click, browser_type, browser_snapshot (like passing tests)
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5000';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

async function callTool(client, name, args = {}) {
  const result = await client.callTool({ name, arguments: args });
  console.log(`\n=== ${name} ===`);
  for (const item of result.content ?? []) {
    if (item.type === 'text') {
      const text = item.text.substring(0, 300);
      console.log(text);
    }
  }
  return result;
}

async function main() {
  const client = new Client({ name: 'us053-proper-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  const timestamp = Date.now();
  const user = {
    username: `us053test${timestamp}`,
    email: `us053test${timestamp}@example.com`,
    password: 'Test123!',
  };
  const projectName = `US053 Test ${timestamp}`;

  console.log('\n🧪 US-050-053 ADMIN DATABASE TOOLS TEST');
  console.log('========================================');
  console.log(`User: ${user.username}`);
  console.log(`Project: ${projectName}`);
  console.log(`Testing: US-053 Recalculate Phoneme Frequencies\n`);

  try {
    // Step 1: Navigate to login and get initial page structure
    await callTool(client, 'browser_navigate', { url: `${BASE}/login` });
    await callTool(client, 'browser_snapshot', {});

    // Step 2: Click Sign Up tab (ref from snapshot: e8)
    await callTool(client, 'browser_click', {
      element: 'Sign Up tab',
      ref: 'e8',
    });
    await callTool(client, 'browser_snapshot', {});

    // Step 3: Fill registration form (refs from signup tab snapshot)
    await callTool(client, 'browser_type', {
      element: 'Username textbox',
      ref: 'e38',
      text: user.username,
    });

    await callTool(client, 'browser_type', {
      element: 'Email textbox',
      ref: 'e41',
      text: user.email,
    });

    await callTool(client, 'browser_type', {
      element: 'Password textbox',
      ref: 'e44',
      text: user.password,
    });

    await callTool(client, 'browser_type', {
      element: 'Confirm Password textbox',
      ref: 'e47',
      text: user.password,
    });

    // Step 4: Submit registration (ref: e48)
    console.log('\n📝 Submitting registration...');
    await callTool(client, 'browser_click', {
      element: 'Create Account button',
      ref: 'e48',
    });

    // Wait for redirect to dashboard
    await callTool(client, 'browser_wait_for', { time: 2 });
    await callTool(client, 'browser_snapshot', {});

    // Step 5: Navigate to create project
    console.log('\n📦 Creating project...');
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
    const createSnap = await callTool(client, 'browser_snapshot', {});

    // Fill project creation form - need to get refs from snapshot
    // Use browser_evaluate as backup for form filling (not clicking)
    await callTool(client, 'browser_evaluate', {
      function: `() => {
        const name = document.querySelector('#name');
        if (name) {
          name.value = '${projectName}';
          name.dispatchEvent(new Event('input', { bubbles: true }));
        }
        const local = document.querySelector('#storage_local');
        if (local) {
          local.checked = true;
          local.dispatchEvent(new Event('change', { bubbles: true }));
        }
        return { name: name?.value, storage: 'local' };
      }`,
    });

    // Find and click Create Project button
    const snap2 = await callTool(client, 'browser_snapshot', {});
    // Look for button ref in output, or use evaluate as fallback
    await callTool(client, 'browser_evaluate', {
      function: "() => { document.querySelector('button.primary, button[type=\"submit\"]')?.click(); return 'submitted'; }",
    });

    await callTool(client, 'browser_wait_for', { time: 2 });

    // Step 6: Go to projects list
    console.log('\n📂 Entering project...');
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
    await callTool(client, 'browser_wait_for', { time: 1 });
    const projSnap = await callTool(client, 'browser_snapshot', {});

    // Click Enter button
    await callTool(client, 'browser_evaluate', {
      function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return 'clicked'; } return 'not-found'; }",
    });

    await callTool(client, 'browser_wait_for', { time: 2 });
    await callTool(client, 'browser_snapshot', {});

    // Step 7: Navigate to admin panel
    console.log('\n🛠️  Accessing admin panel...');
    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` });
    await callTool(client, 'browser_wait_for', { time: 2 });
    await callTool(client, 'browser_snapshot', {});

    // Step 8: Test US-053 endpoint
    console.log('\n🎯 Testing US-053: Recalculate Phoneme Frequencies');
    const us053Result = await callTool(client, 'browser_evaluate', {
      function: `async () => {
        try {
          const response = await fetch('/api/admin/recalculate-phoneme-frequencies', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
          });
          const data = await response.json();
          window.__us053Result = {
            status: response.status,
            ok: response.ok,
            data: data
          };
          return window.__us053Result;
        } catch (error) {
          window.__us053Result = { error: String(error) };
          return window.__us053Result;
        }
      }`,
    });

    // Extract result
    const resultText = us053Result.content?.find(p => p.type === 'text')?.text || '';
    console.log('\n📊 US-053 Response:', resultText);

    // Check for success
    const hasSuccess = resultText.includes('"success":true') || resultText.includes('success: true');
    const hasWordsProcessed = resultText.includes('words_processed') || resultText.includes('Processed');
    const has404 = resultText.includes('404') || resultText.includes('"status":404');
    const has401 = resultText.includes('401') || resultText.includes('Unauthorized');

    if (hasSuccess && hasWordsProcessed) {
      console.log('\n✅✅✅ US-053 ENDPOINT TEST: PASSED ✅✅✅');
      console.log('✅ Recalculate phoneme frequencies endpoint working correctly!');
      console.log('✅ Endpoint returns success with word statistics');
      
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(0);
      
    } else if (has404) {
      console.log('\n❌ US-053 ENDPOINT TEST: FAILED - 404 Not Found');
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(1);
      
    } else if (has401) {
      console.log('\n❌ US-053 ENDPOINT TEST: FAILED - Not Authenticated');
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(1);
      
    } else {
      console.log('\n⚠️  US-053 ENDPOINT TEST: UNCERTAIN RESULT');
      console.log('Full response:', resultText);
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(1);
    }

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
  console.error('[mcp-admin-us053-test] fatal error', err);
  process.exit(1);
});


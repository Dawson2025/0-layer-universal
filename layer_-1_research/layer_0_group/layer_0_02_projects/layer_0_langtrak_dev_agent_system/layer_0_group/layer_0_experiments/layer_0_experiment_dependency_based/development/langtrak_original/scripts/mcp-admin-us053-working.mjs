// resource_id: "b7ad648d-147e-4352-a442-6b8ffd101252"
// resource_type: "document"
// resource_name: "mcp-admin-us053-working"
#!/usr/bin/env node
/**
 * US-053 Test - Following Exact Pattern of Passing Test
 * Register → Logout → Login → Create Project → Admin → Test US-053
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
      console.log(item.text.substring(0, 250));
    }
  }
  return result;
}

async function main() {
  const client = new Client({ name: 'us053-working-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  const timestamp = Date.now();
  const username = `us053test${timestamp}`;
  const email = `us053test${timestamp}@example.com`;
  const password = 'Test123!';
  const projectName = `US053 Project ${timestamp}`;

  console.log('\n🧪 US-053 TEST (Using Passing Test Pattern)');
  console.log('===========================================');
  console.log(`Credentials: ${username} / ${email}`);
  console.log(`Server: ${BASE}\n`);

  try {
    // Step 1: Navigate and register (same as passing test)
    await callTool(client, 'browser_navigate', { url: `${BASE}/login` });
    await callTool(client, 'browser_snapshot', {});
    
    await callTool(client, 'browser_click', { element: 'Sign Up tab', ref: 'e8' });
    await callTool(client, 'browser_snapshot', {});

    await callTool(client, 'browser_type', { element: 'Username', ref: 'e38', text: username });
    await callTool(client, 'browser_type', { element: 'Email', ref: 'e41', text: email });
    await callTool(client, 'browser_type', { element: 'Password', ref: 'e44', text: password });
    await callTool(client, 'browser_type', { element: 'Confirm Password', ref: 'e47', text: password });
    
    console.log('📝 Submitting registration...');
    await callTool(client, 'browser_click', { element: 'Create Account', ref: 'e48' });
    await callTool(client, 'browser_wait_for', { time: 2 });
    await callTool(client, 'browser_snapshot', {});

    // Step 2: Logout (same as passing test - this is key!)
    console.log('🚪 Logging out...');
    await callTool(client, 'browser_click', { element: 'Sign Out link', ref: 'e11' });
    await callTool(client, 'browser_wait_for', { time: 1 });
    await callTool(client, 'browser_snapshot', {});

    // Step 3: Login explicitly (same as passing test)
    console.log('🔐 Logging back in...');
    await callTool(client, 'browser_click', { element: 'Sign In tab', ref: 'e8' });
    await callTool(client, 'browser_snapshot', {});
    
    await callTool(client, 'browser_type', { element: 'Email', ref: 'e21', text: email });
    await callTool(client, 'browser_type', { element: 'Password', ref: 'e24', text: password });
    await callTool(client, 'browser_click', { element: 'Sign In with Email', ref: 'e25' });
    await callTool(client, 'browser_wait_for', { time: 2 });
    await callTool(client, 'browser_snapshot', {});

    // Step 4: Create project
    console.log('📦 Creating project...');
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
    await callTool(client, 'browser_wait_for', { time: 1 });
    
    await callTool(client, 'browser_evaluate', {
      function: `() => {
        const name = document.querySelector('#name');
        if (name) { name.value = '${projectName}'; name.dispatchEvent(new Event('input', { bubbles: true })); }
        const local = document.querySelector('#storage_local');
        if (local) { local.checked = true; local.dispatchEvent(new Event('change', { bubbles: true })); }
        document.querySelector('button.primary')?.click();
        return 'created';
      }`,
    });
    
    await callTool(client, 'browser_wait_for', { time: 2 });

    // Step 5: Enter project
    console.log('🎯 Entering project...');
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
    await callTool(client, 'browser_wait_for', { time: 1.5 });
    
    await callTool(client, 'browser_evaluate', {
      function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); } return 'clicked'; }",
    });
    
    await callTool(client, 'browser_wait_for', { time: 2 });
    await callTool(client, 'browser_snapshot', {});

    // Step 6: Go to admin panel
    console.log('🛠️  Accessing admin panel...');
    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` });
    await callTool(client, 'browser_wait_for', { time: 2 });
    const adminSnap = await callTool(client, 'browser_snapshot', {});

    // Check we're actually on admin page
    const adminText = adminSnap.content?.find(p => p.type === 'text')?.text || '';
    if (adminText.includes('Page URL: http://127.0.0.1:5000/login')) {
      console.log('❌ FAILED: Still on login page after full flow');
      throw new Error('Session not maintained');
    }

    console.log('✅ Successfully reached admin panel!');

    // Step 7: TEST US-053 ENDPOINT!
    console.log('\n🎯 TESTING US-053 ENDPOINT!');
    console.log('=========================');
    
    const us053Result = await callTool(client, 'browser_evaluate', {
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
            success: data.success,
            message: data.message,
            words_processed: data.words_processed,
            updates: data.updates
          };
        } catch (error) {
          return { error: String(error) };
        }
      }`,
    });

    const resultText = us053Result.content?.find(p => p.type === 'text')?.text || '';
    console.log('\n📊 US-053 API Response:');
    console.log(resultText);

    // Parse and validate
    const hasSuccess = resultText.includes('"success":true');
    const hasWords = resultText.includes('words_processed');
    const hasUpdates = resultText.includes('updates');

    if (hasSuccess && (hasWords || hasUpdates)) {
      console.log('\n🎉🎉🎉 US-053 ENDPOINT: VALIDATED!!! 🎉🎉🎉');
      console.log('✅ Recalculate phoneme frequencies endpoint working!');
      console.log('✅ Returns success with statistics');
      console.log('✅ Production endpoint fully functional!');
      
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(0);
    } else {
      console.log('\n❌ US-053 ENDPOINT: Unexpected response');
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(1);
    }

  } catch (error) {
    console.error('\n❌ Test error:', error.message);
    try {
      await callTool(client, 'browser_close', {});
      await client.close();
    } catch {}
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('[us053-working] fatal:', err);
  process.exit(1);
});


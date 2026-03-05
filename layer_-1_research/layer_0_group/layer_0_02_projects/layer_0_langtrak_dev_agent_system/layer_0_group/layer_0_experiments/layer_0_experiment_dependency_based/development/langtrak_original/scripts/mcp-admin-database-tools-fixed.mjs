// resource_id: "3cef69f4-50a2-4a8b-85c1-05f72aa76d0c"
// resource_type: "document"
// resource_name: "mcp-admin-database-tools-fixed"
#!/usr/bin/env node
/**
 * US-050-053: Admin Database Tools
 * FIXED VERSION: Uses window.location.href instead of browser_navigate to preserve session cookies
 */

const BASE = process.env.APP_BASE_URL ?? 'http://127.0.0.1:5000';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

// Test user
const user = {
  username: `admin${Date.now()}`,
  email: `admin${Date.now()}@test.com`,
  password: 'Test123!',
};

// Project name
const projectName = `AdminProject${Date.now()}`;

console.log(`[mcp-admin-database-tools] Starting`);
console.log(`  User: ${user.username}`);
console.log(`  Project: ${projectName}`);

async function main() {
  // Import MCP client dynamically
  const { Client } = await import('@modelcontextprotocol/sdk/client/index.js');
  const { StreamableHTTPClientTransport } = await import(
    '@modelcontextprotocol/sdk/client/streamableHttp.js'
  );

  const client = new Client({
    name: 'admin-test',
    version: '1.0.0',
  });

  const transport = new StreamableHTTPClientTransport(new URL(MCP_URL));
  await client.connect(transport);

  try {
    console.log('\n🔐 Registering user...');
    
    // Navigate to login page
    await client.request(
      { method: 'tools/call', params: { name: 'browser_navigate', arguments: { url: `${BASE}/login` } } },
      null,
    );
    await sleep(1);

    // Switch to register tab and fill form
    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: { function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); }" },
        },
      },
      null,
    );
    await sleep(0.5);

    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: {
            function: `() => {
              const set = (sel, val) => { const el = document.querySelector(sel); if (el) { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); } };
              set('#reg-username', '${user.username}');
              set('#reg-email', '${user.email}');
              set('#reg-password', '${user.password}');
              set('#confirm-password', '${user.password}');
            }`,
          },
        },
      },
      null,
    );

    // Submit and wait for redirect
    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: { function: "() => { document.querySelector('#register-tab .form-button')?.click(); }" },
        },
      },
      null,
    );
    await sleep(3); // Wait for registration and auto-redirect

    console.log('✅ Registered');

    // Create project using window.location (stays in same context)
    console.log('\n📁 Creating project...');
    
    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: { function: `() => { window.location.href = '${BASE}/projects/create'; }` },
        },
      },
      null,
    );
    await sleep(2);

    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: {
            function: `() => {
              const name = document.querySelector('#name');
              if (name) { name.value = '${projectName}'; name.dispatchEvent(new Event('input', { bubbles: true })); }
              const local = document.querySelector('#storage_local');
              if (local) { local.checked = true; local.dispatchEvent(new Event('change', { bubbles: true })); }
            }`,
          },
        },
      },
      null,
    );
    await sleep(0.5);

    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: { function: "() => { document.querySelector('button.button.primary')?.click(); }" },
        },
      },
      null,
    );
    await sleep(2);

    console.log('✅ Project created');

    // Enter project
    console.log('\n🚪 Entering project...');
    
    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: { function: `() => { window.location.href = '${BASE}/projects'; }` },
        },
      },
      null,
    );
    await sleep(1.5);

    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: { function: "() => { document.querySelector('a.action-button.enter')?.click(); }" },
        },
      },
      null,
    );
    await sleep(2);

    console.log('✅ Entered project');

    // Navigate to admin phonemes page
    console.log('\n🔧 Accessing admin phoneme panel...');
    
    await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: { function: `() => { window.location.href = '${BASE}/admin/phonemes'; }` },
        },
      },
      null,
    );
    await sleep(2);

    // Check we're on the admin page (not redirected to login)
    const snapshot1 = await client.request(
      { method: 'tools/call', params: { name: 'browser_snapshot', arguments: {} } },
      null,
    );
    const pageText1 = snapshot1.content?.[0]?.text || '';
    
    if (pageText1.includes('Login') || pageText1.includes('Sign in')) {
      throw new Error('❌ Redirected to login page - session not maintained!');
    }

    console.log('✅ On admin phoneme page');

    // Test US-053: Recalculate phoneme frequencies
    console.log('\n🧮 Testing US-053: Recalculate phoneme frequencies...');
    
    const recalcResult = await client.request(
      {
        method: 'tools/call',
        params: {
          name: 'browser_evaluate',
          arguments: {
            function: `async () => {
              const response = await fetch('${BASE}/api/admin/recalculate-phoneme-frequencies', {
                method: 'POST',
                credentials: 'include',
              });
              const data = await response.json();
              return JSON.stringify(data);
            }`,
          },
        },
      },
      null,
    );

    const recalcData = JSON.parse(recalcResult.content?.[0]?.text || '{}');
    
    if (recalcData.success) {
      console.log(`✅ US-053 PASSED: ${recalcData.message}`);
    } else {
      throw new Error(`❌ US-053 FAILED: ${recalcData.error || 'Unknown error'}`);
    }

    // Close browser
    await client.request({ method: 'tools/call', params: { name: 'browser_close', arguments: {} } }, null);
    await client.close();

    console.log('\n✅ ALL TESTS PASSED');
    process.exit(0);
  } catch (error) {
    console.error('\n❌ TEST FAILED:', error.message);
    try {
      await client.callTool('browser_close', {});
    } catch {}
    await client.close();
    process.exit(1);
  }
}

function sleep(seconds) {
  return new Promise((resolve) => setTimeout(resolve, seconds * 1000));
}

main();

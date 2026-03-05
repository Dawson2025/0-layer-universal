// resource_id: "64dec4a8-f44d-4495-9d02-2f83bcbea9bd"
// resource_type: "document"
// resource_name: "mcp-admin-complete-test"
#!/usr/bin/env node
/**
 * Complete Admin Test with US-053 Validation
 * Uses proper MCP browser tools with dynamic ref extraction
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
      const text = item.text.substring(0, 400);
      console.log(text);
    }
  }
  return result;
}

// Extract specific ref from snapshot output
function findRef(snapResult, searchText) {
  const text = snapResult.content?.find(p => p.type === 'text')?.text || '';
  const lines = text.split('\n');
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.toLowerCase().includes(searchText.toLowerCase())) {
      const refMatch = line.match(/\[ref=(e\d+)\]/);
      if (refMatch) {
        return refMatch[1];
      }
      // Check next line too
      if (i + 1 < lines.length) {
        const nextLine = lines[i + 1];
        const nextRefMatch = nextLine.match(/\[ref=(e\d+)\]/);
        if (nextRefMatch) {
          return nextRefMatch[1];
        }
      }
    }
  }
  return null;
}

async function main() {
  const client = new Client({ name: 'admin-complete-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  const timestamp = Date.now();
  const user = {
    username: `admintest${timestamp}`,
    email: `admintest${timestamp}@example.com`,
    password: 'Test123!',
  };
  const projectName = `Admin Test ${timestamp}`;

  console.log('\n🧪 COMPLETE ADMIN TEST WITH US-053');
  console.log('====================================');
  console.log(`User: ${user.username}`);
  console.log(`Server: ${BASE}\n`);

  try {
    // PHASE 1: REGISTRATION
    console.log('\n📝 PHASE 1: User Registration');
    await callTool(client, 'browser_navigate', { url: `${BASE}/login` });
    let snap = await callTool(client, 'browser_snapshot', {});

    // Click Sign Up tab
    let signupRef = findRef(snap, 'Sign Up');
    if (!signupRef) signupRef = 'e8'; // Fallback to known ref
    
    await callTool(client, 'browser_click', {
      element: 'Sign Up tab',
      ref: signupRef,
    });
    snap = await callTool(client, 'browser_snapshot', {});

    // Fill registration - use fixed refs from passing test
    await callTool(client, 'browser_type', {
      element: 'Username field',
      ref: 'e38',
      text: user.username,
    });

    await callTool(client, 'browser_type', {
      element: 'Email field',
      ref: 'e41',
      text: user.email,
    });

    await callTool(client, 'browser_type', {
      element: 'Password field',
      ref: 'e44',
      text: user.password,
    });

    await callTool(client, 'browser_type', {
      element: 'Confirm Password field',
      ref: 'e47',
      text: user.password,
    });

    // Submit registration
    await callTool(client, 'browser_click', {
      element: 'Create Account button',
      ref: 'e48',
    });

    await callTool(client, 'browser_wait_for', { time: 3 });
    snap = await callTool(client, 'browser_snapshot', {});

    console.log('✅ Registration phase complete');

    // PHASE 2: CREATE PROJECT
    console.log('\n📦 PHASE 2: Project Creation');
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
    await callTool(client, 'browser_wait_for', { time: 1 });
    snap = await callTool(client, 'browser_snapshot', {});

    // Fill project form
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
        return 'filled';
      }`,
    });

    snap = await callTool(client, 'browser_snapshot', {});
    
    // Find and click submit button
    const submitRef = findRef(snap, 'Create Project') || findRef(snap, 'Submit') || findRef(snap, 'button');
    if (submitRef) {
      await callTool(client, 'browser_click', {
        element: 'Create Project button',
        ref: submitRef,
      });
    } else {
      // Fallback
      await callTool(client, 'browser_evaluate', {
        function: "() => { document.querySelector('button.primary')?.click(); return 'clicked'; }",
      });
    }

    await callTool(client, 'browser_wait_for', { time: 2 });
    console.log('✅ Project creation complete');

    // PHASE 3: ENTER PROJECT
    console.log('\n🎯 PHASE 3: Enter Project');
    await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
    await callTool(client, 'browser_wait_for', { time: 1.5 });
    snap = await callTool(client, 'browser_snapshot', {});

    const enterRef = findRef(snap, 'Enter');
    if (enterRef) {
      await callTool(client, 'browser_click', {
        element: 'Enter project button',
        ref: enterRef,
      });
    } else {
      await callTool(client, 'browser_evaluate', {
        function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return 'clicked'; } return 'not-found'; }",
      });
    }

    await callTool(client, 'browser_wait_for', { time: 2 });
    snap = await callTool(client, 'browser_snapshot', {});
    console.log('✅ Project entered - on main menu');

    // PHASE 4: ACCESS ADMIN PANEL
    console.log('\n🛠️  PHASE 4: Access Admin Panel');
    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` });
    await callTool(client, 'browser_wait_for', { time: 2 });
    snap = await callTool(client, 'browser_snapshot', {});

    // Check if we're actually on admin page
    const snapText = snap.content?.find(p => p.type === 'text')?.text || '';
    if (snapText.includes('/login')) {
      console.log('❌ Still on login page - authentication failed');
      console.log('This means the session was not established properly');
      throw new Error('Authentication failed - stuck at login');
    }

    console.log('✅ Admin panel accessed');

    // PHASE 5: TEST US-053 ENDPOINT  
    console.log('\n🎯 PHASE 5: Test US-053 Endpoint');
    const us053Result = await callTool(client, 'browser_evaluate', {
      function: `async () => {
        try {
          console.log('Calling US-053 endpoint...');
          const response = await fetch('/api/admin/recalculate-phoneme-frequencies', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
          });
          console.log('Response status:', response.status);
          const data = await response.json();
          console.log('Response data:', data);
          return {
            status: response.status,
            ok: response.ok,
            data: data
          };
        } catch (error) {
          console.error('Fetch error:', error);
          return { error: String(error), stack: error.stack };
        }
      }`,
    });

    const resultText = us053Result.content?.find(p => p.type === 'text')?.text || '';
    console.log('\n📊 US-053 Full Response:');
    console.log(resultText);

    // Validate success
    const hasSuccess = resultText.includes('"success":true');
    const hasWordsProcessed = resultText.includes('words_processed');
    const hasMessage = resultText.includes('Phoneme frequencies recalculated');

    if (hasSuccess || hasWordsProcessed || hasMessage) {
      console.log('\n✅✅✅ US-053 ENDPOINT TEST: PASSED ✅✅✅');
      console.log('✅ Recalculate phoneme frequencies endpoint working!');
      console.log('✅ Returns success with statistics');
      
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(0);
    } else {
      console.log('\n❌ US-053 ENDPOINT TEST: DID NOT PASS');
      console.log('Response did not contain expected success indicators');
      
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(1);
    }

  } catch (error) {
    console.error('\n❌ Test failed:', error.message);
    try {
      await callTool(client, 'browser_close', {});
      await client.close();
    } catch {}
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('[mcp-admin-complete-test] fatal', err);
  process.exit(1);
});


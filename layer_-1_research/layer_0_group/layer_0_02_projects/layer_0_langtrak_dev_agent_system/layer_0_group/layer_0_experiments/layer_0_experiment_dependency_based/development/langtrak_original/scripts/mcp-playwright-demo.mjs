// resource_id: "50df7e18-dd2c-4e60-8935-1f01b8ec0e87"
// resource_type: "document"
// resource_name: "mcp-playwright-demo"
#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

async function callTool(client, name, args = {}) {
  const result = await client.callTool({ name, arguments: args });
  console.log(`\n=== ${name} (${JSON.stringify(args)}) ===`);
  for (const item of result.content ?? []) {
    if (item.type === 'text') console.log(item.text);
    else console.log(item);
  }
  console.log('=== end ===\n');
  return result;
}

async function main() {
  const client = new Client({ name: 'codex-cli', version: '0.1.0' }, { capabilities: {} });
  const transport = new StreamableHTTPClientTransport(new URL(BASE_URL));
  await client.connect(transport);

  const APP_BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
  
  await callTool(client, 'browser_tabs', { action: 'list' });
  await callTool(client, 'browser_navigate', { url: `${APP_BASE}/login` });
  await callTool(client, 'browser_snapshot', {});
  await callTool(client, 'browser_click', {
    element: 'Sign Up tab',
    ref: 'e8',
  });
  await callTool(client, 'browser_snapshot', {});

  const timestamp = Date.now();
  const username = `testuser${timestamp}`;
  const email = `test${timestamp}@example.com`;
  const password = 'Test123!';
  console.log(`credentials: ${JSON.stringify({ username, email, password })}`);

  await callTool(client, 'browser_type', {
    element: 'Username textbox',
    ref: 'e38',
    text: username,
  });
  await callTool(client, 'browser_type', {
    element: 'Email textbox',
    ref: 'e41',
    text: email,
  });
  await callTool(client, 'browser_type', {
    element: 'Password textbox',
    ref: 'e44',
    text: password,
  });
  await callTool(client, 'browser_type', {
    element: 'Confirm Password textbox',
    ref: 'e47',
    text: password,
  });
  await callTool(client, 'browser_click', {
    element: 'Create Account button',
    ref: 'e48',
  });
  await callTool(client, 'browser_snapshot', {});
  await callTool(client, 'browser_click', {
    element: 'Sign Out link',
    ref: 'e11',
  });
  await callTool(client, 'browser_snapshot', {});
  await callTool(client, 'browser_click', {
    element: 'Sign In tab',
    ref: 'e8',
  });
  await callTool(client, 'browser_type', {
    element: 'Email textbox',
    ref: 'e21',
    text: email,
  });
  await callTool(client, 'browser_type', {
    element: 'Password textbox',
    ref: 'e24',
    text: password,
  });
  await callTool(client, 'browser_click', {
    element: 'Sign In with Email button',
    ref: 'e25',
  });
  await callTool(client, 'browser_snapshot', {});
  await callTool(client, 'browser_navigate', { url: `${APP_BASE}/dashboard` });
  await callTool(client, 'browser_snapshot', {});
  await callTool(client, 'browser_navigate', { url: `${APP_BASE}/projects` });
  await callTool(client, 'browser_snapshot', {});
  await callTool(client, 'browser_navigate', { url: `${APP_BASE}/login` });
  await callTool(client, 'browser_snapshot', {});

  await callTool(client, 'browser_close', {});
  await client.close();
}

main().catch((err) => {
  console.error('[mcp-playwright-demo] failed', err);
  process.exit(1);
});

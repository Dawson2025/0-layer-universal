#!/usr/bin/env node
// Full MCP handshake using Playwright's MCP Client to open a page and print a short result.
const cp = require('child_process');
const net = require('net');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const HELPER = path.join(ROOT, 'scripts', 'mcp-start.sh');
const PORT = process.env.MCP_PORT ? Number(process.env.MCP_PORT) : 9234;
let helperProc = null;

function waitForPort(port, host = '127.0.0.1', timeout = 15000) {
  const start = Date.now();
  return new Promise((resolve, reject) => {
    (function check() {
      const sock = new net.Socket();
      sock.setTimeout(500);
      sock.once('error', () => {
        sock.destroy();
        if (Date.now() - start > timeout) return reject(new Error('timeout'));
        setTimeout(check, 200);
      });
      sock.once('timeout', () => {
        sock.destroy();
        if (Date.now() - start > timeout) return reject(new Error('timeout'));
        setTimeout(check, 200);
      });
      sock.once('connect', () => {
        sock.end();
        resolve();
      });
      sock.connect(port, host);
    })();
  });
}

function startHelper() {
  helperProc = cp.spawn('bash', [HELPER, '--port', String(PORT)], {
    detached: true,
    stdio: ['ignore', 'ignore', 'inherit'],
  });
  return helperProc.pid;
}

async function run() {
  const pid = startHelper();
  console.log('Started helper pid', pid);
  await waitForPort(PORT);
  console.log('Port open; creating MCP client');

  // Use Playwright's MCP client classes directly from the packaged SDK bundle.
  const mcpBundle = require('playwright/lib/mcp/sdk/bundle');

  const Client = mcpBundle.Client;
  const StreamableHTTPClientTransport = mcpBundle.StreamableHTTPClientTransport;

  const client = new Client({ name: 'mcp-handshake-test', version: '0.0.0' }, { capabilities: { roots: {} } });
  const transport = new StreamableHTTPClientTransport(new URL(`http://127.0.0.1:${PORT}/mcp`));

  try {
    await client.connect(transport);
    console.log('Connected to MCP server');

    const { tools } = await client.listTools();
    console.log('Available tools:', Array.isArray(tools) ? tools.map(t => t.name).slice(0, 20) : tools);

    // Call the browser navigation tool as a simple smoke check. If tools are namespaced,
    // 'browser_navigate' is present in Playwright's toolset (see lib/mcp/browser/tools).
    const toolName = 'browser_navigate';
    const hasNavigate = tools && tools.find && tools.find(t => t.name === toolName);
    if (!hasNavigate) {
      console.warn('browser_navigate tool not found; aborting callTool step');
    } else {
      console.log(`Calling tool ${toolName} -> navigate to https://example.com`);
      let result = await client.callTool({ name: toolName, arguments: { url: 'https://example.com' } });
      console.log('callTool result (summary):', {
        isError: result.isError,
        contentLength: Array.isArray(result.content) ? result.content.length : undefined
      });
      // If the server responded with an instruction to install browsers, offer to do it
      const textContent = Array.isArray(result.content) ? result.content.map(p => p.type === 'text' ? p.text : '').join('\n') : '';
      const needsInstall = /install (chrome|chromium)/i.test(textContent) || /Run "npx playwright install/i.test(textContent);
      if (needsInstall) {
        console.warn('Server indicates browser distribution is missing.');
        if (process.env.MCP_ALLOW_INSTALL === '1') {
          console.log('MCP_ALLOW_INSTALL=1 detected — invoking browser_install tool to fetch the browser. This may download large files.');
          try {
            const installResult = await client.callTool({ name: 'browser_install', arguments: {} });
            console.log('browser_install result:', { isError: installResult.isError, contentLength: Array.isArray(installResult.content) ? installResult.content.length : undefined });
            // Try navigate again
            result = await client.callTool({ name: toolName, arguments: { url: 'https://example.com' } });
            console.log('Retry callTool result (summary):', { isError: result.isError });
          } catch (e) {
            console.error('browser_install call failed:', e && (e.stack || e.message || e));
          }
        } else {
          console.log('To allow this script to auto-install the missing browser, re-run with:');
          console.log('  MCP_ALLOW_INSTALL=1 node scripts/mcp-handshake-node-full.cjs');
        }
      }

      // Print any text snippets that came back in content
      if (Array.isArray(result.content)) {
        for (const part of result.content) {
          if (part.type === 'text') console.log(part.text.substring(0, 400));
        }
      }
    }

    // Graceful teardown of client and transport
    try { await transport.terminateSession(); } catch (e) {}
    try { await client.close(); } catch (e) {}
  } finally {
    try { process.kill(-helperProc.pid, 'SIGTERM'); } catch (e) {}
  }
}

run().catch(e => {
  console.error('handshake failed:', e && (e.stack || e.message || e));
  try { process.kill(-helperProc.pid, 'SIGTERM'); } catch (e) {}
  process.exit(2);
});

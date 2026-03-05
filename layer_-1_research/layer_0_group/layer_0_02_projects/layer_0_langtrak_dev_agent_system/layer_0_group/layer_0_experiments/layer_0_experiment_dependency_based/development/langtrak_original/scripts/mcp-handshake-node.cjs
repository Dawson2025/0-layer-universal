// resource_id: "b0831a9e-7503-4542-8ccb-8dca58756639"
// resource_type: "document"
// resource_name: "mcp-handshake-node"
#!/usr/bin/env node
// Diagnostic script to probe @playwright/mcp.createConnection at runtime.
const cp = require('child_process');
const net = require('net');
const path = require('path');

// Minimal diagnostic to exercise @playwright/mcp.createConnection
const ROOT = path.resolve(__dirname, '..');
const HELPER = path.join(ROOT, 'scripts', 'mcp-start.sh');
const PORT = process.env.MCP_PORT ? Number(process.env.MCP_PORT) : 9234;
let helperProc = null;

function waitForPort(port, host = '127.0.0.1', timeout = 10000) {
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

async function main() {
  const pid = startHelper();
  console.log('Started helper pid', pid);
  await waitForPort(PORT, '127.0.0.1', 15000);
  console.log('Port open, requiring @playwright/mcp');
  let pkg;
  try {
    pkg = require('@playwright/mcp');
  } catch (e) {
    console.error('require failed:', e && e.message);
    try { process.kill(-helperProc.pid, 'SIGTERM'); } catch (e) {}
    process.exit(2);
  }
  console.log('pkg keys', Object.keys(pkg));
  if (typeof pkg.createConnection !== 'function') {
    console.error('createConnection not present');
    try { process.kill(-helperProc.pid, 'SIGTERM'); } catch (e) {}
    return;
  }
  try {
    const conn = await pkg.createConnection({ url: `http://127.0.0.1:${PORT}/mcp` });
    console.log('createConnection returned type:', typeof conn);
    if (conn && typeof conn === 'object') console.log('conn keys:', Object.keys(conn));
  } catch (e) {
    console.error('createConnection failed:', e && e.message);
  } finally {
    try { process.kill(-helperProc.pid, 'SIGTERM'); } catch (e) {}
  }
}

main().catch(e => { console.error(e); process.exit(2); });
        try { process.kill(-helperProc.pid, 'SIGTERM'); } catch (e) {}

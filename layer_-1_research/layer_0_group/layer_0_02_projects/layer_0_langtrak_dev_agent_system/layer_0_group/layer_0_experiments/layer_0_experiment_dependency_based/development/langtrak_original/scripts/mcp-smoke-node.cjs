#!/usr/bin/env node
// Simple Node smoke test for Playwright MCP server (CommonJS)
const child_process = require('child_process');
const http = require('http');

const PORT = process.env.PORT || 9234;
const HOST = process.env.HOST || '127.0.0.1';

function startServer() {
  const args = ['scripts/mcp-start.sh', '--port', PORT.toString()];
  const proc = child_process.spawn('bash', args, { stdio: ['ignore', 'ignore', 'ignore'], detached: true });
  proc.unref();
  return proc.pid;
}

function waitForPort(port, host, timeout = 20000) {
  const start = Date.now();
  return new Promise((resolve, reject) => {
    (function check() {
      const req = http.request({ method: 'GET', host, port, path: '/', timeout: 1000 }, res => {
        res.resume();
        resolve();
      });
      req.on('error', () => {
        if (Date.now() - start > timeout) return reject(new Error('timeout'));
        setTimeout(check, 500);
      });
      req.end();
    })();
  });
}

function smokeTest(port, host) {
  return new Promise((resolve, reject) => {
    const req = http.get({ host, port, path: '/mcp', timeout: 5000 }, res => {
      let data = '';
      res.on('data', chunk => data += chunk.toString());
      res.on('end', () => resolve(data));
    });
    req.on('error', reject);
  });
}

(async () => {
  console.log(`Starting MCP server helper on ${HOST}:${PORT}...`);
  const pid = startServer();
  console.log(`Helper started (pid=${pid}), waiting for port...`);
  try {
    await waitForPort(PORT, HOST);
  } catch (e) {
    console.error('Timed out waiting for port', e.message);
    process.exit(2);
  }
  console.log('Port is listening, performing smoke test against /mcp');
  try {
    const resp = await smokeTest(PORT, HOST);
    console.log('Response:', resp.slice(0, 200));
    if (/invalid request/i.test(resp)) {
      console.log('✅ Node smoke test passed');
      process.exit(0);
    } else {
      console.error('❌ Node smoke test failed: unexpected response');
      process.exit(3);
    }
  } catch (err) {
    console.error('Error during smoke test:', err.message);
    process.exit(4);
  } finally {
    try { process.kill(pid); } catch (e) {}
  }
})();

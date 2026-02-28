#!/usr/bin/env node
/**
 * Orchestrator: start Playwright MCP server (Chromium), run user-story automations,
 * then stop the server. Cross-platform (Windows/WSL/macOS/Linux).
 */
import { spawn } from 'node:child_process';
import http from 'node:http';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = path.resolve(__dirname, '..');

const MCP_PORT = process.env.MCP_PORT ? Number(process.env.MCP_PORT) : 9234;
const MCP_HOST = process.env.MCP_HOST || '127.0.0.1';
const MCP_URL = `http://${MCP_HOST}:${MCP_PORT}/mcp`;

const STORIES = (
  process.env.STORIES?.split(',').map((s) => s.trim()).filter(Boolean) || [
    'scripts/mcp-projects-flow-realistic.mjs',
    'scripts/mcp-phoneme-admin-realistic.mjs',
    'scripts/mcp-phonemes-flat-realistic.mjs',
    'scripts/mcp-tts-experience.mjs',
    'scripts/mcp-word-media.mjs',
  ]
).map((p) => path.resolve(PROJECT_ROOT, p));

function waitForPort(port, host, timeoutMs = 30000) {
  const start = Date.now();
  return new Promise((resolve, reject) => {
    (function probe() {
      const req = http.request({ host, port, path: '/mcp', method: 'GET', timeout: 1000 }, (res) => {
        // Any response means server is up (even error)
        res.resume();
        resolve(true);
      });
      req.on('error', () => {
        if (Date.now() - start > timeoutMs) return reject(new Error('timeout waiting for MCP server'));
        setTimeout(probe, 500);
      });
      req.end();
    })();
  });
}

async function runStory(scriptPath, env = {}) {
  console.log(`\n▶ Running story: ${path.relative(PROJECT_ROOT, scriptPath)}`);
  await new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [scriptPath], {
      cwd: PROJECT_ROOT,
      stdio: 'inherit',
      env: { ...process.env, MCP_URL, ...env },
    });
    child.on('exit', (code, signal) => {
      if (signal) return reject(new Error(`terminated by signal ${signal}`));
      if (code !== 0) return reject(new Error(`exit ${code}`));
      resolve();
    });
  });
}

async function installAndOpen(client, baseUrl) {
  // Ensure Chromium bundle is installed
  try {
    await client.callTool({ name: 'browser_install', arguments: {} });
  } catch {}
  // Open a page so tools have a target
  await client.callTool({ name: 'browser_navigate', arguments: { url: baseUrl } });
}

async function portResponds() {
  try {
    await waitForPort(MCP_PORT, MCP_HOST, 2000);
    return true;
  } catch {
    return false;
  }
}

async function main() {
  // Start MCP server via npx @playwright/mcp (only if not already running)
  console.log(`Ensuring Playwright MCP on ${MCP_HOST}:${MCP_PORT}...`);
  const alreadyRunning = await portResponds();
  let startedMcp = false;
  let mcp;
  if (!alreadyRunning) {
    console.log(`Starting Playwright MCP on ${MCP_HOST}:${MCP_PORT}...`);
    const npxArgs = [
      '-y',
      '@playwright/mcp@latest',
      '--port', String(MCP_PORT),
      '--host', MCP_HOST,
      '--headless',
      '--browser', 'chromium',
      '--isolated'
    ];
    mcp = spawn(
      process.platform === 'win32' ? (process.env.ComSpec || 'cmd.exe') : 'npx',
      process.platform === 'win32' ? ['/c', 'npx', ...npxArgs] : npxArgs,
      {
        cwd: process.platform === 'win32' ? process.env.USERPROFILE || process.cwd() : PROJECT_ROOT,
        stdio: ['ignore', 'inherit', 'inherit'],
        env: { ...process.env, PLAYWRIGHT_BROWSERS_PATH: '0' },
      }
    );
    startedMcp = true;
  } else {
    console.log('Detected existing MCP server; reusing it.');
  }

  let ok = false;
  try {
    await waitForPort(MCP_PORT, MCP_HOST, 45000);
    ok = true;
  } catch (err) {
    console.error('Failed to detect MCP server:', err.message);
  }

  if (!ok) {
    try { if (startedMcp && mcp) mcp.kill(); } catch {}
    process.exit(2);
  }

  // Prepare MCP client and ensure browser is installed/open
  const baseHost = process.env.APP_BASE_URL || (process.platform === 'win32' ? 'http://wsl.localhost:5002' : 'http://127.0.0.1:5002');
  const baseUrl = `${baseHost}/login`;
  const client = new Client({ name: 'stories-orchestrator', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));
  await installAndOpen(client, baseUrl);

  // Run stories in order
  for (const story of STORIES) {
    await runStory(story, { APP_BASE_URL: baseHost });
  }

  await client.close();

// Stop server
  try { if (typeof mcp !== 'undefined' && mcp && startedMcp) mcp.kill(); } catch {}
  console.log('\n✅ All stories completed successfully.');
}

main().catch((err) => {
  console.error('\n❌ Automation failed:', err?.message || err);
  process.exit(1);
});
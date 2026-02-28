#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

const BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `ttsuser${timestamp}`,
  email: `ttsuser${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `TTS Project ${timestamp}`;

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'tts-experience', `${timestamp}`);
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

function textFromResult(result) {
  return (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text)
    .join('\n');
}

function normalizeCliJson(raw) {
  if (!raw) return null;
  let text = raw.trim();
  text = text.replace(/^### Result\s*/i, '').trim();
  if (text.startsWith('```')) {
    text = text.replace(/^```(?:json)?/i, '').replace(/```$/i, '').trim();
  }
  const nextSection = text.indexOf('\n###');
  if (nextSection !== -1) {
    text = text.slice(0, nextSection).trim();
  }

  const tryParse = (candidate) => {
    if (!candidate) return null;
    try {
      return JSON.parse(candidate);
    } catch {
      return null;
    }
  };

  let parsed = tryParse(text);

  if (parsed === null && (text.includes('{') || text.includes('['))) {
    const firstBrace = text.indexOf('{');
    const firstBracket = text.indexOf('[');
    const startIdx = (() => {
      if (firstBrace === -1) return firstBracket;
      if (firstBracket === -1) return firstBrace;
      return Math.min(firstBrace, firstBracket);
    })();
    if (startIdx !== -1) {
      text = text.slice(startIdx);
      const endBrace = text.lastIndexOf('}');
      const endBracket = text.lastIndexOf(']');
      const endIdx = Math.max(endBrace, endBracket);
      if (endIdx !== -1) {
        text = text.slice(0, endIdx + 1);
        parsed = tryParse(text);
      }
    }
  }

  if (typeof parsed === 'string') {
    const inner = tryParse(parsed);
    if (inner !== null) parsed = inner;
  }

  if (parsed === null) {
    throw new Error(`Unable to parse CLI JSON payload: ${raw}`);
  }

  return parsed;
}

async function callTool(client, name, args, label, summary) {
  const result = await client.callTool({ name, arguments: args });
  if (label) {
    console.log(`\n=== ${label} ===`);
    const text = textFromResult(result);
    if (text) console.log(text.trim());
  }
  if (summary) {
    summary.steps.push({
      action: label || name,
      args,
      response: textFromResult(result),
    });
  }
  return result;
}

async function browserFetchJSON(client, expression) {
  await client.callTool({
    name: 'browser_evaluate',
    arguments: { function: `async () => { window.__mcpPayload = await (${expression}); return true; }` },
  });
  const result = await client.callTool({
    name: 'browser_evaluate',
    arguments: { function: "() => JSON.stringify(window.__mcpPayload ?? null)" },
  });
  const text = textFromResult(result);
  if (!text) return null;
  return normalizeCliJson(text);
}

async function injectPlaywrightHelpers(client) {
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: `() => {
        window.__ttsPlaybackLog = window.__ttsPlaybackLog || [];
        window.__mcpNotifications = window.__mcpNotifications || [];
        const originalShowMessage = window.showMessage;
        if (!window.__showMessagePatched && typeof originalShowMessage === 'function') {
          window.showMessage = function(message, level) {
            window.__mcpNotifications.push({ message, level, timestamp: Date.now() });
            return originalShowMessage.call(this, message, level);
          };
          window.__showMessagePatched = true;
        }
        return {
          playbackCount: window.__ttsPlaybackLog.length,
          notifications: window.__mcpNotifications.length,
        };
      }`,
    },
  });
}

async function registerAndEnterProject(client, summary) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Navigate to login', summary);
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return true; }" },
    'Switch to registration',
    summary,
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const setValue = (selector, value) => {
          const el = document.querySelector(selector);
          if (el) { el.value = value; el.dispatchEvent(new Event('input', { bubbles: true })); }
        };
        setValue('#reg-username', '${user.username}');
        setValue('#reg-email', '${user.email}');
        setValue('#reg-password', '${user.password}');
        setValue('#confirm-password', '${user.password}');
        return true;
      }`,
    },
    'Fill registration form',
    summary,
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelector('#register-tab .form-button')?.click(); return true; }" },
    'Submit registration',
    summary,
  );
  await callTool(client, 'browser_snapshot', {}, 'Snapshot after registration', summary);

  await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, 'Navigate to create project', summary);
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const name = document.querySelector('#name');
        if (name) { name.value = '${projectName}'; name.dispatchEvent(new Event('input', { bubbles: true })); }
        const local = document.querySelector('#storage_local');
        if (local) { local.checked = true; local.dispatchEvent(new Event('change', { bubbles: true })); }
        document.querySelector('button.button.primary')?.click();
        return true;
      }`,
    },
    'Create local project',
    summary,
  );
  await callTool(client, 'browser_snapshot', {}, 'Snapshot after project creation', summary);

  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Projects list', summary);
  await callTool(
    client,
    'browser_evaluate',
    {
      function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return enter.href || 'clicked'; } return 'not-found'; }",
    },
    'Enter project',
    summary,
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after entering project', summary);
  await callTool(client, 'browser_snapshot', {}, 'Main menu snapshot', summary);
}

async function navigateToWordsUI(client, summary) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/words/create` }, 'Open word creation UI', summary);
  await client.callTool({
    name: 'browser_evaluate',
    arguments: {
      function: `() => {
        if (typeof initializeAudio === 'function') { initializeAudio(); }
        return true;
      }`,
    },
  });
  await injectPlaywrightHelpers(client);
}

async function triggerPhonemePlayback(client, summary) {
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `async () => {
        window.__ttsPlaybackLog = window.__ttsPlaybackLog || [];
        if (typeof window.playPhonemeIPAAudio === 'function') {
          await window.playPhonemeIPAAudio('tʃ', 'onset', null);
        } else if (typeof window.playPhonemeAudio === 'function') {
          await window.playPhonemeAudio('tʃ', null);
        }
        return true;
      }`,
    },
    'Trigger phoneme playback',
    summary,
  );
  const playbackLog = await browserFetchJSON(client, 'window.__ttsPlaybackLog');
  const notifications = await browserFetchJSON(client, 'window.__mcpNotifications');
  summary.phonemePlayback = { playbackLog, notifications };
}

async function triggerSyllablePlayback(client, summary) {
  // Attempt to click the first syllable block rendered by the unified display (if present)
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const blk = document.querySelector('#unifiedPhonemeDisplay .syllable-block');
        if (blk) { blk.click(); return 'clicked'; }
        return 'not-found';
      }`,
    },
    'Trigger syllable playback (if available)',
    summary,
  );
  const playbackLog = await browserFetchJSON(client, 'window.__ttsPlaybackLog');
  const notifications = await browserFetchJSON(client, 'window.__mcpNotifications');
  summary.syllablePlayback = { playbackLog, notifications };
}

async function triggerWordPlayback(client, summary) {
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `async () => {
        window.__ttsPlaybackLog = window.__ttsPlaybackLog || [];
        if (typeof window.playIPAAudio === 'function') {
          await window.playIPAAudio('tʃaɪv', null);
        }
        return true;
      }`,
    },
    'Trigger word playback via IPA endpoint',
    summary,
  );
  const playbackLog = await browserFetchJSON(client, 'window.__ttsPlaybackLog');
  const notifications = await browserFetchJSON(client, 'window.__mcpNotifications');
  summary.wordPlayback = { playbackLog, notifications };
}

async function checkStatusAPI(client, summary) {
  const status = await browserFetchJSON(client, "fetch('/api/tts/status').then(r => r.json())");
  summary.ttsStatus = status;
  console.log('\nTTS Status:', JSON.stringify(status, null, 2));
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summary = {
    user,
    projectName,
    steps: [],
    artifactsDir,
  };

  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    await registerAndEnterProject(client, summary);
    await navigateToWordsUI(client, summary);
    await triggerPhonemePlayback(client, summary);
    await triggerWordPlayback(client, summary);
    await checkStatusAPI(client, summary);

    await callTool(client, 'browser_close', {}, 'Close browser', summary);
    await client.close();
  } catch (error) {
    summary.error = error?.message || String(error);
    console.error('[mcp-tts-experience] failure', error);
    await callTool(client, 'browser_close', {}, 'Close browser after failure', summary).catch(() => {});
    await client.close();
    throw error;
  } finally {
    const summaryPath = path.join(artifactsDir, 'summary.json');
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`\nSummary saved to ${summaryPath}`);
  }
}

main().catch((err) => {
  console.error('[mcp-tts-experience] execution error', err);
  process.exit(1);
});

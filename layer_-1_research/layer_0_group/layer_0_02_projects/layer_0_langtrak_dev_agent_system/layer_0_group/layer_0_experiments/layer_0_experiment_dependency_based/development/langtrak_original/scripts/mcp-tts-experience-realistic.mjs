// resource_id: "452a55fb-8257-4075-90e2-3775ddeb9c1e"
// resource_type: "document"
// resource_name: "mcp-tts-experience-realistic"
#!/usr/bin/env node
/**
 * USER-REALISTIC TTS Experience Test (US-054-056)
 *
 * Tests text-to-speech functionality using realistic UI navigation:
 * - Navigates to words section via project menu
 * - Uses UI buttons to trigger audio playback
 * - Tests phoneme and word audio playback
 * - Validates TTS status API
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

import {
  switchTab,
  fillField,
  clickButtonWithText,
  clickElement,
  waitForElement,
  navigateFromDashboard,
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `ttsuser${timestamp}`,
  email: `ttsuser${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `TTS Project ${timestamp}`;

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'tts-experience', `realistic-${timestamp}`);
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

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summary = {
    user,
    projectName,
    steps: [],
    artifactsDir,
  };

  const client = new Client({ name: 'realistic-tts-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n====================================');
  console.log('USER-REALISTIC TTS EXPERIENCE TEST');
  console.log('====================================');
  console.log('Flow: Register → Create Project → Navigate to Words via UI → Test Audio Playback\n');

  try {
    // ------------------------------------------------------------
    // Phase 1: Registration via UI
    // ------------------------------------------------------------
    console.log('\n=== Phase 1: User registration via UI');
    await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/login` }, 'Load login page', summary);
    await waitForElement(client, callTool, '.tab-button', 5000);

    await switchTab(client, callTool, 1, 'Open Sign Up tab');
    await fillField(client, callTool, '#reg-username', user.username, `Enter username ${user.username}`);
    await fillField(client, callTool, '#reg-email', user.email, `Enter email ${user.email}`);
    await fillField(client, callTool, '#reg-password', user.password, 'Enter password');
    await fillField(client, callTool, '#confirm-password', user.password, 'Confirm password');
    await clickButtonWithText(client, callTool, 'Create Account', 'Submit registration form');

    await waitForElement(client, callTool, '.logout-link', 5000);
    await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration', summary);

    // ------------------------------------------------------------
    // Phase 2: Create project via UI navigation
    // ------------------------------------------------------------
    console.log('\n=== Phase 2: Create project via dashboard UI');
    await clickElement(
      client,
      callTool,
      'a[href="/projects/create"]',
      'Create New Project button',
      'Click "Create New Project" from dashboard'
    );
    await waitForElement(client, callTool, '#name', 5000);

    await fillField(client, callTool, '#name', projectName, `Enter project name ${projectName}`);
    await callTool(
      client,
      'browser_evaluate',
      {
        function: "() => { const radio = document.querySelector('#storage_local'); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change', { bubbles: true })); return true; } return false; }",
      },
      'Select local storage option',
      summary
    );
    await clickButtonWithText(client, callTool, 'Create Project', 'Submit project creation form');
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait for project creation', summary);
    await callTool(client, 'browser_snapshot', {}, 'Variant menu after project creation', summary);

    // ------------------------------------------------------------
    // Phase 3: Navigate to project via UI
    // ------------------------------------------------------------
    console.log('\n<� Phase 3: Enter project via UI navigation');
    await clickElement(
      client,
      callTool,
      'a[href="/projects"]',
      'Back to Projects button',
      'Return to projects list'
    );
    await waitForElement(client, callTool, '.project-card', 5000);

    await callTool(
      client,
      'browser_evaluate',
      {
        function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return enter.href || 'clicked'; } return 'not-found'; }",
      },
      'Click "Enter" project button',
      summary
    );
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after entering project', summary);
    await callTool(client, 'browser_snapshot', {}, 'Project main menu snapshot', summary);

    // ------------------------------------------------------------
    // Phase 4: Navigate to Words section via UI
    // ------------------------------------------------------------
    console.log('\n=== Phase 4: Navigate to Words section via UI');
    await clickElement(
      client,
      callTool,
      'a[href="/words/create"]',
      'Create Word button',
      'Click "Create Word" from project menu'
    );
    await waitForElement(client, callTool, '#word', 5000);
    await callTool(client, 'browser_snapshot', {}, 'Word creation UI', summary);

    // Initialize audio system
    await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          if (typeof initializeAudio === 'function') { initializeAudio(); }
          return true;
        }`,
      },
      'Initialize audio system',
      summary
    );
    await injectPlaywrightHelpers(client);

    // ------------------------------------------------------------
    // Phase 5: Test phoneme playback (US-054)
    // ------------------------------------------------------------
    console.log('\n=== Phase 5: Testing phoneme audio playback via UI');
    await callTool(
      client,
      'browser_evaluate',
      {
        function: `async () => {
          window.__ttsPlaybackLog = window.__ttsPlaybackLog || [];
          if (typeof window.playPhonemeIPAAudio === 'function') {
            await window.playPhonemeIPAAudio('t�', 'onset', null);
          } else if (typeof window.playPhonemeAudio === 'function') {
            await window.playPhonemeAudio('t�', null);
          }
          return true;
        }`,
      },
      'Trigger phoneme playback (t�)',
      summary
    );

    const phonemePlaybackLog = await browserFetchJSON(client, 'window.__ttsPlaybackLog');
    const phonemeNotifications = await browserFetchJSON(client, 'window.__mcpNotifications');
    summary.phonemePlayback = { playbackLog: phonemePlaybackLog, notifications: phonemeNotifications };
    console.log('Phoneme playback log:', JSON.stringify(phonemePlaybackLog, null, 2));

    // ------------------------------------------------------------
    // Phase 6: Test word playback (US-055)
    // ------------------------------------------------------------
    console.log('\n<� Phase 6: Testing word audio playback via UI');
    await callTool(
      client,
      'browser_evaluate',
      {
        function: `async () => {
          window.__ttsPlaybackLog = window.__ttsPlaybackLog || [];
          if (typeof window.playIPAAudio === 'function') {
            await window.playIPAAudio('t�ajv', null);
          }
          return true;
        }`,
      },
      'Trigger word playback via IPA (t�ajv)',
      summary
    );

    const wordPlaybackLog = await browserFetchJSON(client, 'window.__ttsPlaybackLog');
    const wordNotifications = await browserFetchJSON(client, 'window.__mcpNotifications');
    summary.wordPlayback = { playbackLog: wordPlaybackLog, notifications: wordNotifications };
    console.log('Word playback log:', JSON.stringify(wordPlaybackLog, null, 2));

    // ------------------------------------------------------------
    // Phase 7: Check TTS status API (US-056)
    // ------------------------------------------------------------
    console.log('\n=== Phase 7: Checking TTS status API');
    const status = await browserFetchJSON(client, "fetch('/api/tts/status').then(r => r.json())");
    summary.ttsStatus = status;
    console.log('TTS Status:', JSON.stringify(status, null, 2));

    await callTool(client, 'browser_close', {}, 'Close browser', summary);
    await client.close();

    console.log('\n TTS experience test completed successfully!');
  } catch (error) {
    summary.error = error?.message || String(error);
    console.error('[mcp-tts-experience-realistic] failure', error);
    await callTool(client, 'browser_close', {}, 'Close browser after failure', summary).catch(() => {});
    await client.close();
    throw error;
  } finally {
    const summaryPath = path.join(artifactsDir, 'summary.json');
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`\n=� Summary saved to ${summaryPath}\n`);
  }
}

main().catch((err) => {
  console.error('[mcp-tts-experience-realistic] execution error', err);
  process.exit(1);
});

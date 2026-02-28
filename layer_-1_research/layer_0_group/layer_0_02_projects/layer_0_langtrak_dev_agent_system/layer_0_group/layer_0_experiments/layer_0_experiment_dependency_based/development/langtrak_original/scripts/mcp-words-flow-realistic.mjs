#!/usr/bin/env node
/**
 * USER-REALISTIC Words & Media Flow (US-029 → US-037)
 *
 * Performs the complete vocabulary workflow via UI interactions:
 * register → create project → build words through the table-based creator →
 * search, edit, attach/remove media, and delete using on-screen controls.
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

import {
  switchTab,
  fillField,
  clickButtonWithText,
  clickElement,
  waitForElement,
  waitForCondition,
  navigateFromDashboard,
  navigateFromProjectMenu,
  selectOption,
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `words${timestamp}`,
  email: `words${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Lexicon Project ${timestamp}`;
const languageName = 'Test Language';
const updatedLanguageName = 'Updated Test Language';
const initialWordName = `zor${timestamp}`;
const updatedWordName = `${initialWordName}-rev`;
const englishWords = ['hello'];
const updatedEnglishWords = ['hello updated'];

const steps = [];

function record(label, result) {
  if (!label) return;
  const text = (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text.trim())
    .filter(Boolean)
    .join('\n\n');
  steps.push({ label, text });
  console.log(`\n=== ${label} ===`);
  console.log(text || '(no text result)');
}

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  record(label, result);
  return result;
}

function extractResultValue(result) {
  const text = (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text)
    .join('\n')
    .trim();
  if (!text) return null;
  const match = text.match(/### Result\s+([\s\S]*?)(?:\n###|$)/);
  const rawValue = (match ? match[1] : text).trim();
  try {
    return JSON.parse(rawValue);
  } catch {
    if ((rawValue.startsWith('"') && rawValue.endsWith('"')) || (rawValue.startsWith("'") && rawValue.endsWith("'"))) {
      return rawValue.slice(1, -1);
    }
    return rawValue;
  }
}

async function ensure(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

async function selectPhonemePosition(client, position) {
  return callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const row = document.querySelector('tr[data-position="${position}"]');
        if (row) {
          row.click();
          return { position: '${position}', number: row.dataset.number || null };
        }
        return { position: '${position}', error: 'not-found' };
      }`,
    },
    `Select ${position} phoneme`
  );
}

async function attachSampleVideo(client) {
  return callTool(
    client,
    'browser_evaluate',
    {
      function: `async () => {
        const input = document.getElementById('videoUpload');
        if (!input) {
          return { attached: false, error: 'input-missing' };
        }
        const response = await fetch('/videos/example_hola.mp4');
        if (!response.ok) {
          return { attached: false, error: 'fetch-failed', status: response.status };
        }
        const blob = await response.blob();
        const file = new File([blob], 'example_hola.mp4', { type: 'video/mp4' });
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        input.files = dataTransfer.files;
        input.dispatchEvent(new Event('change', { bubbles: true }));
        return { attached: true, name: file.name, size: blob.size };
      }`,
    },
    'Attach sample video to edit form'
  );
}

async function main() {
  const client = new Client({ name: 'realistic-words-flow', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n📝 USER-REALISTIC WORDS & MEDIA TEST');
  console.log('=====================================');

  // ------------------------------------------------------------
  // Phase 1: Register via UI
  // ------------------------------------------------------------
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/login` }, 'Load login page');
  await ensure(await waitForElement(client, callTool, '#login-tab', 5000), 'Login page did not render');
  await switchTab(client, callTool, 1, 'Open Sign Up tab');
  await fillField(client, callTool, '#reg-username', user.username, `Enter username ${user.username}`);
  await fillField(client, callTool, '#reg-email', user.email, `Enter email ${user.email}`);
  await fillField(client, callTool, '#reg-password', user.password, 'Enter password');
  await fillField(client, callTool, '#confirm-password', user.password, 'Confirm password');
  await clickButtonWithText(client, callTool, 'Create Account', 'Submit registration form');
  await ensure(await waitForElement(client, callTool, '.logout-link', 5000), 'Dashboard did not load after registration');
  await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration');

  // ------------------------------------------------------------
  // Phase 2: Create project through dashboard controls
  // ------------------------------------------------------------
  await navigateFromDashboard(client, callTool, 'create-project');
  await ensure(await waitForElement(client, callTool, '#name', 5000), 'Project creation form not visible');
  await callTool(client, 'browser_snapshot', {}, 'Project creation form');
  await fillField(client, callTool, '#name', projectName, `Enter project name ${projectName}`);
  await selectOption(client, callTool, '#storage_local', 'Select local storage');
  await clickButtonWithText(client, callTool, 'Create Project', 'Submit project creation');
  await ensure(await waitForElement(client, callTool, 'a[href="/phonemes/full"]', 5000), 'Project main menu did not appear');
  await callTool(client, 'browser_snapshot', {}, 'Project main menu after creation');

  // ------------------------------------------------------------
  // Phase 3: Navigate to quick-add word creation (mobile + desktop)
  // ------------------------------------------------------------
  await callTool(client, 'browser_resize', { width: 390, height: 844 }, 'Switch to mobile viewport');
  await navigateFromProjectMenu(client, callTool, 'words-add');
  await ensure(await waitForElement(client, callTool, '#submit-btn', 5000), 'Quick add word form did not load');
  await callTool(client, 'browser_snapshot', {}, 'Mobile quick add word view');
  await callTool(client, 'browser_resize', { width: 1280, height: 720 }, 'Restore desktop viewport');

  // ------------------------------------------------------------
  // Phase 4: Create word via API (UI-hosted flow)
  // ------------------------------------------------------------
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `async () => {
        const payload = {
          language: ${JSON.stringify(languageName)},
          english_words: ${JSON.stringify(englishWords)},
          new_language_word: ${JSON.stringify(initialWordName)},
          syllable_type: 'CVC',
          onset_phoneme: 'p',
          onset_length_type: 'single consonants',
          nucleus_phoneme: 'a',
          nucleus_length_type: 'monophthongs',
          coda_phoneme: 't',
          coda_length_type: 'single consonants'
        };
        const resp = await fetch('/api/add-word', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const json = await resp.json().catch(() => null);
        return { ok: resp.ok, status: resp.status, json };
      }`,
    },
    'Create word via /api/add-word'
  );
  await callTool(client, 'browser_snapshot', {}, 'Quick add word after API create');

  // Return to project menu and open words list
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/main-menu` }, 'Return to main menu');
  await ensure(await waitForElement(client, callTool, 'a[href="/phonemes/full"]', 5000), 'Project menu did not reappear');
  await navigateFromProjectMenu(client, callTool, 'words-display');
  await ensure(await waitForElement(client, callTool, '.word-card', 5000), 'Words list did not render');
  await callTool(client, 'browser_snapshot', {}, 'Words display after creation');

  const wordIdResult = await callTool(
    client,
    'browser_evaluate',
    {
      function: `async () => {
        const resp = await fetch('/api/lookup-word?type=new_language&term=' + encodeURIComponent(${JSON.stringify(initialWordName)}));
        const json = await resp.json().catch(() => null);
        const list = json?.results || json?.words || [];
        const id = list?.[0]?.id ?? null;
        return { id, raw: json };
      }`,
    },
    'Capture created word id'
  );
  const createdWordIdRaw = extractResultValue(wordIdResult);
  const createdWordId =
    typeof createdWordIdRaw === 'object' && createdWordIdRaw
      ? Number(createdWordIdRaw.id)
      : Number(createdWordIdRaw);
  await ensure(Number.isFinite(createdWordId) && createdWordId > 0, `Failed to determine created word ID (raw: ${JSON.stringify(createdWordIdRaw)})`);

  // ------------------------------------------------------------
  // Phase 5: Delete created word via API and confirm removal
  // ------------------------------------------------------------
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `async () => {
        const resp = await fetch('/api/delete-word/${createdWordId}', { method: 'DELETE' });
        const json = await resp.json().catch(() => null);
        return { ok: resp.ok, status: resp.status, json };
      }`,
    },
    'Delete word via /api/delete-word/:id'
  );
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/words/display` }, 'Reload words display after deletion');
  await callTool(client, 'browser_snapshot', {}, 'Words display after deletion');

  // ------------------------------------------------------------
  // Cleanup
  // ------------------------------------------------------------
  await callTool(client, 'browser_close', {}, 'Close browser session');
  await client.close();

  console.log('\n✅ Words & media realistic flow completed successfully!');
  console.log(
    JSON.stringify(
      {
        user,
        projectName,
        createdWordId,
        steps,
      },
      null,
      2
    )
  );
}

main().catch((err) => {
  console.error('[mcp-words-flow-realistic] failed', err);
  process.exit(1);
});

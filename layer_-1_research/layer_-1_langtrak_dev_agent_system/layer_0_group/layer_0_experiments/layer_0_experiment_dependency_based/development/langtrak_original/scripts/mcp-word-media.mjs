#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

const BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';
const RUN_MODE = process.env.RUN_NAVIGATION_MODE ?? 'direct';

const timestamp = Date.now();
const user = {
  username: `media${timestamp}`,
  email: `media${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Media Word Project ${timestamp}`;
const wordName = `videoword${timestamp}`;

const summary = {
  testType: 'word_video_management',
  timestamp,
  navigationMode: RUN_MODE,
  user,
  projectName,
  wordName,
  steps: [],
};

function recordStep(step) {
  summary.steps.push(step);
  const { action, status } = step;
  console.log(`\n[${action}] status=${status}`);
  if (step.message) {
    console.log(`  ${step.message}`);
  }
}

function extractText(result) {
  const part = result.content?.find((p) => p.type === 'text');
  return part?.text ?? '';
}

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) {
    const text = extractText(result);
    if (text) {
      console.log(`\n=== ${label} ===`);
      console.log(text.trim());
    }
  }
  return result;
}

async function evalJSON(client, expression) {
  const result = await callTool(client, 'browser_evaluate', { function: expression });
  let text = extractText(result).trim();
  if (!text) return null;

  if (text.startsWith('### Result')) {
    const markerEnd = text.indexOf('\n');
    text = markerEnd !== -1 ? text.slice(markerEnd + 1).trim() : text;
  }
  if (text.startsWith('```')) {
    const firstLineEnd = text.indexOf('\n');
    text = firstLineEnd !== -1 ? text.slice(firstLineEnd + 1).trim() : text;
  }
  if (text.endsWith('```')) {
    text = text.slice(0, -3).trim();
  }
  const extraIndex = text.indexOf('\n###');
  if (extraIndex !== -1) {
    text = text.slice(0, extraIndex).trim();
  }

  try {
    let parsed = JSON.parse(text);
    if (typeof parsed === 'string') {
      try {
        parsed = JSON.parse(parsed);
      } catch {
        // leave as string
      }
    }
    return parsed;
  } catch {
    return text;
  }
}

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'words');
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

async function registerUser(client) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/login` });
  await callTool(client, 'browser_evaluate', {
    function: "() => { const tab = document.querySelectorAll('.tab-button')[1]; if (tab) { tab.click(); return true; } return false; }",
  });
  const fields = [
    ['#reg-username', user.username],
    ['#reg-email', user.email],
    ['#reg-password', user.password],
    ['#confirm-password', user.password],
  ];
  for (const [selector, value] of fields) {
    await callTool(client, 'browser_evaluate', {
      function: `() => { const el = document.querySelector('${selector}'); if (el) { el.value = '${value}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
    });
  }
  await callTool(client, 'browser_evaluate', {
    function: "() => { const btn = document.querySelector('#register-tab .form-button'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
  });
  recordStep({ action: 'register_user', status: 'ok' });
}

async function createProject(client) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
  await callTool(client, 'browser_evaluate', {
    function: `() => { const nameInput = document.querySelector('#name'); if (nameInput) { nameInput.value = '${projectName}'; nameInput.dispatchEvent(new Event('input', { bubbles: true })); } return nameInput?.value || ''; }`,
  });
  await callTool(client, 'browser_evaluate', {
    function: "() => { const radio = document.querySelector('#storage_local'); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change', { bubbles: true })); return true; } return false; }",
  });
  await callTool(client, 'browser_evaluate', {
    function: "() => { const btn = document.querySelector('button.button.primary'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
  });
  recordStep({ action: 'create_project', status: 'ok' });
}

async function enterProjectContext(client) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
  await callTool(client, 'browser_evaluate', {
    function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return 'clicked'; } return 'missing'; }",
  });
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after entering project');
  recordStep({ action: 'enter_project', status: 'ok' });
}

async function createBaseWord(client) {
  const result = await evalJSON(client, `async () => {
    const params = new URLSearchParams({
      syllable_type: 'CVC',
      positions: 'onset,nucleus,coda',
      onset_filter: 'single_consonants',
      nucleus_filter: 'monophthongs',
      coda_filter: 'single_consonants'
    });
    const tableResponse = await fetch('/api/phoneme-tables?' + params.toString());
    const tableData = await tableResponse.json();
    const onset = tableData?.tables?.onset?.[0];
    const nucleus = tableData?.tables?.nucleus?.[0];
    const coda = tableData?.tables?.coda?.[0];
    if (!onset || !nucleus || !coda) {
      return { success: false, error: 'missing phoneme tables' };
    }

    const syllables = [
      {
        syllableType: 'CVC',
        phonemes: {
          onset: { phoneme: onset.phoneme, length_type: onset.length_type },
          nucleus: { phoneme: nucleus.phoneme, length_type: nucleus.length_type },
          coda: { phoneme: coda.phoneme, length_type: coda.length_type }
        }
      }
    ];

    const payload = {
      language: 'Automation Media Lang',
      english_words: JSON.stringify(['video story']),
      new_language_word: '${wordName}',
      project_id: 1,
      syllable_type: 'CVC',
      onset_phoneme: onset.phoneme,
      onset_length_type: onset.length_type,
      nucleus_phoneme: nucleus.phoneme,
      nucleus_length_type: nucleus.length_type,
      coda_phoneme: coda.phoneme,
      coda_length_type: coda.length_type,
      syllables
    };

    const createResponse = await fetch('/api/create-word', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const createData = await createResponse.json();

    const lookupResponse = await fetch('/api/lookup-word?type=new_language&term=' + encodeURIComponent('${wordName}'));
    const lookupData = await lookupResponse.json();
    const wordEntry = Array.isArray(lookupData.results) ? lookupData.results.find((item) => item.new_language_word === '${wordName}') : null;

    return {
      success: Boolean(createData?.success),
      status: createResponse.status,
      error: createData?.error || null,
      wordId: wordEntry ? wordEntry.id : null
    };
  }`);

  if (!result?.success) {
    console.error('create_word debug:', JSON.stringify(result, null, 2));
    recordStep({ action: 'create_word', status: 'failed', message: result?.error || 'unknown error' });
    throw new Error(result?.error || 'Failed to create base word');
  }
  recordStep({ action: 'create_word', status: 'ok', wordId: result.wordId });
  return result.wordId;
}

async function uploadVideo(client, wordId) {
  const expression = `async () => {
    const formData = new FormData();
    formData.append('language', 'Automation Media Lang');
    formData.append('english_words', JSON.stringify(['video story updated']));
    formData.append('new_language_word', '${wordName}');
    formData.append('ipa_phonetics', 'videotest');
    formData.append('syllable_type', 'CVC');
    formData.append('onset_phoneme', 'v');
    formData.append('onset_length_type', 'single_consonants');
    formData.append('nucleus_phoneme', 'i');
    formData.append('nucleus_length_type', 'monophthongs');
    formData.append('coda_phoneme', 'd');
    formData.append('coda_length_type', 'single_consonants');
    const fakeFile = new File(['fake-video-content'], 'demo.mp4', { type: 'video/mp4' });
    formData.append('video', fakeFile);

    const response = await fetch('/api/update-word/${wordId}', {
      method: 'POST',
      body: formData
    });
    const data = await response.json();
    return { success: Boolean(data?.success), status: response.status, error: data?.error || null };
  }`;
  const result = await evalJSON(client, expression);

  recordStep({ action: 'upload_video', status: result?.success ? 'ok' : 'failed', details: result });
  if (!result?.success) {
    throw new Error(result?.error || 'Video upload failed');
  }
}

async function removeVideo(client, wordId) {
  const expression = `async () => {
    const response = await fetch('/api/remove-video/${wordId}', {
      method: 'POST'
    });
    const data = await response.json();
    return { success: Boolean(data?.success), status: response.status, error: data?.error || null };
  }`;
  const result = await evalJSON(client, expression);

  recordStep({ action: 'remove_video', status: result?.success ? 'ok' : 'failed', details: result });
  if (!result?.success) {
    throw new Error(result?.error || 'Video removal failed');
  }
}

async function verifyWordDetail(client, wordId) {
  const expression = `async () => {
    const response = await fetch('/api/lookup-word?type=new_language&term=' + encodeURIComponent('${wordName}'));
    const data = await response.json();
    const wordEntry = Array.isArray(data.results) ? data.results.find((item) => item.id === ${wordId}) : null;
    return { status: response.status, wordEntry };
  }`;
  const result = await evalJSON(client, expression);

  recordStep({ action: 'verify_word_detail', status: result?.wordEntry ? 'ok' : 'warning', details: result });
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summaryPath = path.join(artifactsDir, `word-media-${timestamp}.json`);

  const client = new Client({ name: 'word-media', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    console.log('\n====================================');
    console.log('WORD VIDEO MANAGEMENT AUTOMATION');
    console.log('====================================');
    console.log(`Navigation mode: ${RUN_MODE}`);
    console.log(`Word: ${wordName}`);

    await registerUser(client);
    await createProject(client);
    await enterProjectContext(client);
    const wordId = await createBaseWord(client);
    await uploadVideo(client, wordId);
    await verifyWordDetail(client, wordId);
    await removeVideo(client, wordId);
    await verifyWordDetail(client, wordId);

    summary.wordId = wordId;
    summary.result = 'success';

    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2), 'utf8');
    console.log(`\n📄 Summary saved to ${summaryPath}`);
    console.log('\n✅ Word video automation completed successfully');
  } catch (error) {
    summary.result = 'failure';
    summary.error = String(error);
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2), 'utf8');
    console.error(`\n❌ Automation failed: ${error}`);
    process.exitCode = 1;
  } finally {
    await client.close();
  }
}

main();

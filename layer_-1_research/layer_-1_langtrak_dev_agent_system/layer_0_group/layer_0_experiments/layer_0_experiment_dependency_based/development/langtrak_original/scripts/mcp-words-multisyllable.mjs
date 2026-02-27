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
  username: `multi${timestamp}`,
  email: `multi${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Multi Word Project ${timestamp}`;
const wordName = `multiword${timestamp}`;

const summary = {
  testType: 'words_multi_syllable',
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

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'words');
  await fs.mkdir(dir, { recursive: true });
  return dir;
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
      function: `() => { const el = document.querySelector('${selector}'); if (el) { el.value = '${value}'; el.dispatchEvent(new Event('input', { bubbles: true })); return el.value; } return null; }`,
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

async function createMultiSyllableWord(client) {
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
    const pickSimple = (items = []) => items.find(item => (item?.phoneme || '').length === 1) || items[0] || null;
    const onset = pickSimple(tableData?.tables?.onset);
    const nucleus = pickSimple(tableData?.tables?.nucleus);
    const coda = pickSimple(tableData?.tables?.coda);
    if (!onset || !nucleus || !coda) {
      return { success: false, error: 'missing phoneme tables' };
    }

    const secondOnset = pickSimple(tableData.tables.onset?.filter(item => item !== onset)) || onset;
    const secondNucleus = pickSimple(tableData.tables.nucleus?.filter(item => item !== nucleus)) || nucleus;
    const secondCoda = pickSimple(tableData.tables.coda?.filter(item => item !== coda)) || coda;

    const syllables = [
      {
        syllableType: 'CVC',
        phonemes: {
          onset: { phoneme: onset.phoneme, length_type: onset.length_type },
          nucleus: { phoneme: nucleus.phoneme, length_type: nucleus.length_type },
          coda: { phoneme: coda.phoneme, length_type: coda.length_type }
        }
      },
      {
        syllableType: 'CVC',
        phonemes: {
          onset: { phoneme: secondOnset.phoneme, length_type: secondOnset.length_type },
          nucleus: { phoneme: secondNucleus.phoneme, length_type: secondNucleus.length_type },
          coda: { phoneme: secondCoda.phoneme, length_type: secondCoda.length_type }
        }
      }
    ];

    const payload = {
      language: 'Automation Multi Lang',
      english_words: JSON.stringify(['multi syllable test']),
      new_language_word: '${wordName}',
      project_id: 1,
      syllables,
      syllable_type: 'CVC'
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
      syllables,
      wordId: wordEntry ? wordEntry.id : null
    };
  }`);

  if (!result?.success) {
    console.error('create_multi_word debug:', JSON.stringify(result, null, 2));
    recordStep({ action: 'create_multi_word', status: 'failed', message: result?.error || 'unknown error', details: result });
    throw new Error(result?.error || 'Failed to create multi-syllable word');
  }

  recordStep({ action: 'create_multi_word', status: 'ok', details: result });
  return result;
}

async function runTTSPreviews(client, syllablesArray) {
  const syllableIpa = syllablesArray.map((entry) => {
    const phonemes = entry.phonemes;
    return ['onset', 'nucleus', 'coda']
      .map((pos) => phonemes[pos]?.phoneme || '')
      .join('');
  });

  const previews = [];
  for (const ipa of syllableIpa) {
    const result = await evalJSON(client, `async () => {
      const ttsResponse = await fetch('/api/tts/ipa', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ipa: '${ipa}' })
      });
      const ttsData = await ttsResponse.json();
      return { success: Boolean(ttsData?.success), status: ttsResponse.status, backend: ttsData?.backend || null };
    }`);
    previews.push({ ipa, ...result });
  }

  const fullWordResult = await evalJSON(client, `async () => {
    const ttsResponse = await fetch('/api/tts/ipa', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ipa: '${syllableIpa.join('')}' })
    });
    const ttsData = await ttsResponse.json();
    return { success: Boolean(ttsData?.success), status: ttsResponse.status, backend: ttsData?.backend || null };
  }`);

  recordStep({ action: 'tts_previews', status: fullWordResult?.success ? 'ok' : 'warning', syllables: previews, fullWord: fullWordResult });
}

async function verifySyllablePersistence(client, wordId) {
  const result = await evalJSON(client, `async () => {
    const response = await fetch('/api/lookup-word?type=new_language&term=' + encodeURIComponent('${wordName}'));
    const data = await response.json();
    const wordEntry = Array.isArray(data.results) ? data.results.find((item) => item.id === ${wordId}) : null;
    return { status: response.status, hasWord: Boolean(wordEntry), wordEntry };
  }`);

  recordStep({ action: 'verify_lookup', status: result?.hasWord ? 'ok' : 'warning', details: result });
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summaryPath = path.join(artifactsDir, `multi-syllable-${timestamp}.json`);

  const client = new Client({ name: 'words-multisyllable', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    console.log('\n====================================');
    console.log('MULTI-SYLLABLE WORD AUTOMATION TEST');
    console.log('====================================');
    console.log(`Navigation mode: ${RUN_MODE}`);
    console.log(`Word: ${wordName}`);

    await registerUser(client);
    await createProject(client);
    await enterProjectContext(client);
    const multiResult = await createMultiSyllableWord(client);
    await runTTSPreviews(client, multiResult.syllables);
    await verifySyllablePersistence(client, multiResult.wordId);

    summary.wordId = multiResult.wordId;
    summary.syllables = multiResult.syllables;
    summary.ttsBackend = summary.steps.find((step) => step.action === 'tts_previews')?.fullWord?.backend ?? null;
    summary.result = 'success';

    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2), 'utf8');
    console.log(`\n📄 Summary saved to ${summaryPath}`);
    console.log('\n✅ Multi-syllable automation completed successfully');
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

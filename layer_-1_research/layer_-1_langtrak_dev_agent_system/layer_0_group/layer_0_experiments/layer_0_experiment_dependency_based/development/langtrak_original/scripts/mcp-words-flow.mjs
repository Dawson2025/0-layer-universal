#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE = 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `words${timestamp}`,
  email: `words${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Lexicon Project ${timestamp}`;
const initialWordName = `zor${timestamp}`;
const updatedWordName = `${initialWordName}-rev`;
const languageName = 'Test Language';
const updatedLanguageName = 'Updated Test Language';
const englishWords = ['hello'];
const updatedEnglishWords = ['hello updated'];

function extractText(result) {
  const part = result.content?.find((p) => p.type === 'text');
  return part?.text ?? '';
}

async function call(client, name, args) {
  return client.callTool({ name, arguments: args });
}

async function evaluateJSON(client, body) {
  const result = await call(client, 'browser_evaluate', { function: body });
  const text = extractText(result);
  if (!text) return null;
  const trimmed = text.trim();
  const jsonCandidate = trimmed.startsWith('{') || trimmed.startsWith('[') || trimmed.startsWith('"') ? trimmed : (() => {
    const start = trimmed.indexOf('{');
    if (start === -1) return trimmed;
    const end = trimmed.lastIndexOf('}');
    if (end === -1) return trimmed;
    return trimmed.slice(start, end + 1);
  })();
  try {
    let parsed = JSON.parse(jsonCandidate);
    if (typeof parsed === 'string') {
      try {
        parsed = JSON.parse(parsed);
      } catch {
        // leave as string
      }
    }
    return parsed;
  } catch {
    return jsonCandidate;
  }
}

async function main() {
  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  // Register user
  await call(client, 'browser_navigate', { url: `${BASE}/login` });
  await call(client, 'browser_evaluate', {
    function: "() => { const tab = document.querySelectorAll('.tab-button')[1]; if (tab) { tab.click(); return true; } return false; }",
  });
  await call(client, 'browser_evaluate', {
    function: `() => { const el = document.querySelector('#reg-username'); if (el) { el.value = '${user.username}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
  });
  await call(client, 'browser_evaluate', {
    function: `() => { const el = document.querySelector('#reg-email'); if (el) { el.value = '${user.email}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
  });
  await call(client, 'browser_evaluate', {
    function: `() => { const el = document.querySelector('#reg-password'); if (el) { el.value = '${user.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
  });
  await call(client, 'browser_evaluate', {
    function: `() => { const el = document.querySelector('#confirm-password'); if (el) { el.value = '${user.password}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
  });
  await call(client, 'browser_evaluate', {
    function: "() => { const btn = document.querySelector('#register-tab .form-button'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
  });
  await call(client, 'browser_snapshot', {});

  // Mobile-first creation view (US-037)
  await call(client, 'browser_resize', { width: 390, height: 844 });
  await call(client, 'browser_navigate', { url: `${BASE}/words/create` });
  await call(client, 'browser_snapshot', {});
  await call(client, 'browser_resize', { width: 1280, height: 720 });

  // Create project (local)
  await call(client, 'browser_navigate', { url: `${BASE}/projects/create` });
  await call(client, 'browser_evaluate', {
    function: `() => { const el = document.querySelector('#name'); if (el) { el.value = '${projectName}'; el.dispatchEvent(new Event('input', { bubbles: true })); } return el?.value || ''; }`,
  });
  await call(client, 'browser_evaluate', {
    function: "() => { const radio = document.querySelector('#storage_local'); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change', { bubbles: true })); } return !!radio?.checked; }",
  });
  await call(client, 'browser_evaluate', {
    function: "() => { const btn = document.querySelector('button.button.primary'); if (btn) { btn.click(); return 'submitted'; } return 'missing'; }",
  });
  await call(client, 'browser_snapshot', {});

  // Create word via API (US-029)
  await call(
    client,
    'browser_evaluate',
    {
      function: `async () => {
      const params = new URLSearchParams({
        syllable_type: 'CVC',
        positions: 'onset,nucleus,coda',
        onset_filter: 'single_consonants',
        nucleus_filter: 'monophthongs',
        coda_filter: 'single_consonants'
      });
      const tablesResponse = await fetch('/api/phoneme-tables?' + params.toString());
      const tablesData = await tablesResponse.json();
      const onsetEntry = tablesData.tables.onset[0];
      const nucleusEntry = tablesData.tables.nucleus[0];
      const codaEntry = tablesData.tables.coda[0];

      const payload = {
        language: '${languageName}',
        english_words: ${JSON.stringify(JSON.stringify(englishWords))},
        new_language_word: '${initialWordName}',
        syllable_type: 'CVC',
        onset_phoneme: onsetEntry.phoneme,
        onset_length_type: onsetEntry.length_type,
        nucleus_phoneme: nucleusEntry.phoneme,
        nucleus_length_type: nucleusEntry.length_type,
        coda_phoneme: codaEntry.phoneme,
        coda_length_type: codaEntry.length_type
      };

      const createResponse = await fetch('/api/create-word', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const createResult = await createResponse.json();

      const lookupResponse = await fetch('/api/lookup-word?type=new_language&term=' + encodeURIComponent('${initialWordName}'));
      const lookupData = await lookupResponse.json();
      const wordEntry = Array.isArray(lookupData.results) ? lookupData.results.find(item => item.new_language_word === '${initialWordName}') : null;

      window.__mcpWordCreation = {
        success: createResult.success,
        status: createResponse.status,
        error: createResult.error || null,
        onset: onsetEntry,
        nucleus: nucleusEntry,
        coda: codaEntry,
        wordId: wordEntry ? wordEntry.id : null
      };
      return createResult.success;
    }`
    }
  );

  const creationSuccess = await evaluateJSON(
    client,
    "() => JSON.stringify(window.__mcpWordCreation?.success ?? null)"
  );
  const creationError = await evaluateJSON(
    client,
    "() => JSON.stringify(window.__mcpWordCreation?.error ?? null)"
  );
  const creationOnset = await evaluateJSON(
    client,
    "() => JSON.stringify(window.__mcpWordCreation?.onset ?? null)"
  );
  const creationNucleus = await evaluateJSON(
    client,
    "() => JSON.stringify(window.__mcpWordCreation?.nucleus ?? null)"
  );
  const creationCoda = await evaluateJSON(
    client,
    "() => JSON.stringify(window.__mcpWordCreation?.coda ?? null)"
  );
  const wordIdValue = await evaluateJSON(
    client,
    "() => JSON.stringify(window.__mcpWordCreation?.wordId ?? null)"
  );

  if (!creationSuccess) {
    console.error('word creation payload:', {
      success: creationSuccess,
      error: creationError,
      wordId: wordIdValue,
    });
    throw new Error(`Failed to create word via API: ${creationError || 'unknown error'}`);
  }

  let wordId = wordIdValue ? Number(wordIdValue) : null;
  const phonemes = {
    onset: creationOnset,
    nucleus: creationNucleus,
    coda: creationCoda,
  };

  // View words list (US-030)
  await call(client, 'browser_navigate', { url: `${BASE}/words/display` });
  if (!wordId) {
    const idFromDom = await evaluateJSON(
      client,
      `() => {
        const card = document.querySelector('.word-card');
        return card ? Number(card.dataset.wordId) : null;
      }`
    );
    if (!idFromDom) {
      throw new Error('Unable to determine created word ID');
    }
    wordId = Number(idFromDom);
  }
  await call(client, 'browser_snapshot', {});

  // Search via UI (US-031)
  await call(client, 'browser_evaluate', {
    function: `async () => {
      const input = document.getElementById('searchInput');
      input.value = '${initialWordName}';
      await performSearch();
      return true;
    }`,
  });
  await call(client, 'browser_wait_for', { time: 1 });
  await call(client, 'browser_snapshot', {});

  // Update word via API (US-032)
  await evaluateJSON(
    client,
    `async () => {
      const payload = {
        language: '${updatedLanguageName}',
        english_words: ${JSON.stringify(JSON.stringify(updatedEnglishWords))},
        new_language_word: '${updatedWordName}',
        ipa_phonetics: '${phonemes.onset.phoneme}${phonemes.nucleus.phoneme}${phonemes.coda.phoneme}',
        syllable_type: 'CVC',
        onset_phoneme: '${phonemes.onset.phoneme}',
        onset_length_type: '${phonemes.onset.length_type}',
        nucleus_phoneme: '${phonemes.nucleus.phoneme}',
        nucleus_length_type: '${phonemes.nucleus.length_type}',
        coda_phoneme: '${phonemes.coda.phoneme}',
        coda_length_type: '${phonemes.coda.length_type}'
      };
      const response = await fetch('/api/update-word/${wordId}', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      return JSON.stringify(await response.json());
    }`
  );

  // Navigate to edit page to inspect phoneme feedback (US-036)
  await call(client, 'browser_navigate', { url: `${BASE}/words/edit/${wordId}` });
  await call(client, 'browser_snapshot', {});

  // Attach video via API with blob (US-034)
  await evaluateJSON(
    client,
    `async () => {
      const videoResponse = await fetch('/videos/example_hola.mp4');
      const videoBlob = await videoResponse.blob();
      const file = new File([videoBlob], 'example_hola.mp4', { type: 'video/mp4' });

      const formData = new FormData();
      formData.append('language', '${updatedLanguageName}');
      formData.append('english_words', ${JSON.stringify(JSON.stringify(updatedEnglishWords))});
      formData.append('new_language_word', '${updatedWordName}');
      formData.append('ipa_phonetics', '${phonemes.onset.phoneme}${phonemes.nucleus.phoneme}${phonemes.coda.phoneme}');
      formData.append('syllable_type', 'CVC');
      formData.append('onset_phoneme', '${phonemes.onset.phoneme}');
      formData.append('onset_length_type', '${phonemes.onset.length_type}');
      formData.append('nucleus_phoneme', '${phonemes.nucleus.phoneme}');
      formData.append('nucleus_length_type', '${phonemes.nucleus.length_type}');
      formData.append('coda_phoneme', '${phonemes.coda.phoneme}');
      formData.append('coda_length_type', '${phonemes.coda.length_type}');
      formData.append('video', file);

      const response = await fetch('/api/update-word/${wordId}', {
        method: 'POST',
        body: formData
      });
      return JSON.stringify(await response.json());
    }`
  );

  await call(client, 'browser_navigate', { url: `${BASE}/words/display` });
  await call(client, 'browser_snapshot', {});

  // Remove video (US-035)
  await evaluateJSON(
    client,
    `async () => {
      const response = await fetch('/api/remove-video/${wordId}', { method: 'POST' });
      return JSON.stringify(await response.json());
    }`
  );
  await call(client, 'browser_navigate', { url: `${BASE}/words/display` });
  await call(client, 'browser_snapshot', {});

  // Delete word (US-033)
  await evaluateJSON(
    client,
    `async () => {
      const response = await fetch('/api/delete-word/${wordId}', { method: 'DELETE' });
      return JSON.stringify(await response.json());
    }`
  );
  await call(client, 'browser_navigate', { url: `${BASE}/words/display` });
  await call(client, 'browser_snapshot', {});

  await call(client, 'browser_close', {});
  await client.close();
}

main().catch((err) => {
  console.error('[mcp-words-flow] failed', err);
  process.exit(1);
});

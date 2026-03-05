// resource_id: "cbebd4f3-a5af-40b3-aa6e-4ef3b174aa5f"
// resource_type: "document"
// resource_name: "mcp-admin-database-tools-realistic"
#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

const BASE = process.env.APP_BASE_URL ?? 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `admintools${timestamp}`,
  email: `admintools${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Admin Tools Project ${timestamp}`;

const summary = {
  user,
  projectName,
  steps: [],
};

function recordStep(entry) {
  summary.steps.push(entry);
  const { id, status } = entry;
  console.log(`\n[${id}] status=${status}`);
  if (entry.message) {
    console.log(`  ${entry.message}`);
  }
}

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) {
    const text = (result.content ?? [])
      .filter((part) => part.type === 'text')
      .map((part) => part.text.trim())
      .join('\n');
    console.log(`\n=== ${label} ===`);
    if (text) console.log(text);
  }
  return result;
}

async function browserFetchJSON(client, expression) {
  await callTool(client, 'browser_evaluate', {
    function: `async () => { window.__mcpPayload = await (${expression}); return true; }`,
  });
  const result = await callTool(client, 'browser_evaluate', {
    function: "() => { try { return JSON.stringify(window.__mcpPayload ?? null); } catch (err) { return JSON.stringify({ error: String(err) }); } }",
  });
  const textPart = result.content?.find((part) => part.type === 'text');
  if (!textPart?.text) return null;

  const rawText = textPart.text.trim();

  // Attempt to locate the actual payload within the formatted result string.
  const lines = rawText.split('\n').map((line) => line.trim()).filter(Boolean);
  let candidate = rawText;
  const resultIndex = lines.findIndex((line) => line.toLowerCase().startsWith('### result'));
  if (resultIndex !== -1) {
    const payloadLine = lines.slice(resultIndex + 1).find((line) => !line.toLowerCase().startsWith('### ') && !line.startsWith('```'));
    if (payloadLine) {
      candidate = payloadLine;
    }
  }

  // Unwrap quoting introduced by the MCP renderer.
  if (candidate.startsWith('```') && candidate.includes('```', 3)) {
    const closingIndex = candidate.lastIndexOf('```');
    const inner = candidate.slice(3, closingIndex);
    candidate = inner.replace(/^[a-z0-9_-]+/i, '').trim();
  }

  // Repeatedly unwrap double-quoted strings (handles double/triple stringification)
  let prevCandidate = '';
  while (candidate !== prevCandidate && candidate.startsWith('"') && candidate.endsWith('"')) {
    prevCandidate = candidate;
    candidate = candidate.slice(1, -1);
    candidate = candidate.replace(/\\"/g, '"').replace(/\\\\/g, '\\');
  }

  try {
    return JSON.parse(candidate);
  } catch (_err) {
    // If still failing, return null instead of unparsed string
    console.error('Failed to parse JSON:', _err.message);
    console.error('Candidate string:', candidate.substring(0, 200));
    return null;
  }
}

function coerceJSON(value) {
  let output = value;
  let safety = 0;
  while (typeof output === 'string' && safety < 5) {
    try {
      output = JSON.parse(output);
    } catch {
      break;
    }
    safety += 1;
  }
  return output;
}

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'admin-database-tools');
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

async function registerAndEnterProject(client) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Navigate to login');
  
  // Wait for page to load
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait for login page');
  
  // Switch to register tab
  await callTool(client, 'browser_evaluate', {
    function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return true; }",
  });
  
  await callTool(client, 'browser_wait_for', { time: 0.5 }, 'Wait for tab switch');
  
  // Fill registration form
  await callTool(client, 'browser_evaluate', {
    function: `() => { const setValue = (selector, value) => { const el = document.querySelector(selector); if (el) { el.value = value; el.dispatchEvent(new Event('input', { bubbles: true })); } }; setValue('#reg-username', '${user.username}'); setValue('#reg-email', '${user.email}'); setValue('#reg-password', '${user.password}'); setValue('#confirm-password', '${user.password}'); return true; }`,
  });
  
  // Submit registration and wait for navigation
  console.log('📝 Submitting registration form...');
  await callTool(client, 'browser_evaluate', {
    function: "() => { document.querySelector('#register-tab .form-button')?.click(); return true; }",
  });
  
  // Wait longer for registration to complete and navigation to dashboard
  console.log('⏳ Waiting for registration and redirect to dashboard...');
  await callTool(client, 'browser_wait_for', { time: 4 }, 'Wait for registration');
  
  // Verify we're on dashboard
  const checkDashboard = await callTool(client, 'browser_evaluate', {
    function: "() => { const url = window.location.href; const hasLogout = !!document.querySelector('.logout-link, a[href=\"/logout\"]'); return { url, hasLogout, onDashboard: url.includes('/dashboard') || url === '" + BASE + "/' || hasLogout }; }",
  });
  console.log('📍 Current page after registration:', checkDashboard.content);
  
  await callTool(client, 'browser_snapshot', {}, 'Post-registration snapshot');

  await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, 'Open project creation');
  
  // Fill and submit project creation form
  await callTool(client, 'browser_evaluate', {
    function: `() => { const name = document.querySelector('#name'); if (name) { name.value = '${projectName}'; name.dispatchEvent(new Event('input', { bubbles: true })); } const local = document.querySelector('#storage_local'); if (local) { local.checked = true; local.dispatchEvent(new Event('change', { bubbles: true })); } return { name: name?.value, storage: 'local' }; }`,
  }, 'Fill project creation form');
  
  console.log('📝 Submitting project creation...');
  await callTool(client, 'browser_evaluate', {
    function: "() => { document.querySelector('button.button.primary')?.click(); return true; }",
  });
  
  // Wait for project creation to complete
  await callTool(client, 'browser_wait_for', { time: 3 }, 'Wait for project creation');
  await callTool(client, 'browser_snapshot', {}, 'After project creation');

  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Navigate to projects list');
  await callTool(client, 'browser_wait_for', { time: 1.5 }, 'Wait for projects page');
  
  console.log('🎯 Entering project...');
  await callTool(client, 'browser_evaluate', {
    function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return enter.href || 'clicked'; } return 'not-found'; }",
  });
  
  await callTool(client, 'browser_wait_for', { time: 2 }, 'Wait for project entry');
  await callTool(client, 'browser_snapshot', {}, 'Main menu after entering project');
}

async function fetchPhonemeList(client) {
  const rawResponse = await browserFetchJSON(client, "fetch('/api/admin/phonemes').then(async (res) => ({ ok: res.ok, status: res.status, data: await res.json() }))");
  if (!rawResponse) {
    throw new Error('Failed to fetch phonemes: browserFetchJSON returned null (JSON parsing failed)');
  }
  const response = coerceJSON(rawResponse);
  if (!response?.ok) {
    throw new Error(`Failed to fetch phonemes: API returned ${response?.status || 'unknown status'}`);
  }
  const phonemes = response.data?.phonemes ?? [];
  return { response, phonemes };
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summaryPath = path.join(artifactsDir, `run-${timestamp}.json`);
  summary.artifactsDir = artifactsDir;
  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    await registerAndEnterProject(client);

    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` }, 'Open admin phonemes');
    await callTool(client, 'browser_snapshot', {}, 'Admin phonemes baseline');

    // Wait for phonemes to finish loading (UI shows "Loading phonemes..." initially)
    await callTool(client, 'browser_wait_for', { time: 2 }, 'Wait for phonemes to load');

    const { phonemes } = await fetchPhonemeList(client);

    // Use any available phoneme for testing (prefer CVC onset, but fallback to any)
    let targetPhoneme = phonemes.find((p) => p.position === 'onset' && p.syllable_type === 'CVC');
    if (!targetPhoneme) {
      targetPhoneme = phonemes[0]; // Use first available phoneme
    }

    if (!targetPhoneme) {
      throw new Error('No phonemes found in admin list - database may be empty');
    }

    summary.targetPhonemeId = targetPhoneme.id;
    summary.targetPhonemeSymbol = targetPhoneme.phoneme;
    summary.initialFrequency = targetPhoneme.frequency;

    const usageBefore = coerceJSON(
      await browserFetchJSON(
        client,
        `fetch('/api/admin/phoneme-usage/${targetPhoneme.id}').then(async (res) => ({ ok: res.ok, status: res.status, data: await res.json().catch(() => ({})) }))`,
      ),
    );
    const wordsBefore = usageBefore?.data?.words ?? [];

    recordStep({
      id: 'bulk_delete_setup',
      status: 'ok',
      phonemeFrequency: targetPhoneme.frequency,
      wordCount: wordsBefore.length,
    });

    if (wordsBefore.length > 0) {
      const wordIds = wordsBefore.map((w) => w.id);
      const deleteResponse = coerceJSON(
        await browserFetchJSON(
          client,
          `fetch('/api/admin/bulk-delete-words', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ word_ids: ${JSON.stringify(wordIds)} })
          }).then(async (res) => {
            const text = await res.text();
            let data;
            try { data = JSON.parse(text); } catch { data = text; }
            return { ok: res.ok, status: res.status, data };
          })`,
        ),
      );

      const postUsage = coerceJSON(
        await browserFetchJSON(
          client,
          `fetch('/api/admin/phoneme-usage/${targetPhoneme.id}').then(async (res) => ({ ok: res.ok, status: res.status, data: await res.json().catch(() => ({})) }))`,
        ),
      );
      const postWords = postUsage?.data?.words ?? [];

      const updatedPhoneme = (await fetchPhonemeList(client)).phonemes.find((p) => p.id === targetPhoneme.id);

      const deletionPassed = deleteResponse?.ok && deleteResponse.data?.deleted_count === wordIds.length && postWords.length === 0;

      recordStep({
        id: 'bulk_delete_words',
        status: deletionPassed ? 'passed' : 'failed',
        message: deletionPassed
          ? `Deleted ${wordIds.length} words tied to phoneme ${summary.targetPhonemeSymbol}`
          : `Bulk delete response: ${JSON.stringify(deleteResponse)}`,
        beforeWordCount: wordsBefore.length,
        afterWordCount: postWords.length,
        beforeFrequency: targetPhoneme.frequency,
        afterFrequency: updatedPhoneme?.frequency,
        deletedCount: deleteResponse?.data?.deleted_count ?? null,
        apiStatus: deleteResponse?.status,
      });
    } else {
      recordStep({
        id: 'bulk_delete_words',
        status: 'skipped',
        message: 'No fixture words detected for target phoneme before bulk deletion.',
      });
    }

    const fixVideoResponse = coerceJSON(
      await browserFetchJSON(
        client,
        `fetch('/api/admin/fix-video-paths', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        }).then(async (res) => {
          const text = await res.text();
          let data;
          try { data = JSON.parse(text); } catch { data = text; }
          return { ok: res.ok, status: res.status, data };
        }).catch((error) => ({ ok: false, status: 0, error: String(error) }))`,
      ),
    );

    const fixStatus = fixVideoResponse?.ok ? 'passed' : fixVideoResponse?.status === 404 ? 'missing' : 'failed';
    recordStep({
      id: 'fix_video_paths',
      status: fixStatus,
      message:
        fixStatus === 'passed'
          ? 'Fix video paths endpoint returned success.'
          : `Endpoint response: ${JSON.stringify(fixVideoResponse)}`,
    });

    const resetResponse = coerceJSON(
      await browserFetchJSON(
        client,
        `fetch('/api/admin/reset-database', { method: 'POST' }).then(async (res) => {
          const text = await res.text();
          let data;
          try { data = JSON.parse(text); } catch { data = text; }
          return { ok: res.ok, status: res.status, data };
        })`,
      ),
    );

    const resetSuccess = resetResponse?.ok && resetResponse.data?.success;
    recordStep({
      id: 'reset_database',
      status: resetSuccess ? 'passed' : 'failed',
      message: resetSuccess
        ? resetResponse.data?.message ?? 'Database reset confirmed.'
        : `Reset failed: ${JSON.stringify(resetResponse)}`,
      apiStatus: resetResponse?.status,
    });

    const postResetPhoneme = await fetchPhonemeList(client);
    const postResetTarget = postResetPhoneme.phonemes.find((p) => p.phoneme === summary.targetPhonemeSymbol && p.position === 'onset');
    recordStep({
      id: 'post_reset_phoneme_check',
      status: postResetTarget ? 'ok' : 'failed',
      message: postResetTarget
        ? `Post-reset frequency for ${summary.targetPhonemeSymbol}: ${postResetTarget.frequency}`
        : `Target phoneme missing after reset.`,
      frequency: postResetTarget?.frequency ?? null,
    });

    const recalcResponse = coerceJSON(
      await browserFetchJSON(
        client,
        `fetch('/api/admin/recalculate-phoneme-frequencies', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        }).then(async (res) => {
          const text = await res.text();
          let data;
          try { data = JSON.parse(text); } catch { data = text; }
          return { ok: res.ok, status: res.status, data };
        }).catch((error) => ({ ok: false, status: 0, error: String(error) }))`,
      ),
    );

    const recalcStatus = recalcResponse?.ok
      ? 'passed'
      : recalcResponse?.status === 404
        ? 'missing'
        : 'failed';
    recordStep({
      id: 'recalculate_frequencies',
      status: recalcStatus,
      message:
        recalcStatus === 'passed'
          ? 'Recalculate frequencies endpoint succeeded.'
          : `Endpoint response: ${JSON.stringify(recalcResponse)}`,
    });

    await callTool(client, 'browser_close', {}, 'Close browser');
    await client.close();

    await fs.writeFile(summaryPath, JSON.stringify({ ...summary, artifactsDir }, null, 2));
    console.log(`\nSummary written to ${summaryPath}`);
  } catch (error) {
    summary.error = error?.message ?? String(error);
    console.error('[mcp-admin-database-tools] failed', error);
    await fs.writeFile(summaryPath, JSON.stringify({ ...summary, artifactsDir, error: summary.error }, null, 2));
    await callTool(client, 'browser_close', {}, 'Close browser after failure').catch(() => {});
    await client.close();
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('[mcp-admin-database-tools] execution error', err);
  process.exit(1);
});

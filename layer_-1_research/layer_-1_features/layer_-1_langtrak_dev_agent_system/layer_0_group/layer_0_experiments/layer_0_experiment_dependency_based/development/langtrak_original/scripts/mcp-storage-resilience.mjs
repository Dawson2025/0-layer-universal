#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

const BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `storage${timestamp}`,
  email: `storage${timestamp}@example.com`,
  password: 'Test123!',
};

function resultText(result) {
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
    const braceIdx = text.indexOf('{');
    const bracketIdx = text.indexOf('[');
    const startIdx = (() => {
      if (braceIdx === -1) return bracketIdx;
      if (bracketIdx === -1) return braceIdx;
      return Math.min(braceIdx, bracketIdx);
    })();
    if (startIdx !== -1) {
      const trimmed = text.slice(startIdx);
      const endBrace = trimmed.lastIndexOf('}');
      const endBracket = trimmed.lastIndexOf(']');
      const endIdx = Math.max(endBrace, endBracket);
      if (endIdx !== -1) {
        parsed = tryParse(trimmed.slice(0, endIdx + 1));
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
    const text = resultText(result);
    if (text) console.log(text.trim());
  }
  if (summary) {
    summary.steps.push({
      action: label || name,
      args,
      output: resultText(result),
    });
  }
  return result;
}

async function browserEvalJSON(client, expression) {
  await client.callTool({
    name: 'browser_evaluate',
    arguments: { function: `async () => { window.__mcpPayload = await (${expression}); return true; }` },
  });
  const raw = await client.callTool({
    name: 'browser_evaluate',
    arguments: { function: "() => JSON.stringify(window.__mcpPayload ?? null)" },
  });
  const text = resultText(raw);
  if (!text) return null;
  return normalizeCliJson(text);
}

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'storage-resilience', `${timestamp}`);
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

async function registerUser(client, summary) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Navigate to login', summary);
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return true; }" },
    'Switch to sign-up',
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
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait post registration', summary);
}

async function createProject(client, summary, name, storagePreference) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, `Open create project (${storagePreference})`, summary);
  const result = await browserEvalJSON(
    client,
    `(() => {
      const nameInput = document.querySelector('#name');
      if (nameInput) {
        nameInput.value = '${name}';
        nameInput.dispatchEvent(new Event('input', { bubbles: true }));
      }
      const localRadio = document.querySelector('#storage_local');
      const cloudRadio = document.querySelector('#storage_cloud');
      if ('${storagePreference}' === 'cloud' && cloudRadio && !cloudRadio.disabled) {
        cloudRadio.checked = true;
        cloudRadio.dispatchEvent(new Event('change', { bubbles: true }));
      } else if (localRadio) {
        localRadio.checked = true;
        localRadio.dispatchEvent(new Event('change', { bubbles: true }));
      }
      const btn = document.querySelector('button.button.primary') || document.querySelector('form button[type="submit"]');
      if (btn) btn.click();
      return {
        cloudDisabled: cloudRadio ? cloudRadio.disabled : null,
        cloudChecked: cloudRadio ? cloudRadio.checked : null,
        localChecked: localRadio ? localRadio.checked : null,
      };
    })()`,
  );
  summary.formStates.push({
    projectName: name,
    storage: storagePreference,
    radioState: result,
  });
  await callTool(client, 'browser_wait_for', { time: 1 }, `Wait after creating ${name}`, summary);
}

async function snapshotProjects(client, summary, label) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, `Navigate to projects (${label})`, summary);
  await callTool(client, 'browser_wait_for', { time: 1 }, `Wait on projects (${label})`, summary);
  const storageSummary = await browserEvalJSON(client, 'window.collectStorageSummary ? window.collectStorageSummary() : window.__storageSummary');
  summary.storageSnapshots.push({ label, data: storageSummary });
  return storageSummary;
}

async function inspectCreateForm(client, summary, label) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, `Inspect create form (${label})`, summary);
  const state = await browserEvalJSON(
    client,
    `(() => {
      const cloudInput = document.querySelector('#storage_cloud');
      const localInput = document.querySelector('#storage_local');
      const cloudDesc = cloudInput
        ? (cloudInput.closest('.storage-option')?.querySelector('.storage-option-desc')?.textContent || '').trim()
        : '';
      return {
        cloudDisabled: !!(cloudInput && cloudInput.disabled),
        cloudChecked: !!(cloudInput && cloudInput.checked),
        localChecked: !!(localInput && localInput.checked),
        cloudDesc,
        firebaseBodyFlag: document.body.dataset.firebaseAvailable,
      };
    })()`,
  );
  summary.createFormStates.push({ label, state });
  return state;
}

function analyzeSnapshot(snapshot, output) {
  if (!snapshot || !snapshot.projects) return;
  output.firebaseAvailable = snapshot.firebaseAvailable;
  output.projectCount = snapshot.projects.length;
  output.localProjects = snapshot.projects
    .map((project) => ({
      name: project.name,
      groupId: project.groupId,
      variants: project.variants.filter((variant) => variant.storage === 'local'),
    }))
    .filter((project) => project.variants.length > 0);
  output.cloudProjects = snapshot.projects
    .map((project) => ({
      name: project.name,
      groupId: project.groupId,
      variants: project.variants.filter((variant) => variant.storage === 'cloud'),
    }))
    .filter((project) => project.variants.length > 0);
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summary = {
    user,
    steps: [],
    formStates: [],
    storageSnapshots: [],
    createFormStates: [],
    analysis: {},
    artifactsDir,
  };

  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    await registerUser(client, summary);
    await snapshotProjects(client, summary, 'initial');

    const localProjectName = `Local Project ${timestamp}`;
    await createProject(client, summary, localProjectName, 'local');
    const afterLocal = await snapshotProjects(client, summary, 'after_local_creation');

    const analysis = {};
    analyzeSnapshot(afterLocal, analysis);

    if (analysis.firebaseAvailable) {
      await inspectCreateForm(client, summary, 'before_cloud_creation');
      const cloudProjectName = `Cloud Project ${timestamp}`;
      await createProject(client, summary, cloudProjectName, 'cloud');
      const afterCloud = await snapshotProjects(client, summary, 'after_cloud_creation');
      analyzeSnapshot(afterCloud, analysis);
    } else {
      await inspectCreateForm(client, summary, 'firebase_unavailable_state');
      summary.analysis.notes = 'Firebase unavailable; cloud project creation skipped.';
    }

    summary.analysis = analysis;

    await inspectCreateForm(client, summary, 'final_form_state');
    await callTool(client, 'browser_close', {}, 'Close browser', summary);
    await client.close();
  } catch (error) {
    summary.error = error?.message || String(error);
    console.error('[mcp-storage-resilience] failure', error);
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
  console.error('[mcp-storage-resilience] execution error', err);
  process.exit(1);
});

// resource_id: "dc392c72-e4b6-41c2-83cc-1d49e42cda2d"
// resource_type: "document"
// resource_name: "mcp-journey-onboarding"
#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

const BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `journey${timestamp}`,
  email: `journey${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Onboarding Project ${timestamp}`;
const wordName = `intro-word-${timestamp}`;

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'journeys', `US-064-${timestamp}`);
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

function asText(result) {
  return (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text)
    .join('\n');
}

async function callTool(client, name, args, label, steps) {
  const result = await client.callTool({ name, arguments: args });
  if (label) {
    console.log(`\n=== ${label} ===`);
    const text = asText(result);
    if (text) console.log(text);
  }
  if (steps) {
    steps.push({ action: label || name, args, output: asText(result) });
  }
  return result;
}

async function registerUser(client, steps) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Visit login', steps);
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return true; }" },
    'Switch to sign-up',
    steps,
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const setValue = (sel, val) => { const el = document.querySelector(sel); if (el) { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); } };
        setValue('#reg-username', '${user.username}');
        setValue('#reg-email', '${user.email}');
        setValue('#reg-password', '${user.password}');
        setValue('#confirm-password', '${user.password}');
        return true;
      }`,
    },
    'Fill sign-up form',
    steps,
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelector('#register-tab .form-button')?.click(); return true; }" },
    'Submit registration',
    steps,
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after register', steps);
}

async function createAndEnterProject(client, steps) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` }, 'Open project create', steps);
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
    'Submit project create',
    steps,
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after project create', steps);

  await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Visit My Projects', steps);
  await callTool(
    client,
    'browser_evaluate',
    {
      function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return enter.href || 'clicked'; } return 'missing'; }",
    },
    'Enter project',
    steps,
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after enter', steps);
  await callTool(client, 'browser_snapshot', {}, 'Main menu snapshot', steps);
}

async function applyTemplate(client, steps) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` }, 'Visit templates', steps);
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const buttons = Array.from(document.querySelectorAll('button')).filter((btn) => btn.textContent?.includes('Apply Default Template'));
        if (buttons.length > 0) { buttons[0].click(); return 'clicked'; }
        return 'not-found';
      }`,
    },
    'Apply default template',
    steps,
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after template apply', steps);
}

async function createWord(client, steps) {
  await callTool(client, 'browser_navigate', { url: `${BASE}/words/create/table-based` }, 'Open word builder', steps);
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const setValue = (id, value) => { const el = document.querySelector(id); if (el) { el.value = value; el.dispatchEvent(new Event('input', { bubbles: true })); } };
        setValue('#language', 'Automation');
        setValue('#new_language_word', '${wordName}');
        const english = document.querySelector('#english_words');
        if (english) { english.value = 'hello,hi'; english.dispatchEvent(new Event('input', { bubbles: true })); }
        return true;
      }`,
    },
    'Fill word metadata',
    steps,
  );
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const blocks = Array.from(document.querySelectorAll('.phoneme-cell')).slice(0, 3);
        blocks.forEach((cell) => cell.click());
        return blocks.length;
      }`,
    },
    'Select phonemes',
    steps,
  );
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { const btn = document.querySelector('button.save-word'); if (btn) { btn.click(); return 'saved'; } return 'missing'; }" },
    'Save word',
    steps,
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after save', steps);
  await callTool(client, 'browser_snapshot', {}, 'Word saved snapshot', steps);

  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const listLink = document.querySelector('a.view-all-words');
        if (listLink) { listLink.click(); return 'navigated'; }
        return 'missing';
      }`,
    },
    'Navigate to word list',
    steps,
  );
  await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after word list', steps);
  await callTool(client, 'browser_snapshot', {}, 'Word list snapshot', steps);
}

async function playWordAudio(client, steps) {
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `async () => {
        const firstButton = document.querySelector('button.play-word-audio');
        if (firstButton) { firstButton.click(); return 'played'; }
        return 'missing';
      }`,
    },
    'Play word audio',
    steps,
  );
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summary = {
    user,
    projectName,
    wordName,
    steps: [],
    artifactsDir,
  };

  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    await registerUser(client, summary.steps);
    await createAndEnterProject(client, summary.steps);
    await applyTemplate(client, summary.steps);
    await createWord(client, summary.steps);
    await playWordAudio(client, summary.steps);

    await callTool(client, 'browser_close', {}, 'Close browser', summary.steps);
    await client.close();
  } catch (error) {
    summary.error = error?.message || String(error);
    console.error('[journey-onboarding] failure', error);
    await callTool(client, 'browser_close', {}, 'Close browser after failure', summary.steps).catch(() => {});
    await client.close();
    throw error;
  } finally {
    const summaryPath = path.join(artifactsDir, 'summary.json');
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`\nSummary saved to ${summaryPath}`);
  }
}

main().catch((err) => {
  console.error('[journey-onboarding] execution error', err);
  process.exit(1);
});

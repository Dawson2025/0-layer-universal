// resource_id: "13545845-ff92-496e-9f07-d28e3ab73b5a"
// resource_type: "document"
// resource_name: "mcp-journey-onboarding-realistic"
#!/usr/bin/env node
/**
 * USER-REALISTIC Onboarding Journey Test (US-064)
 *
 * Complete first-time user onboarding flow using realistic UI navigation.
 * This version attempts to navigate ONLY through UI buttons/links that a real user would see.
 *
 * KNOWN NAVIGATION GAPS EXPOSED BY THIS TEST:
 * - Admin templates page may not be accessible via standard UI navigation
 * - Table-based word creation may require direct URL access
 * - These gaps indicate potential UX improvements needed
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
} from './lib/navigation-helpers.mjs';

const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
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
  const dir = path.join(process.cwd(), 'artifacts', 'journeys', `US-064-realistic-${timestamp}`);
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

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summary = {
    user,
    projectName,
    wordName,
    steps: [],
    navigationGaps: [],
    artifactsDir,
  };

  const client = new Client({ name: 'realistic-onboarding-journey', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n<¯ USER-REALISTIC ONBOARDING JOURNEY TEST');
  console.log('========================================');
  console.log('Complete new user onboarding: Sign up ’ Create project ’ Create first word ’ Play audio\n');

  try {
    // Registration
    console.log('\n=Ý Phase 1: New user registration');
    await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/login` }, 'Visit login page', summary.steps);
    await switchTab(client, callTool, 1, 'Switch to Sign Up tab');
    await fillField(client, callTool, '#reg-username', user.username, 'Enter username');
    await fillField(client, callTool, '#reg-email', user.email, 'Enter email');
    await fillField(client, callTool, '#reg-password', user.password, 'Enter password');
    await fillField(client, callTool, '#confirm-password', user.password, 'Confirm password');
    await clickButtonWithText(client, callTool, 'Create Account', 'Submit registration');
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after registration', summary.steps);

    // Create project via UI
    console.log('\n=Â Phase 2: Create first project via UI');
    await clickElement(client, callTool, 'a[href="/projects/create"]', 'Create Project button', 'Navigate to create project');
    await fillField(client, callTool, '#name', projectName, 'Enter project name');
    await callTool(client, 'browser_evaluate', { function: "() => { const radio = document.querySelector('#storage_local'); if (radio) { radio.checked = true; radio.dispatchEvent(new Event('change', { bubbles: true })); } return true; }" }, 'Select local storage', summary.steps);
    await clickButtonWithText(client, callTool, 'Create Project', 'Submit project creation');
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after project creation', summary.steps);

    // Enter project
    await clickElement(client, callTool, 'a[href="/projects"]', 'Back to Projects', 'Return to projects list');
    await callTool(client, 'browser_evaluate', { function: "() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return 'entered'; } return 'missing'; }" }, 'Enter project', summary.steps);
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after entering project', summary.steps);

    // Apply template - NAVIGATION GAP POTENTIAL
    console.log('\n<¨ Phase 3: Apply template (testing for navigation gap)');
    const templateNavAttempt = await clickElement(client, callTool, 'a[href="/admin/templates"]', 'Templates link', 'Attempt to navigate to templates via UI');
    if (!templateNavAttempt) {
      summary.navigationGaps.push({ feature: 'Admin Templates', note: 'Not accessible via standard UI navigation' });
      console.log('   NAVIGATION GAP: Using direct URL for templates page');
      await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/admin/templates` }, 'Direct navigate to templates', summary.steps);
    }
    await callTool(client, 'browser_evaluate', { function: `() => { const btn = Array.from(document.querySelectorAll('button')).find(b => b.textContent?.includes('Apply Default Template')); if (btn) { btn.click(); return 'applied'; } return 'not-found'; }` }, 'Apply default template', summary.steps);
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after template apply', summary.steps);

    // Create word - NAVIGATION GAP POTENTIAL
    console.log('\n=Ý Phase 4: Create first word (testing for navigation gap)');
    const wordCreateAttempt = await clickElement(client, callTool, 'a[href="/words/create/table-based"]', 'Create Word button', 'Attempt to navigate to word builder');
    if (!wordCreateAttempt) {
      summary.navigationGaps.push({ feature: 'Table-based Word Creation', note: 'May require direct URL or alternate UI path' });
      console.log('   NAVIGATION GAP: Using direct URL for word creation');
      await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/words/create/table-based` }, 'Direct navigate to word builder', summary.steps);
    }

    await fillField(client, callTool, '#language', 'Automation', 'Enter language');
    await fillField(client, callTool, '#new_language_word', wordName, 'Enter word');
    await fillField(client, callTool, '#english_words', 'hello,hi', 'Enter English translations');
    await callTool(client, 'browser_evaluate', { function: `() => { const cells = Array.from(document.querySelectorAll('.phoneme-cell')).slice(0, 3); cells.forEach(c => c.click()); return cells.length; }` }, 'Select phonemes', summary.steps);
    await callTool(client, 'browser_evaluate', { function: "() => { const btn = document.querySelector('button.save-word'); if (btn) { btn.click(); return 'saved'; } return 'missing'; }" }, 'Save word', summary.steps);
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after word save', summary.steps);

    // Navigate to word list and play audio
    await callTool(client, 'browser_evaluate', { function: `() => { const link = document.querySelector('a.view-all-words'); if (link) { link.click(); return 'navigated'; } return 'missing'; }` }, 'Navigate to word list', summary.steps);
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait for word list', summary.steps);
    await callTool(client, 'browser_evaluate', { function: `async () => { const btn = document.querySelector('button.play-word-audio'); if (btn) { btn.click(); return 'played'; } return 'missing'; }` }, 'Play word audio', summary.steps);

    await callTool(client, 'browser_close', {}, 'Close browser', summary.steps);
    await client.close();

    console.log('\n Onboarding journey test completed!');
    if (summary.navigationGaps.length > 0) {
      console.log(`\n   Navigation gaps detected: ${summary.navigationGaps.length}`);
      summary.navigationGaps.forEach(gap => console.log(`   - ${gap.feature}: ${gap.note}`));
    }
  } catch (error) {
    summary.error = error?.message || String(error);
    console.error('[journey-onboarding-realistic] failure', error);
    await callTool(client, 'browser_close', {}, 'Close after failure', summary.steps).catch(() => {});
    await client.close();
    throw error;
  } finally {
    const summaryPath = path.join(artifactsDir, 'summary.json');
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`\n=Ä Summary saved to ${summaryPath}\n`);
  }
}

main().catch((err) => {
  console.error('[journey-onboarding-realistic] execution error', err);
  process.exit(1);
});

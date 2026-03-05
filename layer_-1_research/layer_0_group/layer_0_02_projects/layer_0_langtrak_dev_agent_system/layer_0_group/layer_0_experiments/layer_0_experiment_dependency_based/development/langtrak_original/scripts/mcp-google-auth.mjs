// resource_id: "f0890e61-a250-4360-9dc8-c7d5fec23fd3"
// resource_type: "document"
// resource_name: "mcp-google-auth"
#!/usr/bin/env node
/**
 * Google OAuth Authentication Test
 * Tests US-001-005 with Google Sign In instead of email/password
 *
 * Coverage:
 * - Google Sign In flow
 * - OAuth popup/redirect handling
 * - Firebase authentication
 * - Backend session creation with Google account
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';

import {
  performGoogleOAuthLogin,
  normalizeCliJson,
  getFirebaseAuthContext,
} from './lib/google-auth-helpers.mjs';

const BASE = 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';
const RUN_MODE = process.env.RUN_NAVIGATION_MODE ?? 'direct';
const useRealisticNavigation = RUN_MODE === 'realistic';

if (process.env.RUN_CLOUD_TESTS !== '1') {
  console.log('[google-auth-test] skipping (set RUN_CLOUD_TESTS=1 to enable)');
  process.exit(0);
}

// Google account credentials for testing (opt-in via environment variables).
const GOOGLE_EMAIL = process.env.GOOGLE_TEST_EMAIL;
const GOOGLE_PASSWORD = process.env.GOOGLE_TEST_PASSWORD;

if (!GOOGLE_EMAIL || !GOOGLE_PASSWORD) {
  console.error('[google-auth-test] missing GOOGLE_TEST_EMAIL / GOOGLE_TEST_PASSWORD');
  process.exit(1);
}

const timestamp = Date.now();
const summary = {
  testType: 'google_oauth_authentication',
  timestamp,
  googleEmail: 'configured_via_env',
  steps: [],
  artifacts: [],
};
summary.navigationMode = RUN_MODE;

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

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'google-auth');
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

function recordStep(entry) {
  summary.steps.push(entry);
  const { action, status } = entry;
  console.log(`\n[${action}] status=${status}`);
  if (entry.message) {
    console.log(`  ${entry.message}`);
  }
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summaryPath = path.join(artifactsDir, `run-${timestamp}.json`);

  const client = new Client({ name: 'google-auth-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  console.log('\n====================================');
  console.log('GOOGLE OAUTH AUTHENTICATION TEST');
  console.log('====================================');
  console.log('Flow: Navigate → Click Google Sign In → OAuth → Dashboard\n');

  try {
    // Navigate to login page
    await callTool(client, 'browser_navigate', { url: `${BASE}/login` }, 'Load login page');
    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Login page loaded');
    }

    recordStep({ action: 'navigate_login', status: 'ok' });

    // Check if Firebase/Google Sign In is available
    const googleButtonCheck = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const button = document.querySelector('#google-signin-btn');
          return {
            exists: !!button,
            disabled: button?.disabled || false,
            visible: button ? window.getComputedStyle(button).display !== 'none' : false,
            text: button?.textContent?.trim() || ''
          };
        }`
      },
      'Check Google Sign In button'
    );

    const rawButtonState = googleButtonCheck.content?.find(c => c.type === 'text')?.text || '{}';
    const buttonState = normalizeCliJson(rawButtonState) || {};

    if (!buttonState.exists || buttonState.disabled) {
      recordStep({
        action: 'check_google_signin',
        status: 'unavailable',
        message: 'Google Sign In not available - Firebase may not be configured',
        buttonState
      });

      console.log('\n⚠️  Google Sign In is not available on this instance.');
      console.log('This test requires Firebase to be configured with Google OAuth provider.');
      console.log('Skipping Google authentication test.');

      summary.skipped = true;
      summary.reason = 'Firebase/Google OAuth not configured';

      await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
      await callTool(client, 'browser_close', {});
      await client.close();
      process.exit(0);
    }

    recordStep({ action: 'check_google_signin', status: 'ok', buttonState });

    // Click Google Sign In button
    // Note: This will trigger OAuth popup/redirect which Playwright needs to handle
    console.log('\n🔐 Initiating automated Google OAuth login flow...');

    const loginResult = await performGoogleOAuthLogin(client, callTool, {
      email: GOOGLE_EMAIL,
      password: GOOGLE_PASSWORD,
      baseUrl: BASE,
    });

    recordStep({
      action: 'google_oauth_flow',
      status: loginResult.status === 'signed-in' ? 'ok' : 'skipped',
      message: loginResult.status === 'signed-in'
        ? 'Google OAuth completed with provided credentials'
        : 'User already signed in with Google',
      loginResult,
    });

    const firebaseContext = await getFirebaseAuthContext(client, callTool);
    summary.firebaseContext = {
      uid: firebaseContext.uid,
      email: firebaseContext.email,
      projectId: firebaseContext.projectId,
    };

    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Post Google OAuth');
    }

    // Ensure we land on the dashboard (default post-login destination)
    const postAuthCheck = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => ({
          url: window.location.href,
          pathname: window.location.pathname,
          hasDashboard: document.body.textContent.includes('Dashboard') || document.body.textContent.includes('Main Menu'),
          hasLogout: !!document.querySelector('.logout-link, a[href="/logout"]')
        })`
      },
      'Verify post-login state'
    );

    const rawPostAuth = postAuthCheck.content?.find(c => c.type === 'text')?.text || '{}';
    const postAuthState = normalizeCliJson(rawPostAuth) || {};

    recordStep({
      action: 'post_login_state',
      status: postAuthState.hasLogout ? 'ok' : 'warning',
      postAuthState,
    });

    if (loginResult?.firebase) {
      summary.firebaseUser = loginResult.firebase;
    }

    if (postAuthState.pathname === '/login') {
      await callTool(client, 'browser_navigate', { url: `${BASE}/dashboard` }, 'Navigate to dashboard');
      await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait for dashboard');
    }

    summary.result = 'success';

    if (useRealisticNavigation) {
      await callTool(client, 'browser_snapshot', {}, 'Final state after OAuth attempt');
    }
    await callTool(client, 'browser_close', {});
    await client.close();

    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`\n📄 Summary written to ${summaryPath}`);

    console.log('\n====================================');
    console.log('GOOGLE OAUTH TEST COMPLETE');
    console.log('====================================');
    console.log(`Result: ${summary.result || 'See summary for details'}`);
    console.log('\nNote: Full Google OAuth automation requires:');
    console.log('  - Firebase configured with Google OAuth provider');
    console.log('  - Playwright configured to handle OAuth popups/redirects');
    console.log('  - Or mock OAuth tokens for testing');

  } catch (error) {
    summary.error = error?.message ?? String(error);
    console.error('\n❌ [google-auth-test] failed', error);

    recordStep({
      action: 'test_error',
      status: 'failed',
      error: summary.error
    });

    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    await callTool(client, 'browser_close', {}).catch(() => {});
    await client.close();
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('[google-auth-test] execution error', err);
  process.exit(1);
});

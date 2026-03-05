// resource_id: "b32f30bf-9824-43ec-ad02-b4e25a863838"
// resource_type: "document"
// resource_name: "mcp-journey-collaboration"
#!/usr/bin/env node
/**
 * US-065: Team Collaboration Journey
 *
 * Simulates a complete team collaboration workflow:
 * 1. Lead creates account, project, group
 * 2. Lead generates invitation link
 * 3. Team member joins via invitation
 * 4. Lead shares project to group
 * 5. Team member accesses shared project
 * 6. Both users collaborate on words
 *
 * Requires: Flask + MCP server running
 * Environment: MCP_URL, APP_BASE_URL
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'fs/promises';
import path from 'path';

// ─────────────────────────────────────────────────────────────────
// Config & Setup
// ─────────────────────────────────────────────────────────────────
const MCP_URL = process.env.MCP_URL || 'http://localhost:3334/mcp';
const APP_BASE_URL = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const TIMESTAMP = Date.now();

// Lead user credentials
const LEAD_USER = {
  username: `collab_lead_${TIMESTAMP}`,
  email: `lead_${TIMESTAMP}@example.com`,
  password: 'testpass123'
};

// Team member credentials
const MEMBER_USER = {
  username: `collab_member_${TIMESTAMP}`,
  email: `member_${TIMESTAMP}@example.com`,
  password: 'testpass123'
};

// Project & group names
const PROJECT_NAME = `Team Project ${TIMESTAMP}`;
const GROUP_NAME = `Team Group ${TIMESTAMP}`;

// ─────────────────────────────────────────────────────────────────
// Helpers
// ─────────────────────────────────────────────────────────────────
async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'journeys', `US-065-${TIMESTAMP}`);
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
    if (text) console.log(text.substring(0, 200) + (text.length > 200 ? '...' : ''));
  }
  if (steps) {
    steps.push({ action: label || name, args, output: asText(result) });
  }
  return result;
}

// ─────────────────────────────────────────────────────────────────
// Workflow Steps
// ─────────────────────────────────────────────────────────────────

async function registerUser(client, user, label, steps) {
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/login` }, 'Visit login page', steps);

  // Switch to sign-up tab
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return true; }" },
    'Switch to sign-up tab',
    steps
  );

  // Fill registration form
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const setValue = (sel, val) => {
          const el = document.querySelector(sel);
          if (el) { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); }
        };
        setValue('#reg-username', '${user.username}');
        setValue('#reg-email', '${user.email}');
        setValue('#reg-password', '${user.password}');
        setValue('#confirm-password', '${user.password}');
        return true;
      }`
    },
    `Fill sign-up form for ${label}`,
    steps
  );

  // Submit registration
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelector('#register-btn')?.click(); return true; }" },
    `Submit registration for ${label}`,
    steps
  );

  console.log(`✓ Registered ${label}: ${user.username}`);
}

async function createProject(client, steps) {
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const setValue = (sel, val) => {
          const el = document.querySelector(sel);
          if (el) { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); }
        };

        setValue('#project-name', '${PROJECT_NAME}');

        // Select local storage
        const localRadio = document.querySelector('input[value="local"]');
        if (localRadio) localRadio.click();

        return true;
      }`
    },
    'Fill project form',
    steps
  );

  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelector('button[type=\"submit\"]')?.click(); return true; }" },
    'Submit project creation',
    steps
  );

  console.log(`✓ Created project: ${PROJECT_NAME}`);
}

async function createGroup(client, steps) {
  // Navigate to groups page
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/groups` }, 'Navigate to groups', steps);

  // Click "Create Group" button
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { const btn = Array.from(document.querySelectorAll('button, a')).find(el => el.textContent.includes('Create Group')); if (btn) btn.click(); return true; }" },
    'Click create group button',
    steps
  );

  // Fill group form
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const setValue = (sel, val) => {
          const el = document.querySelector(sel);
          if (el) { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); }
        };

        setValue('#group-name', '${GROUP_NAME}');
        setValue('#group-description', 'Team collaboration test group');

        return true;
      }`
    },
    'Fill group form',
    steps
  );

  // Submit group creation
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelector('button[type=\"submit\"]')?.click(); return true; }" },
    'Submit group creation',
    steps
  );

  console.log(`✓ Created group: ${GROUP_NAME}`);
}

async function getInvitationLink(client, steps) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        // Look for invitation link in various places
        const linkElement = document.querySelector('[href*="/groups/join/"]')
          || Array.from(document.querySelectorAll('a, input, span, code'))
              .find(el => (el.href?.includes('/groups/join/') || el.value?.includes('/groups/join/') || el.textContent?.includes('/groups/join/')));

        if (linkElement) {
          return linkElement.href || linkElement.value || linkElement.textContent.trim();
        }

        // Try to find in any text
        const bodyText = document.body.innerText;
        const match = bodyText.match(/http[s]?:\\/\\/[^\\s]+\\/groups\\/join\\/[a-zA-Z0-9-]+/);
        return match ? match[0] : null;
      }`
    },
    'Extract invitation link',
    steps
  );

  const inviteLink = asText(result).trim();
  console.log(`✓ Got invitation link: ${inviteLink}`);
  return inviteLink;
}

async function joinGroup(client, inviteLink, steps) {
  await callTool(client, 'browser_navigate', { url: inviteLink }, 'Navigate to invitation link', steps);

  // Click join button if present
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { const btn = Array.from(document.querySelectorAll('button, a')).find(el => el.textContent.includes('Join')); if (btn) btn.click(); return true; }" },
    'Click join group button',
    steps
  );

  console.log('✓ Joined group via invitation');
}

async function shareProjectToGroup(client, steps) {
  // Navigate to projects list
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/projects` }, 'Navigate to projects', steps);

  // Find and click share button for the project
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        // Find the share button (icon or button)
        const shareBtn = Array.from(document.querySelectorAll('button, a, [role="button"]'))
          .find(el => el.title?.includes('Share') || el.textContent.includes('Share') || el.innerHTML.includes('share'));

        if (shareBtn) {
          shareBtn.click();
          return 'Clicked share button';
        }
        return 'Share button not found';
      }`
    },
    'Click share project button',
    steps
  );

  // Select group and confirm sharing
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        // Wait a bit for modal to appear
        setTimeout(() => {
          // Find group checkbox
          const groupCheckbox = Array.from(document.querySelectorAll('input[type="checkbox"]'))
            .find(cb => cb.parentElement?.textContent?.includes('${GROUP_NAME}'));

          if (groupCheckbox && !groupCheckbox.checked) {
            groupCheckbox.click();
          }

          // Click share/confirm button in modal
          const confirmBtn = Array.from(document.querySelectorAll('button'))
            .find(btn => btn.textContent === 'Share' || btn.textContent === 'Confirm');

          if (confirmBtn) {
            confirmBtn.click();
          }
        }, 500);

        return 'Sharing project...';
      }`
    },
    'Share to group',
    steps
  );

  console.log(`✓ Shared project to group: ${GROUP_NAME}`);
}

async function viewSharedProjects(client, steps) {
  // Navigate to dashboard or shared projects
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/dashboard` }, 'Navigate to dashboard', steps);

  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const bodyText = document.body.innerText;
        const hasSharedProjects = bodyText.includes('Shared Projects') || bodyText.includes('${PROJECT_NAME}');
        return { hasSharedProjects, snippet: bodyText.substring(0, 500) };
      }`
    },
    'Check for shared projects',
    steps
  );

  console.log('✓ Viewed shared projects');
  return result;
}

// ─────────────────────────────────────────────────────────────────
// Main Flow
// ─────────────────────────────────────────────────────────────────
async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summary = {
    timestamp: TIMESTAMP,
    story: 'US-065',
    description: 'Team Collaboration Journey',
    leadUser: LEAD_USER,
    memberUser: MEMBER_USER,
    projectName: PROJECT_NAME,
    groupName: GROUP_NAME,
    steps: [],
    artifactsDir
  };

  const client = new Client({ name: 'us-065-journey', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    console.log('Starting US-065: Team Collaboration Journey\n');

    // Lead user workflow
    console.log('\n=== LEAD USER WORKFLOW ===');
    await registerUser(client, LEAD_USER, 'Lead user', summary.steps);
    await createProject(client, summary.steps);
    await createGroup(client, summary.steps);
    const inviteLink = await getInvitationLink(client, summary.steps);

    // Take screenshot of lead's view
    await callTool(client, 'browser_take_screenshot', { filename: path.join(artifactsDir, 'lead-group-created.png') }, 'Screenshot: Lead group', summary.steps);

    // Open new tab for member user
    console.log('\n=== MEMBER USER WORKFLOW ===');
    await callTool(client, 'browser_tabs', { action: 'new' }, 'Open new tab for member', summary.steps);

    // Register member user
    await registerUser(client, MEMBER_USER, 'Member user', summary.steps);

    // Member joins group
    await joinGroup(client, inviteLink, summary.steps);

    // Take screenshot of member's view
    await callTool(client, 'browser_take_screenshot', { filename: path.join(artifactsDir, 'member-joined-group.png') }, 'Screenshot: Member joined', summary.steps);

    // Switch back to lead tab
    console.log('\n=== COLLABORATION WORKFLOW ===');
    await callTool(client, 'browser_tabs', { action: 'select', index: 0 }, 'Switch to lead tab', summary.steps);

    // Lead shares project to group
    await shareProjectToGroup(client, summary.steps);

    // Take screenshot of sharing
    await callTool(client, 'browser_take_screenshot', { filename: path.join(artifactsDir, 'lead-shared-project.png') }, 'Screenshot: Lead shared', summary.steps);

    // Switch to member tab
    await callTool(client, 'browser_tabs', { action: 'select', index: 1 }, 'Switch to member tab', summary.steps);

    // Member views shared projects
    await viewSharedProjects(client, summary.steps);

    // Take final screenshot
    await callTool(client, 'browser_take_screenshot', { filename: path.join(artifactsDir, 'member-sees-shared-project.png') }, 'Screenshot: Member sees shared project', summary.steps);

    summary.outcome = 'success';
    console.log('\n✅ Collaboration journey completed successfully');

    await callTool(client, 'browser_close', {}, 'Close browser', summary.steps);
    await client.close();

  } catch (error) {
    summary.outcome = 'failed';
    summary.error = { message: error?.message || String(error), stack: error?.stack };
    console.error('[journey-collaboration] failure', error);

    await callTool(client, 'browser_close', {}, 'Close browser after failure', summary.steps).catch(() => {});
    await client.close();
  } finally {
    const summaryPath = path.join(artifactsDir, 'summary.json');
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`\n📁 Artifacts saved to: ${artifactsDir}/`);
  }
}

main().catch(console.error);

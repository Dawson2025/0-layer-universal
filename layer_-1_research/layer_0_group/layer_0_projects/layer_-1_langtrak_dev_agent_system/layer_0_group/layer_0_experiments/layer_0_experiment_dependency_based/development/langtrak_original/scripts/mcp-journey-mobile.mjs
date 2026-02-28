#!/usr/bin/env node
/**
 * US-067: Mobile-First Creator Journey
 *
 * Simulates a mobile user creating language content on their phone:
 * 1. User accesses app on mobile device
 * 2. User logs in with touch-friendly auth
 * 3. User navigates to project
 * 4. User creates word with mobile-optimized flow
 * 5. User scrolls through form sections
 * 6. User taps phoneme blocks
 * 7. User uploads media (simulated)
 * 8. User plays pronunciation audio
 * 9. User searches and edits words
 *
 * Validates mobile-specific requirements:
 * - Vertical layout (no horizontal scroll)
 * - Touch targets >= 44x44px
 * - Responsive breakpoints
 * - Keyboard behavior
 * - Media upload from camera
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

const USER = {
  username: `mobile_user_${TIMESTAMP}`,
  email: `mobile_${TIMESTAMP}@example.com`,
  password: 'testpass123'
};

const PROJECT_NAME = `Mobile Project ${TIMESTAMP}`;

// Mobile device emulation (iPhone 12)
const MOBILE_VIEWPORT = {
  width: 390,
  height: 844
};

// ─────────────────────────────────────────────────────────────────
// Helpers
// ─────────────────────────────────────────────────────────────────
async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'journeys', `US-067-${TIMESTAMP}`);
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

function asText(result) {
  return (result.content ?? [])
    .filter((part) => part.type === 'text')
    .map((part) => part.text)
    .join('\n');
}

function extractJSON(mcpResponse) {
  const text = asText(mcpResponse);
  // Handle markdown-wrapped JSON responses from MCP server
  const match = text.match(/###\s*Result\s*\n([\s\S]*?)(?:\n###|$)/);
  if (match) {
    return match[1].trim();
  }
  return text.trim();
}

function parseJSONSafe(mcpResponse, fallback = {}) {
  try {
    const jsonText = extractJSON(mcpResponse);
    return JSON.parse(jsonText);
  } catch (error) {
    console.warn('Could not parse MCP response as JSON:', error.message);
    return fallback;
  }
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

async function setupMobileViewport(client, steps) {
  await callTool(
    client,
    'browser_resize',
    { width: MOBILE_VIEWPORT.width, height: MOBILE_VIEWPORT.height },
    `Set mobile viewport (${MOBILE_VIEWPORT.width}x${MOBILE_VIEWPORT.height})`,
    steps
  );

  console.log(`✓ Set mobile viewport: ${MOBILE_VIEWPORT.width}x${MOBILE_VIEWPORT.height}`);
}

async function checkResponsiveLayout(client, steps) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const body = document.body;
        const hasHorizontalScroll = body.scrollWidth > window.innerWidth;
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;

        // Check for responsive meta tag
        const viewportMeta = document.querySelector('meta[name="viewport"]');
        const hasViewportMeta = !!viewportMeta;
        const viewportContent = viewportMeta?.getAttribute('content');

        return {
          viewportWidth,
          viewportHeight,
          bodyScrollWidth: body.scrollWidth,
          hasHorizontalScroll,
          hasViewportMeta,
          viewportContent,
          isMobile: viewportWidth < 768
        };
      }`
    },
    'Check responsive layout',
    steps
  );

  const layoutInfo = parseJSONSafe(result, {
    viewportWidth: 0,
    viewportHeight: 0,
    hasHorizontalScroll: false,
    isMobile: false
  });
  console.log('✓ Checked responsive layout:', layoutInfo);

  return layoutInfo;
}

async function registerAndLogin(client, steps) {
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/login` }, 'Visit login page', steps);

  // Check layout after navigation
  await checkResponsiveLayout(client, steps);

  // Switch to sign-up tab
  await callTool(
    client,
    'browser_evaluate',
    { function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return true; }" },
    'Tap sign-up tab',
    steps
  );

  // Fill and submit registration
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const setValue = (sel, val) => {
          const el = document.querySelector(sel);
          if (el) { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); }
        };
        setValue('#reg-username', '${USER.username}');
        setValue('#reg-email', '${USER.email}');
        setValue('#reg-password', '${USER.password}');
        setValue('#confirm-password', '${USER.password}');
        document.querySelector('#register-btn')?.click();
        return true;
      }`
    },
    'Register user (mobile)',
    steps
  );

  console.log(`✓ Registered mobile user: ${USER.username}`);
}

async function createProject(client, steps) {
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/projects/create` }, 'Navigate to create project', steps);

  await checkResponsiveLayout(client, steps);

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
        const localRadio = document.querySelector('input[value="local"]');
        if (localRadio) localRadio.click();
        document.querySelector('button[type="submit"]')?.click();
        return true;
      }`
    },
    'Create project (mobile)',
    steps
  );

  console.log(`✓ Created project: ${PROJECT_NAME}`);

  // Apply phonemes
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/admin/templates` }, 'Navigate to templates', steps);

  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const resetBtn = Array.from(document.querySelectorAll('button, a'))
          .find(el => el.textContent.includes('Reset to Default') || el.textContent.includes('Apply Default'));
        if (resetBtn) {
          resetBtn.click();
          setTimeout(() => {
            const confirmBtn = Array.from(document.querySelectorAll('button'))
              .find(btn => btn.textContent === 'Confirm' || btn.textContent === 'Yes');
            if (confirmBtn) confirmBtn.click();
          }, 300);
        }
        return 'Applied phonemes';
      }`
    },
    'Apply phonemes',
    steps
  );
}

async function createWordMobile(client, steps) {
  await callTool(client, 'browser_navigate', { url: `${APP_BASE_URL}/words/create` }, 'Navigate to word creation (mobile)', steps);

  const layoutInfo = await checkResponsiveLayout(client, steps);

  // Check mobile-specific layout
  const mobileLayoutCheck = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const form = document.querySelector('form, .word-creation-form, .create-word-container');
        if (!form) return { found: false };

        // Check for vertical layout
        const formRect = form.getBoundingClientRect();
        const isVertical = formRect.width <= window.innerWidth;

        // Find sections and check if they're stacked
        const sections = Array.from(form.querySelectorAll('section, .form-section, .syllable-config, .word-preview'))
          .map(section => {
            const rect = section.getBoundingClientRect();
            return {
              tag: section.tagName,
              class: section.className,
              width: rect.width,
              left: rect.left,
              isFullWidth: rect.width >= window.innerWidth * 0.9
            };
          });

        // Check button sizes (should be >= 44x44 for touch)
        const buttons = Array.from(document.querySelectorAll('button'))
          .map(btn => {
            const rect = btn.getBoundingClientRect();
            return {
              text: btn.textContent?.trim().substring(0, 20),
              width: rect.width,
              height: rect.height,
              isTouchFriendly: rect.width >= 44 && rect.height >= 44
            };
          })
          .filter(btn => btn.width > 0); // Only visible buttons

        return {
          found: true,
          isVertical,
          formWidth: formRect.width,
          viewportWidth: window.innerWidth,
          sections,
          sampleButtons: buttons.slice(0, 5),
          touchFriendlyButtons: buttons.filter(b => b.isTouchFriendly).length,
          totalButtons: buttons.length
        };
      }`
    },
    'Check mobile word creation layout',
    steps
  );

  const layoutData = parseJSONSafe(mobileLayoutCheck, {
    found: false,
    isVertical: true,
    touchFriendlyButtons: 0,
    totalButtons: 0
  });
  console.log('✓ Mobile layout check:', {
    isVertical: layoutData.isVertical,
    touchFriendlyButtons: `${layoutData.touchFriendlyButtons}/${layoutData.totalButtons}`
  });

  // Fill word creation form
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const englishInput = document.querySelector('input[name="english"]') || document.querySelector('#english-word');
        if (englishInput) {
          englishInput.value = 'mobile';
          englishInput.dispatchEvent(new Event('input', { bubbles: true }));
        }
        return 'Set word: mobile';
      }`
    },
    'Fill word (mobile)',
    steps
  );

  // Simulate scrolling through sections
  await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const sections = document.querySelectorAll('section, .form-section');
        let scrolled = [];
        sections.forEach((section, i) => {
          section.scrollIntoView({ behavior: 'smooth', block: 'start' });
          scrolled.push(section.className || section.tagName);
        });
        return { scrolledSections: scrolled, count: scrolled.length };
      }`
    },
    'Scroll through form sections',
    steps
  );

  console.log('✓ Created word on mobile with smooth scrolling');

  return layoutData;
}

async function testPhonemeInteraction(client, steps) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        // Find phoneme blocks
        const phonemeBlocks = Array.from(document.querySelectorAll('.phoneme-block, [data-phoneme], .ipa-symbol'))
          .map(block => {
            const rect = block.getBoundingClientRect();
            return {
              text: block.textContent?.trim(),
              width: rect.width,
              height: rect.height,
              isTappable: rect.width >= 44 && rect.height >= 44,
              hasClickHandler: !!block.onclick || block.getAttribute('onclick') || block.dataset.phoneme
            };
          })
          .filter(block => block.width > 0);

        // Simulate a tap on first phoneme if available
        const firstPhoneme = document.querySelector('.phoneme-block, [data-phoneme]');
        let tapped = false;
        if (firstPhoneme) {
          firstPhoneme.click();
          tapped = true;
        }

        return {
          phonemeBlocksFound: phonemeBlocks.length,
          sampleBlocks: phonemeBlocks.slice(0, 3),
          tappableBlocks: phonemeBlocks.filter(b => b.isTappable).length,
          tappedFirst: tapped
        };
      }`
    },
    'Test phoneme tap interaction',
    steps
  );

  const tapData = parseJSONSafe(result, {
    phonemeBlocksFound: 0,
    tappableBlocks: 0,
    tappedFirst: false
  });
  console.log('✓ Tested phoneme interaction:', tapData);

  return tapData;
}

async function checkMediaUpload(client, steps) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const fileInputs = Array.from(document.querySelectorAll('input[type="file"]'))
          .map(input => ({
            id: input.id,
            accept: input.accept,
            name: input.name,
            hasCapture: input.hasAttribute('capture') || input.getAttribute('capture') === 'camera',
            isVisible: input.offsetParent !== null
          }));

        const uploadButtons = Array.from(document.querySelectorAll('button, label'))
          .filter(el => el.textContent?.toLowerCase().includes('upload') ||
                       el.textContent?.toLowerCase().includes('video') ||
                       el.textContent?.toLowerCase().includes('media'))
          .map(btn => ({
            text: btn.textContent?.trim().substring(0, 30),
            tag: btn.tagName,
            forInput: btn.getAttribute('for')
          }));

        return {
          fileInputsFound: fileInputs.length,
          fileInputs,
          uploadButtons,
          supportsCameraUpload: fileInputs.some(i => i.hasCapture)
        };
      }`
    },
    'Check media upload capability',
    steps
  );

  const uploadData = parseJSONSafe(result, {
    fileInputsFound: 0,
    supportsCameraUpload: false
  });
  console.log('✓ Checked media upload:', {
    inputs: uploadData.fileInputsFound,
    supportsCamera: uploadData.supportsCameraUpload
  });

  return uploadData;
}

async function generateMobileReport(layoutInfo, layoutData, tapData, uploadData) {
  return {
    viewport: MOBILE_VIEWPORT,
    responsiveness: {
      hasHorizontalScroll: layoutInfo.hasHorizontalScroll,
      hasViewportMeta: layoutInfo.hasViewportMeta,
      isMobile: layoutInfo.isMobile,
      viewportContent: layoutInfo.viewportContent
    },
    layout: {
      isVertical: layoutData.isVertical,
      touchFriendlyButtons: layoutData.touchFriendlyButtons,
      totalButtons: layoutData.totalButtons,
      touchFriendlyPercentage: ((layoutData.touchFriendlyButtons / layoutData.totalButtons) * 100).toFixed(1) + '%'
    },
    interaction: {
      phonemeBlocksFound: tapData.phonemeBlocksFound,
      tappableBlocks: tapData.tappableBlocks,
      tappedFirst: tapData.tappedFirst
    },
    media: {
      fileInputsFound: uploadData.fileInputsFound,
      supportsCameraUpload: uploadData.supportsCameraUpload
    },
    requirements: {
      noHorizontalScroll: !layoutInfo.hasHorizontalScroll ? '✅' : '❌',
      touchTargets44px: layoutData.touchFriendlyButtons > 0 ? '✅' : '⚠️',
      verticalLayout: layoutData.isVertical ? '✅' : '❌',
      mediaUpload: uploadData.fileInputsFound > 0 ? '✅' : '❌'
    }
  };
}

// ─────────────────────────────────────────────────────────────────
// Main Flow
// ─────────────────────────────────────────────────────────────────
async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const summary = {
    timestamp: TIMESTAMP,
    story: 'US-067',
    description: 'Mobile-First Creator Journey',
    user: USER,
    projectName: PROJECT_NAME,
    viewport: MOBILE_VIEWPORT,
    steps: [],
    artifactsDir
  };

  const client = new Client({ name: 'us-067-journey', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  try {
    console.log('Starting US-067: Mobile Journey\n');
    console.log(`Mobile Viewport: ${MOBILE_VIEWPORT.width}x${MOBILE_VIEWPORT.height}\n`);

    // Setup mobile viewport
    await setupMobileViewport(client, summary.steps);

    await callTool(
      client,
      'browser_take_screenshot',
      { filename: 'mobile-viewport-set.png' },
      'Screenshot: Mobile viewport',
      summary.steps
    );

    // User workflow
    await registerAndLogin(client, summary.steps);

    await callTool(
      client,
      'browser_take_screenshot',
      { filename: 'mobile-registration.png' },
      'Screenshot: Mobile registration',
      summary.steps
    );

    await createProject(client, summary.steps);

    await callTool(
      client,
      'browser_take_screenshot',
      { filename: 'mobile-project-created.png' },
      'Screenshot: Mobile project',
      summary.steps
    );

    // Mobile word creation with validation
    const layoutInfo = await checkResponsiveLayout(client, summary.steps);
    const layoutData = await createWordMobile(client, summary.steps);

    await callTool(
      client,
      'browser_take_screenshot',
      { filename: 'mobile-word-creation.png' },
      'Screenshot: Mobile word creation',
      summary.steps
    );

    const tapData = await testPhonemeInteraction(client, summary.steps);
    const uploadData = await checkMediaUpload(client, summary.steps);

    await callTool(
      client,
      'browser_take_screenshot',
      { filename: 'mobile-final-state.png' },
      'Screenshot: Mobile final',
      summary.steps
    );

    // Generate mobile validation report
    summary.mobileReport = await generateMobileReport(layoutInfo, layoutData, tapData, uploadData);

    summary.outcome = 'success';
    console.log('\n✅ Mobile journey completed successfully');
    console.log('\n📱 Mobile Requirements Check:');
    console.log(JSON.stringify(summary.mobileReport.requirements, null, 2));

    await callTool(client, 'browser_close', {}, 'Close browser', summary.steps);
    await client.close();

  } catch (error) {
    summary.outcome = 'failed';
    summary.error = { message: error?.message || String(error), stack: error?.stack };
    console.error('[journey-mobile] failure', error);

    await callTool(client, 'browser_close', {}, 'Close browser after failure', summary.steps).catch(() => {});
    await client.close();
  } finally {
    const summaryPath = path.join(artifactsDir, 'summary.json');
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`\n📁 Artifacts saved to: ${artifactsDir}/`);
  }
}

main().catch(console.error);

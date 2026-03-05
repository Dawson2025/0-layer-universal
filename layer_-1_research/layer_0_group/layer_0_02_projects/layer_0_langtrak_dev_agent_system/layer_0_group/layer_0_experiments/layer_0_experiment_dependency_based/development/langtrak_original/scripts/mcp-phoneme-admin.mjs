// resource_id: "3b9a339f-e800-45bf-bdb8-c64975076d74"
// resource_type: "document"
// resource_name: "mcp-phoneme-admin"
#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import fs from 'node:fs/promises';
import path from 'node:path';
import {
  navigateFromDashboard,
  navigateFromProjectMenu,
  enterProject,
  clickElement,
  waitForElement,
  waitForCondition,
} from './lib/navigation-helpers.mjs';

const BASE = process.env.APP_BASE_URL || 'http://127.0.0.1:5002';
const MCP_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

const timestamp = Date.now();
const user = {
  username: `admin${timestamp}`,
  email: `admin${timestamp}@example.com`,
  password: 'Test123!',
};
const projectName = `Admin Project ${timestamp}`;
const phonemeSymbol = `Qa${timestamp}`;
const bulkPhonemeSymbols = [`Rb${timestamp}`, `Sc${timestamp}`];
const customLengthType = `automation_length_${timestamp}`;
const customGroupType = `automation_group_${timestamp}`;
const customSubgroupType = `automation_subgroup_${timestamp}`;
const templateName = `Template_${timestamp}`;
const templateDescription = 'Automation export';
const importTemplateName = `Imported_${timestamp}`;
const templateSeedSymbols = [`Tpl${timestamp}A`, `Tpl${timestamp}B`];
const navigationMode = process.env.RUN_NAVIGATION_MODE ?? 'direct';
const useRealisticNavigation = navigationMode === 'realistic';

async function callTool(client, name, args, label) {
  const result = await client.callTool({ name, arguments: args });
  if (label) {
    const text = (result.content ?? [])
      .filter((part) => part.type === 'text')
      .map((part) => part.text.trim())
      .filter(Boolean)
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
    function: "() => JSON.stringify(window.__mcpPayload ?? null)",
  });
  const textPart = result.content?.find((p) => p.type === 'text');
  if (!textPart?.text) return null;
  const raw = textPart.text.trim();

  const attemptParse = (input) => {
    let value = input;
    let iterations = 0;
    while (typeof value === 'string' && iterations < 5) {
      try {
        value = JSON.parse(value);
      } catch {
        return { success: false, value };
      }
      iterations += 1;
    }
    return { success: true, value };
  };

  const cleaned = raw
    .replace(/^### Result\s+/i, '')
    .replace(/^```(?:json)?\s*/i, '')
    .replace(/\s*```$/i, '')
    .trim();
  const diagnosticsIndex = cleaned.indexOf('\n###');
  const baseCleaned = diagnosticsIndex !== -1 ? cleaned.slice(0, diagnosticsIndex).trim() : cleaned;

  const variants = [];
  const seen = new Set();
  const pushVariant = (value) => {
    if (typeof value !== 'string') return;
    if (!seen.has(value)) {
      variants.push(value);
      seen.add(value);
    }
  };

  pushVariant(baseCleaned);
  if (baseCleaned.startsWith('"') && baseCleaned.endsWith('"')) {
    pushVariant(baseCleaned.slice(1, -1));
  }

  for (let i = 0; i < variants.length; i += 1) {
    const current = variants[i];
    pushVariant(current.replace(/\\n/g, '\n').replace(/\\t/g, '\t').replace(/\\r/g, '\r'));
    pushVariant(current.replace(/\\\\/g, '\\'));
    pushVariant(current.replace(/\\"/g, '"'));
    const diagIdx = current.indexOf('\n###');
    if (diagIdx !== -1) {
      pushVariant(current.slice(0, diagIdx).trim());
    }
  }

  for (const candidate of variants) {
    const parsedCandidate = attemptParse(candidate);
    if (parsedCandidate.success) {
      return parsedCandidate.value;
    }
    const start = candidate.indexOf('{');
    const end = candidate.lastIndexOf('}');
    if (start !== -1 && end !== -1 && end > start) {
      const inner = candidate.slice(start, end + 1);
      const parsedInner = attemptParse(inner);
      if (parsedInner.success) {
        return parsedInner.value;
      }
    }
    const arrayStart = candidate.indexOf('[');
    const arrayEnd = candidate.lastIndexOf(']');
    if (arrayStart !== -1 && arrayEnd !== -1 && arrayEnd > arrayStart) {
      const innerArray = candidate.slice(arrayStart, arrayEnd + 1);
      const parsedArray = attemptParse(innerArray);
      if (parsedArray.success) {
        return parsedArray.value;
      }
    }
  }

  return baseCleaned;
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

async function fetchAdminPhonemes(client) {
  const response = await browserFetchJSON(client, "fetch('/api/admin/phonemes').then(r => r.json())");
  const parsed = coerceJSON(response);
  if (!parsed || typeof parsed !== 'object') return null;
  if (parsed.success !== true || !Array.isArray(parsed.phonemes)) return parsed;
  return parsed;
}

async function fetchAdminPhonemesWithRetry(client, symbol, attempts = 8, delayMs = 300) {
  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    const payload = await fetchAdminPhonemes(client);
    const phonemes = payload?.phonemes;
    if (Array.isArray(phonemes) && (!symbol || phonemes.some((p) => p?.phoneme === symbol))) {
      return payload;
    }
    await callTool(client, 'browser_wait_for', { time: delayMs / 1000 }, `Wait before retry phonemes fetch (${attempt}/${attempts})`);
  }
  return await fetchAdminPhonemes(client);
}

async function ensureArtifactsDir() {
  const dir = path.join(process.cwd(), 'artifacts', 'phoneme-admin');
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

async function fetchTemplateSummaries(client) {
  const templates = coerceJSON(
    await browserFetchJSON(
      client,
      `(async () => {
        const res = await fetch('/admin/templates');
        if (!res.ok) {
          return { ok: false, status: res.status };
        }
        const html = await res.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const cards = Array.from(doc.querySelectorAll('.template-card'));
        return cards.map(card => {
          const name = card.querySelector('h4')?.textContent?.trim() || '';
          const applyButton = card.querySelector('button');
          const onclick = applyButton?.getAttribute('onclick') || '';
          const idMatch = onclick.match(/applyTemplate\((\d+)\)/);
          return {
            name,
            id: idMatch ? Number(idMatch[1]) : null,
          };
        });
      })()`
    )
  );
  return Array.isArray(templates) ? templates : [];
}

async function main() {
  const artifactsDir = await ensureArtifactsDir();
  const client = new Client({ name: 'codex-cli', version: '0.1.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(MCP_URL)));

  const summary = {
    user,
    projectName,
    phoneme: phonemeSymbol,
    bulkPhonemes: bulkPhonemeSymbols,
    templateName,
    importTemplateName,
    navigationMode,
    steps: [],
  };

  try {
    // Register user and log in
    await callTool(client, 'browser_navigate', { url: `${BASE}/login` });
    await callTool(client, 'browser_evaluate', {
      function: "() => { document.querySelectorAll('.tab-button')[1]?.click(); return true; }",
    });
    await callTool(client, 'browser_evaluate', {
      function: `() => { const f = (sel, val) => { const el = document.querySelector(sel); if (el) { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); } }; f('#reg-username', '${user.username}'); f('#reg-email', '${user.email}'); f('#reg-password', '${user.password}'); f('#confirm-password', '${user.password}'); return true; }`,
    });
    await callTool(client, 'browser_evaluate', {
      function: "() => { document.querySelector('#register-tab .form-button')?.click(); return true; }",
    });
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after registration');
    await callTool(client, 'browser_snapshot', {}, 'Dashboard after registration');

    // Create local project
    if (useRealisticNavigation) {
      await callTool(client, 'browser_evaluate', {
        function: `() => {
          const el = Array.from(document.querySelectorAll('a.create-button')).find(e => e.textContent.includes("Create New Project"));
          if (el) {
            const payload = { clicked: true, text: el.textContent?.trim() || '', href: el.href || '' };
            window.setTimeout(() => el.click(), 0);
            return payload;
          }
          return { clicked: false, error: 'element-not-found' };
        }`
      });
      const formReady = await waitForElement(client, callTool, '#name', 5000);
      if (!formReady) {
        throw new Error('Project creation form did not load via UI navigation');
      }
    } else {
      await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
    }
    await callTool(client, 'browser_evaluate', {
      function: `() => { document.querySelector('#name').value = '${projectName}'; document.querySelector('#storage_local').checked = true; document.querySelector('button.button.primary')?.click(); return true; }`,
    });
    await callTool(client, 'browser_wait_for', { time: 1 }, 'Wait after project creation');
    await callTool(client, 'browser_snapshot', {}, 'After project creation');

    // Enter project from projects list to ensure session context
    if (useRealisticNavigation) {
      await clickElement(client, callTool, 'a[href="/projects"]', 'Projects breadcrumb', 'Return to projects list');
      const projectsLoaded = await waitForElement(client, callTool, 'a.action-button.enter', 5000);
      if (!projectsLoaded) {
        await callTool(client, 'browser_navigate', { url: `${BASE}/projects` }, 'Fallback navigate to projects');
      }
      await enterProject(client, callTool, 0);
    } else {
      await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
      await callTool(client, 'browser_evaluate', {
        function: `() => { const enter = document.querySelector('a.action-button.enter'); if (enter) { enter.click(); return enter.href || 'clicked'; } return 'not-found'; }`,
      });
    }
    await callTool(client, 'browser_wait_for', { time: 1 });
    await callTool(client, 'browser_snapshot', {});

    // Open admin phonemes dashboard
    if (useRealisticNavigation) {
      await navigateFromProjectMenu(client, callTool, 'admin-phonemes');
      const adminReady = await waitForCondition(
        client,
        callTool,
        "() => window.location.pathname === '/admin/phonemes'",
        5000,
        250,
        'Wait for admin phonemes navigation'
      );
      if (!adminReady) {
        await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` }, 'Fallback navigate to admin phonemes');
      }
    } else {
      await callTool(client, 'browser_navigate', { url: `${BASE}/admin/phonemes` });
    }
    await callTool(client, 'browser_snapshot', {});
    summary.steps.push({ action: 'view_admin_phonemes', status: 'ok' });

    // Fetch existing phonemes
    const phonemeList = coerceJSON(await browserFetchJSON(client, "fetch('/api/admin/phonemes').then(r => r.json())"));
    if (!phonemeList || !Array.isArray(phonemeList.phonemes)) {
      console.error('phonemeList debug typeof', typeof phonemeList);
      console.error('phonemeList debug value', phonemeList);
      throw new Error(`Failed to load phonemes: ${JSON.stringify(phonemeList)}`);
    }
    const onsetFallback = phonemeList.phonemes.find((p) => p.position === 'nucleus') ?? phonemeList.phonemes[0];
    const codaFallback = phonemeList.phonemes.find((p) => p.position === 'coda') ?? phonemeList.phonemes[1];

    // Wait for dropdowns to populate, then add new phoneme via UI form to exercise admin workflow
    const dropdownReady = await waitForCondition(
      client,
      callTool,
      "() => { const select = document.getElementById('lengthTypeSelect'); return !!(select && select.options.length > 1); }",
      5000,
      250,
      'Wait for admin dropdown options'
    );
    if (!dropdownReady) {
      throw new Error('Phoneme admin dropdowns never populated');
    }

    await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const ensureCustomValue = (selectId, inputId, value) => {
            const select = document.getElementById(selectId);
            if (!select) {
              return { ok: false, reason: 'missing-select:' + selectId };
            }
            const hasValue = Array.from(select.options).some((opt) => opt.value === value && opt.value !== 'custom');
            if (hasValue) {
              select.value = value;
              select.dispatchEvent(new Event('change', { bubbles: true }));
              return { ok: true, mode: 'existing', value };
            }
            const customOption = Array.from(select.options).find((opt) => opt.value === 'custom');
            if (!customOption) {
              return { ok: false, reason: 'custom-option-missing:' + selectId };
            }
            select.value = 'custom';
            select.dispatchEvent(new Event('change', { bubbles: true }));
            const input = document.getElementById(inputId);
            if (!input) {
              return { ok: false, reason: 'missing-input:' + inputId };
            }
            input.value = value;
            input.dispatchEvent(new Event('input', { bubbles: true }));
            return { ok: true, mode: 'custom', value };
          };

          const result = {
            length: ensureCustomValue('lengthTypeSelect', 'lengthType', ${JSON.stringify(customLengthType)}),
            group: ensureCustomValue('groupTypeSelect', 'groupType', ${JSON.stringify(customGroupType)}),
            subgroup: ensureCustomValue('subgroupTypeSelect', 'subgroupType', ${JSON.stringify(customSubgroupType)})
          };

          const phonemeInput = document.getElementById('phoneme');
          const frequencyInput = document.getElementById('frequency');
          if (!phonemeInput || !frequencyInput) {
            return { ok: false, reason: 'missing-core-inputs', result };
          }
          phonemeInput.value = ${JSON.stringify(phonemeSymbol)};
          phonemeInput.dispatchEvent(new Event('input', { bubbles: true }));
          frequencyInput.value = '0';
          frequencyInput.dispatchEvent(new Event('input', { bubbles: true }));

          const syllableSelect = document.getElementById('syllableType');
          const positionSelect = document.getElementById('position');
          if (syllableSelect) {
            syllableSelect.value = 'CVC';
            syllableSelect.dispatchEvent(new Event('change', { bubbles: true }));
          }
          if (positionSelect) {
            positionSelect.value = 'onset';
            positionSelect.dispatchEvent(new Event('change', { bubbles: true }));
          }

          const form = document.getElementById('addPhonemeForm');
          form?.requestSubmit();
          return { ok: true, result };
        }`,
      },
      'Submit add phoneme form via UI'
    );

    const phonemeRowAppeared = await waitForCondition(
      client,
      callTool,
      `() => Array.from(document.querySelectorAll('#phonemesTableBody .phoneme-cell'))
        .some((cell) => cell.textContent.trim() === ${JSON.stringify(phonemeSymbol)})`,
      5000,
      250,
      'Wait for newly added phoneme row'
    );
    if (!phonemeRowAppeared) {
      throw new Error('Added phoneme row not detected in UI');
    }
    summary.steps.push({ action: 'add_phoneme', symbol: phonemeSymbol, method: 'ui_form', status: 'ok' });

    // Fetch updated phonemes to get ID
    const updatedPhonemes = await fetchAdminPhonemesWithRetry(client, phonemeSymbol);
    const addedPhonemeEntry = updatedPhonemes.phonemes.find((p) => p.phoneme === phonemeSymbol);
    if (!addedPhonemeEntry) throw new Error('Added phoneme not found');
    const addedPhonemeId = addedPhonemeEntry.id;

    // Increase frequency
    await browserFetchJSON(
      client,
      `fetch('/api/admin/update-phoneme-frequency', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: ${addedPhonemeId}, increment: 1 })
      }).then(r => r.json())`
    );
    summary.steps.push({ action: 'update_frequency', increment: 1, status: 'ok' });

    // Create a word using this phoneme
    const nucleusPhoneme = onsetFallback?.phoneme ?? 'a';
    const nucleusLength = onsetFallback?.length_type ?? 'monophthongs';
    const codaPhoneme = codaFallback?.phoneme ?? 't';
    const codaLength = codaFallback?.length_type ?? 'single_consonants';
    const syllableBundle = [{
      syllableType: 'CVC',
      phonemes: {
        onset: { phoneme: phonemeSymbol, length_type: customLengthType },
        nucleus: { phoneme: nucleusPhoneme, length_type: nucleusLength },
        coda: { phoneme: codaPhoneme, length_type: codaLength },
      },
    }];

    const wordPayload = {
      language: 'Automation Tongue',
      english_words: JSON.stringify(['automation']),
      new_language_word: `auto${timestamp}`,
      syllable_type: 'CVC',
      onset_phoneme: phonemeSymbol,
      onset_length_type: customLengthType,
      nucleus_phoneme: nucleusPhoneme,
      nucleus_length_type: nucleusLength,
      coda_phoneme: codaPhoneme,
      coda_length_type: codaLength,
      syllables: JSON.stringify(syllableBundle),
    };
    const createWordResp = coerceJSON(await browserFetchJSON(
      client,
      `fetch('/api/create-word', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(${JSON.stringify(wordPayload)})
      }).then(r => r.json())`
    ));
    if (!createWordResp?.success) {
      console.error('createWordResp typeof', typeof createWordResp);
      console.error('createWordResp value', createWordResp);
      throw new Error(`Failed to create word: ${JSON.stringify(createWordResp)}`);
    }
    summary.steps.push({ action: 'create_word', status: 'ok' });

    // Lookup the word to get ID
    const lookupResult = coerceJSON(await browserFetchJSON(
      client,
      `fetch('/api/lookup-word?type=new_language&term=${encodeURIComponent(wordPayload.new_language_word)}').then(r => r.json())`
    ));
    const resultList = lookupResult?.results || lookupResult?.words || [];
    const wordId = resultList?.[0]?.id;
    if (!wordId) throw new Error('Unable to determine created word ID');

    // Fetch usage stats
    const usageData = coerceJSON(await browserFetchJSON(
      client,
      `fetch('/api/admin/phoneme-usage/${addedPhonemeId}').then(r => r.json())`
    ));
    summary.steps.push({ action: 'usage_snapshot', words: usageData?.words?.length ?? 0, status: 'ok' });

    // Attempt delete while in use (should fail) using UI controls
    await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const matchRow = Array.from(document.querySelectorAll('#phonemesTableBody tr'))
            .find((row) => row.querySelector('.phoneme-cell')?.textContent.trim() === ${JSON.stringify(phonemeSymbol)});
          if (!matchRow) {
            return { clicked: false, reason: 'row-not-found' };
          }
          const deleteBtn = matchRow.querySelector('.delete-button');
          if (!deleteBtn) {
            return { clicked: false, reason: 'delete-btn-missing' };
          }
          deleteBtn.click();
          return { clicked: true };
        }`,
      },
      'Open delete modal for in-use phoneme'
    );

    await waitForCondition(
      client,
      callTool,
      "() => !!document.querySelector('.modal-overlay .button.button-danger')",
      3000,
      200,
      'Wait for delete confirmation modal'
    );

    await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const modal = document.querySelector('.modal-overlay');
          const confirmBtn = modal?.querySelector('.button.button-danger');
          confirmBtn?.click();
          return !!confirmBtn;
        }`,
      },
      'Confirm delete attempt while phoneme in use'
    );

    const conflictModalVisible = await waitForCondition(
      client,
      callTool,
      "() => !!document.querySelector('.modal-overlay .large-modal')",
      3000,
      200,
      'Wait for conflict modal'
    );

    summary.steps.push({
      action: 'delete_in_use_attempt',
      conflict_dialog: conflictModalVisible,
      status: conflictModalVisible ? 'blocked' : 'unknown',
    });

    // Close any open modals to proceed
    await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          document.querySelectorAll('.modal-overlay .modal-close')
            .forEach((btn) => btn.dispatchEvent(new Event('click', { bubbles: true })));
          return true;
        }`,
      },
      'Dismiss phoneme conflict modal'
    );

    // Delete the word to free phoneme
    await browserFetchJSON(client, `fetch('/api/delete-word/${wordId}', {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' }
    }).then(r => r.json())`);

    // Delete phoneme now unused via UI
    await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const matchRow = Array.from(document.querySelectorAll('#phonemesTableBody tr'))
            .find((row) => row.querySelector('.phoneme-cell')?.textContent.trim() === ${JSON.stringify(phonemeSymbol)});
          if (!matchRow) {
            return { clicked: false, reason: 'row-not-found' };
          }
          const deleteBtn = matchRow.querySelector('.delete-button');
          if (!deleteBtn) {
            return { clicked: false, reason: 'delete-btn-missing' };
          }
          deleteBtn.click();
          return { clicked: true };
        }`,
      },
      'Open delete modal after freeing phoneme'
    );

    await waitForCondition(
      client,
      callTool,
      "() => !!document.querySelector('.modal-overlay .button.button-danger')",
      3000,
      200,
      'Wait for delete confirmation modal (unused phoneme)'
    );

    await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const modal = document.querySelector('.modal-overlay');
          const confirmBtn = modal?.querySelector('.button.button-danger');
          confirmBtn?.click();
          return !!confirmBtn;
        }`,
      },
      'Confirm delete for unused phoneme'
    );

    const rowRemoved = await waitForCondition(
      client,
      callTool,
      `() => !Array.from(document.querySelectorAll('#phonemesTableBody .phoneme-cell'))
        .some((cell) => cell.textContent.trim() === ${JSON.stringify(phonemeSymbol)})`,
      5000,
      250,
      'Wait for phoneme row removal'
    );
    if (!rowRemoved) {
      throw new Error('Phoneme row still present after delete confirmation');
    }
    summary.steps.push({ action: 'delete_phoneme', method: 'ui_controls', status: 'ok' });

    // Add bulk phonemes for zero-frequency deletion
    for (const symbol of bulkPhonemeSymbols) {
      await browserFetchJSON(
        client,
        `fetch('/api/admin/add-phoneme', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            syllable_type: 'CVC',
            position: 'coda',
            length_type: 'single_consonants',
            group_type: 'Automation',
            subgroup_type: 'Bulk',
            phoneme: '${symbol}',
            frequency: 1
          })
        }).then(r => r.json())`
      );
    }

    const bulkDelete = coerceJSON(await browserFetchJSON(client, "fetch('/api/admin/delete-unused-phonemes', { method: 'POST' }).then(r => r.json())"));
    summary.steps.push({ action: 'bulk_delete_unused', deleted: bulkDelete?.deleted_count ?? null, status: bulkDelete?.success ? 'ok' : 'failed' });

    // Seed dedicated phonemes to ensure template export always contains data
    for (const [index, symbol] of templateSeedSymbols.entries()) {
      await browserFetchJSON(
        client,
        `fetch('/api/admin/add-phoneme', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            syllable_type: 'CVC',
            position: index % 2 === 0 ? 'onset' : 'coda',
            length_type: 'single_consonants',
            group_type: 'Automation',
            subgroup_type: 'TemplateSeed',
            phoneme: '${symbol}',
            frequency: 1
          })
        }).then(r => r.json())`
      );
    }
    summary.steps.push({ action: 'seed_template_phonemes', symbols: templateSeedSymbols });

    // Export current phonemes as template
    const exportResult = coerceJSON(await browserFetchJSON(
      client,
      `fetch('/api/admin/export-template', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: '${templateName}', description: '${templateDescription}' })
      }).then(r => r.json())`
    ));
    if (!exportResult?.success) throw new Error(`Template export failed: ${JSON.stringify(exportResult)}`);
    summary.steps.push({ action: 'export_template', status: 'ok' });

    // Capture template list to find exported template ID
    if (useRealisticNavigation) {
      await clickElement(client, callTool, 'a[href="/admin/templates"]', 'Admin templates link', 'Open admin templates');
      const templatesReady = await waitForElement(client, callTool, '.template-card, .admin-template-card', 5000);
      if (!templatesReady) {
        await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` }, 'Fallback navigate to admin templates');
        const fallbackReady = await waitForElement(client, callTool, '.template-card, .admin-template-card', 5000);
        if (!fallbackReady) {
          throw new Error('Admin templates did not render');
        }
      }
    } else {
      await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` });
      const directReady = await waitForElement(client, callTool, '.template-card, .admin-template-card', 5000);
      if (!directReady) {
        throw new Error('Admin templates did not render');
      }
    }
    const templatesLocationConfirmed = await waitForCondition(
      client,
      callTool,
      "() => window.location.pathname === '/admin/templates'",
      5000,
      250,
      'Confirm admin templates location'
    );
    if (!templatesLocationConfirmed) {
      throw new Error('Failed to navigate to admin templates page');
    }
    await callTool(client, 'browser_snapshot', {});

    // Wait for the template to appear in the list with retries
    let templateEntries = [];
    let exportedTemplate = null;
    for (let attempt = 1; attempt <= 5; attempt++) {
        templateEntries = coerceJSON(await browserFetchJSON(
          client,
          `(() => {
            const cards = Array.from(document.querySelectorAll('.template-card'));
            return cards.map(card => {
              const name = card.querySelector('h4')?.textContent?.trim();
              const applyFunc = card.querySelector('button')?.getAttribute('onclick') || '';
              const match = applyFunc.match(/applyTemplate\((\d+)\)/);
              return { name, id: match ? Number(match[1]) : null };
            });
          })()`
        ));
        exportedTemplate = templateEntries?.find((tpl) => tpl.name === templateName);
        if (exportedTemplate?.id) break;
        await callTool(client, 'browser_wait_for', { time: 1 }, `Waiting for exported template (${attempt}/5)`);
        // Optional: reload if taking too long? Better to just wait for JS to render if it's dynamic, 
        // or reload if it's a static list. The previous step was a navigation or reload.
        if (attempt > 2) {
             await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` }, 'Retry reload admin templates');
             await waitForElement(client, callTool, '.template-card, .admin-template-card', 5000);
        }
    }

    if (!exportedTemplate?.id) {
      console.error('[phoneme-admin] template entries (export)', templateEntries);
      throw new Error('Exported template ID not found after retries');
    }

    // Download template JSON
    const templatePayload = await browserFetchJSON(
      client,
      `(async () => {
        const resp = await fetch('/api/admin/download-template/${exportedTemplate.id}');
        const text = await resp.text();
        return text;
      })()`
    );
    const templateJson = typeof templatePayload === 'string' ? templatePayload : JSON.stringify(templatePayload, null, 2);
    const templateFilePath = path.join(artifactsDir, `${templateName}.json`);
    await fs.writeFile(templateFilePath, templateJson, 'utf8');
    summary.steps.push({ action: 'download_template', file: templateFilePath, status: 'ok' });

    // Delete template
    await browserFetchJSON(client, `fetch('/api/templates/${exportedTemplate.id}', { method: 'DELETE' }).then(r => r.json())`);
    summary.steps.push({ action: 'delete_template', id: exportedTemplate.id, status: 'ok' });

    // Import template (modify name to avoid collision)
    const modifiedTemplate = JSON.parse(templateJson);
    modifiedTemplate.name = importTemplateName;
    const importResult = coerceJSON(await browserFetchJSON(
      client,
      `fetch('/api/templates', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(${JSON.stringify(modifiedTemplate)})
      }).then(r => r.json())`
    ));
    if (!importResult?.success) throw new Error(`Import template failed: ${JSON.stringify(importResult)}`);
    summary.steps.push({ action: 'import_template', status: 'ok' });

    // Force a full page reload to ensure template list updates from database
    await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` }, 'Reload admin templates to show imported template');
    const templatesReloaded = await waitForElement(client, callTool, '.template-card, .admin-template-card', 5000);
    if (!templatesReloaded) {
      throw new Error('Admin templates failed to reload after import');
    }
    const importedTemplatesLocationConfirmed = await waitForCondition(
      client,
      callTool,
      "() => window.location.pathname === '/admin/templates'",
      5000,
      250,
      'Confirm admin templates location after import'
    );
    if (!importedTemplatesLocationConfirmed) {
      throw new Error('Failed to remain on admin templates after import');
    }

    // Wait for template cards to fully render with newly imported template
    await callTool(client, 'browser_wait_for', { time: 5 }, 'Wait for imported template to appear in DOM');

    const importedTemplates = coerceJSON(await browserFetchJSON(
      client,
      `(() => {
        const cards = Array.from(document.querySelectorAll('.template-card'));
        return cards.map(card => {
          const name = card.querySelector('h4')?.textContent?.trim();
          const applyFunc = card.querySelector('button')?.getAttribute('onclick') || '';
          const match = applyFunc.match(/applyTemplate\((\d+)\)/);
          return { name, id: match ? Number(match[1]) : null };
        });
      })()`
    ));
    const importedTemplate = importedTemplates?.find((tpl) => tpl.name === importTemplateName);
    if (!importedTemplate?.id) {
      console.error('[phoneme-admin] template entries (import)', importedTemplates);
      throw new Error('Imported template ID not found');
    }

    // Apply imported template
    const applyResult = coerceJSON(await browserFetchJSON(
      client,
      `fetch('/api/templates/${importedTemplate.id}/apply', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
      }).then(r => r.json())`
    ));
    if (!applyResult?.success) throw new Error(`Apply template failed: ${JSON.stringify(applyResult)}`);
    summary.steps.push({ action: 'apply_template', templateId: importedTemplate.id, status: 'ok' });

    // Verify phoneme list still populated
    const finalPhonemes = coerceJSON(await browserFetchJSON(client, "fetch('/api/admin/phonemes').then(r => r.json())"));
    summary.steps.push({ action: 'final_phoneme_count', count: finalPhonemes?.phonemes?.length ?? 0 });

    // Delete imported template
    await browserFetchJSON(client, `fetch('/api/templates/${importedTemplate.id}', { method: 'DELETE' }).then(r => r.json())`);
    summary.steps.push({ action: 'delete_imported_template', status: 'ok' });

    // Attempt reset to default (best effort)
    const resetResult = coerceJSON(await browserFetchJSON(client, `(async () => {
      try {
        const resp = await fetch('/api/admin/reset-to-default', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{}' });
        if (resp.ok) return await resp.json();
        return { success: false, error: 'endpoint_not_available', status: resp.status };
      } catch (err) {
        return { success: false, error: String(err) };
      }
    })()`));
    summary.steps.push({ action: 'reset_to_default_attempt', result: resetResult });

    await callTool(client, 'browser_close', {});
    await client.close();

    console.log(JSON.stringify(summary, null, 2));
  } catch (error) {
    summary.error = String(error);
    console.error('[mcp-phoneme-admin] failed', error);
    await callTool(client, 'browser_close', {});
    await client.close();
    console.log(JSON.stringify(summary, null, 2));
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('[mcp-phoneme-admin] unhandled failure', err);
  process.exit(1);
});

/**
 * Navigation Helpers for Realistic UI Testing
 *
 * Provides utilities for navigating through the app using UI elements
 * instead of direct URL navigation, simulating real user behavior.
 */

/**
 * Click a link or button by finding it in the DOM
 * Includes optional navigation wait for elements that cause page transitions
 */
export async function clickElement(client, callTool, selector, description, label, waitForNav = false) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const el = document.querySelector('${selector}');
        if (el) {
          const payload = { clicked: true, text: el.textContent?.trim() || '', href: el.href || '' };
          window.setTimeout(() => el.click(), 0);
          return payload;
        }
        return { clicked: false, error: 'element-not-found' };
      }`
    },
    label || `Click: ${description}`
  );

  // If element causes navigation, wait for page transition to complete
  if (waitForNav) {
    await new Promise(resolve => setTimeout(resolve, 1500));
  }

  return result;
}

/**
 * Click a button containing specific text
 * Includes navigation wait for buttons that cause page transitions
 */
export async function clickButtonWithText(client, callTool, text, label, waitForNav = false) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const buttons = Array.from(document.querySelectorAll('button, a, [role="button"]'));
        const button = buttons.find(b => b.textContent.includes('${text}'));
        if (button) {
          const payload = { clicked: true, text: button.textContent?.trim() };
          window.setTimeout(() => button.click(), 0);
          return payload;
        }
        return { clicked: false, error: 'button-not-found', available: buttons.map(b => b.textContent.trim()).slice(0, 5) };
      }`
    },
    label || `Click button: ${text}`
  );

  // If button causes navigation, wait for page transition to complete
  if (waitForNav) {
    await new Promise(resolve => setTimeout(resolve, 1500));
  }

  return result;
}

/**
 * Navigate using breadcrumb links
 */
export async function clickBreadcrumb(client, callTool, linkText, label) {
  return await clickElement(
    client,
    callTool,
`a[href], button`
    `Breadcrumb: ${linkText}`,
    label
  );
}

/**
 * Fill a form field and trigger input event
 */
export async function fillField(client, callTool, selector, value, label) {
  const safeSelector = JSON.stringify(selector);
  const safeValue = JSON.stringify(value);

  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const el = document.querySelector(${safeSelector});
        if (el) {
          el.value = ${safeValue};
          el.dispatchEvent(new Event('input', { bubbles: true }));
          el.dispatchEvent(new Event('change', { bubbles: true }));
          return { filled: true, value: el.value };
        }
        return { filled: false, error: 'field-not-found' };
      }`
    },
    label || `Fill ${selector}: ${value}`
  );
}

/**
 * Fill multiple form fields at once
 */
export async function fillForm(client, callTool, fields, label) {
  const safeEntries = JSON.stringify(
    Object.entries(fields).map(([selector, value]) => [selector, value])
  );

  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const entries = ${safeEntries};
        const setValue = (selector, value) => {
          const el = document.querySelector(selector);
          if (el) {
            el.value = value;
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
          }
        };
        entries.forEach(([selector, value]) => setValue(selector, value));
        return { filled: true, count: ${Object.keys(fields).length} };
      }`
    },
    label || 'Fill form fields'
  );
}

/**
 * Submit a form by clicking its submit button
 * Automatically waits for navigation to complete
 */
export async function submitForm(client, callTool, buttonSelector, label) {
  await clickElement(
    client,
    callTool,
    buttonSelector,
    'Submit button',
    label || 'Submit form',
    true  // Always wait for navigation on form submission
  );
  
  // Additional wait for page to stabilize after navigation
  await new Promise(resolve => setTimeout(resolve, 1500));
  
  return true;
}

/**
 * Navigate from Dashboard to specific section
 */
export async function navigateFromDashboard(client, callTool, section) {
  const sectionMap = {
    'projects': { selector: 'a[href="/projects"]', label: 'Open My Projects' },
    'groups': { selector: 'a[href="/groups/create"]', label: 'Create New Group' },
    'create-project': { selector: 'a[href="/projects/create"].create-button, a.create-button[href="/projects/create"]', label: 'Create New Project' },
  };

  const config = sectionMap[section];
  if (!config) {
    throw new Error(`Unknown section: ${section}`);
  }

  return await clickElement(
    client,
    callTool,
    config.selector,
    config.label,
    `Navigate to ${section} from Dashboard`,
    true
  );
}

/**
 * Navigate using the main menu from project context
 */
export async function navigateFromProjectMenu(client, callTool, destination) {
  const destMap = {
    // Legacy alias: "flat" view is now the full hierarchy page.
    'phonemes-flat': { selector: 'a[href="/phonemes/full"]', label: 'Full Hierarchy' },
    'phonemes-nested': { selector: 'a[href="/phonemes/nested"]', label: 'Nested View' },
    'phonemes-full': { selector: 'a[href="/phonemes/full"]', label: 'Full Hierarchy' },
    'words-create': { selector: 'a[href="/words/create/table-based"]', label: 'Create New Word' },
    'words-add': { selector: 'a[href="/words/add"]', label: 'Quick Add Word' },
    'words-display': { selector: 'a[href="/words/display"]', label: 'View All Words' },
    'words-lookup': { selector: 'a[href="/words/lookup"]', label: 'Lookup Word' },
    'admin': { selector: 'a[href="/admin"]', label: 'Admin Panel' },
    'admin-phonemes': { selector: 'a[href="/admin/phonemes"]', label: 'Manage Phonemes' },
    'admin-templates': { selector: 'a[href="/admin/templates"]', label: 'Phoneme Templates' },
  };

  const config = destMap[destination];
  if (!config) {
    throw new Error(`Unknown destination: ${destination}`);
  }

  return await clickElement(
    client,
    callTool,
    config.selector,
    config.label,
    `Navigate to ${destination} from project menu`
  );
}

/**
 * Switch between tabs (like Sign In / Sign Up)
 */
export async function switchTab(client, callTool, tabIndex, label) {
  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const tabs = document.querySelectorAll('.tab-button');
        if (tabs[${tabIndex}]) {
          tabs[${tabIndex}].click();
          return { switched: true, text: tabs[${tabIndex}].textContent?.trim() };
        }
        return { switched: false, error: 'tab-not-found', available: tabs.length };
      }`
    },
    label || `Switch to tab ${tabIndex}`
  );
}

/**
 * Wait for an element to appear (useful after navigation)
 */
export async function waitForElement(client, callTool, selector, timeout = 5000) {
  const start = Date.now();
  while (Date.now() - start < timeout) {
    const result = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          return { exists: !!document.querySelector('${selector}') };
        }`
      }
    );

    // Parse result
    const rawText = result.content?.find((c) => c.type === 'text')?.text || '';
    const text = rawText.trim().toLowerCase();
    if (
      text === 'true' ||
      text === '"true"' ||
      text.includes('"exists":true') ||
      text.includes('exists: true') ||
      /(^|[^a-z])true([^a-z]|$)/.test(text)
    ) {
      return true;
    }

    await new Promise(resolve => setTimeout(resolve, 200));
  }
  return false;
}

/**
 * Extract text content from an element
 */
export async function getElementText(client, callTool, selector) {
  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const el = document.querySelector('${selector}');
        return el ? el.textContent?.trim() : null;
      }`
    },
    `Get text from ${selector}`
  );
}

/**
 * Check if an element exists
 */
export async function elementExists(client, callTool, selector) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        return !!document.querySelector('${selector}');
      }`
    },
    `Check if ${selector} exists`
  );

  const text = result.content?.find(c => c.type === 'text')?.text || '';
  return text.includes('true');
}

/**
 * Select a radio button or checkbox
 */
export async function selectOption(client, callTool, selector, label) {
  const safeSelector = JSON.stringify(selector);
  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const el = document.querySelector(${safeSelector});
        if (el) {
          el.checked = true;
          el.dispatchEvent(new Event('change', { bubbles: true }));
          return { selected: true, value: el.value };
        }
        return { selected: false, error: 'element-not-found' };
      }`
    },
    label || `Select ${selector}`
  );
}

/**
 * Poll until a condition returns true within the page context.
 */
export async function waitForCondition(client, callTool, conditionFnSource, timeout = 5000, interval = 200, label) {
  const start = Date.now();
  const functionSource = conditionFnSource.trim().startsWith('(')
    ? conditionFnSource
    : `() => { ${conditionFnSource} }`;

  while (Date.now() - start < timeout) {
    const result = await callTool(
      client,
      'browser_evaluate',
      {
        function: `${functionSource}`,
      },
      label
    );
    const rawText = result.content?.find((part) => part.type === 'text')?.text || '';
    const text = rawText.trim().toLowerCase();
    // Check for true using multiple patterns to handle various MCP response formats
    if (
      text === 'true' ||
      text === '"true"' ||
      text.includes('"exists":true') ||
      text.includes('exists: true') ||
      text.includes(':true') ||
      text.includes('"success":true') ||
      /(^|[^a-z])true([^a-z]|$)/.test(text)
    ) {
      return true;
    }
    await new Promise((resolve) => setTimeout(resolve, interval));
  }
  return false;
}

/**
 * Select an <option> within a <select> by matching its text content.
 */
export async function selectDropdownOption(client, callTool, selector, optionText, label) {
  const safeSelector = JSON.stringify(selector);
  const safeOption = JSON.stringify(optionText);

  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const selectEl = document.querySelector(${safeSelector});
        if (!selectEl) {
          return { selected: false, error: 'select-not-found' };
        }
        const options = Array.from(selectEl.options);
        const match = options.find((opt) => (opt.textContent || '').trim().includes(${safeOption}));
        if (match) {
          selectEl.value = match.value;
          selectEl.dispatchEvent(new Event('change', { bubbles: true }));
          return { selected: true, value: match.value, text: match.textContent?.trim() };
        }
        return { selected: false, error: 'option-not-found', available: options.map(opt => opt.textContent?.trim()).slice(0, 5) };
      }`
    },
    label || `Select option "${optionText}" in ${selector}`
  );
}

/**
 * Click an action button within a project card by project name.
 */
export async function clickProjectCardAction(client, callTool, projectName, actionText, label) {
  const safeProject = JSON.stringify(projectName);
  const safeAction = JSON.stringify(actionText);

  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const cards = Array.from(document.querySelectorAll('.project-card, .item-card'));
        const getTitle = (card) => (card.querySelector('.project-name')?.textContent || '').trim();

        const exactMatches = cards.filter((card) => getTitle(card) === ${safeProject});
        const fuzzyMatches = cards.filter((card) => (card.textContent || '').includes(${safeProject}));

        const candidates = exactMatches.length ? exactMatches : fuzzyMatches;
        for (const card of candidates) {
          const targets = Array.from(card.querySelectorAll('button, a'));
          const action = targets.find((el) => (el.textContent || '').includes(${safeAction}));
          if (action) {
            window.setTimeout(() => action.click(), 0);
            return { clicked: true, project: getTitle(card) || ${safeProject}, action: ${safeAction} };
          }
        }

        if (!candidates.length) {
          return { clicked: false, error: 'project-not-found', project: ${safeProject} };
        }
        return { clicked: false, error: 'action-not-found', project: ${safeProject}, candidates: candidates.map(getTitle).slice(0, 3) };
      }`
    },
    label || `Click "${actionText}" on project "${projectName}"`
  );
}

/**
 * Navigate to a specific project card and click Enter
 */
export async function enterProject(client, callTool, projectIndex = 0) {
  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const candidates = Array.from(document.querySelectorAll('a.action-button.enter, a, button'));
        const enterButtons = candidates.filter((el) => {
          const text = (el.textContent || '').trim();
          return text.includes('Enter') || text.includes('🎯') || text.includes('Open') || text.includes('🚀');
        });
        const target = enterButtons[${projectIndex}];
        if (target) {
          const payload = { clicked: true, href: target.href || null };
          window.setTimeout(() => target.click(), 0);
          return payload;
        }
        return { clicked: false, available: enterButtons.length };
      }`
    },
    `Enter project #${projectIndex + 1}`
  );
}

/**
 * Enter a project by matching its name.
 */
export async function enterProjectByName(client, callTool, projectName, label) {
  const safeProject = JSON.stringify(projectName);
  return await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const cards = Array.from(document.querySelectorAll('.project-card, .item-card'));
        const getTitle = (card) => (card.querySelector('.project-name')?.textContent || '').trim();
        const isEnterLink = (el) => {
          const text = (el.textContent || '').trim();
          const href = (el.getAttribute && el.getAttribute('href')) || '';
          return (
            text.includes('Enter') ||
            text.includes('🎯') ||
            text.includes('Open') ||
            text.includes('🚀') ||
            href.endsWith('/enter') ||
            href.includes('/enter')
          );
        };

        const exact = cards.find((card) => getTitle(card) === ${safeProject});
        const fuzzy = cards.find((card) => (card.textContent || '').includes(${safeProject}));
        const card = exact || fuzzy;
        if (!card) {
          return { clicked: false, error: 'project-not-found', project: ${safeProject} };
        }

        const enterTargets = Array.from(card.querySelectorAll('a, button')).filter(isEnterLink);
        const target = enterTargets[0];
        if (!target) {
          return { clicked: false, error: 'enter-not-found', project: getTitle(card) || ${safeProject} };
        }

        const payload = { clicked: true, href: target.href || null, project: getTitle(card) || ${safeProject} };
        window.setTimeout(() => target.click(), 0);
        return payload;
      }`
    },
    label || `Enter project "${projectName}"`
  );
}

/**
 * Submit a form button that causes navigation
 * Enhanced version with explicit navigation handling
 */
export async function submitFormWithNavigation(client, callTool, buttonText, label) {
  const result = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        const buttons = Array.from(document.querySelectorAll('button, input[type="submit"], a[role="button"]'));
        const button = buttons.find(b => b.textContent.includes('${buttonText}') || b.value?.includes('${buttonText}'));
        if (button) {
          button.click();
          return { submitted: true, text: button.textContent?.trim() || button.value };
        }
        return { submitted: false, error: 'button-not-found' };
      }`
    },
    label || `Submit form: ${buttonText}`
  );
  
  // Wait for navigation to complete
  await new Promise(resolve => setTimeout(resolve, 2500));
  
  return result;
}

export default {
  clickElement,
  clickButtonWithText,
  clickBreadcrumb,
  fillField,
  fillForm,
  submitForm,
  submitFormWithNavigation,
  navigateFromDashboard,
  navigateFromProjectMenu,
  switchTab,
  waitForElement,
  waitForCondition,
  getElementText,
  elementExists,
  selectOption,
  selectDropdownOption,
  enterProject,
  clickProjectCardAction,
  enterProjectByName,
};

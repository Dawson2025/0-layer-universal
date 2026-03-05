// resource_id: "c1f612b6-5c38-4af0-800b-1026cfdd670a"
// resource_type: "document"
// resource_name: "google-auth-helpers"
/**
 * Google OAuth helper utilities for MCP browser automation scripts.
 *
 * Provides a reusable flow to authenticate against Google's OAuth pages
 * using Playwright-driven browser tools exposed through the MCP harness.
 */

export function normalizeCliJson(raw) {
  if (!raw) return null;
  let text = raw.trim();
  text = text.replace(/^### Result\s*/i, '').trim();

  if (text.startsWith('```')) {
    const closing = text.lastIndexOf('```');
    if (closing > 0) {
      text = text.substring(3, closing);
      // Remove optional language hint
      text = text.replace(/^[a-z0-9_-]+\s*/i, '').trim();
    }
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

  return parsed;
}

function extractJson(result) {
  const textPart = result.content?.find((part) => part.type === 'text');
  if (!textPart?.text) return null;
  return normalizeCliJson(textPart.text);
}

function extractText(result) {
  const parts = result.content ?? [];
  return parts.filter((part) => part.type === 'text').map((part) => part.text).join('\n');
}

function parseTabList(text) {
  const tabs = [];
  let currentIndex = 0;
  const lines = text.split('\n');
  for (const line of lines) {
    const match = line.match(/^- (\d+):\s*(?:\((current)\)\s*)?\[(.*?)\]\s*\((.*?)\)/);
    if (!match) continue;
    const index = Number(match[1]);
    const isCurrent = match[2] === 'current';
    const title = match[3] ?? '';
    const url = match[4] ?? '';
    tabs.push({ index, title, url, isCurrent });
    if (isCurrent) currentIndex = index;
  }
  return { tabs, currentIndex };
}

async function wait(ms) {
  await new Promise((resolve) => setTimeout(resolve, ms));
}

async function poll(condition, { interval = 500, timeout = 15000 } = {}) {
  const start = Date.now();
  while (Date.now() - start < timeout) {
    const value = await condition();
    if (value) return value;
    await wait(interval);
  }
  return null;
}

export async function ensureGoogleRedirect(client, callTool, { baseUrl }) {
  const baseOrigin = new URL(baseUrl).origin;

  const initialTabsResult = await callTool(
    client,
    'browser_tabs',
    { action: 'list' },
    'List tabs before Google Sign In'
  );
  const initialTabsText = extractText(initialTabsResult) ?? '';
  const initialTabInfo = parseTabList(initialTabsText);
  const originalTabIndex = initialTabInfo.currentIndex ?? 0;

  const locationState = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => ({ url: window.location.href, origin: window.location.origin })`
    },
    'Check current location'
  );

  const loc = extractJson(locationState) ?? {};
  if (loc.url?.includes('accounts.google')) {
    return { stage: 'google', method: 'existing', tabIndex: originalTabIndex, originalTabIndex };
  }
  if (loc.origin === baseOrigin && loc.url?.includes('/dashboard')) {
    return { stage: 'app', method: 'already-signed-in', originalTabIndex };
  }

  const startResult = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => {
        try {
          const firebase = window.firebase || globalThis.firebase;
          if (firebase?.auth) {
            const auth = firebase.auth();
            const provider = new firebase.auth.GoogleAuthProvider();
            auth.useDeviceLanguage?.();
            auth.signInWithRedirect(provider);
            return { started: true, method: 'redirect' };
          }
        } catch (err) {
          return { started: false, error: String(err) };
        }

        const button = document.querySelector('#google-signin-btn');
        if (button) {
          button.click();
          return { started: true, method: 'button' };
        }

        return { started: false, error: 'google-signin-button-missing' };
      }`
    },
    'Initiate Google Sign In'
  );

  const start = extractJson(startResult) ?? {};

  if (!start.started) {
    return { stage: 'error', error: start.error ?? 'unknown-init-error', originalTabIndex };
  }

  let googleTabIndex = null;
  const googleLoc = await poll(async () => {
    const tabsResult = await callTool(
      client,
      'browser_tabs',
      { action: 'list' }
    );
    const tabsText = extractText(tabsResult) ?? '';
    const tabInfo = parseTabList(tabsText);
    const currentIndex = tabInfo.currentIndex ?? originalTabIndex;
    const googleTab = tabInfo.tabs.find((tab) => (tab.url || '').toLowerCase().includes('accounts.google'));

    if (googleTab) {
      googleTabIndex = googleTab.index;
      if (!googleTab.isCurrent) {
        await callTool(
          client,
          'browser_tabs',
          { action: 'select', index: googleTab.index },
          'Switch to Google OAuth tab'
        );
        await wait(300);
        return null;
      }
    }

    const locResult = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => ({ url: window.location.href, origin: window.location.origin })`
      }
    );
    const data = extractJson(locResult) ?? {};
    if (data.url?.includes('accounts.google')) {
      return {
        stage: 'google',
        method: start.method ?? (googleTab ? 'button' : 'redirect'),
        tabIndex: googleTabIndex ?? currentIndex,
        originalTabIndex,
      };
    }

    // If we are already back at the app origin and firebase redirected quickly.
    if (data.origin === baseOrigin && data.url?.includes('/__')) {
      return {
        stage: 'google',
        method: start.method ?? 'redirect',
        tabIndex: currentIndex,
        originalTabIndex,
      };
    }

    return null;
  }, { interval: 500, timeout: 20000 });

  return googleLoc ?? { stage: 'timeout', originalTabIndex };
}

async function fillGoogleEmail(client, callTool, email) {
  const emailStage = await poll(async () => {
    const result = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const accountChips = Array.from(document.querySelectorAll('div[data-identifier]'));
          const account = accountChips.find(el => el.getAttribute('data-identifier') === ${JSON.stringify(email)});
          if (!document.querySelector('input[type="email"], input[id="identifierId"], input[name="identifier"]') && account) {
            account.click();
            return { stage: 'account-chosen' };
          }

          const emailInput = document.querySelector('input[type="email"], input[id="identifierId"], input[name="identifier"]');
          const passwordInput = document.querySelector('input[type="password"], input[name="password"], input[name="Passwd"]');

          if (!emailInput && passwordInput) {
            return { stage: 'password' };
          }

          if (!emailInput) {
            return null;
          }

          emailInput.focus();
          emailInput.value = ${JSON.stringify(email)};
          emailInput.dispatchEvent(new Event('input', { bubbles: true }));
          emailInput.dispatchEvent(new Event('change', { bubbles: true }));

          const nextButton = document.querySelector('#identifierNext button, #identifierNext');
          if (nextButton) {
            nextButton.removeAttribute('disabled');
            nextButton.click();
          }

          return { stage: 'email-submitted' };
        }`
      },
      'Fill Google email'
    );

    const data = extractJson(result);
    if (!data) return null;
    if (data.stage === 'account-chosen') return data;
    if (data.stage === 'email-submitted') return data;
    if (data.stage === 'password') return data;
    return null;
  }, { interval: 500, timeout: 15000 });

  if (!emailStage) {
    throw new Error('Google email field not available or timed out');
  }

  return emailStage.stage;
}

async function fillGooglePassword(client, callTool, password) {
  const passwordStage = await poll(async () => {
    const result = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const passwordInput = document.querySelector('input[type=\"password\"], input[name=\"password\"], input[name=\"Passwd\"]');
          const host = window.location.hostname || '';

          if (!passwordInput) {
            if (!host.includes('google.')) {
              return { stage: 'password-not-required' };
            }
            return null;
          }

          passwordInput.focus();
          passwordInput.value = ${JSON.stringify(password)};
          passwordInput.dispatchEvent(new Event('input', { bubbles: true }));
          passwordInput.dispatchEvent(new Event('change', { bubbles: true }));

          const nextButton = document.querySelector('#passwordNext button, #passwordNext');
          if (nextButton) {
            nextButton.removeAttribute('disabled');
            nextButton.click();
          }

          return { stage: 'password-submitted' };
        }`
      },
      'Fill Google password'
    );

    const data = extractJson(result);
    if (!data) return null;
    if (data.stage === 'password-not-required') return data;
    if (data.stage === 'password-submitted') return data;
    return null;
  }, { interval: 500, timeout: 15000 });

  if (!passwordStage) {
    throw new Error('Google password field not available or timed out');
  }

  return passwordStage.stage;
}

async function handlePostLoginScreens(client, callTool) {
  await poll(async () => {
    const result = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const allowButton = document.querySelector('[id="submit_approve_access"]');
          if (allowButton) {
            allowButton.click();
            return { handled: true, action: 'approve-access' };
          }

          const confirmButton = document.querySelector('button[jsname][data-mdc-dialog-action="accept"], button#confirm');
          if (confirmButton) {
            confirmButton.click();
            return { handled: true, action: 'confirm-dialog' };
          }

          return { handled: false };
        }`
      },
      'Handle additional Google prompts'
    );

    const data = extractJson(result);
    return data?.handled ? data : null;
  }, { interval: 500, timeout: 10000 });
}

async function switchToTab(client, callTool, index, label = 'Switch tab') {
  await callTool(
    client,
    'browser_tabs',
    { action: 'select', index },
    label
  );
  await wait(300);
}

async function waitForPopupClose(client, callTool, index) {
  if (index === null || index === undefined) return true;
  const closed = await poll(async () => {
    const tabsResult = await callTool(
      client,
      'browser_tabs',
      { action: 'list' }
    );
    const tabsText = extractText(tabsResult) ?? '';
    const tabInfo = parseTabList(tabsText);
    const exists = tabInfo.tabs.some((tab) => tab.index === index);
    return exists ? null : true;
  }, { interval: 500, timeout: 20000 });

  return !!closed;
}

async function waitForAppReturn(client, callTool, { baseUrl }) {
  const baseOrigin = new URL(baseUrl).origin;

  const returnState = await poll(async () => {
    const result = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => ({
          url: window.location.href,
          origin: window.location.origin,
          pathname: window.location.pathname
        })`
      }
    );

    const data = extractJson(result);
    if (data?.origin === baseOrigin) {
      return data;
    }
    return null;
  }, { interval: 500, timeout: 30000 });

  if (!returnState) {
    throw new Error('Timed out waiting for redirect back to application');
  }

  return returnState;
}

async function waitForFirebaseUser(client, callTool, email) {
  const authState = await poll(async () => {
    const result = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => {
          const firebase = window.firebase || globalThis.firebase;
          if (!firebase?.auth) {
            const logoutLink = document.querySelector('.logout-link, a[href="/logout"]');
            const signOutText = Array.from(document.querySelectorAll('a, button')).some(el => (el.textContent || '').includes('Sign Out'));
            if (logoutLink || signOutText) {
              return { ready: true, email: null, source: 'ui' };
            }
            return { ready: false };
          }
          const user = firebase.auth().currentUser;
          if (user) {
            return { ready: true, email: user.email, uid: user.uid, source: 'firebase' };
          }
          return { ready: false };
        }`
      }
    );

    const data = extractJson(result);
    if (data?.ready) return data;
    return null;
  }, { interval: 500, timeout: 15000 });

  if (!authState) {
    throw new Error('Firebase auth state did not resolve after Google login');
  }

  if (email && authState.email && authState.email.toLowerCase() !== email.toLowerCase()) {
    throw new Error(`Unexpected Google account: ${authState.email}`);
  }

  if (!authState.email && email) {
    authState.email = email;
  }

  return authState;
}

/**
 * Perform the full Google OAuth login flow, returning when the application
 * has redirected back and Firebase authentication is established.
 */
export async function performGoogleOAuthLogin(client, callTool, {
  email,
  password,
  baseUrl,
} = {}) {
  if (!email || !password) {
    throw new Error('Google email and password must be provided');
  }
  if (!baseUrl) {
    throw new Error('Application baseUrl is required for Google OAuth login');
  }

  const redirectState = await ensureGoogleRedirect(client, callTool, { baseUrl });
  if (redirectState.stage === 'error') {
    throw new Error(`Failed to initiate Google Sign In: ${redirectState.error}`);
  }
  if (redirectState.stage === 'timeout') {
    throw new Error('Timed out waiting for Google OAuth redirect');
  }
  if (redirectState.stage === 'app' && redirectState.method === 'already-signed-in') {
    const firebaseState = await waitForFirebaseUser(client, callTool, email);
    return {
      status: 'already-signed-in',
      firebase: firebaseState,
      finalUrl: `${baseUrl}/dashboard`,
      flow: 'existing-session',
    };
  }

  if (redirectState.tabIndex !== undefined && redirectState.tabIndex !== null) {
    await switchToTab(client, callTool, redirectState.tabIndex, 'Focus Google OAuth tab');
  }

  await fillGoogleEmail(client, callTool, email);
  await wait(750);

  await fillGooglePassword(client, callTool, password);
  await wait(750);

  await handlePostLoginScreens(client, callTool);

  const loginFlow = redirectState.method === 'button' ? 'popup' : 'redirect';

  if (loginFlow === 'popup') {
    await waitForPopupClose(client, callTool, redirectState.tabIndex);
    if (redirectState.originalTabIndex !== undefined && redirectState.originalTabIndex !== null) {
      await switchToTab(client, callTool, redirectState.originalTabIndex, 'Return to main tab after Google OAuth');
    }

    const firebaseState = await waitForFirebaseUser(client, callTool, email);

    const pageStateResult = await callTool(
      client,
      'browser_evaluate',
      {
        function: `() => ({
          url: window.location.href,
          origin: window.location.origin,
          pathname: window.location.pathname
        })`
      },
      'Check app state after Google popup login'
    );

    const pageState = extractJson(pageStateResult) ?? {};

    return {
      status: 'signed-in',
      finalUrl: pageState.url ?? `${baseUrl}/dashboard`,
      firebase: firebaseState,
      flow: 'popup',
    };
  }

  const returnState = await waitForAppReturn(client, callTool, { baseUrl });
  const firebaseState = await waitForFirebaseUser(client, callTool, email);

  return {
    status: 'signed-in',
    finalUrl: returnState.url,
    firebase: firebaseState,
    flow: 'redirect',
  };
}

export async function getFirebaseAuthContext(client, callTool) {
  const contextResult = await callTool(
    client,
    'browser_evaluate',
    {
      function: `() => (async () => {
        const fallbackConfigs = {
          "lang-trak-dev": {
            apiKey: "AIzaSyCXoBKM6UQx5wCvBYQ_KvhCPmjcNyis9XE",
            authDomain: "lang-trak-dev.firebaseapp.com",
            projectId: "lang-trak-dev",
            storageBucket: "lang-trak-dev.firebasestorage.app",
            messagingSenderId: "894561101654",
            appId: "1:894561101654:web:fc234c159fd669749d98f7"
          },
          "lang-trak-prod": {
            apiKey: "AIzaSyCxFhAeOmRD050V-GgZQ56HWvM_TW6pRf0",
            authDomain: "lang-trak-prod.firebaseapp.com",
            projectId: "lang-trak-prod",
            storageBucket: "lang-trak-prod.firebasestorage.app",
            messagingSenderId: "730887785875",
            appId: "1:730887785875:web:564d7accd1d4e9e41b2c66",
            measurementId: "G-87P3T0B3V7"
          }
        };

        let config = window.FIREBASE_CONFIG || {};
        const inferredProject =
          config.projectId ||
          window.__mcpFirebaseProjectId ||
          (window.location.hostname.includes('prod') ? 'lang-trak-prod' : 'lang-trak-dev');
        const fallbackProjectId = inferredProject || 'lang-trak-dev';

        if (!config.apiKey) {
          config = Object.assign({}, fallbackConfigs[fallbackProjectId] || fallbackConfigs['lang-trak-dev']);
        }

        const ensureApp = async () => {
          if (window.firebaseAuth?.getCurrentUser) {
            const user = await window.firebaseAuth.getCurrentUser();
            if (user) {
              return {
                auth: {
                  currentUser: user,
                  projectId:
                    window.FIREBASE_CONFIG?.projectId ||
                    (window.firebase?.app?.()?.options?.projectId) ||
                    fallbackProjectId,
                },
              };
            }
          }

          if (window.__mcpFirebaseAuth?.currentUser) {
            return {
              auth: window.__mcpFirebaseAuth,
              projectId: window.__mcpFirebaseProjectId || fallbackProjectId,
            };
          }

          try {
            const [{ initializeApp, getApps, getApp }, authModule] = await Promise.all([
              import('https://www.gstatic.com/firebasejs/10.0.0/firebase-app.js'),
              import('https://www.gstatic.com/firebasejs/10.0.0/firebase-auth.js'),
            ]);

            const apps = getApps ? getApps() : [];
            const app = apps.length ? (getApp ? getApp() : apps[0]) : initializeApp(config);

            const getAuth = authModule.getAuth || authModule.default || (() => null);
            const authInstance = getAuth(app);

            window.__mcpFirebaseApp = app;
            window.__mcpFirebaseAuth = authInstance;
            window.__mcpFirebaseProjectId =
              window.FIREBASE_CONFIG?.projectId ||
              app?.options?.projectId ||
              fallbackProjectId;

            return { auth: authInstance, projectId: window.__mcpFirebaseProjectId };
          } catch (err) {
            return { error: 'import-failed', message: err?.message || String(err) };
          }
        };

        const ensured = await ensureApp();
        if (ensured.error) {
          return { loggedIn: false, error: ensured.error, message: ensured.message };
        }

        const auth = ensured.auth;
        const projectId = ensured.projectId || fallbackProjectId;
        if (!auth) {
          return { loggedIn: false, error: 'auth-not-initialised' };
        }

        const awaitUser = () =>
          new Promise((resolve) => {
            const current = auth.currentUser;
            if (current) {
              resolve(current);
              return;
            }
            const unsubscribe = auth.onAuthStateChanged(
              (user) => {
                unsubscribe?.();
                resolve(user);
              },
              () => {
                unsubscribe?.();
                resolve(null);
              },
            );
            setTimeout(() => {
              unsubscribe?.();
              resolve(null);
            }, 5000);
          });

        const user = auth.currentUser || await awaitUser();
        if (!user) {
          return { loggedIn: false, error: 'no-user' };
        }

        const idToken = await user.getIdToken(true);
        const providerData = (user.providerData || []).map((provider) => ({
          providerId: provider?.providerId || null,
          uid: provider?.uid || null,
          email: provider?.email || null,
        }));

        return {
          loggedIn: true,
          uid: user.uid,
          email: user.email,
          displayName: user.displayName,
          idToken,
          projectId,
          providerData,
          apiKey: config.apiKey || null,
        };
      })()`,
    },
    'Fetch Firebase auth context'
  );

  const context = extractJson(contextResult) ?? {};
  if (!context.loggedIn) {
    throw new Error(
      `Firebase auth context unavailable: ${context.error || 'unknown-reason'}`
    );
  }

  if (!context.projectId) {
    throw new Error('Firebase projectId unavailable in client context');
  }

  return context;
}

function encodeFirestoreValue(value) {
  if (value === null || value === undefined) return { nullValue: null };
  if (typeof value === 'boolean') return { booleanValue: value };
  if (typeof value === 'number') {
    if (Number.isInteger(value)) return { integerValue: value.toString() };
    return { doubleValue: value };
  }
  if (value instanceof Date) return { timestampValue: value.toISOString() };
  if (Array.isArray(value)) {
    return {
      arrayValue: {
        values: value.map((item) => encodeFirestoreValue(item)),
      },
    };
  }
  if (typeof value === 'object') {
    return {
      mapValue: {
        fields: Object.fromEntries(
          Object.entries(value).map(([key, val]) => [key, encodeFirestoreValue(val)])
        ),
      },
    };
  }
  return { stringValue: String(value) };
}

function decodeFirestoreValue(value) {
  if (value === undefined || value === null) return undefined;
  if ('stringValue' in value) return value.stringValue;
  if ('booleanValue' in value) return value.booleanValue;
  if ('integerValue' in value) return Number(value.integerValue);
  if ('doubleValue' in value) return value.doubleValue;
  if ('nullValue' in value) return null;
  if ('timestampValue' in value) return value.timestampValue;
  if ('bytesValue' in value) return value.bytesValue;
  if ('arrayValue' in value) {
    const vals = value.arrayValue?.values ?? [];
    return vals.map((item) => decodeFirestoreValue(item));
  }
  if ('mapValue' in value) {
    const fields = value.mapValue?.fields ?? {};
    return Object.fromEntries(
      Object.entries(fields).map(([key, val]) => [key, decodeFirestoreValue(val)])
    );
  }
  return undefined;
}

function decodeFirestoreDocument(doc) {
  if (!doc) return null;
  const fields = doc.fields ?? {};
  const data = Object.fromEntries(
    Object.entries(fields).map(([key, val]) => [key, decodeFirestoreValue(val)])
  );
  return {
    name: doc.name,
    createTime: doc.createTime,
    updateTime: doc.updateTime,
    fields: data,
  };
}

export async function firestoreGetDocument(authContext, path) {
  const baseUrl = `https://firestore.googleapis.com/v1/projects/${authContext.projectId}/databases/(default)/documents`;
  const apiKeyParam = authContext.apiKey ? `?key=${encodeURIComponent(authContext.apiKey)}` : '';
  const url = `${baseUrl}/${path}${apiKeyParam}`;

  const response = await fetch(url, {
    headers: {
      Authorization: `Bearer ${authContext.idToken}`,
    },
  });

  if (response.status === 404) {
    return null;
  }

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`Firestore getDocument failed (${response.status}): ${body}`);
  }

  const json = await response.json();
  return decodeFirestoreDocument(json);
}

export async function firestoreRunQuery(authContext, collectionId, filters = [], options = {}) {
  const apiKeyParam = authContext.apiKey ? `?key=${encodeURIComponent(authContext.apiKey)}` : '';
  const url = `https://firestore.googleapis.com/v1/projects/${authContext.projectId}/databases/(default)/documents:runQuery${apiKeyParam}`;

  const filterClauses = filters
    .filter((filter) => filter && filter.fieldPath && filter.value !== undefined)
    .map((filter) => ({
      fieldFilter: {
        field: { fieldPath: filter.fieldPath },
        op: filter.op ?? 'EQUAL',
        value: encodeFirestoreValue(filter.value),
      },
    }));

  let whereClause = undefined;
  if (filterClauses.length === 1) {
    whereClause = filterClauses[0];
  } else if (filterClauses.length > 1) {
    whereClause = {
      compositeFilter: {
        op: 'AND',
        filters: filterClauses,
      },
    };
  }

  const structuredQuery = {
    from: [{ collectionId }],
    limit: options.limit ?? 50,
  };

  if (whereClause) {
    structuredQuery.where = whereClause;
  }

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${authContext.idToken}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ structuredQuery }),
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`Firestore runQuery failed (${response.status}): ${body}`);
  }

  const json = await response.json();
  const documents = [];
  for (const entry of json) {
    if (entry.document) {
      documents.push(decodeFirestoreDocument(entry.document));
    }
  }
  return documents;
}

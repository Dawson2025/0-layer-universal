---
resource_id: "8a578163-e1ac-4a7a-bc05-60b3ca34d985"
resource_type: "document"
resource_name: "MCP_WORK_LOG"
---
# MCP Work Log — Playwright MCP server support

This document records the step-by-step work done to make the Playwright MCP server startable and testable locally, the scripts I added, experiments I ran, the results, and next steps.

Date range: ongoing (session captured on Oct 16, 2025)

<!-- section_id: "1b3dc75b-fe0d-476b-9b7e-41b7f6fbf45f" -->
## Goal

- Make the Playwright MCP server easy to run locally and provide smoke tests + end-to-end handshake tests in Node and Python.

<!-- section_id: "d374927c-1971-4b62-962f-c2abbd489b9e" -->
## What I changed (summary)

- Added and modified helper scripts:
  - `scripts/mcp-start.sh` — helper to start the Playwright MCP server using `npx @playwright/mcp` (now sets `PLAYWRIGHT_BROWSERS_PATH=0`, `PLAYWRIGHT_MCP_BROWSER=chromium`, and passes `--browser=chromium`).
  - `scripts/mcp-smoke-test.sh` (existing) — shell smoke tests (basic HTTP checks for /mcp endpoint).
  - `scripts/mcp-smoke-node.cjs` — Node.js smoke test that starts helper, polls port, GETs /mcp and validates response.
  - `scripts/mcp-smoke-py.py` — Python smoke test equivalent.

- Implemented diagnostic and handshake scripts:
  - `scripts/mcp-handshake-node.cjs` — diagnostic probe that starts the helper, requires `@playwright/mcp`, calls `createConnection(...)` and prints returned object keys (repaired after earlier corruption).
  - `scripts/mcp-handshake-node-full.cjs` — Node.js MCP client that uses Playwright's MCP Client (StreamableHTTPClientTransport) to connect, list tools and call `browser_navigate`. Includes optional auto-install flow when `MCP_ALLOW_INSTALL=1`.
  - `scripts/mcp-handshake-py.py` — Python wrapper that runs the Node full-handshake script.

- Cleaned temporary artifacts:
  - Deleted corrupted temporary file `scripts/mcp-handshake-node.cjs.tmp`.

- Documentation:
  - `docs/setup/MCP_SERVER_SETUP.md` (existing) — updated earlier. This file complements that with a detailed work log (this file).

<!-- section_id: "b1747087-cbaa-4dad-a576-1257d240fd58" -->
## Detailed timeline & notes

1. Initial analysis
   - I inspected the project and identified Playwright MCP entry points at `node_modules/@playwright/mcp` which re-exports `createConnection` from `playwright/lib/mcp/index.js`.
   - Observed that Playwright MCP server exposes `/mcp` and `/sse` endpoints and that the server enforces strict JSON-RPC schema validation.

2. Diagnostic script restoration
   - Rewrote `scripts/mcp-handshake-node.cjs` to be a safe diagnostic: spawn `scripts/mcp-start.sh` detached, poll TCP port, `require('@playwright/mcp')` and call `createConnection` with the server URL. Log the shape of the object returned by `createConnection`.
   - Verified the diagnostic can create a connection object (when the server is running). The diagnostic prints keys like `_options`, `_requestMessageId`, etc.

3. Full MCP client approach
   - Implemented `scripts/mcp-handshake-node-full.cjs` to use Playwright's MCP client classes rather than trying to use the server-side `createConnection` API to do client RPCs.
   - The client approach uses `require('playwright/lib/mcp/sdk/bundle')` to access `Client` and `StreamableHTTPClientTransport`.
   - Sequence in `mcp-handshake-node-full.cjs`:
     - Start helper server (detached)
     - Wait for TCP port
     - Create Client/Transport and connect
     - List available tools via `client.listTools()`
     - Call `browser_navigate` via `client.callTool({ name: 'browser_navigate', arguments: { url } })`
     - Print summary of result
     - Attempt graceful teardown (terminateSession, client.close)

4. Observed failure due to missing browser
   - The server returned an error: "Chromium distribution 'chrome' is not found at /opt/google/chrome/chrome" and suggested running `npx playwright install chrome`.
   - To avoid silently downloading large browser artifacts in automated runs, I implemented a guarded auto-install flow in `scripts/mcp-handshake-node-full.cjs` that only runs when `MCP_ALLOW_INSTALL=1`.
   - If `MCP_ALLOW_INSTALL=1` is set, the script calls the server's `browser_install` tool (via `client.callTool({ name: 'browser_install' })`) and then retries navigation. This mirrors Playwright's own approach to installing browser distributions via the CLI.

5. Helper script adjustments
   - Updated `scripts/mcp-start.sh` to set `PLAYWRIGHT_BROWSERS_PATH=0` (to avoid persistent cache), `PLAYWRIGHT_MCP_BROWSER=chromium` and pass `--browser=chromium` to the `npx @playwright/mcp` call. This reduces the chance Playwright tries to use the 'chrome' channel.

6. Python runner
   - Added `scripts/mcp-handshake-py.py` which runs the Node handshake script. This is a pragmatic approach, since there is no dedicated Python MCP client in Playwright's packages.

7. Cleanup
   - Removed the corrupted temporary file `scripts/mcp-handshake-node.cjs.tmp` left over from earlier edits.

<!-- section_id: "2184a7c5-1beb-4789-a1f9-91eb8a2c0b08" -->
## Commands I ran (representative)

- Start server manually (what you may have run):

```bash
PLAYWRIGHT_BROWSERS_PATH=0 npx -y @playwright/mcp@latest --port 9234 --host 127.0.0.1 --headless
```

- Run Node full handshake (no auto-install):

```bash
node scripts/mcp-handshake-node-full.cjs
```

- Run Node full handshake with auto-install (will download browsers):

```bash
MCP_ALLOW_INSTALL=1 node scripts/mcp-handshake-node-full.cjs
```

- Run Python wrapper (delegates to Node):

```bash
python3 scripts/mcp-handshake-py.py
```

<!-- section_id: "56f3e261-6e32-43ba-aec4-0f941d8f7fee" -->
## Observed outputs

- `node scripts/mcp-handshake-node-full.cjs` (example output):

  - Connected to MCP server
  - Available tools: [ 'browser_close', ..., 'browser_navigate', ... ]
  - Calling tool browser_navigate -> navigate to https://example.com
  - callTool result (summary): { isError: true, contentLength: 1 }
  - Server indicates browser distribution is missing.
  - To allow this script to auto-install the missing browser, re-run with:
      MCP_ALLOW_INSTALL=1 node scripts/mcp-handshake-node-full.cjs
  - Error: Chromium distribution 'chrome' is not found at /opt/google/chrome/chrome
    Run "npx playwright install chrome"

<!-- section_id: "bd83713f-6800-44cf-92da-adbac7b60542" -->
## Files edited/created (detailed)

- scripts/mcp-start.sh (modified)
  - Sets the browser env vars and passes `--browser=chromium`.
- scripts/mcp-handshake-node.cjs (created/updated)
  - Diagnostic script that calls `require('@playwright/mcp').createConnection(...)` and prints keys.
- scripts/mcp-handshake-node-full.cjs (created/updated)
  - Client-based MCP handshake using `playwright/lib/mcp/sdk/bundle` Client & StreamableHTTPClientTransport.
  - Optional browser install support via MCP_ALLOW_INSTALL.
- scripts/mcp-handshake-py.py (added)
  - Python wrapper that runs the Node handshake script.
- scripts/mcp-handshake-node.cjs.tmp (deleted)
- docs/setup/MCP_WORK_LOG.md (this file)

<!-- section_id: "faa34b92-48b2-4723-9238-7bc1b1ee4e19" -->
## Next steps / recommendations

- If you want an automated end-to-end run now, run with auto-install enabled (note: it will download browsers):
  - `MCP_ALLOW_INSTALL=1 node scripts/mcp-handshake-node-full.cjs`

- If you prefer manual control, run the suggested Playwright install command and then re-run the handshake:
  - `npx playwright install chrome`
  - `node scripts/mcp-handshake-node-full.cjs`

- Add convenience npm scripts to `package.json` for running the handshake and smoke tests (I can add these if you want).

- Optional: Implement a more polished Python wrapper that captures and parses the Node client output and returns JSON.

- Optional: Add unit tests for the smoke test scripts (shell + Node + Python) and run them in CI with a Playwright MCP server image that has browsers pre-installed.

<!-- section_id: "91728df2-22eb-4216-ae20-d8b1963bd69f" -->
## Caveats and known issues

- Auto-install will download browser distributions (multi-hundred MB). It's optional and guarded by `MCP_ALLOW_INSTALL=1`.
- There is no official Python MCP client packaged by Playwright today; delegating to the Node client is pragmatic and stable.
- Some Playwright server options may still try to launch a specific browser channel ('chrome') depending on the server config; `--browser=chromium` reduces that likelihood.

<!-- section_id: "c7cd3e3b-6abf-4065-9c12-ce6498e30cfd" -->
## Contact / follow-up

If you'd like, I can:
- Run the auto-install handshake now (if you permit downloading browsers).
- Add npm scripts and a short README section with one-line commands for each test.
- Implement structured JSON output for the Python wrapper.

---
Generated by the in-repo MCP support work (session recorded Oct 16, 2025).

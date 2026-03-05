---
resource_id: "1032826e-2910-4186-bdfa-34ee9a2ae2bb"
resource_type: "document"
resource_name: "codex-vscode-manual-tests.sync-conflict-20260126-035814-IF2WOGZ"
---
# Codex VS Code Manual Tasks

Use this walkthrough to repeat the manual steps we executed while finishing the Codex + VS Code setup on Windows.

<!-- section_id: "cdcf2f8e-34de-4c43-aaa5-acf1186d86bb" -->
## Prerequisites

- Codex CLI installed in WSL and working (`codex --version`)
- Repository checked out under `~/code/setup-hub`
- `scripts/check-codex-setup.sh` available (run `./scripts/check-codex-setup.sh` to verify the baseline)

<!-- section_id: "4ea604ef-9453-475f-bc03-ccfeb4e0f881" -->
## 1. Enable Developer Mode on Windows

1. Press `Win + R`, type `ms-settings:developers`, and press Enter.
2. Toggle **Developer Mode** to **On**.
3. Approve any confirmation dialogs, then close Settings.
4. Back in WSL, run `./scripts/check-codex-setup.sh` to confirm the script now reports `Developer Mode: Enabled`.

<!-- section_id: "9219a778-e43c-44e0-a7c4-51be531d0de9" -->
## 2. Install the Remote - WSL extension in VS Code

1. Launch VS Code (Windows desktop version).
2. Open the Extensions view (`Ctrl+Shift+X`) and search for `Remote - WSL`.
3. Install the Microsoft extension named **WSL** (`ms-vscode-remote.remote-wsl`).
4. Reload VS Code when prompted.
5. From a WSL terminal, run `./scripts/check-codex-setup.sh` again. It should now print `VS Code Remote - WSL extension installed`.

<!-- section_id: "cef31b3e-17ad-4fe4-9138-53b9ba6ce4d2" -->
## 3. Reopen the project inside WSL

1. In a WSL terminal, switch to the repository:

   ```bash
   cd ~/code/setup-hub
   ```

2. Launch VS Code from WSL so the Remote extension attaches automatically:

   ```bash
   code .
   ```

3. Confirm the VS Code status bar shows `WSL: Ubuntu`.

<!-- section_id: "d798f559-79bc-4d2f-8c3f-1cb2dff118c2" -->
## 4. Verify Codex extension behaviour

1. Open the Codex panel and run `/status` to ensure the model (`gpt-5-codex`), mode, and working directory are correct.
2. While in **Chat** mode, ask Codex to append a small note to a scratch file (for example, `text.txt`). Review the diff and approve it—this confirms the approval workflow.
3. Optional: switch to **Agent** mode, request another small edit, then return to Chat mode so you know how to toggle access levels.
4. Ask Codex to run a benign command (e.g., `pwd`). The output should show `/home/dawson/code/setup-hub`.

<!-- section_id: "7bb08328-73e9-4825-afb4-6b619db3a3d8" -->
## 5. Validate browser automation prerequisites

1. In the WSL terminal, ensure Playwright MCP browsers are installed via Node.js Playwright only:

   ```bash
   npx -y playwright@latest install chromium
   ```

   If you ever ran `python3 -m playwright install`, delete those Python caches (`rm -rf ~/.cache/ms-playwright/chromium-*`) before re-running the Node command so Codex/Cursor stop redownloading browsers.

2. Confirm Google Chrome is available for Chrome DevTools MCP (required for Chrome-specific debugging):

   ```bash
   google-chrome --version
   which google-chrome
   ```

   Install it via `wget ... google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb` if those commands fail, then restart Codex after installation.

<!-- section_id: "ccab20bb-337e-4204-aa9a-c78557e05b39" -->
## 6. Launch Codex via VS Code task (optional)

1. Create `.vscode/tasks.json` (if not present) with the `Launch Codex` task from `docs/codex-windows-vscode.md`.
2. Press `Ctrl+Shift+B` (or your custom binding) to ensure the Codex CLI session starts in a new panel.
3. Exit the CLI session with `exit` when finished.

<!-- section_id: "32df40d3-c3c8-4a23-a2f3-03a9243aa959" -->
## 7. Re-run the checklist

- Run `./scripts/check-codex-setup.sh` one more time. Use the output as a quick health check whenever your environment changes (VS Code updates, Codex CLI upgrades, etc.).

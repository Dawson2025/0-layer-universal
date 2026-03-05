---
resource_id: "17c3b8d1-dd98-4857-a1ba-572d63336c03"
resource_type: "document"
resource_name: "codex-vscode-manual-tests"
---
# Codex VS Code Manual Tasks

Use this walkthrough to repeat the manual steps we executed while finishing the Codex + VS Code setup on Windows.

## Prerequisites

- Codex CLI installed in WSL and working (`codex --version`)
- Repository checked out under `~/code/setup-hub`
- `scripts/check-codex-setup.sh` available (run `./scripts/check-codex-setup.sh` to verify the baseline)

## 1. Enable Developer Mode on Windows

1. Press `Win + R`, type `ms-settings:developers`, and press Enter.
2. Toggle **Developer Mode** to **On**.
3. Approve any confirmation dialogs, then close Settings.
4. Back in WSL, run `./scripts/check-codex-setup.sh` to confirm the script now reports `Developer Mode: Enabled`.

## 2. Install the Remote - WSL extension in VS Code

1. Launch VS Code (Windows desktop version).
2. Open the Extensions view (`Ctrl+Shift+X`) and search for `Remote - WSL`.
3. Install the Microsoft extension named **WSL** (`ms-vscode-remote.remote-wsl`).
4. Reload VS Code when prompted.
5. From a WSL terminal, run `./scripts/check-codex-setup.sh` again. It should now print `VS Code Remote - WSL extension installed`.

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

## 4. Verify Codex extension behaviour

1. Open the Codex panel and run `/status` to ensure the model (`gpt-5-codex`), mode, and working directory are correct.
2. While in **Chat** mode, ask Codex to append a small note to a scratch file (for example, `text.txt`). Review the diff and approve it—this confirms the approval workflow.
3. Optional: switch to **Agent** mode, request another small edit, then return to Chat mode so you know how to toggle access levels.
4. Ask Codex to run a benign command (e.g., `pwd`). The output should show `/home/dawson/code/setup-hub`.

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

## 6. Launch Codex via VS Code task (optional)

1. Create `.vscode/tasks.json` (if not present) with the `Launch Codex` task from `docs/codex-windows-vscode.md`.
2. Press `Ctrl+Shift+B` (or your custom binding) to ensure the Codex CLI session starts in a new panel.
3. Exit the CLI session with `exit` when finished.

## 7. Re-run the checklist

- Run `./scripts/check-codex-setup.sh` one more time. Use the output as a quick health check whenever your environment changes (VS Code updates, Codex CLI upgrades, etc.).

---
resource_id: "201d7995-2ddc-411f-965d-3916eb20f281"
resource_type: "document"
resource_name: "codex-windows-vscode.sync-conflict-20260126-035816-IF2WOGZ"
---
# Codex on Windows + VS Code

This guide follows the official [Running Codex on Windows](https://developers.openai.com/codex/windows) playbook and adds a few quality-of-life tweaks for VS Code users.

<!-- section_id: "d10c6be8-bfee-4423-9f86-98cbb5ae6465" -->
## Prerequisites

- Windows 11 (22H2+) or Windows 10 (22H2) with administrator access
- Stable internet connection and GitHub account
- Optional: backups of existing VS Code or shell configurations

<!-- section_id: "c592637b-83d8-433b-9c9a-a06d8519bea5" -->
## Progress checklist

Copy these checkboxes into your notes (or mark them directly in VS Code’s markdown preview) to see which steps are complete. The commands help you confirm progress.

- [ ] Windows updates applied, Developer Mode enabled, Windows Terminal installed.
- [ ] `wsl -l -v` lists the Ubuntu distro with VERSION `2`.
- [ ] `sudo apt update && sudo apt upgrade -y` ran without errors.
- [ ] `git --version` works and `git config --global user.name` shows your details.
- [ ] `nvm --version` and `node -v` report Node.js 22.x.
- [ ] `codex --version` prints the CLI version and `codex` launches successfully.
- [ ] Active repositories live under `~/code` (verify with `pwd`), not `/mnt/c`.
- [ ] VS Code Remote WSL extension shows “WSL: Ubuntu” in the status bar.
- [ ] Running `codex work` (or your task shortcut) opens a Codex session without errors.

<!-- section_id: "38ed344c-f103-40d3-a218-8ae7d36f7c7a" -->
### Quick progress commands

Use these one-liners to check where you stand:

- PowerShell (Windows side):

  ```powershell
  # Show WSL distros and versions
  wsl -l -v

  # Verify Developer Mode is enabled (returns 1 when enabled)
  (Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock).AllowDevelopmentWithoutDevLicense
  ```

- WSL (Ubuntu shell):

  ```bash
  git --version && git config --global user.name
  nvm --version && node -v
  codex --version && which codex
  pwd
  ```

<!-- section_id: "b2455656-4aeb-4a23-bb9c-5cf37061b875" -->
### Self-check script (WSL)

Run the bundled script to see a consolidated status report:

```bash
cd ~/code/setup-hub
./scripts/check-codex-setup.sh
```

To keep a copy in your home directory (optional):

```bash
cp ./scripts/check-codex-setup.sh ~/check-codex-setup.sh
chmod +x ~/check-codex-setup.sh
~/check-codex-setup.sh
```

Re-run the script after major changes (Node upgrades, Codex updates, VS Code reinstalls) to ensure nothing regressed.

<!-- section_id: "70298f70-a2db-44ee-9afd-7f82b87d3dac" -->
## 1. Prepare Windows

1. Apply pending Windows Updates and reboot.
2. Turn on Developer Mode (`Settings > Privacy & security > For developers`).
3. Install [Windows Terminal](https://aka.ms/terminal) from the Microsoft Store.
4. Plan to set Ubuntu as the default terminal profile after WSL is in place.

<!-- section_id: "ede4c632-dd2d-499a-af6c-f29d6242417a" -->
## 2. Install WSL 2

Run these commands in an elevated PowerShell or Windows Terminal:

```powershell
wsl --install
```

When prompted, reboot. After restart, open Windows Terminal and launch the Ubuntu profile (`wsl`) to create your Linux username and password.

<!-- section_id: "76e3b787-901e-4851-8a5c-a76fa0e51c6b" -->
## 3. Bootstrap your WSL environment

Inside the Ubuntu shell:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl git unzip ca-certificates
```

Configure Git (replace placeholders):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
git config --global core.autocrlf input
```

<!-- section_id: "72a0a6ef-ce42-457d-a095-c21cc6190003" -->
## 4. Install Node.js with `nvm`

Codex CLI is published as an npm package, so install Node.js inside WSL via `nvm`:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.nvm/nvm.sh
nvm install 22
nvm use 22
```

Open a new terminal if `nvm` is not immediately available.

<!-- section_id: "711c6191-2c39-41ea-b308-6414f135d3e4" -->
## 5. Install Codex CLI

```bash
npm i -g @openai/codex
codex            # first-run setup
which codex      # confirm it is on PATH
```

If your organization requires authentication:

```bash
codex auth login
```

<!-- section_id: "356b6b71-46fc-4221-a48d-88abc6583ffa" -->
## 6. Keep projects inside WSL

- Create a workspace folder for repositories:

  ```bash
  mkdir -p ~/code && cd ~/code
  ```

- Clone repos directly inside this directory (`git clone …`).
- Access the same files from Windows via `\\wsl$\<Distro>\home\<user>\code` in Explorer.
- Avoid syncing repositories through OneDrive/Dropbox/iCloud folders—these services can lock files, rewrite line endings, or duplicate symlinks. If you need a Windows-only checkout for native tools, use a folder like `C:\dev` (outside cloud sync) and clone separately from WSL (`/mnt/c/dev/...`) only when necessary.

<!-- section_id: "c234d0be-19b7-4c7f-9ea6-34cc4822fd92" -->
## 7. Install VS Code and essential extensions

1. Install [VS Code](https://code.visualstudio.com/Download) (System Installer recommended).
2. Install extensions:
   - `ms-vscode-remote.remote-wsl`
   - `GitHub.copilot` (optional, complements Codex)
   - `ms-vscode.powershell` (for Windows-side scripting)
   - Project-specific linters and formatters
3. Sign in and sync settings if you use Settings Sync.

<!-- section_id: "1eed5449-6013-40f0-bf98-d861f0dd8d98" -->
## 8. Configure VS Code defaults for Codex

- `File > Preferences > Settings`:
  - `terminal.integrated.defaultProfile.windows`: `Ubuntu (WSL)`
  - `files.autoSave`: `onFocusChange` for smoother Codex edits
  - `git.confirmSync`: `false` to avoid extra prompts during automated syncs
- Add project-specific preferences in `.vscode/settings.json` as needed.

<!-- section_id: "2e86616d-4258-41e0-ba2c-ea52fa66989a" -->
## 9. Add a Codex task (optional but handy)

Create `.vscode/tasks.json` in your project:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Launch Codex",
      "type": "shell",
      "command": "codex work",
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "problemMatcher": []
    }
  ]
}
```

Bind the task to a shortcut (`File > Preferences > Keyboard Shortcuts (JSON)`):

```json
{
  "key": "ctrl+shift+,",
  "command": "workbench.action.tasks.runTask",
  "args": "Launch Codex"
}
```

<!-- section_id: "9f94f019-484d-4139-adfa-ec7fb380ddb9" -->
## 10. Run and validate Codex

1. Open your repo from the WSL path (`code .`).
2. Start the Codex task (`Ctrl+Shift+B` by default, or your custom binding).
3. Run a smoke test (e.g., ask Codex to edit a file or run a project script).

<!-- section_id: "cc8455de-003d-4aec-99a7-f1e52a1107a7" -->
## 11. Browser automation MCP servers (Playwright + Chrome)

Some Codex workflows rely on browser automation via MCP servers. Set these up once per machine so future projects (Cursor, Codex CLI, VS Code agents, etc.) can launch browsers without repeatedly downloading gigabytes of binaries.

<!-- section_id: "03708e66-2a99-41f4-ad0a-40ce2e883360" -->
### Playwright MCP (Chromium)

- Install browsers with **Node.js Playwright** only:

  ```bash
  npx -y playwright@latest install chromium
  ```

- **Do not** run `python3 -m playwright install ...`; the Python build stores browsers in a different cache so Codex/Cursor will never see them and will redownload every session.
- If you already used the Python installer, wipe those caches (`rm -rf ~/.cache/ms-playwright/chromium-*`) and repeat the Node command above; then restart Codex so it re-detects the browsers.

<!-- section_id: "2334d37d-82ab-420b-9776-edbe322a06c9" -->
### Chrome DevTools MCP

Chrome DevTools MCP requires actual Google Chrome, not Playwright’s Chromium bundle.

1. Install Chrome inside WSL (Ubuntu example):

   ```bash
   cd /tmp
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo apt install ./google-chrome-stable_current_amd64.deb
   ```

2. Verify availability:

   ```bash
   google-chrome --version
   which google-chrome
   ```

3. Update your `.mcp.json` entry to launch `chrome-devtools-mcp` via `npx -y chrome-devtools-mcp@latest` (omit `--browserUrl` so it can auto-start Chrome) and restart Codex.

If Chrome isn’t installed, Chrome DevTools MCP will spawn repeatedly and fail. Keeping Chromium (Playwright) and Chrome (system) separate prevents most “browser not installed” loops.

<!-- section_id: "c4679dab-74a3-4a33-b7e5-495fbd685b19" -->
## 12. Troubleshooting & FAQ

- **Extension installed but unresponsive**: Install the [Visual Studio Build Tools (C++ workload)](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and the latest [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist), then restart VS Code. Winget shortcut:

  ```powershell
  winget install --id Microsoft.VisualStudio.2022.BuildTools -e
  ```

- **Codex binary not found**: Run `which codex`. If it is missing, reload your shell (`nvm use 22`) and re-run `npm i -g @openai/codex`.
- **Slow performance on large repos**: Keep projects inside `/home/<user>` rather than `/mnt/c`; update WSL if things feel sluggish:

  ```powershell
  wsl --update
  wsl --shutdown
  ```

- **CLI vs IDE behavior**: In CLI mode (`codex work`) Codex uses Linux sandboxing inside WSL. In the VS Code extension, start with Chat mode (approval-based) and only switch to Agent (full access) if you trust the workspace.

<!-- section_id: "29a31689-9335-4741-bb13-8332ee4fb413" -->
## 13. Stay up to date

- Update Codex CLI periodically:

  ```bash
  npm update -g @openai/codex
  ```

- Keep VS Code and extensions on auto-update.
- Rotate credentials (SSH keys, tokens) when teams or roles change.
- Capture dotfiles and `.vscode/` snippets so new machines can be bootstrapped quickly.

---
resource_id: "30c1e758-4fb1-44ab-b37a-f0b7dd26ca9a"
resource_type: "document"
resource_name: "codex-windows-vscode"
---
# Codex on Windows + VS Code

This guide follows the official [Running Codex on Windows](https://developers.openai.com/codex/windows) playbook and adds a few quality-of-life tweaks for VS Code users.

<!-- section_id: "95c6609b-1ddb-4cc4-b5e9-af61ed062343" -->
## Prerequisites

- Windows 11 (22H2+) or Windows 10 (22H2) with administrator access
- Stable internet connection and GitHub account
- Optional: backups of existing VS Code or shell configurations

<!-- section_id: "4712c752-4f1a-4f46-8554-93ae44068bd0" -->
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

<!-- section_id: "3341fa52-fb1f-4b8c-9c33-60746df1a236" -->
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

<!-- section_id: "97c429d8-fc43-4d00-83d9-986739389450" -->
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

<!-- section_id: "18059066-37a5-4572-ae39-43150fb98f92" -->
## 1. Prepare Windows

1. Apply pending Windows Updates and reboot.
2. Turn on Developer Mode (`Settings > Privacy & security > For developers`).
3. Install [Windows Terminal](https://aka.ms/terminal) from the Microsoft Store.
4. Plan to set Ubuntu as the default terminal profile after WSL is in place.

<!-- section_id: "ca47e6c3-011c-481e-b810-8a21ad64abf8" -->
## 2. Install WSL 2

Run these commands in an elevated PowerShell or Windows Terminal:

```powershell
wsl --install
```

When prompted, reboot. After restart, open Windows Terminal and launch the Ubuntu profile (`wsl`) to create your Linux username and password.

<!-- section_id: "c2936dea-d2c1-483d-8f47-d839e762ae29" -->
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

<!-- section_id: "d23294c8-5e94-4a8f-b07d-d59817b3c344" -->
## 4. Install Node.js with `nvm`

Codex CLI is published as an npm package, so install Node.js inside WSL via `nvm`:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.nvm/nvm.sh
nvm install 22
nvm use 22
```

Open a new terminal if `nvm` is not immediately available.

<!-- section_id: "d1138862-9097-4123-9f60-ffaad50a70cc" -->
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

<!-- section_id: "ff37eba0-602b-44a1-8924-3b89b54dc6a8" -->
## 6. Keep projects inside WSL

- Create a workspace folder for repositories:

  ```bash
  mkdir -p ~/code && cd ~/code
  ```

- Clone repos directly inside this directory (`git clone …`).
- Access the same files from Windows via `\\wsl$\<Distro>\home\<user>\code` in Explorer.
- Avoid syncing repositories through OneDrive/Dropbox/iCloud folders—these services can lock files, rewrite line endings, or duplicate symlinks. If you need a Windows-only checkout for native tools, use a folder like `C:\dev` (outside cloud sync) and clone separately from WSL (`/mnt/c/dev/...`) only when necessary.

<!-- section_id: "6399ed71-3c66-4c2a-b3f9-c528ed81924e" -->
## 7. Install VS Code and essential extensions

1. Install [VS Code](https://code.visualstudio.com/Download) (System Installer recommended).
2. Install extensions:
   - `ms-vscode-remote.remote-wsl`
   - `GitHub.copilot` (optional, complements Codex)
   - `ms-vscode.powershell` (for Windows-side scripting)
   - Project-specific linters and formatters
3. Sign in and sync settings if you use Settings Sync.

<!-- section_id: "6206e9d7-09e9-4a43-ba8f-b7763d80b7d4" -->
## 8. Configure VS Code defaults for Codex

- `File > Preferences > Settings`:
  - `terminal.integrated.defaultProfile.windows`: `Ubuntu (WSL)`
  - `files.autoSave`: `onFocusChange` for smoother Codex edits
  - `git.confirmSync`: `false` to avoid extra prompts during automated syncs
- Add project-specific preferences in `.vscode/settings.json` as needed.

<!-- section_id: "1bf523a1-dfda-495e-bdfe-758c5eca2a29" -->
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

<!-- section_id: "f6f90d3e-b0de-4d3a-98f9-52579a5eaea5" -->
## 10. Run and validate Codex

1. Open your repo from the WSL path (`code .`).
2. Start the Codex task (`Ctrl+Shift+B` by default, or your custom binding).
3. Run a smoke test (e.g., ask Codex to edit a file or run a project script).

<!-- section_id: "84cb1319-4aa7-4ead-a03b-11a021a6900f" -->
## 11. Browser automation MCP servers (Playwright + Chrome)

Some Codex workflows rely on browser automation via MCP servers. Set these up once per machine so future projects (Cursor, Codex CLI, VS Code agents, etc.) can launch browsers without repeatedly downloading gigabytes of binaries.

<!-- section_id: "a8402a1e-3ce1-4498-b70f-af7b9f45563f" -->
### Playwright MCP (Chromium)

- Install browsers with **Node.js Playwright** only:

  ```bash
  npx -y playwright@latest install chromium
  ```

- **Do not** run `python3 -m playwright install ...`; the Python build stores browsers in a different cache so Codex/Cursor will never see them and will redownload every session.
- If you already used the Python installer, wipe those caches (`rm -rf ~/.cache/ms-playwright/chromium-*`) and repeat the Node command above; then restart Codex so it re-detects the browsers.

<!-- section_id: "79e4fc17-254a-4b29-b9d7-15a3fa71d09c" -->
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

<!-- section_id: "679b9375-bc99-49b5-a8dd-d3773288df67" -->
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

<!-- section_id: "cc9bd69d-e63d-49f7-adf1-f67c8551651e" -->
## 13. Stay up to date

- Update Codex CLI periodically:

  ```bash
  npm update -g @openai/codex
  ```

- Keep VS Code and extensions on auto-update.
- Rotate credentials (SSH keys, tokens) when teams or roles change.
- Capture dotfiles and `.vscode/` snippets so new machines can be bootstrapped quickly.

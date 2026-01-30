# Codex on Windows + VS Code

This guide follows the official [Running Codex on Windows](https://developers.openai.com/codex/windows) playbook and adds a few quality-of-life tweaks for VS Code users.

## Prerequisites

- Windows 11 (22H2+) or Windows 10 (22H2) with administrator access
- Stable internet connection and GitHub account
- Optional: backups of existing VS Code or shell configurations

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

## 1. Prepare Windows

1. Apply pending Windows Updates and reboot.
2. Turn on Developer Mode (`Settings > Privacy & security > For developers`).
3. Install [Windows Terminal](https://aka.ms/terminal) from the Microsoft Store.
4. Plan to set Ubuntu as the default terminal profile after WSL is in place.

## 2. Install WSL 2

Run these commands in an elevated PowerShell or Windows Terminal:

```powershell
wsl --install
```

When prompted, reboot. After restart, open Windows Terminal and launch the Ubuntu profile (`wsl`) to create your Linux username and password.

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

## 4. Install Node.js with `nvm`

Codex CLI is published as an npm package, so install Node.js inside WSL via `nvm`:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.nvm/nvm.sh
nvm install 22
nvm use 22
```

Open a new terminal if `nvm` is not immediately available.

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

## 6. Keep projects inside WSL

- Create a workspace folder for repositories:

  ```bash
  mkdir -p ~/code && cd ~/code
  ```

- Clone repos directly inside this directory (`git clone …`).
- Access the same files from Windows via `\\wsl$\<Distro>\home\<user>\code` in Explorer.
- Avoid syncing repositories through OneDrive/Dropbox/iCloud folders—these services can lock files, rewrite line endings, or duplicate symlinks. If you need a Windows-only checkout for native tools, use a folder like `C:\dev` (outside cloud sync) and clone separately from WSL (`/mnt/c/dev/...`) only when necessary.

## 7. Install VS Code and essential extensions

1. Install [VS Code](https://code.visualstudio.com/Download) (System Installer recommended).
2. Install extensions:
   - `ms-vscode-remote.remote-wsl`
   - `GitHub.copilot` (optional, complements Codex)
   - `ms-vscode.powershell` (for Windows-side scripting)
   - Project-specific linters and formatters
3. Sign in and sync settings if you use Settings Sync.

## 8. Configure VS Code defaults for Codex

- `File > Preferences > Settings`:
  - `terminal.integrated.defaultProfile.windows`: `Ubuntu (WSL)`
  - `files.autoSave`: `onFocusChange` for smoother Codex edits
  - `git.confirmSync`: `false` to avoid extra prompts during automated syncs
- Add project-specific preferences in `.vscode/settings.json` as needed.

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

## 10. Run and validate Codex

1. Open your repo from the WSL path (`code .`).
2. Start the Codex task (`Ctrl+Shift+B` by default, or your custom binding).
3. Run a smoke test (e.g., ask Codex to edit a file or run a project script).

## 11. Browser automation MCP servers (Playwright + Chrome)

Some Codex workflows rely on browser automation via MCP servers. Set these up once per machine so future projects (Cursor, Codex CLI, VS Code agents, etc.) can launch browsers without repeatedly downloading gigabytes of binaries.

### Playwright MCP (Chromium)

- Install browsers with **Node.js Playwright** only:

  ```bash
  npx -y playwright@latest install chromium
  ```

- **Do not** run `python3 -m playwright install ...`; the Python build stores browsers in a different cache so Codex/Cursor will never see them and will redownload every session.
- If you already used the Python installer, wipe those caches (`rm -rf ~/.cache/ms-playwright/chromium-*`) and repeat the Node command above; then restart Codex so it re-detects the browsers.

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

## 13. Stay up to date

- Update Codex CLI periodically:

  ```bash
  npm update -g @openai/codex
  ```

- Keep VS Code and extensions on auto-update.
- Rotate credentials (SSH keys, tokens) when teams or roles change.
- Capture dotfiles and `.vscode/` snippets so new machines can be bootstrapped quickly.

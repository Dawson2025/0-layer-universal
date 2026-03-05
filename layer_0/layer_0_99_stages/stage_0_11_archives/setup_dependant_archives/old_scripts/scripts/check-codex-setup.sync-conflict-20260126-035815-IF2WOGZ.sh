#!/usr/bin/env bash
# resource_id: "63523495-02c3-4c40-b51e-a10a7da94738"
# resource_type: "script"
# resource_name: "check-codex-setup.sync-conflict-20260126-035815-IF2WOGZ"
set -euo pipefail

export NVM_DIR="$HOME/.nvm"
if [[ -s "$NVM_DIR/nvm.sh" ]]; then
  # shellcheck disable=SC1090
  source "$NVM_DIR/nvm.sh"
fi

to_unix() {
  # Convert CRLF PowerShell output to Unix newlines.
  tr -d $'\r'
}

echo "== WSL Distro Version =="
wsl.exe -l -v

echo
echo "== Windows prerequisites =="
dev_mode=$(
  powershell.exe -Command "Try { (Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock').AllowDevelopmentWithoutDevLicense } Catch { '' }" |
    to_unix
)
if [[ "$dev_mode" == "1" ]]; then
  echo "Developer Mode: Enabled"
else
  echo "Developer Mode: Disabled (enable via Settings > Privacy & security > For developers)"
fi
wt_path=$(
  powershell.exe -Command "(Get-AppxPackage Microsoft.WindowsTerminal).InstallLocation" | to_unix || true
)
if [[ -n "$wt_path" ]]; then
  echo "Windows Terminal: Installed at $wt_path"
else
  echo "Windows Terminal: Not found (install from Microsoft Store)"
fi

echo
echo "== Git config =="
git --version
git config --global user.name || echo "user.name not set"
git config --global user.email || echo "user.email not set"

echo
echo "== Node & Codex =="
if command -v nvm >/dev/null 2>&1; then nvm --version; else echo "nvm not found"; fi
if command -v node >/dev/null 2>&1; then node -v; else echo "node not found"; fi
if command -v codex >/dev/null 2>&1; then codex --version; else echo "codex not found"; fi
if command -v codex >/dev/null 2>&1; then
  codex work --help >/dev/null && echo "codex work command available"
fi

echo
echo "== Workspace path =="
pwd
if [[ $PWD == /mnt/* ]]; then
  echo "⚠️  You are under /mnt; move projects into ~/code"
else
  echo "👍 Running inside WSL home"
fi

echo
echo "== VS Code extensions =="
host_extensions=$(
  powershell.exe -Command "Try { Push-Location \$env:USERPROFILE; if (Get-Command code -ErrorAction Stop) { code --list-extensions }; Pop-Location } Catch { '' }" |
    to_unix
)
if echo "$host_extensions" | grep -qi 'ms-vscode-remote.remote-wsl'; then
  echo "VS Code Remote - WSL extension installed"
elif [[ -z "$host_extensions" ]]; then
  echo "VS Code CLI 'code' not found on Windows PATH (open VS Code > Command Palette > \"Shell Command: Install 'code' command in PATH\")"
else
  echo "VS Code Remote - WSL extension missing (install from VS Code marketplace on Windows)"
fi

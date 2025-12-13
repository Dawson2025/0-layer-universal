# GitHub `byui-math-dept` HTTPS PAT Helper (SAML SSO)

This setup installs a **Git credential helper** that reads a Personal Access Token (PAT) from a local file and automatically authenticates Git-over-HTTPS operations for **GitHub org** `byui-math-dept` (which enforces SAML SSO).

## What It Does

- Configures Git to use a custom credential helper for `https://github.com/byui-math-dept/*`.
- The helper reads the PAT from: `~/.config/git/pats/byui-math-dept.pat`
- Git config keys used:
  - `credential.helper=/home/dawson/.local/bin/git-credential-github-byui-math-dept`
  - `credential.useHttpPath=true` (required so Git includes `byui-math-dept/<repo>.git` in credential requests)

## OS / Environment Compatibility

**Works as-is (same approach + same helper script):**
- **WSL (Ubuntu, Debian, etc.)**: applies inside the WSL distro user environment.
- **Native Linux (Ubuntu, Debian, Fedora, etc.)**: applies per-user on that machine.
- **macOS**: applies per-user (bash script; same Git credential helper mechanism). Paths remain valid if `$HOME` is correct.

**Does not automatically apply (needs separate setup/adaptation):**
- **Windows (Git for Windows)**: you must set up an equivalent helper in the Windows environment (different filesystem paths; optionally PowerShell helper).
- **Containers / CI**: possible, but you should prefer ephemeral tokens via CI secrets; don’t bake PAT files into images.

## Scope / Portability

- **Per-user**: stored in `~/.gitconfig` and `~/.local/bin/`.
- **Per-machine / per-environment**: you must repeat setup on each machine, and separately inside WSL vs Windows host.

## SSO Notes (Critical)

- Org-enforced SAML SSO requires the PAT to be **SSO-authorized for `byui-math-dept`**.
- If you see a 403 with an `authorization_request=...` URL, open it in a browser and complete the BYU-I SSO flow for the token.

## Security Notes

- Treat PATs like passwords.
- Keep the token file permissions locked: `chmod 600 ~/.config/git/pats/byui-math-dept.pat`
- Do not paste PATs into AI chats, logs, or committed files.

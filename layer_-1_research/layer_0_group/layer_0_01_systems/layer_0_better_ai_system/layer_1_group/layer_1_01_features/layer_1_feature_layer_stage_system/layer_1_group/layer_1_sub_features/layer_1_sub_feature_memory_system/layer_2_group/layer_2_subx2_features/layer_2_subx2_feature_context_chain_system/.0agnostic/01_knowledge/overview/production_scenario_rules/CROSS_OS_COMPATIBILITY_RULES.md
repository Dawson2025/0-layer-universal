---
resource_id: "c8109dc2-8d1c-4789-8764-1157d1724ad6"
resource_type: "knowledge"
resource_name: "CROSS_OS_COMPATIBILITY_RULES"
---
# Cross-OS Compatibility Rules

**Layer**: 0 (Universal)
**Purpose**: Guidelines for creating files, folders, and code that work across Windows, Linux, and macOS
**Created**: 2026-01-17

---

<!-- section_id: "d7ddfa60-2956-4d3a-ad29-d9dcc7726adc" -->
## CRITICAL: File and Folder Naming

<!-- section_id: "86a82313-690c-4c97-979d-da84771cb041" -->
### Forbidden Characters by OS

| Character | Windows | Linux | macOS | Recommendation |
|-----------|---------|-------|-------|----------------|
| `*` | ❌ FORBIDDEN | ✅ Allowed | ✅ Allowed | **NEVER USE** |
| `?` | ❌ FORBIDDEN | ✅ Allowed | ✅ Allowed | **NEVER USE** |
| `<` | ❌ FORBIDDEN | ✅ Allowed | ✅ Allowed | **NEVER USE** |
| `>` | ❌ FORBIDDEN | ✅ Allowed | ✅ Allowed | **NEVER USE** |
| `:` | ❌ FORBIDDEN | ✅ Allowed | ❌ FORBIDDEN | **NEVER USE** |
| `"` | ❌ FORBIDDEN | ✅ Allowed | ✅ Allowed | **NEVER USE** |
| `\|` | ❌ FORBIDDEN | ✅ Allowed | ✅ Allowed | **NEVER USE** |
| `\` | ❌ Path sep | ✅ Allowed | ✅ Allowed | **NEVER USE** |
| `/` | ❌ Path sep | ❌ Path sep | ❌ Path sep | **NEVER USE** |

<!-- section_id: "3e962c01-4b34-4d99-a75a-d548cd8a5b17" -->
### Safe Naming Rules

1. **Use only**: `a-z`, `A-Z`, `0-9`, `_`, `-`, `.`
2. **Avoid spaces** - use `_` or `-` instead
3. **Avoid starting with** `.` (hidden on Linux/macOS)
4. **Avoid starting with** `-` (conflicts with CLI flags)
5. **Keep paths under 260 characters** (Windows limit)

<!-- section_id: "d82a5821-2d92-47a3-a237-af9a20e24b4a" -->
### Examples

| Bad (Cross-OS Issues) | Good (Universal) |
|-----------------------|------------------|
| `layer_3_subx2_projects` | `layer_3_subx2_projects` |
| `file:name.txt` | `file_name.txt` |
| `what?.md` | `what.md` |
| `<config>.json` | `config.json` |
| `my file.txt` | `my_file.txt` |

---

<!-- section_id: "78e1fc2b-49d0-4b2d-a3b2-1cec3640221d" -->
## Path Handling

<!-- section_id: "a0092af7-e301-427b-9af8-0c9d79e648c3" -->
### Path Separators

| OS | Separator | Example |
|----|-----------|---------|
| Windows | `\` | `C:\Users\Dawson\file.txt` |
| Linux | `/` | `/home/dawson/file.txt` |
| macOS | `/` | `/Users/dawson/file.txt` |

<!-- section_id: "2fa2610f-1ed7-4a94-b13c-f58335154f58" -->
### Best Practices

1. **In code**: Use language's path library (e.g., `os.path.join()`, `path.join()`)
2. **In configs**: Use forward slashes `/` (works on all OS in most contexts)
3. **In scripts**: Use variables like `$HOME` or `%USERPROFILE%`

---

<!-- section_id: "cbd97418-b788-4029-9ef4-ed507c0e9e3b" -->
## Line Endings

| OS | Line Ending | Hex |
|----|-------------|-----|
| Windows | CRLF | `\r\n` (0x0D 0x0A) |
| Linux | LF | `\n` (0x0A) |
| macOS | LF | `\n` (0x0A) |

<!-- section_id: "f4d9a7d1-8215-4247-9fcf-7d6aad71c39b" -->
### Best Practices

1. **Configure Git**: `git config --global core.autocrlf true` (Windows)
2. **Use `.gitattributes`**: `* text=auto`
3. **Editors**: Set to use LF for cross-platform projects

---

<!-- section_id: "a969b938-e2da-4efc-b0bc-8f44f3163f93" -->
## Case Sensitivity

| OS | Case Sensitive? |
|----|-----------------|
| Windows | ❌ No (`File.txt` = `file.txt`) |
| Linux | ✅ Yes (`File.txt` ≠ `file.txt`) |
| macOS | ❌ No (by default) |

<!-- section_id: "162ee8aa-2fa0-4f99-b3fe-abefd863097d" -->
### Best Practices

1. **Always use lowercase** for file/folder names
2. **Never rely on case** to differentiate files
3. **Be consistent** with naming conventions

---

<!-- section_id: "ca87a531-bff9-4481-b26d-2cddee134178" -->
## Permissions

<!-- section_id: "b17c6788-1863-487e-98eb-b558183a846b" -->
### Windows vs Linux/macOS

| Concept | Windows | Linux/macOS |
|---------|---------|-------------|
| Execute bit | N/A | Required for scripts |
| File modes | ACLs | chmod (rwx) |
| Hidden files | Attribute | Dot prefix |

<!-- section_id: "edc6793b-10b8-43ee-9f80-6404e7134276" -->
### Best Practices

1. **Scripts**: Add shebang `#!/bin/bash` and `chmod +x`
2. **Git**: Preserves execute bit across systems
3. **Hidden files**: Use dot prefix for Linux/macOS, not Windows hidden attribute

---

<!-- section_id: "49a06640-a95c-40e3-972d-a1faf303eac6" -->
## Symlinks

| OS | Support | Command |
|----|---------|---------|
| Windows | Limited (admin) | `mklink` |
| Linux | Full | `ln -s` |
| macOS | Full | `ln -s` |

<!-- section_id: "7d337b36-2675-4c7a-a6d6-479913794e14" -->
### Best Practices

1. **Avoid symlinks** in synced folders (Syncthing, Git)
2. **Use relative paths** if symlinks needed
3. **Document** any symlink requirements

---

<!-- section_id: "1d29ef29-d473-4bc5-b192-4815147becde" -->
## Shell Scripts

<!-- section_id: "a76c0c5c-66cb-46b3-b35b-f8f27011bd13" -->
### Cross-Platform Scripting

```bash
# BAD - Windows-specific
dir /b

# BAD - Linux-specific
ls -la

# GOOD - Use cross-platform tools or detect OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows (Git Bash/MSYS)
    cmd /c dir
else
    # Linux/macOS
    ls -la
fi
```

<!-- section_id: "d9864e51-9783-4cf2-9220-5e6b28359f33" -->
### Shebang Lines

```bash
#!/usr/bin/env bash    # GOOD - portable
#!/bin/bash            # OK - Linux/macOS
#!/bin/sh              # OK - POSIX only
```

---

<!-- section_id: "c53f31e8-7d4e-4868-bb55-e8e8b115080d" -->
## Environment Variables

| Variable | Windows | Linux | macOS |
|----------|---------|-------|-------|
| Home dir | `%USERPROFILE%` | `$HOME` | `$HOME` |
| Temp dir | `%TEMP%` | `/tmp` | `/tmp` |
| Path sep | `;` | `:` | `:` |

---

<!-- section_id: "810900a2-0361-4c7b-b170-d235b1ab0695" -->
## Git and Syncthing Considerations

<!-- section_id: "06f7e9c1-2515-4bfc-b659-1af1612a2f66" -->
### Git

1. **`.gitattributes`**: Define line endings per file type
2. **`.gitignore`**: Include OS-specific ignores
3. **Filename issues**: Git will fail to checkout files with invalid names on Windows

<!-- section_id: "80d62d53-c574-4153-a625-830f48ae2c89" -->
### Syncthing

1. **Ignores**: Configure `.stignore` for OS-specific files
2. **Conflicts**: May occur if files differ only by case
3. **Symlinks**: May not sync properly

---

<!-- section_id: "a35ac9eb-ccf3-4e99-94f3-ad01a0561621" -->
## Checklist Before Creating Files/Folders

- [ ] No forbidden characters (`* ? < > : " | \ /`)
- [ ] No spaces (use `_` or `-`)
- [ ] All lowercase
- [ ] Path length under 200 characters
- [ ] No leading dots unless intentionally hidden
- [ ] No leading dashes

---

<!-- section_id: "18be6377-3ffb-4173-b73c-27b6c6f00e06" -->
## Known Issues Log

| Date | Issue | Cause | Fix |
|------|-------|-------|-----|
| 2026-01-17 | Git pull fails on Windows | Filename contains `*` | Rename on Linux: `*` → `x` |

---

<!-- section_id: "76487036-5c6d-4952-af7d-789415b438e5" -->
## AI Assistant Instructions

When creating files or folders in this repository:

1. **ALWAYS** follow the safe naming rules above
2. **NEVER** use characters forbidden on Windows
3. **PREFER** lowercase with underscores
4. **CHECK** path length on deeply nested structures
5. **TEST** on multiple OS before committing critical changes

**If you see a filename with forbidden characters:**
1. Flag it immediately
2. Suggest a cross-OS compatible alternative
3. Create a fix script if needed

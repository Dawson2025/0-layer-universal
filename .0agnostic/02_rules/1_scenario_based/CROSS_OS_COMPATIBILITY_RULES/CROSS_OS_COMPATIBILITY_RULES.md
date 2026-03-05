---
resource_id: "7b9e144f-7a80-4664-a802-8bea61e6a3fa"
resource_type: "rule"
resource_name: "CROSS_OS_COMPATIBILITY_RULES"
---
# Cross-OS Compatibility Rules

**Layer**: 0 (Universal)
**Purpose**: Guidelines for creating files, folders, and code that work across Windows, Linux, and macOS
**Created**: 2026-01-17

---

<!-- section_id: "84c97ace-245b-44b5-9c2d-0c4aab5cccc2" -->
## CRITICAL: File and Folder Naming

<!-- section_id: "b4f65b6c-9724-42a2-bd40-aadd22841267" -->
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

<!-- section_id: "a3bf74fd-95c5-4adf-b777-e26630b1f0c7" -->
### Safe Naming Rules

1. **Use only**: `a-z`, `A-Z`, `0-9`, `_`, `-`, `.`
2. **Avoid spaces** - use `_` or `-` instead
3. **Avoid starting with** `.` (hidden on Linux/macOS)
4. **Avoid starting with** `-` (conflicts with CLI flags)
5. **Keep paths under 260 characters** (Windows limit)

<!-- section_id: "b6c8185e-53cc-4dd7-be2f-ea9dc05e83e8" -->
### Examples

| Bad (Cross-OS Issues) | Good (Universal) |
|-----------------------|------------------|
| `layer_3_subx2_projects` | `layer_3_subx2_projects` |
| `file:name.txt` | `file_name.txt` |
| `what?.md` | `what.md` |
| `<config>.json` | `config.json` |
| `my file.txt` | `my_file.txt` |

---

<!-- section_id: "eaa580b6-bfb1-4776-884e-ffac62ae6f32" -->
## Path Handling

<!-- section_id: "c6d3e9aa-b205-49a6-821f-89f72ea17b07" -->
### Path Separators

| OS | Separator | Example |
|----|-----------|---------|
| Windows | `\` | `C:\Users\Dawson\file.txt` |
| Linux | `/` | `/home/dawson/file.txt` |
| macOS | `/` | `/Users/dawson/file.txt` |

<!-- section_id: "77c6808d-1f72-4695-a469-edfb07740c41" -->
### Best Practices

1. **In code**: Use language's path library (e.g., `os.path.join()`, `path.join()`)
2. **In configs**: Use forward slashes `/` (works on all OS in most contexts)
3. **In scripts**: Use variables like `$HOME` or `%USERPROFILE%`

---

<!-- section_id: "465a26f3-bbc9-419e-b73b-e0198b207a1f" -->
## Line Endings

| OS | Line Ending | Hex |
|----|-------------|-----|
| Windows | CRLF | `\r\n` (0x0D 0x0A) |
| Linux | LF | `\n` (0x0A) |
| macOS | LF | `\n` (0x0A) |

<!-- section_id: "5bf993b0-a876-47cc-886d-1e2cf1556359" -->
### Best Practices

1. **Configure Git**: `git config --global core.autocrlf true` (Windows)
2. **Use `.gitattributes`**: `* text=auto`
3. **Editors**: Set to use LF for cross-platform projects

---

<!-- section_id: "baed4368-4744-4910-83b3-3c30350030de" -->
## Case Sensitivity

| OS | Case Sensitive? |
|----|-----------------|
| Windows | ❌ No (`File.txt` = `file.txt`) |
| Linux | ✅ Yes (`File.txt` ≠ `file.txt`) |
| macOS | ❌ No (by default) |

<!-- section_id: "f18db56c-a5ad-4ac4-866d-adb310b16eea" -->
### Best Practices

1. **Always use lowercase** for file/folder names
2. **Never rely on case** to differentiate files
3. **Be consistent** with naming conventions

---

<!-- section_id: "44ae7205-9002-4ad7-876c-19499b749402" -->
## Permissions

<!-- section_id: "f039bc0d-6c5b-46b7-b63f-6933199c09eb" -->
### Windows vs Linux/macOS

| Concept | Windows | Linux/macOS |
|---------|---------|-------------|
| Execute bit | N/A | Required for scripts |
| File modes | ACLs | chmod (rwx) |
| Hidden files | Attribute | Dot prefix |

<!-- section_id: "6452dc7c-9bf2-4fec-b1df-8a62b2567502" -->
### Best Practices

1. **Scripts**: Add shebang `#!/bin/bash` and `chmod +x`
2. **Git**: Preserves execute bit across systems
3. **Hidden files**: Use dot prefix for Linux/macOS, not Windows hidden attribute

---

<!-- section_id: "4cff59e4-19c7-4e37-aafc-d753ade5fc4e" -->
## Symlinks

| OS | Support | Command |
|----|---------|---------|
| Windows | Limited (admin) | `mklink` |
| Linux | Full | `ln -s` |
| macOS | Full | `ln -s` |

<!-- section_id: "08ad26e1-890c-4596-8791-3a5678e51d06" -->
### Best Practices

1. **Avoid symlinks** in synced folders (Syncthing, Git)
2. **Use relative paths** if symlinks needed
3. **Document** any symlink requirements

---

<!-- section_id: "8c3e1b06-7438-45ed-9a31-e76b08f792d8" -->
## Shell Scripts

<!-- section_id: "39a3722e-6b9c-4fe3-819d-8d3a6affb16e" -->
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

<!-- section_id: "80b7b90e-8a0d-441e-80fa-ef01f9ffa0fb" -->
### Shebang Lines

```bash
#!/usr/bin/env bash    # GOOD - portable
#!/bin/bash            # OK - Linux/macOS
#!/bin/sh              # OK - POSIX only
```

---

<!-- section_id: "fd8a5727-fb6e-4c82-a4b4-19c7b38bf4a1" -->
## Environment Variables

| Variable | Windows | Linux | macOS |
|----------|---------|-------|-------|
| Home dir | `%USERPROFILE%` | `$HOME` | `$HOME` |
| Temp dir | `%TEMP%` | `/tmp` | `/tmp` |
| Path sep | `;` | `:` | `:` |

---

<!-- section_id: "5be21b21-d48f-4df3-b051-2dbeb5e25c5f" -->
## Git and Syncthing Considerations

<!-- section_id: "6aac0bbe-c0ae-4ccd-91d1-50be4c3758d1" -->
### Git

1. **`.gitattributes`**: Define line endings per file type
2. **`.gitignore`**: Include OS-specific ignores
3. **Filename issues**: Git will fail to checkout files with invalid names on Windows

<!-- section_id: "388f0e10-781b-4f26-b9b7-801737cc9d88" -->
### Syncthing

1. **Ignores**: Configure `.stignore` for OS-specific files
2. **Conflicts**: May occur if files differ only by case
3. **Symlinks**: May not sync properly

---

<!-- section_id: "21694434-68cd-43cd-996a-40a3d1ae5137" -->
## Checklist Before Creating Files/Folders

- [ ] No forbidden characters (`* ? < > : " | \ /`)
- [ ] No spaces (use `_` or `-`)
- [ ] All lowercase
- [ ] Path length under 200 characters
- [ ] No leading dots unless intentionally hidden
- [ ] No leading dashes

---

<!-- section_id: "5241f0f7-b97e-44e0-9652-2852e997a05f" -->
## Known Issues Log

| Date | Issue | Cause | Fix |
|------|-------|-------|-----|
| 2026-01-17 | Git pull fails on Windows | Filename contains `*` | Rename on Linux: `*` → `x` |

---

<!-- section_id: "b9c1654b-a6f4-44b8-971a-d59a8b2090d6" -->
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

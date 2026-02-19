# Cross-OS Compatibility Rules

**Layer**: 0 (Universal)
**Purpose**: Guidelines for creating files, folders, and code that work across Windows, Linux, and macOS
**Created**: 2026-01-17

---

## CRITICAL: File and Folder Naming

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

### Safe Naming Rules

1. **Use only**: `a-z`, `A-Z`, `0-9`, `_`, `-`, `.`
2. **Avoid spaces** - use `_` or `-` instead
3. **Avoid starting with** `.` (hidden on Linux/macOS)
4. **Avoid starting with** `-` (conflicts with CLI flags)
5. **Keep paths under 260 characters** (Windows limit)

### Examples

| Bad (Cross-OS Issues) | Good (Universal) |
|-----------------------|------------------|
| `layer_3_subx2_projects` | `layer_3_subx2_projects` |
| `file:name.txt` | `file_name.txt` |
| `what?.md` | `what.md` |
| `<config>.json` | `config.json` |
| `my file.txt` | `my_file.txt` |

---

## Path Handling

### Path Separators

| OS | Separator | Example |
|----|-----------|---------|
| Windows | `\` | `C:\Users\Dawson\file.txt` |
| Linux | `/` | `/home/dawson/file.txt` |
| macOS | `/` | `/Users/dawson/file.txt` |

### Best Practices

1. **In code**: Use language's path library (e.g., `os.path.join()`, `path.join()`)
2. **In configs**: Use forward slashes `/` (works on all OS in most contexts)
3. **In scripts**: Use variables like `$HOME` or `%USERPROFILE%`

---

## Line Endings

| OS | Line Ending | Hex |
|----|-------------|-----|
| Windows | CRLF | `\r\n` (0x0D 0x0A) |
| Linux | LF | `\n` (0x0A) |
| macOS | LF | `\n` (0x0A) |

### Best Practices

1. **Configure Git**: `git config --global core.autocrlf true` (Windows)
2. **Use `.gitattributes`**: `* text=auto`
3. **Editors**: Set to use LF for cross-platform projects

---

## Case Sensitivity

| OS | Case Sensitive? |
|----|-----------------|
| Windows | ❌ No (`File.txt` = `file.txt`) |
| Linux | ✅ Yes (`File.txt` ≠ `file.txt`) |
| macOS | ❌ No (by default) |

### Best Practices

1. **Always use lowercase** for file/folder names
2. **Never rely on case** to differentiate files
3. **Be consistent** with naming conventions

---

## Permissions

### Windows vs Linux/macOS

| Concept | Windows | Linux/macOS |
|---------|---------|-------------|
| Execute bit | N/A | Required for scripts |
| File modes | ACLs | chmod (rwx) |
| Hidden files | Attribute | Dot prefix |

### Best Practices

1. **Scripts**: Add shebang `#!/bin/bash` and `chmod +x`
2. **Git**: Preserves execute bit across systems
3. **Hidden files**: Use dot prefix for Linux/macOS, not Windows hidden attribute

---

## Symlinks

| OS | Support | Command |
|----|---------|---------|
| Windows | Limited (admin) | `mklink` |
| Linux | Full | `ln -s` |
| macOS | Full | `ln -s` |

### Best Practices

1. **Avoid symlinks** in synced folders (Syncthing, Git)
2. **Use relative paths** if symlinks needed
3. **Document** any symlink requirements

---

## Shell Scripts

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

### Shebang Lines

```bash
#!/usr/bin/env bash    # GOOD - portable
#!/bin/bash            # OK - Linux/macOS
#!/bin/sh              # OK - POSIX only
```

---

## Environment Variables

| Variable | Windows | Linux | macOS |
|----------|---------|-------|-------|
| Home dir | `%USERPROFILE%` | `$HOME` | `$HOME` |
| Temp dir | `%TEMP%` | `/tmp` | `/tmp` |
| Path sep | `;` | `:` | `:` |

---

## Git and Syncthing Considerations

### Git

1. **`.gitattributes`**: Define line endings per file type
2. **`.gitignore`**: Include OS-specific ignores
3. **Filename issues**: Git will fail to checkout files with invalid names on Windows

### Syncthing

1. **Ignores**: Configure `.stignore` for OS-specific files
2. **Conflicts**: May occur if files differ only by case
3. **Symlinks**: May not sync properly

---

## Checklist Before Creating Files/Folders

- [ ] No forbidden characters (`* ? < > : " | \ /`)
- [ ] No spaces (use `_` or `-`)
- [ ] All lowercase
- [ ] Path length under 200 characters
- [ ] No leading dots unless intentionally hidden
- [ ] No leading dashes

---

## Known Issues Log

| Date | Issue | Cause | Fix |
|------|-------|-------|-----|
| 2026-01-17 | Git pull fails on Windows | Filename contains `*` | Rename on Linux: `*` → `x` |

---

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

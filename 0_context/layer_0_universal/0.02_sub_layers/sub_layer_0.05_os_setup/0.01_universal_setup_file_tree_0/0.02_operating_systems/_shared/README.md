# Cross-OS Setup (_shared)

This directory contains setup documentation that applies across **all operating systems**.

## When to Use This Directory

Use this directory for:
- Setup steps that work identically on Linux, macOS, Windows, and WSL
- General configuration that doesn't depend on OS-specific tools
- Cross-platform tool setup (Node.js, Python, Git when using cross-platform patterns)
- Universal environment variables or configuration patterns

## When NOT to Use This Directory

Don't use this directory for:
- OS-specific package managers (apt, brew, winget)
- OS-specific paths or file structures
- OS-specific permissions or security models
- Platform-specific tools or dependencies

If setup varies by OS, place it in the specific OS directory instead.

## Next Level

Navigate to `0.03_environments/` to continue down the setup hierarchy.

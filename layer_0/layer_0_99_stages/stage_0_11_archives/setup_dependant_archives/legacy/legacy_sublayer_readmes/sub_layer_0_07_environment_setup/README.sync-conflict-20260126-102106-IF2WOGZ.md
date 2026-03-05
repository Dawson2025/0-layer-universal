---
resource_id: "cbe226f0-bb66-4c0c-945c-962310a1f66e"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-102106-IF2WOGZ"
---
# ⚠️ DEPRECATED - This Sublayer Has Been Consolidated

**Deprecation Date**: 2026-01-01
**Replaced By**: `sub_layer_0_05-0.014_setup`

This sublayer has been consolidated into the unified setup sublayer for better organization and discoverability.

## Migration Path

All setup documentation is now located in:
```
sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/
```

Navigate the file tree by your configuration:
1. Choose your OS: `0.05_operating_systems/<os>/`
2. Choose your environment: `0.06_environments/<env>/`
3. Choose your coding app: `0.07_coding_apps/<app>/`
4. Continue through all levels to find your specific setup documentation

## Why Consolidate?

- **Single entry point** for all setup docs
- **Better discoverability** through hierarchical file tree
- **Cross-cutting organization** with `_shared/` folders at every level
- **Easier maintenance** - one structure instead of 10

## Legacy Content Below

The original content of this sublayer is preserved below for reference, but should not be updated. All new setup documentation should go into the consolidated sublayer.

---

# Sub Layer 0.06: Environment Setup

**Purpose**: Environment-level setup that is not OS-specific and not tied to a single coding/AI application (e.g., Git/GitHub auth patterns, credentials, cross-app environment rules).

## Included Topics

- Git and GitHub authentication (PATs, SSO/SAML, credential storage patterns)
- Cross-tool environment conventions (paths, permissions, shells)

## Documentation

- **GitHub SSO (PAT) Setup**: `trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md`


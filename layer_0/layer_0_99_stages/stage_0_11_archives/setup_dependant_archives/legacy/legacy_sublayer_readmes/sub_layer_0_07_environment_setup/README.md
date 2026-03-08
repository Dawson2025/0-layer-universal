---
resource_id: "77ce3e40-a5d7-4aaa-8b8c-78c01996a1d2"
resource_type: "readme_document"
resource_name: "README"
---
# ⚠️ DEPRECATED - This Sublayer Has Been Consolidated

**Deprecation Date**: 2026-01-01
**Replaced By**: `sub_layer_0_05-0.014_setup`

This sublayer has been consolidated into the unified setup sublayer for better organization and discoverability.

<!-- section_id: "926beb89-f602-446d-90ba-a3f1ea43f71b" -->
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

<!-- section_id: "6205c780-dcc8-4b6a-b8a7-97566ee5e7b3" -->
## Why Consolidate?

- **Single entry point** for all setup docs
- **Better discoverability** through hierarchical file tree
- **Cross-cutting organization** with `_shared/` folders at every level
- **Easier maintenance** - one structure instead of 10

<!-- section_id: "caf90f26-10cf-4322-9d51-d59a4796d9c6" -->
## Legacy Content Below

The original content of this sublayer is preserved below for reference, but should not be updated. All new setup documentation should go into the consolidated sublayer.

---

# Sub Layer 0.06: Environment Setup

**Purpose**: Environment-level setup that is not OS-specific and not tied to a single coding/AI application (e.g., Git/GitHub auth patterns, credentials, cross-app environment rules).

<!-- section_id: "0d18c762-7370-4cdd-8d45-b86ce727d0ef" -->
## Included Topics

- Git and GitHub authentication (PATs, SSO/SAML, credential storage patterns)
- Cross-tool environment conventions (paths, permissions, shells)

<!-- section_id: "273504a4-cb6a-44a3-ba45-a018d311da8a" -->
## Documentation

- **GitHub SSO (PAT) Setup**: `trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md`


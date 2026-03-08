# Handoff: Fix agnostic-sync.sh Format Detection

**Date**: 2026-03-07
**Type**: Handoff (bug fix task for future agent)
**Entity**: layer_1_sub_feature_tool_and_app_agnostic
**Priority**: High -- this causes silent failures across the entire agnostic system

---

## Problem Summary

`agnostic-sync.sh` has a brittle format detection mechanism that causes silent failures. The script is responsible for generating ALL tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md) from 0AGNOSTIC.md. When format detection fails, generated files are wrong or empty, and no error is reported.

---

## Current Detection Logic (lines 44-48 of agnostic-sync.sh)

```bash
FORMAT="minimal"
if grep -q '^# ═══ STATIC CONTEXT' "$DIR/0AGNOSTIC.md"; then
    FORMAT="new"
elif grep -q '^## ' "$DIR/0AGNOSTIC.md"; then
    FORMAT="old"
fi
```

---

## Issues

### 1. Exact Unicode string matching
The detection relies on matching `═══` (Unicode box-drawing characters). A single typo, copy-paste loss, or editor encoding change breaks detection silently.

### 2. Silent fallthrough
If "new" format detection fails, the script silently falls through to "old" format with different AWK extraction logic, producing wrong output. There is no warning or error.

### 3. No change detection
The script always regenerates output even when nothing changed. There is no hash comparison (e.g., sha256sum) to skip unnecessary regeneration.

### 4. No output validation
After sync, the script does not verify that CLAUDE.md (or other tool files) was generated correctly. An empty or malformed output goes undetected.

### 5. Observed failure
In the agentic TTS / mobile agentic TTS entities, 0AGNOSTIC.md was correct but CLAUDE.md was not regenerated properly because format detection classified the file under the wrong format branch.

---

## Recommended Fix Direction

1. **Replace Unicode marker detection with semantic section detection** -- look for `## Identity`, `## Triggers`, `## Pointers`, `## Where to Contribute` instead of a brittle Unicode header string. These section headings are the actual structural contract of 0AGNOSTIC.md.

2. **Add hash-based change tracking** -- compute sha256sum of 0AGNOSTIC.md before sync. Compare against a stored hash (e.g., `.0agnostic/.sync-hash`). Skip regeneration if unchanged.

3. **Fail loudly if required sections are missing** -- if the script cannot find expected sections (`## Identity` at minimum), exit with a non-zero code and print an error. Never silently degrade.

4. **Add output validation after generation** -- after writing CLAUDE.md, verify it is non-empty and contains expected markers (e.g., the `## Identity` content from the source).

5. **Add a `--validate` flag** -- allow pre-sync validation without actually regenerating files. Useful for CI checks and manual debugging.

---

## Script Location

The production script lives at (relative to repo root):

```
.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh
```

Symlinks or copies may exist at entity roots as `agnostic-sync.sh` -- but the canonical source is the path above.

---

## Related Research

The trigger_pointer_system design work analyzed this issue in detail:

```
layer_1_group/layer_1_01_features/layer_1_feature_layer_stage_system/
  layer_1_group/layer_1_sub_features/layer_1_sub_feature_memory_system/
    layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/
      layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_trigger_pointer_system/
        layer_3_group/layer_3_99_stages/stage_3_04_design/outputs/
          operations_and_interface_design.md
```

Operation A5 (Resolve `{{resolve:UUID}}` placeholders) depends on agnostic-sync.sh working correctly. If format detection fails, placeholder resolution produces wrong output.

---

## Why This Belongs in tool_and_app_agnostic

agnostic-sync.sh is the core bridge between the agnostic system (0AGNOSTIC.md) and every tool-specific file. It is the single point of failure for cross-tool context delivery. Fixing it is squarely within this entity's scope: "Agnostic sync, merge system, tool-specific overrides, cross-tool compatibility."

---

## Acceptance Criteria

- [ ] Format detection no longer relies on Unicode marker strings
- [ ] Script fails loudly (non-zero exit, stderr message) when 0AGNOSTIC.md is unparseable
- [ ] Hash-based skip when nothing changed
- [ ] Output validation confirms generated files are non-empty and structurally correct
- [ ] `--validate` flag works for dry-run checks
- [ ] Existing entities that currently sync correctly continue to work (backward compatible)

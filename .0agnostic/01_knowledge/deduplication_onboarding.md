---
resource_id: "f7fd4d75-e4fd-477c-93bf-fb384e851903"
resource_type: "knowledge"
resource_name: "deduplication_onboarding"
---
# Deduplication Pattern Onboarding Guide

<!-- section_id: "22d87c7d-7076-4f6e-a0a0-1b7d6f9dc9dc" -->
## For New Team Members & Agents

This guide explains the **single-source-of-truth deduplication pattern** used throughout the codebase and how to maintain it.

---

<!-- section_id: "39406266-498f-4b4d-8b6f-0cbb6cf01734" -->
## Quick Start (3 minutes)

<!-- section_id: "2cafb101-0797-4426-a1fd-1a117e00f098" -->
### The Problem We Solved
- Same documentation existed in 10+ locations
- Updating one location meant manually updating all others
- Risk of inconsistency and drift

<!-- section_id: "34f626ab-7dad-4f4a-8108-17bdd5538e65" -->
### The Solution
- **Canonical** versions at root `.0agnostic/`
- **Pointer** files in research subdirectories link to canonical
- Update one place → automatically used everywhere

<!-- section_id: "43136607-e473-453f-921a-a4304e6a2820" -->
### Your Role
- **When editing**: Always edit the canonical file (at root)
- **When reading**: Follow pointers to canonical sources
- **When creating**: Check if documentation already exists before creating duplicates

---

<!-- section_id: "d1a0a43e-cc5d-43e2-b3f9-4f6dc2c0a41d" -->
## Understanding the Structure

<!-- section_id: "3f62e27e-8f91-45ac-84a9-58a76d93e1a6" -->
### Three-Tier System

```
┌─────────────────────────────────────────────────────────────┐
│ Tier 0: CANONICAL (Edit Here)                               │
│ Location: .0agnostic/01_knowledge/, .0agnostic/02_rules/    │
│ Content: Full, detailed, authoritative                       │
│ Examples: INSTANTIATION_GUIDE.md, LAYERS_EXPLAINED.md       │
└─────────────────────────────────────────────────────────────┘
                           ↑ Referenced by
┌─────────────────────────────────────────────────────────────┐
│ Tier 1: POINTERS (Don't Edit)                               │
│ Location: layer_-1_research/.../.0agnostic/                 │
│ Content: "Read canonical X.md" links only                    │
│ Purpose: Prevent duplication in research subdirectories      │
└─────────────────────────────────────────────────────────────┘
                           ↑ Referenced by
┌─────────────────────────────────────────────────────────────┐
│ Tier 2: CONCEPTUAL (High-Level Only)                        │
│ Location: README.md, overviews, summaries                    │
│ Content: 1-2 sentence summaries only                         │
│ Purpose: Quick understanding without full details            │
└─────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "a8b3cdb6-fc2f-42a2-bdf6-2d2976139da7" -->
## Common Scenarios

<!-- section_id: "33c5e647-af45-4ed5-bc82-7e4496799a82" -->
### Scenario 1: You Need to Update Documentation

**Question:** Where should I make the change?

**Answer:** Always edit the canonical version at root.

```
❌ DON'T:   Edit layer_-1_research/.../LAYERS_EXPLAINED.md
✓ DO:      Edit .0agnostic/01_knowledge/layer_stage_system/LAYERS_EXPLAINED.md
```

**Why:** The research file is a pointer. It automatically shows the latest canonical version.

---

<!-- section_id: "641ccd28-fe0a-46fe-80f0-76fa18c64799" -->
### Scenario 2: You Find Duplicate Documentation

**Question:** I found the same document in two places. What do I do?

**Answer:** Replace the research copy with a pointer to canonical.

**Steps:**
1. Confirm both files have similar content
2. Check if the root `.0agnostic/` version exists (canonical)
3. Replace the research version with a pointer file
4. Commit: `[AI Context] Replace duplicate [filename] with canonical pointer`

**Example:**
```bash
# Found duplicate:
# - .0agnostic/02_rules/context_scope_boundaries.md (canonical)
# - layer_3_subx3_feature_context_chain_system/.0agnostic/01_knowledge/.../context_scope_boundaries.md (duplicate)

# Replace the research file with:
# This file has been replaced with a pointer to the canonical source.
# [READ CANONICAL CONTEXT_SCOPE_BOUNDARIES.md](../../../../../../../.0agnostic/02_rules/context_scope_boundaries.md)
```

---

<!-- section_id: "5b026f14-f6bc-469d-bec9-6b995e3e9db4" -->
### Scenario 3: You're Reading Documentation

**Question:** I found a pointer file. How do I read the full content?

**Answer:** Click or follow the link to the canonical source.

```
Pointer file content:
═══════════════════════════════════════════════════════════
This file has been replaced with a pointer to the canonical source.

[READ CANONICAL LAYERS_EXPLAINED.md](.../.0agnostic/01_knowledge/layer_stage_system/LAYERS_EXPLAINED.md)
═══════════════════════════════════════════════════════════

→ Click this link to read the full content
```

---

<!-- section_id: "ce04c81a-da04-408e-b9a0-2dd93da6f4a0" -->
### Scenario 4: You're Creating New Documentation

**Question:** Should I create a new document or reference an existing one?

**Answer:** Check these locations first (in order):

1. `.0agnostic/01_knowledge/` — Universal knowledge
2. `.0agnostic/02_rules/` — Universal rules
3. `.0agnostic/03_protocols/` — Universal protocols
4. `.0agnostic/06_context_avenue_web/` — Skills and agent definitions

If it exists, use/reference it. If not, create it at the appropriate level.

---

<!-- section_id: "2931b173-8f76-4778-8a4f-cce09de7012e" -->
## Red Flags: When to Take Action

<!-- section_id: "0d7a6229-1ff5-42e3-a1de-9f44f78a9696" -->
### 🚩 Red Flag 1: You Find a Duplicate

**Scenario:** Same file name in both:
- Root `.0agnostic/`
- Research subdirectory

**Action:** Convert research copy to pointer (see Scenario 2)

---

<!-- section_id: "1321106c-2045-485c-b98a-cae2bce76f63" -->
### 🚩 Red Flag 2: You See Stale Information in a Pointer

**Scenario:** A pointer link seems outdated

**Action:** The pointer should always show current content. If it doesn't:
1. Check the canonical source (follow the link)
2. If canonical is outdated, update it
3. If pointer link is broken, fix the path

---

<!-- section_id: "dfcc7703-f907-43a6-816c-48171d63a29e" -->
### 🚩 Red Flag 3: A File Says "Inherits From" Another File

**Scenario:** You see text like "Inherits from: `.0agnostic/02_rules/...`"

**Status:** This is legacy pattern (pre-deduplication). If you see this:
1. Check if a canonical exists at root
2. If yes, convert to pointer format
3. Update the documentation to follow new pattern

---

<!-- section_id: "5c27bcb9-6179-471a-a7ba-d853ee691736" -->
### 🚩 Red Flag 4: Multiple Files with Same Name at Same Level

**Scenario:** Two different `.0agnostic/` directories at the same layer both have `my_rule.md`

**Problem:** This might be intentional (entity-specific) or accidental (duplicate)

**Action:**
- If entity-specific: Document why in file header
- If duplicate: Replace one with pointer to canonical
- If both are canonical (shouldn't happen): Consolidate to root

---

<!-- section_id: "7ff89185-492b-45c3-a890-dd7b3e7c8df5" -->
## Maintenance Checklist

Use this checklist when adding new content to keep the pattern intact:

- [ ] Is this documentation a duplicate of something at root `.0agnostic/`?
  - If YES: Use a pointer instead of copying
  - If NO: Continue below

- [ ] Is this entity-specific (only relevant to this sub-feature)?
  - If YES: OK to create locally
  - If NO: Should be at root `.0agnostic/`

- [ ] Will other entities need this documentation?
  - If YES: Create at root and pointer locally
  - If NO: OK to create locally

- [ ] Is this a rule, protocol, or knowledge that applies broadly?
  - If YES: Create at root `.0agnostic/`
  - If NO: Create locally

- [ ] Have I checked the naming convention?
  - [ ] Canonical: No prefix, full content
  - [ ] Pointer: Same name, redirect link

---

<!-- section_id: "047590f5-a473-4958-afb9-062806fe08fc" -->
## How to Calculate Pointer Paths

<!-- section_id: "270b0194-0ce8-4a92-9114-e32d861dff75" -->
### Quick Formula

**From:** `layer_-1_research/layer_0_group/layer_0_01_systems/layer_0_better_ai_system/layer_0_01_features/layer_0_feature_X/layer_1_group/layer_1_sub_features/layer_1_sub_feature_Y/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_Z/.0agnostic/02_rules/my_rule.md`

**To:** `.0agnostic/02_rules/my_rule.md`

**Path:** Count up to root, then down to target
```
../../../../../../../../../../../../../.0agnostic/02_rules/my_rule.md
 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑  ↑
 Go up to root         Navigate to .0agnostic/
```

<!-- section_id: "6ddd9233-84de-4045-b2a1-d2bf6337ac33" -->
### Tools
- **Manual:** Count directory levels, use `../` for each level
- **Git:** Use `git show` to see file paths
- **IDE:** Most editors show relative paths in breadcrumbs

<!-- section_id: "f28b810f-9700-406e-8072-80228dd01b4b" -->
### Verification
After creating a pointer:
1. Check the link in an editor
2. Verify it resolves to the canonical file
3. Test by reading the canonical content through the pointer

---

<!-- section_id: "671f090f-589f-41af-9edc-6a3aa661872e" -->
## Integration with Workflow

<!-- section_id: "13c037bf-26f4-4da3-b8ed-16874bdd4ee0" -->
### When Reviewing Code/Documentation

✓ **Good signs:**
- Canonical files at root are well-maintained
- Pointers in research are simple and clear
- No duplicate content in different locations

❌ **Warning signs:**
- Stale content in research that differs from canonical
- Multiple files with same name in different locations
- Pointer links that are broken or incomplete

<!-- section_id: "429783e9-a567-4604-8331-fd6fdc42e36c" -->
### When Committing

Use this commit message format for deduplication work:

```
[AI Context] Replace duplicate [filename] with canonical pointer

- Removed: [old location]
- Now points to: [canonical location]
- Lines saved: [number]
```

Example:
```
[AI Context] Replace duplicate context_scope_boundaries.md with canonical pointer

- Removed: layer_3_subx3_feature_context_chain_system/.0agnostic/01_knowledge/...
- Now points to: .0agnostic/02_rules/context_scope_boundaries.md
- Lines saved: 150
```

---

<!-- section_id: "d2a675fd-7692-4cf1-b56f-4ac28f70024d" -->
## Key Principles

<!-- section_id: "0276f656-0552-47d8-a772-a11e9616b4d0" -->
### 1. Single Source of Truth
One canonical location for each piece of documentation. No duplication.

<!-- section_id: "03ce56e9-bb29-4ad6-b629-4c8c2289ddc8" -->
### 2. Progressive Disclosure
- Pointers provide lightweight references
- Canonical provides full details
- Conceptual provides quick summaries

<!-- section_id: "1daee1a6-2f4c-425b-b823-ce5734d3528b" -->
### 3. Lazy Loading
Only load details when needed. Pointers let readers decide when to dive deep.

<!-- section_id: "787d990b-101d-4f43-a7a4-cc60715e9382" -->
### 4. Automatic Consistency
Update canonical once → all pointers automatically current. No manual syncing.

<!-- section_id: "fb25096f-64d5-4318-a9a5-8b9013d4f07b" -->
### 5. Entity Specificity
Entity-specific knowledge stays local. Universal knowledge goes to root `.0agnostic/`.

---

<!-- section_id: "cfdbcaf6-a532-47cd-9ee8-3ee7f09e3fdd" -->
## Troubleshooting

<!-- section_id: "723e622d-e0fe-4d50-b7e9-604c3c9ca336" -->
### Problem: Pointer link is broken

**Fix:** Recalculate the path using the quick formula above.

Example broken path:
```
../../../../../../.0agnostic/02_rules/file.md  ← Wrong: 6 levels
```

Correct path (for context_chain_system):
```
../../../../../../../../../../../.0agnostic/02_rules/file.md  ← Correct: 13 levels
```

---

<!-- section_id: "b7a0ca2b-f58b-469c-bb1a-acab8e839e2b" -->
### Problem: You see conflicting information

**Diagnosis:**
1. Is this in a pointer file? → Follow link to canonical
2. Is this in canonical? → This is the authoritative version
3. Is this in a local research file? → Check if it's entity-specific

**Action:** If canonical and local conflict, canonical wins. Update local if needed.

---

<!-- section_id: "6f9b5f93-36ff-43ee-8f8f-c93bea035e80" -->
### Problem: You're not sure if something should be canonical or local

**Decision tree:**
```
Is this used by multiple entities?
  ├─ YES → Canonical at root
  ├─ NO → Used by this entity only?
  │        ├─ YES → Local at entity
  │        ├─ NO → Where is the original?
  │               ├─ Root → Make it canonical
  │               ├─ Local → Consider promoting to root
```

---

<!-- section_id: "b27f89b3-fd2d-48f4-9eec-f72f81b3cd6c" -->
## Resources

- **Detailed rules:** `.0agnostic/01_knowledge/deduplication_pattern.md`
- **Project summary:** `.0agnostic/01_knowledge/deduplication_project_summary.md`
- **Canonical documents list:** See deduplication_pattern.md "Current Canonical Documents" section

---

<!-- section_id: "f3f0146c-a1fd-42a0-9afa-aef2e66826eb" -->
## Questions?

If something is unclear:
1. Check `deduplication_pattern.md` for detailed rules
2. Look at existing pointers to understand the format
3. Review recent commits with `[AI Context]` prefix to see examples

---

*Last Updated: 2026-02-28*
*Version: 1.0 (Post-Deduplication Implementation)*

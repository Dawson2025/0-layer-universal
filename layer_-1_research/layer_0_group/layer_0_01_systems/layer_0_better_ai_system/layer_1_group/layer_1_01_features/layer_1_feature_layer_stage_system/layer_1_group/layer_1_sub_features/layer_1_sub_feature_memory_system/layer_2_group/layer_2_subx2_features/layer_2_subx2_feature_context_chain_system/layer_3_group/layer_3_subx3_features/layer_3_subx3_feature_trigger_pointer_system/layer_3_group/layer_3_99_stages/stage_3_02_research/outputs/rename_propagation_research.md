---
resource_id: "235ffdcf-5946-447e-992d-c2d1abe67af8"
resource_type: "output"
resource_name: "rename_propagation_research"
---
# Research: Entity/Directory Rename Propagation in Pointer/Reference Systems

<!-- section_id: "2b4cd72a-ba33-4abf-857c-98c8f434bdfb" -->
## Executive Summary

When managing pointer files that reference entities by name in a hierarchical filesystem, **renames break all references** unless explicitly handled. This research evaluates 7 approaches for maintaining reference integrity during renames, examining real-world implementations from monorepo tools, documentation systems, package managers, and IDEs.

**Key Finding**: No single approach dominates all scenarios. The optimal solution depends on:
- **Scale**: Number of references and frequency of renames
- **Automation requirements**: Manual intervention vs. zero-touch
- **System maturity**: Prototyping vs. production
- **User expertise**: Technical users vs. broader audience

**Recommendation**: Implement a **hybrid approach** combining:
1. **Find-and-replace CLI** (immediate solution) for migration and manual corrections
2. **Git hook integration** (medium-term) for prevention and detection
3. **Stable IDs** (low overhead, high reliability) as the primary reference mechanism long-term

---

<!-- section_id: "c6499e62-ef0a-444f-ba74-e58eabd1af27" -->
## Context: Current System

**System**: `pointer-sync.sh` manages pointer files with YAML frontmatter:
```yaml
canonical_entity: "layer_1_feature_context_chain"
canonical_stage: "03_instructions"
canonical_subpath: "methodology/validation_rules.md"
```

**Current Behavior**:
- Moves (same name, new location): `find -type d -name "X"` resolves correctly
- Renames (name change): All pointers with `canonical_entity: "old_name"` become BROKEN

**Goal**: Enable renames without breaking the pointer network.

---

<!-- section_id: "363565db-50b1-4878-a22a-16dcc2f9ff7b" -->
## Approach 1: Find-and-Replace CLI Flag

<!-- section_id: "f3b6abe4-5e19-4204-8068-9e7285669d39" -->
### Description
Add a `--rename old new` flag to `pointer-sync.sh` that updates YAML frontmatter across all pointer files.

<!-- section_id: "a9096b21-1dbd-4dfb-8b63-95067281351f" -->
### Implementation (Bash)
```bash
if [[ "$1" == "--rename" ]]; then
    old_name="$2"
    new_name="$3"
    find . -type f -name "*.md" -exec grep -l "canonical_entity: ['\"]${old_name}['\"]" {} + |
    while read file; do
        sed -i "s/canonical_entity: ['\"]${old_name}['\"]/canonical_entity: \"${new_name}\"/" "$file"
        echo "Updated: $file"
    done
fi
```

<!-- section_id: "aac60620-fa6f-446e-9d79-eee16cd9da31" -->
### Real-World Examples
- **Sublime Text Package Control**: Uses `previous_names` array to map old-to-new package names automatically
- **PowerShell Registry Scripts**: Simple find-replace for bulk registry updates

<!-- section_id: "1bd58aaa-f57d-45e8-92f1-319edac0950a" -->
### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Low | ~30 lines of bash, grep + sed |
| Reliability | Medium | Catches YAML frontmatter references; misses comments/docs |
| UX | Good | Single command, immediate results |
| Edge Cases | Weak | Partial renames, typos leave system inconsistent |

**Strengths**: Immediate solution, no architectural changes, scriptable.
**Weaknesses**: No validation of rename success, user must remember to run, doesn't prevent future breaks.

**Verdict**: Implement as Phase 1 -- solves immediate pain, low risk.

---

<!-- section_id: "19490366-17e4-4a61-9d2e-5958dabce463" -->
## Approach 2: Stable IDs Instead of Names

<!-- section_id: "64ce5baa-f87a-4889-82b9-45bf5ced3d6d" -->
### Description
Replace `canonical_entity: "layer_1_feature_X"` with `canonical_entity_id: "550e8400-e29b-41d4-..."`. Store name-to-UUID mapping in entity metadata:

```yaml
# In entity's 0AGNOSTIC.md
entity_id: "550e8400-e29b-41d4-a957-446655440000"
entity_name: "layer_1_feature_context_chain"  # Can change freely
```

<!-- section_id: "43194bfd-f9db-43d7-b679-947eb7f15f8b" -->
### Implementation
```bash
# Generate UUID v5 (deterministic from path)
entity_path="/full/path/to/entity"
uuid=$(echo -n "$entity_path" | sha1sum | awk '{print $1}' |
       sed 's/\(........\)\(....\)\(....\)\(....\)\(............\)/\1-\2-\3-\4-\5/')
```

<!-- section_id: "fd5748a8-d8cd-4c6e-95e2-5d93ba247314" -->
### Real-World Examples
- **Git**: Content-addressable via SHA-1 hashes (objects never renamed, only referenced by hash)
- **Docker**: Image IDs (sha256 hashes) decouple from image tags
- **OSCAL (security standards)**: Uses UUIDs to namespace security objects across systems

<!-- section_id: "3223d1e3-f010-4774-8976-e233797ddfc1" -->
### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Medium | Requires UUID assignment + migration |
| Reliability | Excellent | Immune to renames by design |
| UX | Weak | Users must look up UUIDs, not human-friendly |
| Edge Cases | Strong | Handles all rename scenarios |

**Hybrid Optimization**: Keep both name (for humans) and ID (for machines):
```yaml
canonical_entity_id: "550e8400-e29b-41d4-a957-446655440000"
canonical_entity_name: "layer_1_feature_context_chain"  # Display name, not for resolution
```

**Verdict**: Implement as Phase 3 -- best long-term solution, requires migration planning.

---

<!-- section_id: "61dcecec-c3ec-4043-b4ab-d64268b842cb" -->
## Approach 3: Git Hook Integration

<!-- section_id: "2cd281bc-0816-4cb6-b764-97e44f4e06ae" -->
### Description
Use `pre-commit` hooks to detect renames via `git diff --diff-filter=R` and block commits until pointers are updated.

<!-- section_id: "36e910cb-3311-4f18-8697-283fc65f93b0" -->
### Implementation
```bash
#!/bin/bash
# .git/hooks/pre-commit
renames=$(git diff --cached --diff-filter=R --name-status HEAD | grep '/$')
if [[ -n "$renames" ]]; then
    echo "Directory rename detected:"
    echo "$renames"
    echo "Run: pointer-sync.sh --rename \"old\" \"new\""
    exit 1
fi
```

<!-- section_id: "dc6266d0-e031-432e-b6c7-defcbf78d0b6" -->
### Real-World Examples
- **Pre-commit Framework**: Python-based hooks with rename detection plugins
- **Git-annex**: Tracks symlink renames for content-addressed files

<!-- section_id: "6aa38781-1be1-4296-9c23-69138b83324a" -->
### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Low-Medium | ~40 lines of bash, uses native git |
| Reliability | Good | Catches most directory renames |
| UX | Fair | Blocks commits but guides user to fix |
| Edge Cases | Fair | Misses low-similarity renames (<50% file match) |

**Strengths**: Prevention over cure, zero-config for users, integrates with existing workflow.
**Weaknesses**: Git doesn't natively detect directory renames (infers from file patterns), can be bypassed with `--no-verify`.

**Verdict**: Implement as Phase 2 -- excellent safety net, complements CLI flag.

---

<!-- section_id: "1b14bc83-50fd-4c94-8695-e271170af559" -->
## Approach 4: Symlink/Alias Transition

<!-- section_id: "0cae9c6e-5d10-46cd-8eb7-33636014639b" -->
### Description
When renaming, create a symlink `old_name -> new_name` as a temporary bridge while gradually migrating pointers.

```bash
mv layer_1_feature_old layer_1_feature_new
ln -s layer_1_feature_new layer_1_feature_old
```

<!-- section_id: "fab72856-1ea4-4c9d-9353-476fe7da3602" -->
### Real-World Examples
- **npm**: Deprecates old package names but keeps them installable (mapping to new)
- **Linux alternatives system**: Symlinks allow multiple tool versions to coexist

<!-- section_id: "8d053e2b-e3b1-4633-a720-88147a179756" -->
### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Very Low | Single `ln -s` command |
| Reliability | Medium | Works until symlink removed |
| UX | Good | Zero disruption during transition |
| Edge Cases | Weak | Symlink loops, confusing dual paths, git tracking issues |

**Verdict**: Use sparingly -- good for urgent renames during active development, not a permanent solution.

---

<!-- section_id: "adaa8057-4f66-4734-9964-b81d7b314c04" -->
## Approach 5: Registry/Manifest File

<!-- section_id: "343a52e8-1ee7-4110-b616-2b6a34fb2ee8" -->
### Description
Maintain a central `entity-registry.json` mapping entity IDs/names to current filesystem paths:

```json
{
  "entities": [
    {
      "id": "550e8400-...",
      "name": "layer_1_feature_context_chain",
      "current_path": "/path/to/entity",
      "previous_names": ["layer_1_feature_old_name"]
    }
  ]
}
```

<!-- section_id: "bdb77cd2-7101-407f-a41f-68381ade4ebb" -->
### Real-World Examples
- **Bazel MODULE.bazel**: Central registry of dependencies with names-to-URLs
- **Docker Manifest Lists**: Maps image names to registry locations
- **ESP-IDF idf_component.yml**: Component registry with paths and exclusions

<!-- section_id: "3a310b07-b4a9-4a4f-a47e-efa52ca5a084" -->
### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | High | Requires registry CRUD + sync logic |
| Reliability | Excellent | Single source of truth |
| UX | Fair | Hidden from users, but must be maintained |
| Edge Cases | Strong | Handles renames, moves, aliases, history |

**Verdict**: Defer to Phase 4+ -- best for mature systems (100+ entities); premature at current scale.

---

<!-- section_id: "bec6b365-0123-4bd9-9337-da7425ed7c34" -->
## Approach 6: Content-Addressable References

<!-- section_id: "a958c60b-c920-4c98-b8b2-1aef7189f3c7" -->
### Description
Reference entities by hash of their canonical content (like Git objects). Renames don't affect references because identity is tied to content, not name/path.

<!-- section_id: "ef3fb653-b751-46e3-9349-c86cf9d1d666" -->
### Real-World Examples
- **Git**: All objects referenced by SHA-1
- **IPFS**: Files addressed by content hash (CID)
- **Docker**: Layers identified by sha256

<!-- section_id: "d3b37db2-65bb-4dd1-b29e-1abeb545d18b" -->
### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Very High | Requires hash computation + index |
| Reliability | Perfect | Immune to all renames/moves |
| UX | Poor | Hashes are opaque to humans |
| Edge Cases | Weak | Every content change = new hash (references break) |

**Verdict**: Not recommended -- CAS is for immutable content (Git commits, Docker layers), not evolving entities whose content changes regularly.

---

<!-- section_id: "138f0b2a-8e1e-475f-9ef2-8657fe2143ba" -->
## Approach 7: IDE-Style Rename Refactoring

<!-- section_id: "07b47f0a-0395-4cd2-b66c-d613ce6365d8" -->
### Description
Build a tool that mimics IDE refactoring: parse all pointer files, find references, update atomically with preview.

<!-- section_id: "b1382a12-1c62-459d-a576-dc76a4769038" -->
### Real-World Examples
- **IntelliJ IDEA**: Rename class updates all imports, references, filenames atomically
- **VSCode + LSP**: F2 rename propagates via `textDocument/rename`
- **OpenRewrite**: Automated recipe system for package renames (e.g., `javax -> jakarta`)

<!-- section_id: "775287dd-c099-485e-80bf-c07bd86c6bdc" -->
### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Very High | Full parser, indexer, transaction system |
| Reliability | Excellent | Atomic, validated updates |
| UX | Excellent | Preview, undo, guided workflow |
| Edge Cases | Excellent | Handles conflicts, scope limits |

**Verdict**: Not practical for bash tooling -- inspiring design but requires full IDE/language-server architecture.

---

<!-- section_id: "d86e0956-e12a-410f-8832-6dd4f7ea52c5" -->
## Comparative Analysis

<!-- section_id: "57fbe685-9c72-4dfd-ae6a-9ddbe049190b" -->
### Decision Matrix by System Scale

| Scale | Recommended Approach | Rationale |
|-------|---------------------|-----------|
| Small (1-10 entities, rare renames) | CLI Flag + Symlinks | Manual intervention acceptable |
| Medium (10-100 entities, occasional renames) | CLI Flag + Git Hooks + Stable IDs | Balanced automation |
| Large (100+ entities, frequent renames) | Stable IDs + Registry | Architecture investment pays off |
| Enterprise (1000+ entities, distributed teams) | IDE-style Refactor | Requires dedicated tooling team |

---

<!-- section_id: "59637279-5a45-42b4-bb63-6368c5ccf8bc" -->
## Failure Modes & Edge Cases

<!-- section_id: "36ea5fb1-40b4-441f-a357-29f4414d672e" -->
### Common Pitfalls

1. **Incomplete Propagation**: Rename tool misses references in comments/documentation. Mitigation: broad grep search + manual review.
2. **Name Collision**: `new_name` already exists. Mitigation: pre-check for conflicts.
3. **Partial Rename Success**: Filesystem rename succeeds but pointer updates fail mid-operation. Mitigation: update pointers first, verify, then rename filesystem.
4. **Transitive Renames**: A->B then B->C leaves intermediate state. Mitigation: registry with `previous_names` tracks full history.

<!-- section_id: "9dc6e154-b825-4539-bed2-b6eeb6fbd411" -->
### Layer-Stage Specific Edge Cases

1. **Stage Renames**: Stage numbers (01-11) provide implicit stable IDs -- stage names rarely change.
2. **Cross-Layer Pointers**: Layer 0 renames affect multiple layer 1 projects -- layer 0 should use stable IDs first.
3. **Subpath Renames**: File-level renames within entity not tracked by entity rename tool -- need separate file-rename detection.

---

<!-- section_id: "d7fa8ce5-e4d9-49ac-8a2c-613ab4ad6d28" -->
## Recommendations

<!-- section_id: "288bf5d4-030e-47d7-ba4f-82bcd117cda4" -->
### Phase 1: Immediate
**Implement CLI Flag (Approach 1)**

Add `--rename old_name new_name` flag to `pointer-sync.sh`. Supports `--dry-run` preview. Handles `canonical_entity`, `canonical_stage`, and `canonical_subpath` fields.

Effort: 2-4 hours. Risk: Low.

<!-- section_id: "f3e96e1e-be8b-4c46-a14f-266eeab38aad" -->
### Phase 2: Near-Term
**Add Git Hook Prevention (Approach 3)**

Pre-commit hook detecting directory renames. Blocks commit with user-friendly fix instructions.

Effort: 4-6 hours. Risk: Low.

<!-- section_id: "fba4515b-a343-484b-9088-2a3a0d7d541e" -->
### Phase 3: Mid-Term
**Migrate to Stable IDs (Approach 2)**

Generate UUIDs for all entities. Update pointer-sync.sh to resolve by ID (primary) with name fallback (legacy). Gradual migration with deprecation warnings.

Effort: 2-3 days. Risk: Medium (migration required).

<!-- section_id: "0201309a-49bc-41df-8512-fc04c5c86860" -->
### Phase 4: Future (If Needed)
**Registry System (Approach 5)** -- only if entity count exceeds 100, multiple tools need entity metadata, or audit trail requirements emerge.

---

<!-- section_id: "c7cc0c4a-cd95-4b66-9f8f-b5a86288f6f2" -->
## Sources

<!-- section_id: "50ee7400-84b6-48f8-bbfe-fbfa4b68604d" -->
### Monorepo Tools & Build Systems
- [Nx Managing TypeScript Packages in Monorepos](https://nx.dev/blog/managing-ts-packages-in-monorepos)
- [Bazel Style Guide](https://bazel.build/build/style-guide)
- [IntelliJ Bazel Plugin Issue #6211: Rename Refactoring](https://github.com/bazelbuild/intellij/issues/6211)

<!-- section_id: "d0541c55-3b38-47a4-9387-6241fd040462" -->
### Documentation Systems
- [Sphinx Cross-Referencing Guide](https://docs.readthedocs.com/platform/latest/guides/cross-referencing-with-sphinx.html)
- [MkDocs Writing Documentation](https://www.mkdocs.org/user-guide/writing-your-docs/)

<!-- section_id: "5c36f9f2-786f-4cfe-a221-ecf5866443e8" -->
### Package Managers
- [Sublime Text Package Control: Renaming](https://docs.sublimetext.io/guide/package-control/renaming.html)
- [npm: Deprecating Packages](https://docs.npmjs.com/deprecating-and-undeprecating-packages-or-package-versions/)
- [OpenRewrite ChangePackage Recipe](https://docs.openrewrite.org/recipes/java/changepackage)

<!-- section_id: "9531aa75-8971-4925-8eba-9b462cf6669f" -->
### Stable IDs & Content Addressing
- [IETF UUID Draft (RFC 4122bis)](https://www.ietf.org/archive/id/draft-ietf-uuidrev-rfc4122bis-10.html)
- [NIST OSCAL: Identifier Use](https://pages.nist.gov/OSCAL/learn/concepts/identifier-use/)

<!-- section_id: "ea4d0822-4e95-4a56-a38c-fe77cc70beff" -->
### Git Hooks & Rename Detection
- [Git Documentation: Hooks](https://git-scm.com/docs/githooks)
- [Git Diff Documentation](https://git-scm.com/docs/git-diff)

<!-- section_id: "16693b27-855b-4083-88fe-bb22ba26b1b8" -->
### IDE Refactoring
- [JetBrains: Rename Refactoring](https://www.jetbrains.com/help/idea/rename-refactorings.html)
- [VSCode: Java Refactoring](https://code.visualstudio.com/docs/java/java-refactoring)

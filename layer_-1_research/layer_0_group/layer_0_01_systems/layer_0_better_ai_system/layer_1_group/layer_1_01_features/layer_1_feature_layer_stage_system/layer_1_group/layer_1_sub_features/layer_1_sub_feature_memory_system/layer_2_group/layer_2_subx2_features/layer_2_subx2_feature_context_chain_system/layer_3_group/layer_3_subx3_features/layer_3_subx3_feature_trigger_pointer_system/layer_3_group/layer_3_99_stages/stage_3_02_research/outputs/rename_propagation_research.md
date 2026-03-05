---
resource_id: "235ffdcf-5946-447e-992d-c2d1abe67af8"
resource_type: "output"
resource_name: "rename_propagation_research"
---
# Research: Entity/Directory Rename Propagation in Pointer/Reference Systems

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

## Approach 1: Find-and-Replace CLI Flag

### Description
Add a `--rename old new` flag to `pointer-sync.sh` that updates YAML frontmatter across all pointer files.

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

### Real-World Examples
- **Sublime Text Package Control**: Uses `previous_names` array to map old-to-new package names automatically
- **PowerShell Registry Scripts**: Simple find-replace for bulk registry updates

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

## Approach 2: Stable IDs Instead of Names

### Description
Replace `canonical_entity: "layer_1_feature_X"` with `canonical_entity_id: "550e8400-e29b-41d4-..."`. Store name-to-UUID mapping in entity metadata:

```yaml
# In entity's 0AGNOSTIC.md
entity_id: "550e8400-e29b-41d4-a957-446655440000"
entity_name: "layer_1_feature_context_chain"  # Can change freely
```

### Implementation
```bash
# Generate UUID v5 (deterministic from path)
entity_path="/full/path/to/entity"
uuid=$(echo -n "$entity_path" | sha1sum | awk '{print $1}' |
       sed 's/\(........\)\(....\)\(....\)\(....\)\(............\)/\1-\2-\3-\4-\5/')
```

### Real-World Examples
- **Git**: Content-addressable via SHA-1 hashes (objects never renamed, only referenced by hash)
- **Docker**: Image IDs (sha256 hashes) decouple from image tags
- **OSCAL (security standards)**: Uses UUIDs to namespace security objects across systems

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

## Approach 3: Git Hook Integration

### Description
Use `pre-commit` hooks to detect renames via `git diff --diff-filter=R` and block commits until pointers are updated.

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

### Real-World Examples
- **Pre-commit Framework**: Python-based hooks with rename detection plugins
- **Git-annex**: Tracks symlink renames for content-addressed files

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

## Approach 4: Symlink/Alias Transition

### Description
When renaming, create a symlink `old_name -> new_name` as a temporary bridge while gradually migrating pointers.

```bash
mv layer_1_feature_old layer_1_feature_new
ln -s layer_1_feature_new layer_1_feature_old
```

### Real-World Examples
- **npm**: Deprecates old package names but keeps them installable (mapping to new)
- **Linux alternatives system**: Symlinks allow multiple tool versions to coexist

### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Very Low | Single `ln -s` command |
| Reliability | Medium | Works until symlink removed |
| UX | Good | Zero disruption during transition |
| Edge Cases | Weak | Symlink loops, confusing dual paths, git tracking issues |

**Verdict**: Use sparingly -- good for urgent renames during active development, not a permanent solution.

---

## Approach 5: Registry/Manifest File

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

### Real-World Examples
- **Bazel MODULE.bazel**: Central registry of dependencies with names-to-URLs
- **Docker Manifest Lists**: Maps image names to registry locations
- **ESP-IDF idf_component.yml**: Component registry with paths and exclusions

### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | High | Requires registry CRUD + sync logic |
| Reliability | Excellent | Single source of truth |
| UX | Fair | Hidden from users, but must be maintained |
| Edge Cases | Strong | Handles renames, moves, aliases, history |

**Verdict**: Defer to Phase 4+ -- best for mature systems (100+ entities); premature at current scale.

---

## Approach 6: Content-Addressable References

### Description
Reference entities by hash of their canonical content (like Git objects). Renames don't affect references because identity is tied to content, not name/path.

### Real-World Examples
- **Git**: All objects referenced by SHA-1
- **IPFS**: Files addressed by content hash (CID)
- **Docker**: Layers identified by sha256

### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Very High | Requires hash computation + index |
| Reliability | Perfect | Immune to all renames/moves |
| UX | Poor | Hashes are opaque to humans |
| Edge Cases | Weak | Every content change = new hash (references break) |

**Verdict**: Not recommended -- CAS is for immutable content (Git commits, Docker layers), not evolving entities whose content changes regularly.

---

## Approach 7: IDE-Style Rename Refactoring

### Description
Build a tool that mimics IDE refactoring: parse all pointer files, find references, update atomically with preview.

### Real-World Examples
- **IntelliJ IDEA**: Rename class updates all imports, references, filenames atomically
- **VSCode + LSP**: F2 rename propagates via `textDocument/rename`
- **OpenRewrite**: Automated recipe system for package renames (e.g., `javax -> jakarta`)

### Evaluation

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Complexity | Very High | Full parser, indexer, transaction system |
| Reliability | Excellent | Atomic, validated updates |
| UX | Excellent | Preview, undo, guided workflow |
| Edge Cases | Excellent | Handles conflicts, scope limits |

**Verdict**: Not practical for bash tooling -- inspiring design but requires full IDE/language-server architecture.

---

## Comparative Analysis

### Decision Matrix by System Scale

| Scale | Recommended Approach | Rationale |
|-------|---------------------|-----------|
| Small (1-10 entities, rare renames) | CLI Flag + Symlinks | Manual intervention acceptable |
| Medium (10-100 entities, occasional renames) | CLI Flag + Git Hooks + Stable IDs | Balanced automation |
| Large (100+ entities, frequent renames) | Stable IDs + Registry | Architecture investment pays off |
| Enterprise (1000+ entities, distributed teams) | IDE-style Refactor | Requires dedicated tooling team |

---

## Failure Modes & Edge Cases

### Common Pitfalls

1. **Incomplete Propagation**: Rename tool misses references in comments/documentation. Mitigation: broad grep search + manual review.
2. **Name Collision**: `new_name` already exists. Mitigation: pre-check for conflicts.
3. **Partial Rename Success**: Filesystem rename succeeds but pointer updates fail mid-operation. Mitigation: update pointers first, verify, then rename filesystem.
4. **Transitive Renames**: A->B then B->C leaves intermediate state. Mitigation: registry with `previous_names` tracks full history.

### Layer-Stage Specific Edge Cases

1. **Stage Renames**: Stage numbers (01-11) provide implicit stable IDs -- stage names rarely change.
2. **Cross-Layer Pointers**: Layer 0 renames affect multiple layer 1 projects -- layer 0 should use stable IDs first.
3. **Subpath Renames**: File-level renames within entity not tracked by entity rename tool -- need separate file-rename detection.

---

## Recommendations

### Phase 1: Immediate
**Implement CLI Flag (Approach 1)**

Add `--rename old_name new_name` flag to `pointer-sync.sh`. Supports `--dry-run` preview. Handles `canonical_entity`, `canonical_stage`, and `canonical_subpath` fields.

Effort: 2-4 hours. Risk: Low.

### Phase 2: Near-Term
**Add Git Hook Prevention (Approach 3)**

Pre-commit hook detecting directory renames. Blocks commit with user-friendly fix instructions.

Effort: 4-6 hours. Risk: Low.

### Phase 3: Mid-Term
**Migrate to Stable IDs (Approach 2)**

Generate UUIDs for all entities. Update pointer-sync.sh to resolve by ID (primary) with name fallback (legacy). Gradual migration with deprecation warnings.

Effort: 2-3 days. Risk: Medium (migration required).

### Phase 4: Future (If Needed)
**Registry System (Approach 5)** -- only if entity count exceeds 100, multiple tools need entity metadata, or audit trail requirements emerge.

---

## Sources

### Monorepo Tools & Build Systems
- [Nx Managing TypeScript Packages in Monorepos](https://nx.dev/blog/managing-ts-packages-in-monorepos)
- [Bazel Style Guide](https://bazel.build/build/style-guide)
- [IntelliJ Bazel Plugin Issue #6211: Rename Refactoring](https://github.com/bazelbuild/intellij/issues/6211)

### Documentation Systems
- [Sphinx Cross-Referencing Guide](https://docs.readthedocs.com/platform/latest/guides/cross-referencing-with-sphinx.html)
- [MkDocs Writing Documentation](https://www.mkdocs.org/user-guide/writing-your-docs/)

### Package Managers
- [Sublime Text Package Control: Renaming](https://docs.sublimetext.io/guide/package-control/renaming.html)
- [npm: Deprecating Packages](https://docs.npmjs.com/deprecating-and-undeprecating-packages-or-package-versions/)
- [OpenRewrite ChangePackage Recipe](https://docs.openrewrite.org/recipes/java/changepackage)

### Stable IDs & Content Addressing
- [IETF UUID Draft (RFC 4122bis)](https://www.ietf.org/archive/id/draft-ietf-uuidrev-rfc4122bis-10.html)
- [NIST OSCAL: Identifier Use](https://pages.nist.gov/OSCAL/learn/concepts/identifier-use/)

### Git Hooks & Rename Detection
- [Git Documentation: Hooks](https://git-scm.com/docs/githooks)
- [Git Diff Documentation](https://git-scm.com/docs/git-diff)

### IDE Refactoring
- [JetBrains: Rename Refactoring](https://www.jetbrains.com/help/idea/rename-refactorings.html)
- [VSCode: Java Refactoring](https://code.visualstudio.com/docs/java/java-refactoring)

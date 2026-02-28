# Skill: Avenue Check

## Purpose

Check that all 8 context delivery avenues are functional for a given entity, reporting per-avenue status and overall coverage percentage.

## When to Use

- After creating a new entity to verify context is discoverable
- After modifying context files (0AGNOSTIC.md, CLAUDE.md, rules, skills)
- During periodic audits of the context chain system
- When debugging why an agent cannot find expected context

## When NOT to Use

- For validating the parent chain only (use `/chain-validate` instead)
- For creating missing structure (use `/entity-creation` instead)
- For general context discovery (use `/context-gathering` instead)

## Protocol

### 1. Check System Prompt Avenue

Verify `CLAUDE.md` exists in the entity root and contains an `## Identity` section.

- **PASS**: File exists with Identity section
- **SCAFFOLDED**: File exists but is a placeholder (< 5 lines of content)
- **FAIL**: File does not exist

### 2. Check Path Rules Avenue

Verify `.claude/rules/` directory contains at least one `.md` rule file.

- **PASS**: Directory has 1+ rule files with substantive content (> 5 lines)
- **SCAFFOLDED**: Directory exists but is empty or files are placeholders
- **FAIL**: Directory does not exist

### 3. Check Skills Avenue

Verify `.0agnostic/skills/` or `.claude/skills/` contains at least one skill with a `SKILL.md`.

- **PASS**: 1+ skill directories with SKILL.md files
- **SCAFFOLDED**: Skill directories exist but SKILL.md files are empty
- **FAIL**: No skill directories found

### 4. Check Parent References Avenue

Verify `0AGNOSTIC.md` exists and has a `## Parent` line that resolves to an existing file.

- **PASS**: Parent path resolves to existing 0AGNOSTIC.md
- **SCAFFOLDED**: 0AGNOSTIC.md exists but Parent path is missing or empty
- **FAIL**: 0AGNOSTIC.md does not exist

### 5. Check JSON-LD Avenue

Verify at least one `.gab.jsonld` file exists and contains an `@graph` array.

- **PASS**: File exists with valid @graph
- **SCAFFOLDED**: File exists but @graph is empty
- **FAIL**: No .gab.jsonld files found

### 6. Check Integration Avenue

Verify at least one `.integration.md` file exists with substantive content (> 5 lines).

- **PASS**: File exists with > 5 lines
- **SCAFFOLDED**: File exists but is a stub
- **FAIL**: No .integration.md files found

### 7. Check Episodic Memory Avenue

Verify `.0agnostic/episodic_memory/` directory exists.

- **PASS**: Directory exists with index.md
- **SCAFFOLDED**: Directory exists but index.md is missing or empty
- **FAIL**: Directory does not exist

### 8. Check Agnostic System Avenue

Verify `.0agnostic/` contains `rules/` or `skills/` with content.

- **PASS**: Has rules/ or skills/ with substantive files
- **SCAFFOLDED**: Directories exist but are empty
- **FAIL**: .0agnostic/ does not exist

### 9. Report Results

```
Avenue Coverage Report
======================
Entity: layer_3_subx3_feature_context_chain_system

  1. System Prompt (CLAUDE.md)        [PASS]
  2. Path Rules (.claude/rules/)      [PASS]
  3. Skills (.0agnostic/skills/)      [PASS]
  4. Parent References (0AGNOSTIC.md) [PASS]
  5. JSON-LD Agent Defs (.gab.jsonld) [SCAFFOLDED]
  6. Integration (.integration.md)    [SCAFFOLDED]
  7. Episodic Memory                  [PASS]
  8. Agnostic System (.0agnostic/)    [PASS]

Coverage: 6/8 PASS, 2/8 SCAFFOLDED, 0/8 FAIL
Overall:  75% functional (100% reachable)
```

## Checklist

- [ ] All 8 avenues checked
- [ ] Each avenue rated PASS / SCAFFOLDED / FAIL
- [ ] Coverage percentage calculated
- [ ] Remediation actions listed for any FAIL results

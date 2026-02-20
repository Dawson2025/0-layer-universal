#!/usr/bin/env bash
# validate-entity.sh — Check entity completeness against canonical structure
# Usage: bash .0agnostic/01_knowledge/layer_stage_system/resources/tools/validate-entity.sh <entity-path>
# Reference: @imports/entity_structure.md

set -uo pipefail
# NOTE: Do NOT use set -e — check functions intentionally trigger failures

ENTITY="${1:?Usage: validate-entity.sh <entity-path>}"
ENTITY="${ENTITY%/}" # Strip trailing slash

PASS=0
FAIL=0
WARN=0

pass() { ((PASS++)) || true; echo "  PASS  $1"; }
fail() { ((FAIL++)) || true; echo "  FAIL  $1"; }
warn() { ((WARN++)) || true; echo "  WARN  $1"; }

check_dir()  { if [ -d "$ENTITY/$1" ]; then pass "$1"; else fail "$1 (directory missing)"; fi; }
check_file() { if [ -f "$ENTITY/$1" ]; then pass "$1"; else fail "$1 (file missing)"; fi; }

echo "=== Entity Validation: $(basename "$ENTITY") ==="
echo "Path: $ENTITY"
echo ""

# --- Entity Root Files ---
echo "--- Root Files ---"
check_file "0AGNOSTIC.md"
check_file "CLAUDE.md"
check_file "AGENTS.md"
check_file "GEMINI.md"
check_file "OPENAI.md"

# Optional but expected
[ -f "$ENTITY/0INDEX.md" ]  && pass "0INDEX.md"  || warn "0INDEX.md (recommended)"
[ -f "$ENTITY/README.md" ]  && pass "README.md"  || warn "README.md (recommended)"

echo ""

# --- Orchestrator ---
echo "--- Entity Orchestrator ---"
# Find the orchestrator .gab.jsonld at entity root
orch_count=$(find "$ENTITY" -maxdepth 1 -name "*.gab.jsonld" -type f 2>/dev/null | wc -l)
if [ "$orch_count" -gt 0 ]; then
  pass "Entity orchestrator .gab.jsonld found"
  # Check matching .integration.md
  for f in "$ENTITY"/*.gab.jsonld; do
    base="${f%.gab.jsonld}"
    if [ -f "${base}.integration.md" ]; then
      pass "$(basename "${base}.integration.md")"
    else
      fail "$(basename "${base}.integration.md") (missing — run jsonld-to-md.sh)"
    fi
  done
else
  fail "No .gab.jsonld orchestrator at entity root"
fi

echo ""

# --- Config Directories ---
echo "--- Config Directories (Entity Root) ---"

# .0agnostic (numbered subdirectories)
check_dir ".0agnostic"
check_dir ".0agnostic/01_knowledge"
check_dir ".0agnostic/02_rules"
check_dir ".0agnostic/02_rules/static"
check_dir ".0agnostic/02_rules/dynamic"
check_dir ".0agnostic/03_protocols"
check_dir ".0agnostic/04_episodic_memory/sessions"
check_dir ".0agnostic/04_episodic_memory/changes"
check_dir ".0agnostic/05_handoff_documents"
check_dir ".0agnostic/06_context_avenue_web/05_skills"
check_dir ".0agnostic/06_context_avenue_web/06_agents"
check_dir ".0agnostic/06_context_avenue_web/08_hooks/scripts"
check_dir ".0agnostic/07+_setup_dependant"

# Warn about unnumbered .0agnostic/ dirs (old pattern)
for old_dir in knowledge rules agents skills hooks episodic_memory protocols; do
  if [ -d "$ENTITY/.0agnostic/$old_dir" ]; then
    warn ".0agnostic/$old_dir/ still uses unnumbered name (run migrate-sub-layers-to-0agnostic.sh)"
  fi
done

# Warn about old numbering convention dirs
for old_dir in 04_agents 05_skills "06_hooks" "07_episodic_memory" "08_episodic_memory" "04+_setup_dependant"; do
  if [ -d "$ENTITY/.0agnostic/$old_dir" ]; then
    warn ".0agnostic/$old_dir/ uses old numbering convention (run migrate-sub-layers-to-0agnostic.sh)"
  fi
done

# .1merge (6 tools × 3 tiers)
TOOLS=(.1claude_merge .1cursor_merge .1gemini_merge .1aider_merge .1codex_merge .1copilot_merge)
TIERS=(0_synced 1_overrides 2_additions)
for tool in "${TOOLS[@]}"; do
  for tier in "${TIERS[@]}"; do
    check_dir ".1merge/$tool/$tier"
  done
done

# Tool directories with episodic_memory
check_dir ".claude/rules"
check_dir ".claude/episodic_memory/sessions"
check_dir ".claude/episodic_memory/changes"
check_dir ".cursor/rules"
check_dir ".cursor/episodic_memory/sessions"
check_dir ".cursor/episodic_memory/changes"
check_dir ".gemini/episodic_memory/sessions"
check_dir ".gemini/episodic_memory/changes"
check_dir ".codex/episodic_memory/sessions"
check_dir ".codex/episodic_memory/changes"
check_dir ".github/instructions"

# outputs and synthesis
check_dir "outputs/episodic_memory/sessions"
check_dir "outputs/episodic_memory/changes"
check_dir "synthesis"

echo ""

# --- Internal layer_N_group ---
echo "--- Internal Structure (layer_N_group/) ---"

# Find the layer_N_group directory
group_dir=$(find "$ENTITY" -maxdepth 1 -type d -name "layer_*_group" 2>/dev/null | head -1)
if [ -n "$group_dir" ]; then
  group_name=$(basename "$group_dir")
  pass "$group_name/ exists"

  # Check _group suffix convention
  bare_dir=$(echo "$group_name" | sed 's/_group$//')
  if [ -d "$ENTITY/$bare_dir" ] && [ "$bare_dir" != "$group_name" ]; then
    fail "Both $bare_dir/ and ${group_name}/ exist — remove the bare one"
  fi

  # Extract layer number from group dir name
  layer_num=$(echo "$group_name" | grep -oP 'layer_\K[0-9]+')

  # Check internal directories (no more sub_layers)
  check_dir "$group_name/layer_${layer_num}_00_layer_registry"
  check_dir "$group_name/layer_${layer_num}_01_ai_manager_system"
  check_dir "$group_name/layer_${layer_num}_02_manager_handoff_documents"
  check_dir "$group_name/layer_${layer_num}_02_manager_handoff_documents/incoming/from_above"
  check_dir "$group_name/layer_${layer_num}_02_manager_handoff_documents/incoming/from_below"
  check_dir "$group_name/layer_${layer_num}_02_manager_handoff_documents/outgoing/to_above"
  check_dir "$group_name/layer_${layer_num}_02_manager_handoff_documents/outgoing/to_below"

  # Warn about stale sub_layers directory
  for sl_dir in "$ENTITY/$group_name"/layer_*_sub_layers; do
    if [ -d "$sl_dir" ]; then
      warn "Stale sub_layers directory: $(basename "$sl_dir") (run migrate-sub-layers-to-0agnostic.sh)"
    fi
  done

  # Stages
  stages_dir="$group_name/layer_${layer_num}_99_stages"
  check_dir "$stages_dir"

  echo ""
  echo "--- Stages ---"

  # Check stages orchestrator
  if ls "$ENTITY/$stages_dir/"*_orchestrator.gab.jsonld 1>/dev/null 2>&1; then
    pass "Stages orchestrator .gab.jsonld found"
    for f in "$ENTITY/$stages_dir/"*_orchestrator.gab.jsonld; do
      base="${f%.gab.jsonld}"
      [ -f "${base}.integration.md" ] && pass "$(basename "${base}.integration.md")" || fail "$(basename "${base}.integration.md") (missing)"
    done
  else
    fail "No stages orchestrator .gab.jsonld"
  fi

  [ -f "$ENTITY/$stages_dir/status_${layer_num}.json" ] && pass "status_${layer_num}.json" || fail "status_${layer_num}.json (missing)"
  [ -f "$ENTITY/$stages_dir/0AGNOSTIC.md" ] && pass "$stages_dir/0AGNOSTIC.md" || fail "$stages_dir/0AGNOSTIC.md (missing)"

  # Check each stage
  stage_count=0
  for stage_dir in "$ENTITY/$stages_dir"/stage_${layer_num}_*/; do
    [ -d "$stage_dir" ] || continue
    stage_count=$((stage_count + 1))
    stage_name=$(basename "$stage_dir")
    rel="$stages_dir/$stage_name"

    # 0AGNOSTIC.md
    [ -f "$stage_dir/0AGNOSTIC.md" ] && pass "$rel/0AGNOSTIC.md" || fail "$rel/0AGNOSTIC.md (missing)"

    # Agent .jsonld + .integration.md
    agent_jsonld=$(find "$stage_dir" -maxdepth 1 -name "*_agent.jsonld" -type f 2>/dev/null | head -1)
    if [ -n "$agent_jsonld" ]; then
      pass "$rel/$(basename "$agent_jsonld")"
      integ="${agent_jsonld%.jsonld}.integration.md"
      [ -f "$integ" ] && pass "$rel/$(basename "$integ")" || fail "$rel/$(basename "$integ") (missing — run jsonld-to-md.sh)"
    else
      fail "$rel/*_agent.jsonld (missing)"
    fi

    # Config dirs in stage
    for d in .0agnostic .1merge .claude .cursor .gemini .codex .github synthesis; do
      [ -d "$stage_dir/$d" ] || fail "$rel/$d/ (missing)"
    done

    # Episodic memory in stage tool dirs
    for tool in .0agnostic/04_episodic_memory .claude .cursor .gemini .codex; do
      if [ "$tool" = ".0agnostic/04_episodic_memory" ]; then
        [ -d "$stage_dir/$tool/sessions" ] || fail "$rel/$tool/sessions (missing)"
      else
        [ -d "$stage_dir/$tool/episodic_memory/sessions" ] || fail "$rel/$tool/episodic_memory/sessions (missing)"
      fi
    done
  done

  if [ "$stage_count" -ge 12 ]; then
    pass "Stage count: $stage_count (>= 12)"
  else
    fail "Stage count: $stage_count (expected >= 12)"
  fi
else
  fail "No layer_N_group/ directory found (internal structure missing)"
fi

echo ""

# --- Stale References Check ---
echo "--- Reference Checks ---"

# Check for bare "episodic/" that should be "episodic_memory/"
stale_episodic=$(find "$ENTITY" -type d -name "episodic" 2>/dev/null | wc -l)
if [ "$stale_episodic" -eq 0 ]; then
  pass "No stale 'episodic/' directories (all are episodic_memory/)"
else
  fail "$stale_episodic directories still named 'episodic/' instead of 'episodic_memory/'"
fi

# Check for bare layer_N/ without _group suffix (excluding layer_N+1_group children)
if [ -n "$group_dir" ]; then
  bare_layer=$(echo "$group_name" | sed 's/_group$//')
  if [ -d "$ENTITY/$bare_layer" ]; then
    fail "Bare '$bare_layer/' exists without _group suffix"
  else
    pass "No bare layer dir without _group suffix"
  fi
fi

# Check all .jsonld files have matching .integration.md
echo ""
echo "--- Integration File Coverage ---"
all_jsonld=$(find "$ENTITY" -name "*.jsonld" -type f 2>/dev/null)
if [ -n "$all_jsonld" ]; then
  while IFS= read -r jf; do
    if [[ "$jf" == *.gab.jsonld ]]; then
      integ="${jf%.gab.jsonld}.integration.md"
    else
      integ="${jf%.jsonld}.integration.md"
    fi
    rel_jf="${jf#$ENTITY/}"
    rel_integ="${integ#$ENTITY/}"
    [ -f "$integ" ] && pass "$rel_integ" || fail "$rel_integ (missing for $rel_jf)"
  done <<< "$all_jsonld"
else
  warn "No .jsonld files found"
fi

echo ""
echo "================================"
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
echo "  WARN: $WARN"
echo "================================"

if [ "$FAIL" -gt 0 ]; then
  echo "Entity is INCOMPLETE — $FAIL items need fixing."
  exit 1
else
  echo "Entity structure is COMPLETE."
  exit 0
fi

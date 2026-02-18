#!/usr/bin/env bash
# validate-avenue-web.sh
# Validate 8 Avenue Web routes for layer/stage entities under better_ai_system.
# Usage: validate-avenue-web.sh [target_root] [report_path]

set -u

TARGET_ROOT="${1:-layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system}"
REPORT_PATH="${2:-$TARGET_ROOT/layer_0_group/layer_0_99_stages/stage_0_07_testing/outputs/by_topic/avenue_web_validation_report.md}"

if [ ! -d "$TARGET_ROOT" ]; then
  echo "Target root not found: $TARGET_ROOT" >&2
  exit 1
fi

mkdir -p "$(dirname "$REPORT_PATH")"

PASS=0
FAIL=0
WARN=0

# CSV-like rows for markdown
ROWS=""

add_row() {
  local path="$1"
  local type="$2"
  local a1="$3"
  local a2="$4"
  local a3="$5"
  local a4="$6"
  local a5="$7"
  local a6="$8"
  local a7="$9"
  local a8="${10}"
  local score="${11}"
  ROWS+="| \`$path\` | $type | $a1 | $a2 | $a3 | $a4 | $a5 | $a6 | $a7 | $a8 | $score |"$'\n'
}

is_ok() {
  [ "$1" = "PASS" ]
}

check_entity() {
  local ent="$1"
  local rel="${ent#$TARGET_ROOT/}"
  [ "$rel" = "$ent" ] && rel="."

  local type="layer"
  [[ "$(basename "$ent")" == stage_* ]] && type="stage"

  local a1 a2 a3 a4 a5 a6 a7 a8
  local score=0

  # Avenue 1: system prompt chain files
  if [ -f "$ent/CLAUDE.md" ] && [ -f "$ent/AGENTS.md" ] && [ -f "$ent/GEMINI.md" ] && [ -f "$ent/OPENAI.md" ]; then
    a1="PASS"; score=$((score+1)); PASS=$((PASS+1))
  else
    a1="FAIL"; FAIL=$((FAIL+1))
  fi

  # Avenue 2: path-specific rules surfaces
  if [ -d "$ent/.claude/rules" ] || [ -d "$ent/.cursor/rules" ] || [ -d "$ent/.github/instructions" ]; then
    a2="PASS"; score=$((score+1)); PASS=$((PASS+1))
  else
    a2="FAIL"; FAIL=$((FAIL+1))
  fi

  # Avenue 3: skills surface
  if [ -d "$ent/.0agnostic/skills" ]; then
    a3="PASS"; score=$((score+1)); PASS=$((PASS+1))
  else
    a3="FAIL"; FAIL=$((FAIL+1))
  fi

  # Avenue 4: reference chaining (@import or knowledge refs)
  if rg -q "@import|@imports|knowledge/" "$ent/0AGNOSTIC.md" "$ent/CLAUDE.md" "$ent/AGENTS.md" "$ent/GEMINI.md" "$ent/OPENAI.md" 2>/dev/null; then
    a4="PASS"; score=$((score+1)); PASS=$((PASS+1))
  elif [ -d "$ent/.0agnostic/knowledge" ]; then
    a4="WARN"; WARN=$((WARN+1))
  else
    a4="FAIL"; FAIL=$((FAIL+1))
  fi

  # Avenue 5: JSON-LD graph family presence (local entity scope)
  local jsonld_count
  jsonld_count=$(find "$ent" -maxdepth 2 -type f -name "*.jsonld" | wc -l | tr -d ' ')
  if [ "$jsonld_count" -gt 0 ]; then
    a5="PASS"; score=$((score+1)); PASS=$((PASS+1))
  else
    a5="FAIL"; FAIL=$((FAIL+1))
  fi

  # Avenue 6: integration summaries for local jsonld files
  local missing=0
  while IFS= read -r jf; do
    [ -z "$jf" ] && continue
    local integ
    if [[ "$jf" == *.gab.jsonld ]]; then
      integ="${jf%.gab.jsonld}.integration.md"
    else
      integ="${jf%.jsonld}.integration.md"
    fi
    [ -f "$integ" ] || missing=$((missing+1))
  done < <(find "$ent" -maxdepth 2 -type f -name "*.jsonld")

  if [ "$jsonld_count" -eq 0 ]; then
    a6="WARN"; WARN=$((WARN+1))
  elif [ "$missing" -eq 0 ]; then
    a6="PASS"; score=$((score+1)); PASS=$((PASS+1))
  else
    a6="FAIL"; FAIL=$((FAIL+1))
  fi

  # Avenue 7: episodic memory
  if [ -d "$ent/.0agnostic/episodic_memory/sessions" ] || [ -d "$ent/outputs/episodic_memory/sessions" ] || [ -d "$ent/.claude/episodic_memory/sessions" ]; then
    a7="PASS"; score=$((score+1)); PASS=$((PASS+1))
  else
    a7="FAIL"; FAIL=$((FAIL+1))
  fi

  # Avenue 8: direct canonical fallback
  if [ -f "$ent/0AGNOSTIC.md" ]; then
    a8="PASS"; score=$((score+1)); PASS=$((PASS+1))
  else
    a8="FAIL"; FAIL=$((FAIL+1))
  fi

  add_row "$rel" "$type" "$a1" "$a2" "$a3" "$a4" "$a5" "$a6" "$a7" "$a8" "$score/8"
}

# Build entity list: directories with 0AGNOSTIC.md that are layer- or stage-scoped
mapfile -t ENTITIES < <(find "$TARGET_ROOT" -type f -name "0AGNOSTIC.md" -print | sed 's#/0AGNOSTIC.md$##' | sort)

for ent in "${ENTITIES[@]}"; do
  base="$(basename "$ent")"

  # Exclude template/reference trees from active hierarchy scoring.
  if [[ "$ent" == *"/reference_implementation/"* ]]; then
    continue
  fi

  # Include:
  # - Explicit target root (feature root)
  # - Stage entities (stage_* dirs)
  # - Feature/sub-feature entities
  # Exclude structural containers (layer_*_group, layer_*_99_stages, etc.).
  if [ "$ent" = "$TARGET_ROOT" ]; then
    check_entity "$ent"
  elif [[ "$base" == stage_* ]]; then
    check_entity "$ent"
  elif [[ "$base" == *"_feature_"* ]] || [[ "$base" == *"_sub_feature_"* ]]; then
    check_entity "$ent"
  fi
done

# Global JSON-LD class coverage for this target
layer_orch=$(find "$TARGET_ROOT" -type f -name "layer_*_orchestrator.gab.jsonld" | wc -l | tr -d ' ')
stage_orch=$(find "$TARGET_ROOT" -type f -name "layer_*_99_stages_orchestrator.gab.jsonld" | wc -l | tr -d ' ')
stage_agents=$(find "$TARGET_ROOT" -type f -name "stage_*_agent.jsonld" | wc -l | tr -d ' ')
index_jsonld=$(find "$TARGET_ROOT" -type f -name "index.jsonld" | wc -l | tr -d ' ')
gab_runtime=$(find "$TARGET_ROOT" -type f \( -name "gab.jsonld" -o -name "gab-runtime.jsonld" -o -name "gab-formats.jsonld" -o -name "*gab*.jsonld" \) | wc -l | tr -d ' ')

cat > "$REPORT_PATH" <<EOF2
# Avenue Web Validation Report

- Target root: \`$TARGET_ROOT\`
- Generated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")

## Entity Results (8 Avenues)

| Entity | Type | A1 Prompts | A2 Path Rules | A3 Skills | A4 Refs | A5 JSON-LD | A6 Integration | A7 Memory | A8 0AGNOSTIC | Score |
|---|---|---|---|---|---|---|---|---|---|---|
$ROWS

## JSON-LD Class Coverage (Global)

- Layer orchestrators: **$layer_orch**
- Stage orchestrators: **$stage_orch**
- Stage agents: **$stage_agents**
- Layer/feature indexes: **$index_jsonld**
- GAB/runtime/spec-like JSON-LDs: **$gab_runtime**

## Summary

- PASS checks: **$PASS**
- FAIL checks: **$FAIL**
- WARN checks: **$WARN**

EOF2

echo "Wrote report: $REPORT_PATH"
# Non-zero if failures exist
[ "$FAIL" -eq 0 ]

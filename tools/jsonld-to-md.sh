#!/bin/bash
# jsonld-to-md.sh — Transpile AALang JSON-LD to markdown integration reference
# Usage: ./jsonld-to-md.sh <input.gab.jsonld> [output.integration.md]
#
# Generates a .integration.md file from a .gab.jsonld file.
# If no output path given, replaces .gab.jsonld extension with .integration.md

set -euo pipefail

INPUT="${1:?Usage: $0 <input.gab.jsonld> [output.integration.md]}"

if [ ! -f "$INPUT" ]; then
    echo "Error: File not found: $INPUT" >&2
    exit 1
fi

# Determine output path
if [ -n "${2:-}" ]; then
    OUTPUT="$2"
else
    OUTPUT="${INPUT%.gab.jsonld}.integration.md"
fi

BASENAME=$(basename "$INPUT" .gab.jsonld)
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Start generating markdown
{
    echo "# ${BASENAME} — Integration Reference"
    echo "<!-- AUTO-GENERATED from $(basename "$INPUT") — do not edit directly -->"
    echo "<!-- Last transpiled: ${TIMESTAMP} -->"
    echo "<!-- Source: ${INPUT} -->"
    echo ""

    # --- Modes ---
    MODES=$(jq -r '
        ."@graph"[] |
        select(."@type" == "gab:Mode") |
        "| \(."@id") | \(.purpose // "—") |"
    ' "$INPUT" 2>/dev/null || true)

    if [ -n "$MODES" ]; then
        echo "## Modes"
        echo ""
        echo "| Mode | Purpose |"
        echo "|------|---------|"
        echo "$MODES"
        echo ""
    fi

    # --- Mode Transitions ---
    TRANSITIONS=$(jq -r '
        ."@graph"[] |
        select(."@type" == "gab:ModeTransition" or ."@type" == "gab:Transition") |
        "| \(.["gab:fromMode"] // .fromMode // "—") | \(.["gab:toMode"] // .toMode // "—") | \(.["gab:gate"].["gab:condition"] // .gate.condition // .condition // "—") |"
    ' "$INPUT" 2>/dev/null || true)

    if [ -n "$TRANSITIONS" ]; then
        echo "## Mode Transitions"
        echo ""
        echo "| From | To | Condition |"
        echo "|------|----|-----------|"
        echo "$TRANSITIONS"
        echo ""
    fi

    # --- State Actors ---
    STATE_ACTORS=$(jq -r '
        ."@graph"[] |
        select(."@id" | test("StateActor")) |
        "| \(."@id") | \(.purpose // .description // "—") |"
    ' "$INPUT" 2>/dev/null || true)

    if [ -n "$STATE_ACTORS" ]; then
        echo "## State Actors"
        echo ""
        echo "| Actor | Purpose |"
        echo "|-------|---------|"
        echo "$STATE_ACTORS"
        echo ""
    fi

    # --- Mode Actors (Personas) ---
    PERSONAS=$(jq -r '
        ."@graph"[] |
        select(."@id" | test("Persona")) |
        "| \(."@id") | \(.purpose // .role // "—") |"
    ' "$INPUT" 2>/dev/null || true)

    if [ -n "$PERSONAS" ]; then
        echo "## Mode Actors (Personas)"
        echo ""
        echo "| Persona | Role |"
        echo "|---------|------|"
        echo "$PERSONAS"
        echo ""
    fi

    # --- Isolated States ---
    ISOLATED_STATES=$(jq -r '
        ."@graph"[] |
        select(."@type" == "gab:IsolatedState" or ."@type" == "IsolatedState") |
        "| \(."@id") | \(.mode // "—") | \(.scope // "—") | \(.includes | if type == "array" then join("; ") else . // "—" end) |"
    ' "$INPUT" 2>/dev/null || true)

    if [ -n "$ISOLATED_STATES" ]; then
        echo "## Isolated States"
        echo ""
        echo "| State | Mode | Scope | Includes |"
        echo "|-------|------|-------|----------|"
        echo "$ISOLATED_STATES"
        echo ""
    fi

    # --- Prohibitions/Constraints ---
    PROHIBITIONS=$(jq -r '
        .prohibitions[]? |
        "| \(.action // .description // .rule // "—") | \(.severity // "—") |"
    ' "$INPUT" 2>/dev/null || true)

    if [ -n "$PROHIBITIONS" ]; then
        echo "## Constraints (Prohibitions)"
        echo ""
        echo "| Rule | Severity |"
        echo "|------|----------|"
        echo "$PROHIBITIONS"
        echo ""
    fi

    # --- Mode Constraints (MUST/MUST NOT per mode) ---
    MODE_CONSTRAINTS=$(jq -r '
        ."@graph"[] |
        select(."@type" == "gab:Mode" and .constraints != null) |
        "### \(."@id")\n\(.constraints | if type == "object" then
            (if .MUST then "**MUST**: " + (.MUST | if type == "array" then join(", ") else tostring end) + "\n" else "" end) +
            (if .MUST_NOT then "**MUST NOT**: " + (.MUST_NOT | if type == "array" then join(", ") else tostring end) + "\n" else "" end)
        elif type == "array" then
            ([.[] | "- " + tostring] | join("\n")) + "\n"
        else tostring + "\n" end)"
    ' "$INPUT" 2>/dev/null || true)

    if [ -n "$MODE_CONSTRAINTS" ]; then
        echo "## Mode-Specific Constraints"
        echo ""
        echo -e "$MODE_CONSTRAINTS"
        echo ""
    fi

    # --- Execution Instructions ---
    EXEC_INSTRUCTIONS=$(jq -r '
        ."@graph"[] |
        select(."@id" | test("ExecutionInstructions")) |
        .["gab:instructions"] // .instructions // empty |
        if type == "array" then .[] else . end
    ' "$INPUT" 2>/dev/null || true)

    if [ -n "$EXEC_INSTRUCTIONS" ]; then
        echo "## Execution Instructions"
        echo ""
        echo "$EXEC_INSTRUCTIONS"
        echo ""
    fi

    # --- Navigation ---
    echo "## Navigation"
    echo ""
    echo "To explore this agent definition interactively:"
    echo '```bash'
    echo "# List all nodes"
    echo "jq '.\"@graph\"[].\"@id\"' $(basename "$INPUT")"
    echo ""
    echo "# Get a specific mode"
    echo "jq '.\"@graph\"[] | select(.\"@id\" == \"MODE_ID\")' $(basename "$INPUT")"
    echo ""
    echo "# Get all modes with purposes"
    echo "jq '.\"@graph\"[] | select(.\"@type\" == \"gab:Mode\") | {id: .\"@id\", purpose: .purpose}' $(basename "$INPUT")"
    echo '```'
    echo ""

    echo "---"
    echo "*Auto-generated by tools/jsonld-to-md.sh from $(basename "$INPUT")*"

} > "$OUTPUT"

echo "Generated: $OUTPUT"

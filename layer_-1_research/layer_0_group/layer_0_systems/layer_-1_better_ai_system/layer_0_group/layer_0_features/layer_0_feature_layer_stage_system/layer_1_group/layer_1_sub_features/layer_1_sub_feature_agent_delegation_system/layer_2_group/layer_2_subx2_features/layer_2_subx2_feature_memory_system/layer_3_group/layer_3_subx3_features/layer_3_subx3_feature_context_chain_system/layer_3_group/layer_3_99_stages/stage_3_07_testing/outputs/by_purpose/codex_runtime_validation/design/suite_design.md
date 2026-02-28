# Codex Runtime Validation Suite Design

## Goal
Verify real Codex runtime behavior and required execution mode.

## Required Runtime Mode
- `codex exec --dangerously-bypass-approvals-and-sandbox`

## Primary Checks
1. Codex can execute core test scripts and return strict PASS/FAIL outputs.
2. Codex discovers required static context paths from AGENTS.

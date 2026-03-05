---
resource_id: "44edb0d4-7415-40a2-872a-d9276b43725a"
resource_type: "output"
resource_name: "suite_design"
---
# Codex Runtime Validation Suite Design

<!-- section_id: "99d16688-259f-4e76-9e06-2d31d6c5a3d3" -->
## Goal
Verify real Codex runtime behavior and required execution mode.

<!-- section_id: "d19fb96e-7d04-4616-b1c2-95c42b56eb20" -->
## Required Runtime Mode
- `codex exec --dangerously-bypass-approvals-and-sandbox`

<!-- section_id: "609c66e6-718f-4497-921d-2d6462c70e1b" -->
## Primary Checks
1. Codex can execute core test scripts and return strict PASS/FAIL outputs.
2. Codex discovers required static context paths from AGENTS.

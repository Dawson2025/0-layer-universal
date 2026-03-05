---
resource_id: "49bc1ee8-0363-40ce-9b60-07349f2f2c4d"
resource_type: "readme
document"
resource_name: "README"
---
# Context Gathering Documentation

<!-- section_id: "8f349e5a-f793-4398-8a11-d9045501f062" -->
## Overview
This directory contains the rules and guidelines for how AI agents gather context within the Layer-Stage Framework.

<!-- section_id: "9010284e-6fdd-406b-b674-43449d06d410" -->
## Documents

<!-- section_id: "b0eb9da8-8bcd-4e1e-8101-e3839c12522e" -->
### vertical_chain_rules.md
Rules for gathering context from ancestors (up) and descendants (down) in the hierarchy.

<!-- section_id: "9cb73651-ce11-4cc6-9e07-90bb533fa9f0" -->
### horizontal_sibling_rules.md
Rules for determining when sibling entities should be included in context.

<!-- section_id: "c8f9ca6b-0aa1-4983-b4ce-885f06080bc9" -->
### task_source_identification.md
How to identify and prioritize task sources.

<!-- section_id: "ea996e6e-0b18-4b39-bd5e-06cc02ffbfae" -->
### init_prompt_chain.md
How init_prompt.md files chain together to form complete context.

<!-- section_id: "91ae15e1-7ffa-4c11-8159-576abcf614b9" -->
## Core Principle
**Vertical = Always, Horizontal = When Relevant**

The vertical chain (ancestors and descendants) always provides relevant context. Horizontal siblings only provide relevant context when they are both RELATED to the current entity AND RELEVANT to the current task.

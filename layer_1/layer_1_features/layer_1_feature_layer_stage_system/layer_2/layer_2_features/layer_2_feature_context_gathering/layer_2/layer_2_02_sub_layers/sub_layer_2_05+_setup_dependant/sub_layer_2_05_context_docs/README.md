---
resource_id: "49bc1ee8-0363-40ce-9b60-07349f2f2c4d"
resource_type: "readme
document"
resource_name: "README"
---
# Context Gathering Documentation

## Overview
This directory contains the rules and guidelines for how AI agents gather context within the Layer-Stage Framework.

## Documents

### vertical_chain_rules.md
Rules for gathering context from ancestors (up) and descendants (down) in the hierarchy.

### horizontal_sibling_rules.md
Rules for determining when sibling entities should be included in context.

### task_source_identification.md
How to identify and prioritize task sources.

### init_prompt_chain.md
How init_prompt.md files chain together to form complete context.

## Core Principle
**Vertical = Always, Horizontal = When Relevant**

The vertical chain (ancestors and descendants) always provides relevant context. Horizontal siblings only provide relevant context when they are both RELATED to the current entity AND RELEVANT to the current task.

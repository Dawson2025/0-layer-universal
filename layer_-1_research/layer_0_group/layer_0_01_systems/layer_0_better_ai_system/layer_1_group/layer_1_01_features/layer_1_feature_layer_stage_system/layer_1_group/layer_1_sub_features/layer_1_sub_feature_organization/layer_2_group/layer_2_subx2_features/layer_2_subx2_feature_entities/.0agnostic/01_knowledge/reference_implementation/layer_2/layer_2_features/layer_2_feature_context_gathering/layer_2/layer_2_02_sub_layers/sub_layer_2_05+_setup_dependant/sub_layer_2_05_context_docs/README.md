---
resource_id: "e71ac48b-cfff-47dd-a66d-843d04efdb69"
resource_type: "readme
knowledge"
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

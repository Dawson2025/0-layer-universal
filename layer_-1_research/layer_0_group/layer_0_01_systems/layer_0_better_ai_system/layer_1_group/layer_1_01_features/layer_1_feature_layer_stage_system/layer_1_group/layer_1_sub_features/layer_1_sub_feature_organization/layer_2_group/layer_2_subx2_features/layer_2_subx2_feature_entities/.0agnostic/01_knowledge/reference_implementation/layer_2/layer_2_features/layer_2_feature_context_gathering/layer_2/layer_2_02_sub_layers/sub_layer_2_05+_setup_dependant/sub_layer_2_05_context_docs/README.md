---
resource_id: "e71ac48b-cfff-47dd-a66d-843d04efdb69"
resource_type: "readme_knowledge"
resource_name: "README"
---
# Context Gathering Documentation

<!-- section_id: "f520e46f-22be-497d-a134-ad98ba27dad6" -->
## Overview
This directory contains the rules and guidelines for how AI agents gather context within the Layer-Stage Framework.

<!-- section_id: "97dbc497-bb04-4e8e-b3e8-c9b872e70f1a" -->
## Documents

<!-- section_id: "43a7f0ee-5e58-4413-8823-02f5f282e4e5" -->
### vertical_chain_rules.md
Rules for gathering context from ancestors (up) and descendants (down) in the hierarchy.

<!-- section_id: "aaaeb7fc-07a4-49fa-ac1f-ac3f0a601e07" -->
### horizontal_sibling_rules.md
Rules for determining when sibling entities should be included in context.

<!-- section_id: "20416166-cbc2-44d2-a56c-ec6dd1511966" -->
### task_source_identification.md
How to identify and prioritize task sources.

<!-- section_id: "afe3b6d7-c966-4c23-a9b0-06876f940c29" -->
### init_prompt_chain.md
How init_prompt.md files chain together to form complete context.

<!-- section_id: "b7b5c600-3ffd-4328-ada3-48c55467638c" -->
## Core Principle
**Vertical = Always, Horizontal = When Relevant**

The vertical chain (ancestors and descendants) always provides relevant context. Horizontal siblings only provide relevant context when they are both RELATED to the current entity AND RELEVANT to the current task.

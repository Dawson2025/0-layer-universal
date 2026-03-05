---
resource_id: "0f256403-76fe-4cad-b04c-ca5d3ae1e619"
resource_type: "document"
resource_name: "spec-kit-selection"
---
# GitHub Spec Kit Implementation for Language Tracker
*Trickle-Down Level 1.0: Project AI Coding System Selection*

<!-- section_id: "577c44e3-8c42-4adc-856c-9e32e3a85b22" -->
## Our Choice: GitHub Spec Kit (Specification-Driven Development)

**Project Decision:** The Language Tracker project uses GitHub Spec Kit for AI-assisted development.

<!-- section_id: "2bbbdcd3-000d-4478-b80e-16ca2cdb7706" -->
## Why We Chose Spec Kit for This Project

**Complexity:** High - Complex phoneme hierarchy, multiple storage backends, TDD framework
**Quality Requirements:** Highest - Linguistic accuracy is critical
**Timeline:** Long-term - Sustainable development approach needed

<!-- section_id: "c1329720-e00e-48c6-b92d-3ab4f3f4051d" -->
## Spec Kit Workflow for Language Tracker

<!-- section_id: "4e6c329c-9042-4b1c-81ec-243a2900cbb9" -->
### Phase 1: Constitution
Command: /speckit.constitution
Input: TD1 constitution.md (our comprehensive project constitution)
Status: ✅ Ready - Constitution contains TDD framework, user stories, quality standards

<!-- section_id: "2f5aff5b-cd17-4945-bc33-b929db6dd8b3" -->
### Phase 2: Feature Specification
Command: /speckit.specify [feature description]
Maps to: TD2 feature domains (authentication, learning, content, advanced, system)

<!-- section_id: "a063011d-0121-445d-832f-373a7586d194" -->
### Phase 3: Implementation Planning
Command: /speckit.plan
Context: WSL Ubuntu environment (TD0.5), project architecture standards

<!-- section_id: "a7b1ffeb-45a0-4df8-a9a3-c841f6efeca2" -->
### Phase 4: Task Generation
Command: /speckit.tasks
Output: Parallelizable tasks for AI agents and developers

<!-- section_id: "f363a40b-b1cb-44e3-9156-5e7294d4b86c" -->
### Phase 5: Implementation
Command: /speckit.implement
Result: Working code that matches specifications, updates TD3 documentation

<!-- section_id: "a4b42517-0a5c-45d5-b7df-216b50afddd2" -->
## Installation & Setup

<!-- section_id: "6162aca3-d97a-4b5c-ac0c-631053dec412" -->
### Install Specify CLI (WSL Ubuntu)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

<!-- section_id: "9d996e34-1772-4262-aa47-f80586042886" -->
### Initialize Project
specify init lang-trak-features --ai claude --here
specify check

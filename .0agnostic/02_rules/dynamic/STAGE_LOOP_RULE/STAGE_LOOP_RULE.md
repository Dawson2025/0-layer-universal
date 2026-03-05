---
resource_id: "616abca3-741e-4f79-a4fd-38b852f86000"
resource_type: "rule"
resource_name: "STAGE_LOOP_RULE"
---
# Stage Loop Rule

**Type**: Dynamic (triggered by scenario)
**Trigger**: When a stage needs to loop back to a previous stage

<!-- section_id: "7a4a9a56-9fe3-4261-b910-1feb0633f304" -->
## Rule

When a later stage discovers that earlier stage work needs revision, it MUST:

1. Document what needs revision in its stage report
2. Hand off to the appropriate earlier stage (not fix it in place)
3. The earlier stage revises, updates its stage report, and hands off forward again

<!-- section_id: "1088d2b3-76e8-43fd-b2fe-5b7b5c72d8b5" -->
## Common Loops

| From | Back To | When |
|------|---------|------|
| Stage 07 (testing) | Stage 09 (fixing) | Test failures found |
| Stage 08 (criticism) | Stage 09 (fixing) | Quality issues identified |
| Stage 09 (fixing) | Stage 07 (testing) | Fixes applied, need re-verification |
| Stage 04 (design) | Stage 02 (research) | Design questions need investigation |
| Stage 06 (development) | Stage 04 (design) | Implementation reveals design issues |
| Stage 08 (criticism) | Stage 01 (request gathering) | Requirements need revision |

<!-- section_id: "f1f191af-0b06-44f8-bea5-402b87546ec2" -->
## The Quality Loop

The most common loop: **07 → 08 → 09 → 07**

1. Testing (07) validates artifacts
2. Criticism (08) reviews quality
3. Fixing (09) addresses issues
4. Testing (07) re-validates

This loop continues until criticism finds no critical or major issues.

<!-- section_id: "b4a6a6ad-c223-4120-a37c-48c6f0e3ee78" -->
## Rationale

Stages are not strictly linear. Quality emerges from iteration. But loops must be explicit — work should flow through the proper stages, not be done ad hoc within a single stage.

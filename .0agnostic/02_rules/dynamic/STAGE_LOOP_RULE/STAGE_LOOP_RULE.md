# Stage Loop Rule

**Type**: Dynamic (triggered by scenario)
**Trigger**: When a stage needs to loop back to a previous stage

## Rule

When a later stage discovers that earlier stage work needs revision, it MUST:

1. Document what needs revision in its stage report
2. Hand off to the appropriate earlier stage (not fix it in place)
3. The earlier stage revises, updates its stage report, and hands off forward again

## Common Loops

| From | Back To | When |
|------|---------|------|
| Stage 07 (testing) | Stage 09 (fixing) | Test failures found |
| Stage 08 (criticism) | Stage 09 (fixing) | Quality issues identified |
| Stage 09 (fixing) | Stage 07 (testing) | Fixes applied, need re-verification |
| Stage 04 (design) | Stage 02 (research) | Design questions need investigation |
| Stage 06 (development) | Stage 04 (design) | Implementation reveals design issues |
| Stage 08 (criticism) | Stage 01 (request gathering) | Requirements need revision |

## The Quality Loop

The most common loop: **07 → 08 → 09 → 07**

1. Testing (07) validates artifacts
2. Criticism (08) reviews quality
3. Fixing (09) addresses issues
4. Testing (07) re-validates

This loop continues until criticism finds no critical or major issues.

## Rationale

Stages are not strictly linear. Quality emerges from iteration. But loops must be explicit — work should flow through the proper stages, not be done ad hoc within a single stage.

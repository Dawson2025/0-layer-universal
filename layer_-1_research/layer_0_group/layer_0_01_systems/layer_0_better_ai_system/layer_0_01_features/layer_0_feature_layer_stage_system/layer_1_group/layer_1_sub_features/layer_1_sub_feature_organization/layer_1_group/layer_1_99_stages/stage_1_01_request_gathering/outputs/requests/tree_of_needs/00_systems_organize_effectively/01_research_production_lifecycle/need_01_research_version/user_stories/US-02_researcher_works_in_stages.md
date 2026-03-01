# Researcher Works in Stages

**As a** researcher conducting an experimental investigation,
**I want to** progress through stages (01 request gathering → 02 research → 04 design → ... → 10 current product) within my research entity,
**So that** my exploratory work follows a repeatable, structured process that produces traceable deliverables at each phase.

## Acceptance Criteria

**Scenario 1: Stage agent provides methodology on entry**
- **Given** I navigate to `stage_01_request_gathering/` within my research entity,
- **When** I read the stage's `0AGNOSTIC.md`,
- **Then** I find a clear methodology (e.g., "Tree of Needs"), defined inputs and outputs, and a delegation contract explaining what I should and should not do in this stage.

**Scenario 2: Stage outputs accumulate as I progress**
- **Given** I have completed work in stage 01 (tree of needs written) and stage 02 (research notes captured),
- **When** I enter stage 04 (design),
- **Then** I can read the outputs from stages 01 and 02 as inputs, and the design stage's `0AGNOSTIC.md` tells me where to find them.

**Scenario 3: Each stage is independently workable**
- **Given** I want to work on stage 04 (design) before completing stage 02 (research),
- **When** I enter stage 04 directly,
- **Then** the stage agent loads its own identity and methodology without requiring stage 02 to be complete — stages are guideposts, not hard gates.

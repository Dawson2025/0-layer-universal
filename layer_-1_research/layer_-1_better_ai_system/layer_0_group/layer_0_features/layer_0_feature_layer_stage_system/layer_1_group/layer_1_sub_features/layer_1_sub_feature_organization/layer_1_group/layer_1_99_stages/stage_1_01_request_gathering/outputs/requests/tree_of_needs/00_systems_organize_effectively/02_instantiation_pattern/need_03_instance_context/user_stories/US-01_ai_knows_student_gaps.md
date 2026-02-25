# AI Knows Student's Knowledge Gaps

**As an** AI tutor working with a specific student,
**I want to** access the student's knowledge state from their instance context,
**So that** I can identify which concepts they haven't mastered and tailor my explanations to bridge those specific gaps.

## Acceptance Criteria

**Scenario 1: Knowledge state is stored in instance context**
- **Given** Alice's instance entity exists with her enrolled courses,
- **When** the AI agent reads her instance's `.0agnostic/01_knowledge/` or context area,
- **Then** it finds a knowledge state record listing topics as "mastered", "in-progress", or "not-started", organized by course.

**Scenario 2: Gaps are identifiable through knowledge graph comparison**
- **Given** the school system's knowledge graph defines that "eigenvalues" requires "matrix multiplication" as a prerequisite,
- **When** the AI checks Alice's knowledge state and finds "matrix multiplication" marked as "not-started",
- **Then** the AI identifies "matrix multiplication" as a foundational gap that must be addressed before teaching "eigenvalues".

**Scenario 3: Gap information informs tutoring approach**
- **Given** Alice asks for help with "eigenvalues" and the AI has identified "matrix multiplication" as a gap,
- **When** the AI prepares its explanation,
- **Then** it either starts with a review of matrix multiplication or explicitly tells Alice she needs to master that prerequisite first — rather than assuming she already knows it.

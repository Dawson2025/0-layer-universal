# AI Tailors Teaching to Student

**As an** AI tutor with access to a student's personalized instance,
**I want to** adapt my explanations based on the student's knowledge level, learning style, and goals,
**So that** I provide the right level of detail — not too basic for advanced students, not too complex for beginners.

## Acceptance Criteria

**Scenario 1: Student model is accessible from instance**
- **Given** Alice's student instance exists with a populated student model,
- **When** the AI agent loads her instance context,
- **Then** the student model includes: current knowledge state per topic (mastered/in-progress/not-started), identified misconceptions, learning preferences (e.g., prefers examples over theory), and stated goals.

**Scenario 2: AI adjusts difficulty based on student model**
- **Given** Alice has mastered "basic calculus" but is struggling with "integration by parts",
- **When** Alice asks for help with integration,
- **Then** the AI skips the basics (no "let me explain what an integral is") and focuses on the specific technique she's struggling with, using examples at her current level.

**Scenario 3: AI adapts when student model changes**
- **Given** Alice completes an assessment that shows she has now mastered "integration by parts",
- **When** her student model is updated to reflect this,
- **Then** the AI's next interaction treats "integration by parts" as known background and builds on it rather than re-explaining it.

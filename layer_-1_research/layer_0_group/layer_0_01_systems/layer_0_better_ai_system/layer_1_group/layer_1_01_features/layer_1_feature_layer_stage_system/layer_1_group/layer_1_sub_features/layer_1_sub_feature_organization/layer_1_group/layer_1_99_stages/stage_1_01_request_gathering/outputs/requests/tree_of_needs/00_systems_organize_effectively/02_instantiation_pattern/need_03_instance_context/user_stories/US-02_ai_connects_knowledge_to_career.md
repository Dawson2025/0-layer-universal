---
resource_id: "ce488541-0503-4a0b-9abf-6a8e1ffd1ebc"
resource_type: "output"
resource_name: "US-02_ai_connects_knowledge_to_career"
---
# AI Connects Knowledge to Career Goals

**As an** AI tutor helping a student stay motivated,
**I want to** connect the student's current coursework to their stated career goals,
**So that** I can explain why specific topics matter and help the student prioritize their learning effectively.

## Acceptance Criteria

**Scenario 1: Career goals are accessible from instance context**
- **Given** Alice's instance entity stores her career goal as "machine learning engineer",
- **When** the AI agent loads her instance context,
- **Then** it finds her career goal along with any associated skill requirements (e.g., "linear algebra", "Python", "statistics").

**Scenario 2: AI maps coursework to career requirements**
- **Given** Alice is studying linear algebra and her career goal requires it,
- **When** Alice asks "why do I need to learn this?",
- **Then** the AI explains the connection: "Linear algebra is fundamental to machine learning — you'll use it for understanding neural networks, dimensionality reduction, and model optimization."

**Scenario 3: AI prioritizes topics by career relevance**
- **Given** Alice has limited study time and multiple topics to review,
- **When** the AI suggests a study plan,
- **Then** it weights topics by their relevance to Alice's career goal — prioritizing "statistics" and "linear algebra" over electives that don't directly support her path to machine learning engineering.

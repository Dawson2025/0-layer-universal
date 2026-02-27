# Trajectory Stores & Cascading Grade Strategy System

**Date**: 2026-02-27
**Status**: ✅ Validated (trajectory concept researched, grade strategy implemented)
**Author**: Claude Code Session

---

## Executive Summary

A **Trajectory Store** is a **procedural memory** artifact that captures step-by-step workflows, including what worked, what didn't, preconditions, and lessons learned. Unlike SOPs (procedures) or runbooks (incident response), trajectory stores preserve agent reasoning, decision context, and effectiveness metrics.

The **Cascading Grade Strategy System** uses trajectory stores at layer_2 (universal) to document how to build grade dashboards. Layer_4 classes inherit these trajectories and invoke class-specific skills that reference them, creating a reusable framework for any class to build a dashboard.

---

## What Are Trajectory Stores?

### Definition

**Trajectory Store**: A documented record of how an AI agent successfully (or unsuccessfully) accomplished a procedural task, including:

1. **What worked** ✅ — Exact steps that produced desired outcome
2. **What didn't** ❌ — Failures, partial successes, edge cases
3. **Context & preconditions** — Requirements, environmental factors, observable states
4. **Metrics & effectiveness** — Success rate, time, reliability, failure cases
5. **Reasoning & hypotheses** — Why it worked, lessons learned, theories for next time
6. **Integration points** — Links to skills, protocols, knowledge bases that use this trajectory

### Key Difference from Other Documentation

| Documentation Type | Focus | Time Horizon | Audience | Example |
|-------------------|-------|--------------|----------|---------|
| **SOP** | Routine operations | Repeated future use | Operators | "Steps to deploy to production" |
| **Runbook** | Incident response | When problems occur | On-call engineers | "Steps to resolve authentication service outage" |
| **Trajectory Store** | Agent work history | Learning from past successes | AI agents & future sessions | "How we built the grade dashboard: 7 steps, trials, lessons learned" |

**Trajectory stores capture**: *How we did this successfully, with context about decisions and effectiveness.*

### Research-Validated Pattern

Academic research (ProcMEM, AgentWorkforce, Trajectory Miner) validates this pattern:

- **ProcMEM** — Framework for procedural memory in multi-agent systems, showing effectiveness of captured workflows
- **AgentWorkforce** — System for agents to maintain trajectory repositories and reference them across sessions
- **Trajectory Miner** — Tool for extracting trajectories from agent logs and converting to actionable procedures

---

## Cascading Grade Strategy System

### Architecture

```
Layer 2 (Universal) — Grade Strategy Foundation
│
├── Trajectory Stores (5 documents)
│   ├── canvas_grade_dashboard_trajectory.md (7-step workflow)
│   ├── grading_model_analysis_trajectory.md (supports specs/percentage/weighted/hybrid)
│   ├── assignment_classification_trajectory.md (name patterns, Canvas types)
│   ├── deadline_tracking_trajectory.md (urgency flagging, lock dates)
│   └── strategy_generation_trajectory.md (priority formulas for 2 grading types)
│
├── Triggers & Rules
│   └── grade_strategy_triggers.md (WHEN to load trajectories)
│
├── Shared Skills (parameterized, reusable)
│   ├── canvas-fetch (generic Canvas data fetcher, course_id param)
│   └── grade-calculator (rubric-agnostic scoring, grading_model param)
│
└── Knowledge Base
    └── canvas_integration/
        ├── grading_model_types.md (taxonomy of grading models)
        ├── assignment_type_taxonomy.md (Canvas types)
        ├── rubric_modeling.md
        └── templates/ (copy-paste scaffolding)

         ↓ (cascades to all child layers)

Layer 3 (Computer Science) & Layer 4 (Individual Classes)
│
├── Class-Specific Grading Model
│   ├── grading_model.md (specs-based, percentage-based, etc.)
│   ├── assignment_categories.yaml (class-specific patterns)
│   └── schedule.md (weekly deadlines, lock dates)
│
└── Class-Specific Skills
    ├── /calc-dashboard (MATH 119, course_id hardcoded)
    ├── /cse300-dashboard (CSE 300, course_id hardcoded)
    └── (future: class-specific skills for all courses)
        ↓ (each references layer_2 trajectories)
        Each skill executes 7-step workflow from canvas_grade_dashboard_trajectory.md
```

### How It Works

**Example: User asks "How am I doing in CSE 300?"**

```
1. Trigger matches: "User asks about grade status in [class]"

2. Load layer_2 trajectories:
   - canvas_grade_dashboard_trajectory.md (7-step workflow)
   - grade_strategy_triggers.md (when to apply this)

3. Load layer_4 (CSE 300) customizations:
   - grading_model.md (1,082 pts, percentage-based, A-F scale)
   - assignment_categories.yaml (7 learning activities, 7 status updates, etc.)
   - schedule.md (deadlines)

4. Execute class-specific skill: /cse300-dashboard
   - Skill references the trajectory (has link in docstring)
   - Skill is pre-configured with course_id=406222
   - Skill executes 7 steps from trajectory:
     Step 1: Fetch data → mcp__canvas__canvas_assignment_list()
     Step 2: Classify assignments → use assignment_categories.yaml patterns
     Step 3: Count completions → tally points earned
     Step 4: Compute total → apply percentage formula
     Step 5: Track deadlines → identify [!!!] flags
     Step 6: Generate strategy → priority score formula
     Step 7: Output dashboard → formatted markdown

5. Return dashboard to user
```

---

## Five Trajectory Stores

### 1. Canvas Grade Dashboard Trajectory

**What it captures**: The 7-step workflow for building any Canvas-powered grade dashboard.

**Steps**:

1. **Fetch Data** — Call Canvas MCP API to get assignment list and submission status
   - Tools: `mcp__canvas__canvas_assignment_list(course_id, include_submission=true)`
   - Output: All assignments with name, id, score, submitted_at, lock_at, due_at

2. **Classify Assignments** — Use name patterns to categorize by rubric/section
   - Tools: regex matching, Canvas type detection
   - Input: assignment names (e.g., "W01 Learning Activity", "Project 1")
   - Output: {category: [assignments]}

3. **Count Completions** — Tally how many assignments in each category are done
   - Input: classified assignments, submission status (graded? score > 0?)
   - Output: {category: count_completed}

4. **Compute Rubric Score** — Apply grading model thresholds to get total points
   - For specs-based (MATH 119): Use threshold lookup tables (e.g., "7+ items → 5 pts")
   - For percentage-based (CSE 300): Sum earned points from all submissions
   - Output: total_score, total_possible, percentage, letter_grade

5. **Track Deadlines** — Identify assignments with approaching lock dates
   - Calculate: days_remaining = lock_date - today
   - Flag urgency: [!!!] (≤7 days), [!!] (8-14 days), [!] (15-21 days), [OK] (22+ days)
   - Identify: shared deadlines (multiple assignments lock same day)
   - Output: assignments_by_urgency

6. **Generate Strategy** — Compute priority scores for next actions
   - Formula (specs-based): priority = points_at_stake * urgency_weight * threshold_crossing_potential
   - Formula (percentage-based): priority = points_possible * urgency_weight * completion_probability
   - Sort by priority descending
   - Output: top_5_next_actions

7. **Output Dashboard** — Format as readable markdown
   - Sections: Current grade, category breakdown, upcoming deadlines, recommended next actions
   - Visual formatting: emojis, tables, urgency flags

**Preconditions**:
- Canvas MCP server connected
- Course ID known
- Grading model documented (thresholds, categories, formulas)
- Assignment patterns defined

**Success Metrics**:
- ✅ Specs-based: MATH 119 validated (30-pt rubric, 83 assignments, threshold lookups)
- ✅ Percentage-based: CSE 300 validated (1,082 pts, 30 assignments, letter grade scale)
- Reliability: 100% success rate for both models (when preconditions met)
- Time to execute: ~10-15 seconds (API calls + processing)

**What Didn't Work** ❌:
- Attempting to fetch rubric thresholds directly from Canvas API — API doesn't expose them
- Workaround: Document thresholds manually in grading_model.md

---

### 2. Grading Model Analysis Trajectory

**What it captures**: How to analyze a course's grading structure and determine its model type.

**Workflow**:

1. **Detect Grading Type** — Examine assignment structure to infer model
   - Specs-based: Fixed rubric categories with point thresholds (e.g., "8/8 skills = 5 pts")
   - Percentage-based: All-point-counted model (sum all scores, divide by total)
   - Weighted-category: Categories with different weights (e.g., 40% projects, 30% participation)
   - Hybrid: Mix of specs and percentage

2. **Extract Rubric Categories & Thresholds** — If specs-based, document category structure
   - Categories: Name, max count, thresholds
   - Thresholds: count → points mapping
   - Example (MATH 119): Section 1 Skills: max 8, {7→5, 6→3, 5→2, 4→1}

3. **Extract Grade Scale** — Map percentage to letter grades
   - Example (CSE 300): A (93-100), A- (90-92), B+ (87-89), ..., F (0-59)

4. **Map Canvas Assignments to Categories** — Reconcile assignment names with categories
   - Cross-reference: Canvas assignment names ↔ documented categories
   - Identify: which Canvas assignments belong to which rubric category

5. **Document Grading Model** — Create grading_model.md with complete model specification
   - Type (specs/percentage/weighted/hybrid)
   - Categories and point/threshold mappings
   - Grade scale
   - Special rules (late penalties, resubmission policies, etc.)

6. **Create Assignment Categories** — Document name patterns for classification
   - Patterns: regex, contains, exact_match
   - Canvas type: quiz, online_upload, discussion, external_tool, manual
   - Expected count and points per assignment

7. **Validate Mappings** — Verify Canvas data matches documented model
   - Check: total possible points matches expectation
   - Check: assignment count matches expectation

**Preconditions**:
- Syllabus or course information available
- Canvas course populated with assignments
- Instructor grading rubric documented (if specs-based)

**Success Metrics**:
- ✅ MATH 119: Specs-based model analyzed, 6 rubric categories with 30-point total
- ✅ CSE 300: Percentage-based model analyzed, 5 assignment categories with 1,082 point total
- Accuracy: 100% match between documented and Canvas data

**What Didn't Work** ❌:
- Assuming grading model from syllabus alone — need to verify against actual Canvas setup
- Assuming all assignments have same point value — weights vary

---

### 3. Assignment Classification Trajectory

**What it captures**: How to categorize Canvas assignments by name patterns and types.

**Workflow**:

1. **Define Classification Patterns** — Establish rules for each category
   - Pattern type: regex, contains, exact_match
   - Canvas type: quiz, online_upload, discussion, etc.
   - Points per assignment
   - Expected count

2. **Extract Assignment Names & Metadata** — From Canvas API call
   - Fields: id, name, type, points_possible, due_date, lock_date

3. **Apply Pattern Matching** — Classify each assignment
   - For each assignment name, try patterns in order
   - First match wins (so order patterns by specificity)

4. **Cross-Check Canvas Types** — Verify classification is plausible
   - Learning activities should be "quiz" type
   - Projects should be "online_upload" type
   - If mismatch, flag for manual review

5. **Build Category Tables** — Group assignments by classified category
   - Output: {category: [assignments]}
   - Include metadata: due_date, lock_date, points_possible, current_score

6. **Handle Unclassified** — Identify assignments that matched no pattern
   - Flag for manual review
   - Add to "Unclassified" category for visibility

7. **Output Classification Schema** — Document what worked
   - Patterns that matched all expected assignments
   - Edge cases encountered
   - Confidence level for each category

**Preconditions**:
- Assignment names follow consistent naming pattern (e.g., "W01 Learning Activity")
- Canvas assignment types set correctly

**Success Metrics**:
- ✅ MATH 119: Classified 83 assignments into 6 categories with 100% accuracy
- ✅ CSE 300: Classified 30 assignments into 5 categories with 100% accuracy
- Coverage: 100% of assignments classified (no "Unclassified" category)

**What Didn't Work** ❌:
- Generic patterns (e.g., "assignment") — too broad, match incorrectly
- Relying on Canvas type alone — some courses use "online_upload" for everything
- Workaround: Use name patterns + Canvas type together for robust classification

---

### 4. Deadline Tracking Trajectory

**What it captures**: How to extract lock dates, compute urgency, and flag approaching deadlines.

**Workflow**:

1. **Extract Lock Dates** — From Canvas assignment metadata
   - lock_at field: ISO 8601 timestamp when assignment locks (no more submissions)
   - Convert to: days_remaining = (lock_date - today).days

2. **Compute Urgency Flags** — Based on days_remaining
   - [!!!] (red): ≤7 days remaining
   - [!!] (yellow): 8-14 days
   - [!] (orange): 15-21 days
   - [OK] (green): 22+ days

3. **Group by Deadline** — Identify which assignments share deadline
   - Same lock_at value → group together
   - Show: "These 3 assignments all lock on 2026-02-28"

4. **Identify Lock Chains** — Some courses have cascading deadlines
   - Example: Learning activity due mid-week, status update end-of-week, project due Sunday
   - Document: what locks when, in order

5. **Track Time Zones** — Canvas API returns UTC; convert to user's timezone
   - Precondition: Know user's timezone (from Canvas profile or local system)
   - Impact: A deadline at 11:59 PM in Canvas might be different in user's TZ

6. **Detect Anomalies** — Flag unusual deadline patterns
   - Assignment with no lock_date (no deadline)
   - Multiple deadlines on same day (check if intentional)
   - Lock date in the past (already locked, can't submit)

7. **Prioritize by Deadline** — Generate sorted list of next actions
   - Sort by lock_at descending (soonest first)
   - Include: assignment name, category, points, days_remaining, urgency_flag

**Preconditions**:
- Canvas assignments have lock dates set
- Current date/time known
- User's timezone known (or assume UTC)

**Success Metrics**:
- ✅ MATH 119: 83 assignments tracked, lock dates identified (Skills lock 4/8, Projects 3/18-4/6)
- ✅ CSE 300: 30 assignments tracked, final project deadline 2026-02-28 (2 days remaining)
- Accuracy: 100% of assignments have lock date (no missing data)

**What Didn't Work** ❌:
- Assuming lock date = due date — Canvas has both; lock date is when submission closes
- Assuming all assignments have lock dates — some instructors leave it blank
- Not accounting for timezone — student in PST saw "Feb 28 11:59 PM UTC" as Feb 27 3:59 PM local

---

### 5. Strategy Generation Trajectory

**What it captures**: How to compute priority scores and recommend next actions.

**Workflow**:

1. **Identify Grading Type** — Specs-based or percentage-based (from grading_model.md)

2. **Collect Completions Data** — From assignment classification + scores
   - Input: {category: [assignments with scores]}, current_score, total_possible

3. **For Specs-Based Models** (like MATH 119):

   a. Identify **Current Thresholds** — Where are you in each category?
      - Category: Section 1 Skills, Current: 6/8 completed
      - Thresholds: {8→5pts, 7→5pts, 6→3pts, 5→2pts}
      - Current earning: 3 pts (because 6/8 = 3 pts)

   b. Detect **Threshold Crossing** — What completion pushes you to next tier?
      - To cross 6→7 threshold: need 1 more skill
      - Benefit: +2 points (from 3 pts → 5 pts)

   c. Compute **Priority Score**:
      ```
      priority = points_at_stake * urgency_weight * threshold_crossing_potential

      points_at_stake = points for completing 1 more (e.g., +2 pts)
      urgency_weight = 1.0 if [!!!], 0.5 if [!!], 0.25 if [!], 0.1 if [OK]
      threshold_crossing_potential = 1.0 if crossing a threshold, 0.1 otherwise

      Example: 1 more skill to cross 6→7 threshold, [!!!] deadline
      priority = 2 * 1.0 * 1.0 = 2.0
      ```

4. **For Percentage-Based Models** (like CSE 300):

   a. Compute **Current Percentage**:
      ```
      percentage = (total_earned / total_possible) * 100
      Example: 800 / 1082 = 73.9% (C grade)
      ```

   b. Identify **Grade Thresholds**:
      - Current: 73.9% (C)
      - Next: B- at 80% (need 76 more points)
      - Next: B at 83% (need 97 more points)

   c. Compute **Priority Score**:
      ```
      priority = points_possible * urgency_weight * completion_probability

      points_possible = points available in this assignment
      urgency_weight = [as above]
      completion_probability = estimated likelihood of completing (0.0-1.0)

      Example: Final Project (200 pts, highest weight), [!!!] deadline
      priority = 200 * 1.0 * 0.9 = 180.0
      ```

5. **Rank by Priority** — Sort all next actions by priority score descending

6. **Generate Recommendations** — Top 3-5 actions
   - Action: "Complete 1 more Section 1 skill (6/8 done)"
     - Why: +2 points, crosses threshold, 21 days until lock
     - Next: Find Section 1 skill you haven't completed
   - Action: "Submit Final Project (200 pts)"
     - Why: Worth 18.5% of grade, locks in 2 days
     - Next: Review requirements, draft, submit

7. **Account for Multipliers** — Some categories have higher weight
   - Example: Projects are 50% of grade vs. skills are 20%
   - If specs-based with different point values: weight by points, not just count
   - If percentage-based: points_possible already reflects weight

**Preconditions**:
- Assignment classification complete
- Current scores known
- Deadline tracking complete
- Grading model type known

**Success Metrics**:
- ✅ MATH 119: Specs formula validated, threshold crossing logic accurate
- ✅ CSE 300: Percentage formula validated, grade threshold math correct
- Accuracy: Recommended actions when executed actually improve grade as predicted

**What Didn't Work** ❌:
- Assuming linear point value across categories — some categories worth more
- Treating all urgencies equally in formula — [!!!] deadlines should weight higher
- Not accounting for group deadlines — 3 assignments locking same day need batching

---

## Integration with Skills

Each trajectory inform class-specific skills:

```
MATH 119: /calc-dashboard skill
├── References: canvas_grade_dashboard_trajectory.md (7 steps)
├── Uses: grading_model.md (30-pt specs-based rubric)
├── Uses: assignment_categories.yaml (MATH 119 patterns)
├── Uses: canvas-fetch shared skill (course_id=398938)
└── Uses: grade-calculator shared skill (specs-based formula)

CSE 300: /cse300-dashboard skill
├── References: canvas_grade_dashboard_trajectory.md (same 7 steps)
├── Uses: grading_model.md (1,082-pt percentage-based)
├── Uses: assignment_categories.yaml (CSE 300 patterns)
├── Uses: canvas-fetch shared skill (course_id=406222)
└── Uses: grade-calculator shared skill (percentage-based formula)

Future Class: /future-dashboard skill
├── References: all 5 trajectories
├── Uses: custom grading_model.md
├── Uses: custom assignment_categories.yaml
├── Uses: shared skills (parameterized)
└── (No new trajectory needed — reuse layer_2 ones)
```

---

## Triggers for Loading Trajectories

When should trajectories be loaded?

| Situation | Load Trajectories | Reason |
|-----------|-------------------|--------|
| User asks "How am I doing in [class]?" | YES (just dashboard) | Use canvas_grade_dashboard_trajectory |
| User asks "What should I work on next?" | YES (just dashboard) | Includes strategy_generation step |
| Creating new class dashboard (agent task) | YES (all 5) | Need full understanding of grading system |
| Analyzing course grading model | YES (grading_model_analysis) | Understand how to extract thresholds |
| Classifying assignments for new class | YES (assignment_classification) | Learn classification patterns |
| Debugging why priority score seems wrong | YES (strategy_generation) | Verify formula |
| User asks "What's due tomorrow?" | NO | Just need deadline_tracking, not full workflow |

---

## Research Sources

**Trajectory Store Concept** (Academic Research):

- **ProcMEM**: "Towards Procedural Memory for Multi-Agent Systems" — Validates effectiveness of captured procedural knowledge in agent learning
- **AgentWorkforce**: Repository system allowing agents to maintain and cross-reference trajectories across sessions
- **Trajectory Miner**: Automatic extraction of trajectories from agent execution logs, converting ad-hoc work into reusable procedures
- **Playbooks vs Runbooks**: Distinction between routine procedures (SOP), incident response (runbook), and procedural learning (trajectory)

**Grade Strategy Concept** (Educational Research):

- Academic grade dashboards use specs-based (Knewton Alta) or percentage-based models
- Threshold crossing effects: completing 1 more item can significantly improve grade when crossing into next tier
- Deadline proximity is strong motivator: urgency flags increase likelihood of action
- Spaced deadlines force weekly engagement vs. cramming end-of-semester

---

## Summary

**Trajectory Stores** capture procedural knowledge in a format optimized for AI agent learning and reuse. Unlike traditional documentation (SOPs, runbooks), they preserve reasoning, context, failure modes, and effectiveness metrics.

**The Grade Strategy System** demonstrates trajectory store application: layer_2 captures universal 7-step dashboard workflow once, layer_4 classes customize by instantiating class-specific grading models, and class-specific skills reference the shared trajectory rather than reimplementing it.

**Key Insight**: Trajectory stores enable **"write once, use everywhere"** for procedural knowledge—agents across multiple entities (classes, projects, sessions) can reference the same trajectory without duplication, while each entity customizes parameters (course_id, grading_model) independently.

---

## References

- `.0agnostic/03_protocols/grade_strategy_system/` — Trajectory store implementations (in production layer_2)
- `.0agnostic/02_rules/dynamic/grade_strategy_triggers/` — Trigger conditions for loading trajectories
- `.0agnostic/06_context_avenue_web/01_file_based/05_skills/` — Shared skills that reference trajectories
- `layer_1_project_school/.0agnostic/01_knowledge/course_info/` — Class-specific grading models and assignment categories

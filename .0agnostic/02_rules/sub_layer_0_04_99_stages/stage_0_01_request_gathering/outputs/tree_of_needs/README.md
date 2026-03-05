---
resource_id: "d0503145-c497-4086-9350-a7c8661cbbd1"
resource_type: "readme
rule"
resource_name: "README"
---
# Needs Tree: Critical Rules Enforcement System

## Overview

This needs tree defines the complete set of requirements for implementing a system that enforces critical governance rules without subject to Anthropic's discretionary context filtering.

## Tree Structure

```
ROOT NEED: Enforce Critical Rules Without Deprioritization
│
├─ O1: RULE IDENTIFICATION & CATEGORIZATION
│  │   (How do we identify and understand what a critical rule is?)
│  │
│  └─ P1: Overcome Discretionary Disclaimer
│     ├─ 1.1: Understand discretionary wrapper mechanism
│     ├─ 1.2: Identify system prompt vs. foundational context
│     ├─ 1.3: Evaluate customization approaches
│     ├─ 1.4: Select viable approach
│     └─ 1.5: Plan implementation path
│
├─ O2: RULE MANAGEMENT
│  │   (How are critical rules stored, organized, extracted, and maintained?)
│  │
│  └─ P2: Extract Critical Rules Dynamically
│     ├─ 2.1: Parse [CRITICAL] sections from CLAUDE.md
│     ├─ 2.2: Handle rule hierarchy and inheritance
│     ├─ 2.3: Validate rule syntax and structure
│     ├─ 2.4: Cache rules for performance
│     └─ 2.5: Support rule versioning
│
├─ O3: RULE ENFORCEMENT
│  │   (How are critical rules guaranteed to execute?)
│  │
│  ├─ P3: Inject Rules into System Prompt
│  │  ├─ 3.1: Format rules for injection
│  │  ├─ 3.2: Use Agent SDK initialization
│  │  ├─ 3.3: Verify rules in system prompt
│  │  ├─ 3.4: Confirm no discretionary wrapper
│  │  └─ 3.5: Test rule immutability
│  │
│  └─ P4: Create Execution Infrastructure
│     ├─ 4.1: Build critical-rules-injector.js
│     ├─ 4.2: Create wrapper script
│     ├─ 4.3: Support multiple execution modes
│     ├─ 4.4: Add shell aliases
│     └─ 4.5: Create installation guide
│
└─ O4: RULE VERIFICATION & COMPLIANCE
   │   (How do we know critical rules are working?)
   │
   └─ P5: Ensure Reliability & Maintenance
      ├─ 5.1: Validate API call enforcement
      ├─ 5.2: Test edge cases
      ├─ 5.3: Create troubleshooting guide
      ├─ 5.4: Plan version updates
      ├─ 5.5: Create upgrade procedure
      └─ 5.6: Document limitations
```

## How to Navigate

### Starting Points

- **See the root problem**: `root_need/ROOT_NEED_enforce_critical_rules.md`
- **Pick a strategic area**: Start with any `OVERARCHING_OX.md` file
- **Explore a tactical area**: Go into any `PARENT_NEED_PX.md` file
- **Read specific requirements**: See individual `X_Y_*.md` files

### Navigation Paths

**For understanding the complete picture**:
1. Read `root_need/ROOT_NEED_enforce_critical_rules.md`
2. Read each `OVERARCHING_OX.md` (4 files)
3. Read each `PARENT_NEED_PX.md` (5 files)

**For implementation planning**:
1. Focus on O3 (Rule Enforcement)
2. Read P3 and P4 in detail
3. Cross-reference with O2 (Rule Management) for data handling

**For testing & validation**:
1. Read O4 branch (Rule Verification & Compliance)
2. Review P5 requirements
3. Check cross-references to O3 enforcement mechanism

## Requirement Hierarchy

### Level 1: Root Need
- `ROOT_NEED_enforce_critical_rules.md` - The core problem and objective

### Level 2: Overarching Branches (O1-O4)
Strategic dimensions covering what the system must do:
- **O1**: Identifies and understands critical rules
- **O2**: Stores and manages critical rules
- **O3**: Executes and enforces critical rules
- **O4**: Verifies rules are working correctly

### Level 3: Parent Tactical Needs (P1-P5)
Tactical requirement categories that implement overarching branches:
- **P1**: Solves the discretionary disclaimer problem
- **P2**: Extracts rules from source files
- **P3**: Injects rules into system prompt
- **P4**: Builds execution infrastructure
- **P5**: Validates and maintains system

### Level 4: Child Tactical Needs (1.1-5.6)
Specific, actionable requirements with:
- Clear description
- Acceptance criteria
- Dependencies on other needs
- Owner stage (which development stage handles it)

## Lookup Index

### By Branch
- `O1_rule_identification_and_categorization/` - Understanding critical rules
- `O2_rule_management/` - Managing rule storage and extraction
- `O3_rule_enforcement/` - Building and deploying the enforcement system
- `O4_rule_verification_and_compliance/` - Testing and validating the system

### By Priority
All needs listed here are required (no prioritization in request gathering stage).

### By Stage Ownership
- **Stage 0_02_research** (current): Informs O1 (understanding the problem)
- **Stage 0_03_instructions**: Defines constraints for O2-O4
- **Stage 0_04_planning**: Breaks O2-O4 into implementation tasks
- **Stage 0_05_design**: Designs architecture for O2-O3
- **Stage 0_06_development**: Implements O2-O4
- **Stage 0_07_testing**: Validates O4

## Cross-References

Each need file includes:
- **Parent**: Link to overarching and parent needs
- **Siblings**: Links to related needs in same parent
- **Dependencies**: What other needs must be met first
- **Research basis**: Links to research stage findings
- **Acceptance criteria**: How we know it's satisfied

## Next Steps

After request gathering is complete:
1. **Stage 0_03_instructions**: Define implementation constraints
2. **Stage 0_04_planning**: Create detailed task breakdown
3. **Stage 0_05_design**: Design architecture for each need
4. **Stage 0_06_development**: Implement according to needs
5. **Stage 0_07_testing**: Validate against need acceptance criteria

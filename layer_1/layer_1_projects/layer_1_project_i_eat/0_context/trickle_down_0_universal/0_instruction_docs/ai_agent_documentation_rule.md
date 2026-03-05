---
resource_id: "ccf05c25-8fcf-4d12-bc7f-85fe07ee7590"
resource_type: "document"
resource_name: "ai_agent_documentation_rule"
---
# AI AGENT DOCUMENTATION RULE

<!-- section_id: "0046b773-3f1f-47b8-9d80-5a23ea2c4235" -->
## **MANDATORY REQUIREMENT**

**ALL AI agents MUST create, update, and maintain comprehensive documentation in the `/home/dawson/dawson-workspace/code/I-eat-repo/0_context` directory for EVERY SINGLE AI TURN in EVERY SESSION, regardless of the scope or type of changes made.**

<!-- section_id: "db331b34-249d-467a-9466-9412aee54890" -->
### **TURN-BY-TURN DOCUMENTATION REQUIREMENT**

**EVERY AI TURN MUST RESULT IN DOCUMENTATION UPDATES, INCLUDING:**

1. **Code Changes**: Any modification to existing files or creation of new files
2. **Bug Fixes**: Any resolution of issues, errors, or problems
3. **Feature Implementations**: Any new functionality or enhancements
4. **System Modifications**: Any changes to configuration, settings, or architecture
5. **Testing Activities**: Any testing, validation, or verification performed
6. **Documentation Updates**: Any changes to existing documentation
7. **Analysis Activities**: Any investigation, research, or analysis conducted
8. **Planning Activities**: Any planning, design, or architectural decisions
9. **Debugging Activities**: Any troubleshooting or debugging performed
10. **Configuration Changes**: Any changes to environment, dependencies, or settings

**NO AI TURN IS EXEMPT FROM THIS REQUIREMENT.**

<!-- section_id: "00e4595a-8eec-4932-9b46-c98444f6a846" -->
### **GIT COMMIT REQUIREMENT**

**ALL AI agents MUST commit ALL changes to git at the end of EVERY SINGLE AI TURN in EVERY SESSION, regardless of the scope or type of changes made.**

**GIT COMMIT REQUIREMENTS:**
1. **Every Turn Must Commit**: No turn is complete without a git commit
2. **Comprehensive Commits**: All changes made during the turn must be committed
3. **Descriptive Commit Messages**: Clear, detailed commit messages explaining what was done
4. **Atomic Commits**: Each turn should result in a single, cohesive commit
5. **No Partial Commits**: All changes from a turn must be committed together
6. **Documentation Included**: All documentation updates must be included in the commit

<!-- section_id: "28635ba3-9c29-4871-8c60-09768fc170dc" -->
## **RULE SCOPE**

This rule applies to:
- Code modifications and implementations
- Bug fixes and issue resolutions
- Feature development and enhancements
- Integration testing and validation
- System architecture changes
- Performance optimizations
- Security improvements
- Database schema modifications
- API changes and updates

<!-- section_id: "e03b8747-3f8c-4f42-ad12-abe63ae9dfee" -->
## **REQUIRED DOCUMENTATION ACTIONS**

<!-- section_id: "a9db5f49-c51c-4ba7-ba5c-85132dbaa325" -->
### **1. IMMEDIATE DOCUMENTATION (Every AI Turn)**

For EVERY SINGLE AI TURN in EVERY SESSION, agents MUST:

1. **Create/Update Change Log**: Document what was changed, why, and when
2. **Update Technical Documentation**: Reflect changes in relevant technical docs
3. **Maintain Test Documentation**: Update test results and validation status
4. **Preserve Decision History**: Document reasoning behind technical decisions
5. **Update Status Reports**: Keep current status of all system components
6. **Document Turn Activities**: Record all activities performed during the turn
7. **Update Session Log**: Maintain session-level documentation
8. **Preserve Context**: Document context and reasoning for future turns
9. **Commit to Git**: Commit all changes with descriptive commit message
10. **Verify Git Status**: Ensure all changes are properly committed

<!-- section_id: "b2991304-a5c4-407a-ab3b-817271228ee6" -->
### **2. DOCUMENTATION STRUCTURE**

All documentation must follow the established hierarchy in `/home/dawson/dawson-workspace/code/I-eat-repo/0_context`:

```
0_context/
├── trickle_down_0_universal/0_instruction_docs/     # Universal rules and instructions
├── trickle_down_1_project/                          # Project-specific documentation
├── trickle_down_2_implementation/                   # Implementation details
├── trickle_down_3_testing/                          # Testing documentation
├── trickle_down_4_deployment/                       # Deployment and operations
└── MASTER_DOCUMENTATION_INDEX.md                    # Master index
```

<!-- section_id: "6d4e00aa-6620-40a4-bcf0-69391154eda2" -->
### **3. REQUIRED DOCUMENTATION TYPES**

#### **A. Turn-by-Turn Change Logs**
- **File**: `trickle_down_1_project/change_logs/YYYY-MM-DD_session_[session_id]_turn_[turn_number].md`
- **Content**: Detailed log of all changes made during the specific AI turn
- **Format**: Session ID, Turn Number, Date, changes made, files affected, reasoning, impact
- **Example**: `2025-01-27_session_001_turn_003.md`

#### **B. Bug Fix Documentation**
- **File**: `trickle_down_3_testing/bug_reports/YYYY-MM-DD_bug_fixes.md`
- **Content**: Bug descriptions, root causes, solutions, validation
- **Format**: Bug ID, description, cause, solution, test results

#### **C. Integration Test Results**
- **File**: `trickle_down_3_testing/integration_tests/YYYY-MM-DD_test_results.md`
- **Content**: Test execution, results, coverage, issues found
- **Format**: Test suite, results, coverage percentage, issues

#### **D. Technical Implementation Notes**
- **File**: `trickle_down_2_implementation/technical_notes/YYYY-MM-DD_implementation.md`
- **Content**: Technical decisions, architecture changes, code patterns
- **Format**: Component, changes, rationale, impact

#### **E. Session Activity Logs**
- **File**: `trickle_down_1_project/session_logs/YYYY-MM-DD_session_[session_id].md`
- **Content**: Complete log of all activities performed during the session
- **Format**: Turn-by-turn breakdown, cumulative changes, session summary
- **Example**: `2025-01-27_session_001.md`

#### **F. Turn Activity Records**
- **File**: `trickle_down_1_project/turn_logs/YYYY-MM-DD_session_[session_id]_turn_[turn_number].md`
- **Content**: Detailed record of activities performed in a specific turn
- **Format**: Activities performed, tools used, decisions made, outcomes
- **Example**: `2025-01-27_session_001_turn_003.md`

<!-- section_id: "2a9de270-0873-4a70-ae9f-259e9d87cda8" -->
### **4. DOCUMENTATION STANDARDS**

#### **A. File Naming Convention**
```
YYYY-MM-DD_[category]_[brief_description].md
```

Examples:
- `2025-01-27_bug_fixes_realtime_sync_transaction_logging.md`
- `2025-01-27_integration_tests_comprehensive_validation.md`
- `2025-01-27_implementation_points_service_enhancements.md`

#### **B. Content Structure**
```markdown
# [Title]

## **DATE**: YYYY-MM-DD
## **AI AGENT**: [Agent Name/ID]
## **CATEGORY**: [Bug Fix/Feature/Test/etc.]

## **SUMMARY**
Brief description of changes made.

## **DETAILS**
Detailed explanation of what was done.

## **FILES AFFECTED**
- file1.js: description of changes
- file2.js: description of changes

## **TESTING**
- Tests performed
- Results obtained
- Issues found/resolved

## **IMPACT**
- System impact
- User impact
- Performance impact

## **NEXT STEPS**
- Follow-up actions needed
- Future improvements
- Monitoring requirements
```

<!-- section_id: "cbefa906-6216-48c5-9ac2-fe5eedd7531c" -->
### **5. MANDATORY DOCUMENTATION CHECKLIST**

For EVERY AI turn, agents MUST verify:

- [ ] Change log created/updated
- [ ] Relevant technical docs updated
- [ ] Test documentation updated
- [ ] Master index updated (if new files created)
- [ ] All file paths are absolute and correct
- [ ] Documentation follows established format
- [ ] All changes are properly categorized
- [ ] Impact assessment completed
- [ ] All changes committed to git
- [ ] Git commit message is descriptive and accurate
- [ ] Git status shows no uncommitted changes
- [ ] Commit includes all documentation updates

<!-- section_id: "8dae185f-c5c1-4bc6-af1e-98ead04690b2" -->
### **6. DOCUMENTATION VALIDATION**

Before completing any AI turn, agents MUST:

1. **Verify Documentation Completeness**: All changes documented
2. **Check File Structure**: Proper directory placement
3. **Validate Content Quality**: Clear, comprehensive, accurate
4. **Update Master Index**: New files referenced
5. **Ensure Consistency**: Format and style consistency
6. **Commit All Changes**: Execute git commit with descriptive message
7. **Verify Git Status**: Confirm no uncommitted changes remain
8. **Validate Commit**: Ensure commit includes all changes and documentation

<!-- section_id: "9bb39464-3753-40f9-a985-ed2ef379a71d" -->
## **BENEFITS OF THIS RULE**

- **Complete Audit Trail**: Every change tracked and documented
- **Knowledge Preservation**: Technical decisions and reasoning preserved
- **Team Collaboration**: Clear communication of changes and status
- **Debugging Support**: Historical context for troubleshooting
- **Project Continuity**: New team members can understand project evolution
- **Quality Assurance**: Documentation forces thorough analysis
- **Compliance**: Meets documentation standards for professional development
- **Version Control**: Complete git history of all changes
- **Rollback Capability**: Ability to revert to any previous state
- **Change Tracking**: Clear visibility into what changed and when
- **Collaborative Development**: Multiple agents can work on same project
- **Backup and Recovery**: All changes safely stored in git repository

<!-- section_id: "70f99b9d-7ddf-450b-9149-a2d0a1daa162" -->
## **ENFORCEMENT**

This rule is **MANDATORY** and **NON-NEGOTIABLE**. 

**Failure to comply with this rule will result in:**
- Incomplete AI turn completion
- Documentation gaps that impact project continuity
- Loss of valuable technical knowledge
- Reduced team collaboration effectiveness
- Loss of version control history
- Inability to track changes over time
- Risk of data loss without git commits
- Broken project continuity

**This rule takes precedence over all other tasks and must be completed before marking any AI turn as complete.**

<!-- section_id: "1fc7bb26-7589-46ae-977b-8b9ad497fde0" -->
### **GIT COMMIT MESSAGE STANDARDS**

**Every git commit must follow this format:**
```
[CATEGORY] Brief description of changes

Detailed description of what was changed and why:
- Specific changes made
- Files affected
- Reasoning behind changes
- Impact of changes

Session: [session_id]
Turn: [turn_number]
Date: YYYY-MM-DD
```

**Example:**
```
[BUGFIX] Fix real-time synchronization and transaction logging

Fixed two critical bugs in the I-Eat application:
- Enabled real-time for students table in Supabase
- Fixed transaction logging schema mismatch in points service
- Added proper user authentication for transaction records
- Improved error handling in PointsManager component

Session: 001
Turn: 003
Date: 2025-01-27
```

---

**This rule is effective immediately and applies to all AI agents working on this project.**

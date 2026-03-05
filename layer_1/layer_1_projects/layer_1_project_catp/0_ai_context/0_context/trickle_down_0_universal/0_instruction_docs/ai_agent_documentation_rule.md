---
resource_id: "e9cec6eb-0212-43ef-98fe-d47088783f0f"
resource_type: "document"
resource_name: "ai_agent_documentation_rule"
---
# AI AGENT DOCUMENTATION RULE

<!-- section_id: "66442297-f627-4bc2-942f-4cbe5ea35ae0" -->
## **MANDATORY REQUIREMENT**

**ALL AI agents MUST create, update, and maintain comprehensive documentation in the `/home/dawson/dawson-workspace/code/I-eat-repo/0_context` directory for EVERY SINGLE AI TURN in EVERY SESSION, regardless of the scope or type of changes made.**

<!-- section_id: "e1f4b729-8da9-4892-897f-07710a819591" -->
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

<!-- section_id: "644d5376-01cc-4981-8233-e096d3d34f11" -->
### **GIT COMMIT REQUIREMENT**

**ALL AI agents MUST commit ALL changes to git at the end of EVERY SINGLE AI TURN in EVERY SESSION, regardless of the scope or type of changes made.**

**GIT COMMIT REQUIREMENTS:**
1. **Every Turn Must Commit**: No turn is complete without a git commit
2. **Comprehensive Commits**: All changes made during the turn must be committed
3. **Descriptive Commit Messages**: Clear, detailed commit messages explaining what was done
4. **Atomic Commits**: Each turn should result in a single, cohesive commit
5. **No Partial Commits**: All changes from a turn must be committed together
6. **Documentation Included**: All documentation updates must be included in the commit

<!-- section_id: "51ae963f-ac49-4aea-b458-6e0489375fb8" -->
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

<!-- section_id: "0d7d7b85-a3de-4e6e-8dba-c805d295e023" -->
## **REQUIRED DOCUMENTATION ACTIONS**

<!-- section_id: "77f4dfbd-31ab-4a99-bb78-ce8fa48c262d" -->
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

<!-- section_id: "c3bb44e8-35fe-4a0d-bb93-8fe2883777ae" -->
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

<!-- section_id: "ba47eac7-d22d-432d-922e-487591f72856" -->
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

<!-- section_id: "2738d75b-74e9-41af-81c8-87e80a6467e7" -->
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

<!-- section_id: "f232be07-d437-4e6e-aa3c-52d515930407" -->
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

<!-- section_id: "0251cefe-01fe-498e-84ac-5b648927e2ef" -->
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

<!-- section_id: "a793efbc-1422-4818-91c5-99d6018c79c4" -->
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

<!-- section_id: "99c23068-dd62-4b98-bcf1-67c9484d0f0c" -->
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

<!-- section_id: "989669ee-7083-4e54-a6ce-97619e24c7e4" -->
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

# GIT COMMIT AND SYNC RULE

## **MANDATORY REQUIREMENTS**

**ALL AI agents MUST:**

1. **Pull from cloud at the START of EVERY SESSION** - Sync with remote repository before beginning any work
2. **Pull from cloud at the START of EVERY AI TURN** - Ensure local repository is up to date before making changes
3. **Commit ALL changes to git at the END of EVERY SINGLE AI TURN** - Track all changes in version control
4. **Push to cloud at the END of EVERY SINGLE AI TURN** - Sync all commits to remote repository immediately

**NO EXCEPTIONS. NO AI TURN OR SESSION IS EXEMPT FROM THESE REQUIREMENTS.**

## **RULE SCOPE**

This rule applies to:
- **Session initialization** - Pull from cloud before starting any session
- **Turn initialization** - Pull from cloud before starting any turn
- Code modifications and implementations
- Bug fixes and issue resolutions
- Feature development and enhancements
- Documentation updates and changes
- Configuration modifications
- Testing activities and results
- Analysis and research activities
- Planning and design decisions
- Debugging and troubleshooting
- Any file changes whatsoever
- **Turn completion** - Commit and push all changes before ending turn

**NO AI TURN OR SESSION IS EXEMPT FROM THESE REQUIREMENTS.**

## **GIT SYNC AND COMMIT REQUIREMENTS**

### **1. MANDATORY PULL ACTIONS (START OF SESSION/TURN)**

**At the START of EVERY SESSION, agents MUST:**

1. **Check Current Branch**: `git branch` to identify current branch
2. **Fetch Latest Changes**: `git fetch origin` to get latest from remote
3. **Pull Latest Changes**: `git pull origin <branch>` to sync local repository
4. **Verify Sync**: `git status` to confirm local is up to date with remote
5. **Handle Conflicts**: If conflicts exist, resolve them before proceeding

**At the START of EVERY AI TURN, agents MUST:**

1. **Fetch Latest Changes**: `git fetch origin` to check for remote updates
2. **Pull Latest Changes**: `git pull origin <branch>` to sync local repository
3. **Verify Sync**: `git status` to confirm local is up to date with remote
4. **Handle Conflicts**: If conflicts exist, resolve them before making changes

**CRITICAL**: Never start work without pulling first. Always ensure local repository matches remote before making any changes.

### **2. MANDATORY COMMIT AND SYNC ACTIONS (END OF TURN)**

For EVERY AI turn, agents MUST:

1. **Stage All Changes**: `git add .` to stage all modified files
2. **Review Changes**: `git status` to verify all changes are staged
3. **Create Descriptive Commit**: Use proper commit message format
4. **Execute Commit**: `git commit -m "message"` with detailed message
5. **Verify Commit**: `git log --oneline -1` to confirm commit was created
6. **Check Clean Status**: `git status` to ensure working directory is clean
7. **Sync to Cloud (MANDATORY)**: `git push origin <branch>` to push all commits to remote repository
8. **Verify Sync**: `git status` to confirm branch is up to date with remote

### **3. COMMIT MESSAGE FORMAT**

**Required Format:**
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

**Categories:**
- `[BUGFIX]` - Bug fixes and issue resolutions
- `[FEATURE]` - New features and enhancements
- `[DOCS]` - Documentation updates and changes
- `[TEST]` - Testing activities and test results
- `[REFACTOR]` - Code refactoring and improvements
- `[CONFIG]` - Configuration and setup changes
- `[ANALYSIS]` - Analysis and research activities
- `[PLANNING]` - Planning and design decisions
- `[DEBUG]` - Debugging and troubleshooting
- `[INTEGRATION]` - Integration and system changes

### **4. COMMIT MESSAGE EXAMPLES**

#### **Bug Fix Example:**
```
[BUGFIX] Fix real-time synchronization and transaction logging

Fixed two critical bugs in the I-Eat application:
- Enabled real-time for students table in Supabase dashboard
- Fixed transaction logging schema mismatch in points service
- Added proper user authentication for transaction records
- Improved error handling in PointsManager component

Files affected:
- website/src/services/points.js
- Supabase configuration (students table)

Session: 001
Turn: 003
Date: 2025-01-27
```

#### **Feature Implementation Example:**
```
[FEATURE] Add comprehensive integration testing framework

Implemented comprehensive integration testing system:
- Created detailed test documentation structure
- Added real-time synchronization testing
- Implemented cross-tab testing scenarios
- Added performance and scalability testing

Files affected:
- 0_context/trickle_down_3_testing/integration_tests/
- 0_context/trickle_down_3_testing/bug_reports/
- 0_context/trickle_down_2_implementation/technical_notes/

Session: 001
Turn: 004
Date: 2025-01-27
```

#### **Documentation Update Example:**
```
[DOCS] Update AI agent documentation rules

Enhanced documentation requirements for AI agents:
- Added turn-by-turn documentation requirement
- Specified git commit requirements
- Created comprehensive documentation checklist
- Added session and turn tracking

Files affected:
- 0_context/trickle_down_0_universal/0_instruction_docs/ai_agent_documentation_rule.md
- 0_context/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md

Session: 001
Turn: 005
Date: 2025-01-27
```

### **5. PULL VALIDATION CHECKLIST (START OF SESSION/TURN)**

Before starting any work, agents MUST verify:

- [ ] **Fetched latest changes** (`git fetch origin`)
- [ ] **Pulled latest changes** (`git pull origin <branch>`)
- [ ] **Local repository is up to date** (git status shows "Your branch is up to date")
- [ ] **No uncommitted local changes** (working directory clean or changes committed)
- [ ] **No merge conflicts** (all conflicts resolved if they existed)
- [ ] **Current branch identified** (know which branch you're working on)

**CRITICAL**: Do not proceed with any work until all pull requirements are met.

### **6. COMMIT AND SYNC VALIDATION CHECKLIST (END OF TURN)**

Before completing any AI turn, agents MUST verify:

- [ ] All changes are staged (`git add .`)
- [ ] Git status shows no unstaged changes
- [ ] Commit message follows required format
- [ ] Commit message includes session and turn information
- [ ] Commit message describes all changes made
- [ ] Commit is successfully created
- [ ] Working directory is clean after commit
- [ ] All documentation updates are included in commit
- [ ] **Changes are pushed to remote repository** (`git push origin <branch>`)
- [ ] **Git status confirms branch is up to date with remote**
- [ ] **No local commits ahead of remote** (all changes synced to cloud)

### **7. PULL COMMANDS (START OF SESSION/TURN)**

**Standard Pull Sequence (MANDATORY AT START OF EVERY SESSION AND TURN):**
```bash
# Identify current branch
git branch
# OR
git branch --show-current

# Fetch latest changes from remote
git fetch origin

# Pull latest changes (merge with local)
git pull origin main
# OR if on different branch:
# git pull origin <branch-name>

# Verify sync status
git status
# Should show: "Your branch is up to date with 'origin/main'"

# If conflicts occur, resolve them:
# 1. Review conflicts: git status
# 2. Open conflicted files and resolve
# 3. Stage resolved files: git add <file>
# 4. Complete merge: git commit
# 5. Verify: git status
```

**CRITICAL**: The `git pull` step is **MANDATORY** at the start of every session and every turn. Never start work without pulling first.

### **8. COMMIT AND SYNC COMMANDS (END OF TURN)**

**Standard Commit and Sync Sequence (MANDATORY FOR EVERY TURN):**
```bash
# Stage all changes
git add .

# Check status
git status

# Create commit with message
git commit -m "[CATEGORY] Brief description

Detailed description of what was changed and why:
- Specific changes made
- Files affected
- Reasoning behind changes
- Impact of changes

Session: [session_id]
Turn: [turn_number]
Date: YYYY-MM-DD"

# Verify commit was created
git log --oneline -1

# Confirm clean working directory
git status

# SYNC TO CLOUD (MANDATORY - NO EXCEPTIONS)
git push origin main
# OR if on different branch:
# git push origin <branch-name>

# Verify sync completed
git status
# Should show: "Your branch is up to date with 'origin/main'"
```

**CRITICAL**: The `git push` step is **MANDATORY** and **NON-NEGOTIABLE**. Every turn must end with all changes synced to the cloud repository. No turn is complete until changes are pushed.

### **9. SPECIAL CASES**

#### **No Changes Made**
Even if no code changes were made, if any documentation was updated or any analysis was performed, a commit is still required:

```
[ANALYSIS] Investigate system performance and document findings

Conducted comprehensive analysis of system performance:
- Analyzed real-time synchronization performance
- Documented findings in technical notes
- Updated integration test documentation
- No code changes required

Session: 001
Turn: 006
Date: 2025-01-27
```

#### **Documentation Only Changes**
```
[DOCS] Update bug fix documentation with validation results

Updated bug fix documentation with comprehensive validation:
- Added detailed test results
- Documented performance metrics
- Updated impact assessment
- Added next steps and monitoring requirements

Files affected:
- 0_context/trickle_down_3_testing/bug_reports/2025-01-27_bug_fixes_realtime_sync_transaction_logging.md

Session: 001
Turn: 007
Date: 2025-01-27
```

### **10. SYNC AND COMMIT FREQUENCY**

**Every AI Turn Must Result in a Commit:**
- No exceptions
- No batching of changes across turns
- No skipping commits for "minor" changes
- No deferring commits to "later"

**Pull Timing:**
- **At the START of every session** - before any work begins
- **At the START of every AI turn** - before making any changes
- **NO EXCEPTIONS** - always pull before starting work

**Commit and Sync Timing:**
- At the end of each AI turn
- Before marking turn as complete
- After all documentation is updated
- After all changes are made
- **IMMEDIATELY after commit** - push to cloud without delay
- **NO EXCEPTIONS** - every turn must end with both commit AND push

**Complete Workflow:**
1. **START OF SESSION**: Pull from cloud → Start work
2. **START OF EACH TURN**: Pull from cloud → Make changes
3. **END OF EACH TURN**: Commit changes → Push to cloud → Turn complete

### **11. COMMIT QUALITY STANDARDS**

**Commit Messages Must Be:**
- Descriptive and clear
- Include all relevant details
- Follow the required format
- Include session and turn information
- Explain the reasoning behind changes
- List all affected files

**Commits Must Include:**
- All code changes made during the turn
- All documentation updates
- All configuration changes
- All test results and validation
- All analysis and research findings

## **BENEFITS OF THIS RULE**

- **Complete Version History**: Every change tracked in git
- **Cloud Backup**: All changes immediately synced to remote repository
- **Rollback Capability**: Ability to revert to any previous state
- **Change Tracking**: Clear visibility into what changed and when
- **Collaborative Development**: Multiple agents can work on same project with real-time sync
- **Backup and Recovery**: All changes safely stored in git repository and cloud
- **Audit Trail**: Complete history of all activities available in cloud
- **Project Continuity**: New agents can understand project evolution from cloud repository
- **Quality Assurance**: Forces thorough analysis before committing
- **No Data Loss**: Changes are never lost due to local-only commits
- **Cross-Device Access**: Changes available from any machine via cloud repository

## **ENFORCEMENT**

This rule is **MANDATORY** and **NON-NEGOTIABLE**.

**Failure to comply with this rule will result in:**
- Incomplete AI turn completion
- Loss of version control history
- Inability to track changes over time
- Risk of data loss without git commits and cloud sync
- Broken project continuity
- Reduced collaborative development capability
- **Loss of changes if local machine fails** (without cloud sync)
- **Inability for other agents to access latest changes**
- **Version conflicts when multiple agents work on same project**

**This rule takes precedence over all other tasks and must be completed before marking any AI turn as complete.**

**CRITICAL**: Both commit AND push are required. A turn is NOT complete until:
1. All changes are committed to git
2. All commits are pushed to the remote repository
3. Git status confirms branch is up to date with remote

---

**This rule is effective immediately and applies to all AI agents working on this project.**

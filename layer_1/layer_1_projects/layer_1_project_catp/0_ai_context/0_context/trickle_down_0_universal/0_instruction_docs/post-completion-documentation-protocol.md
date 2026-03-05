---
resource_id: "1a7f9159-05a7-48a0-a7ce-ab1a2f022a1c"
resource_type: "document"
resource_name: "post-completion-documentation-protocol"
---
# Post-Completion Documentation Protocol
*Universal AI Agent Documentation Standards*

<!-- section_id: "0da07e28-0632-4b55-af72-c0f0137eb062" -->
## 📋 Document Organization Structure

<!-- section_id: "1a737875-f9be-4fc7-8722-2df025f76671" -->
### **Directory Structure**
Each trickle-down level contains three numbered subdirectories:
- `0_instruction_docs/` - How-to guides, protocols, and procedures
- `1_status_progress_docs/` - Current status, progress reports, and active work
- `2_archive_docs/` - Completed work, resolutions, and historical documentation

<!-- section_id: "6321d716-e219-4935-92ac-9cabb8df46e3" -->
### **File Naming Convention**
Based on web search best practices, use this standardized format:
```
YYYYMMDD_ProjectName_DocumentType_Version.md
```

**Examples:**
- `20251023_GoogleSignIn_Resolution_v1.0.md`
- `20251023_FirebaseSetup_Status_v1.0.md`
- `20251023_Authentication_Implementation_v1.0.md`

<!-- section_id: "d07a45b2-50be-47b5-aa6a-5c9b2503ce13" -->
## 📁 Document Types by Directory

<!-- section_id: "fd2de4db-9d51-4825-9f34-3cf6e1e10203" -->
### **0_instruction_docs/**
**Purpose**: How-to guides, protocols, and procedures
**Content Types**:
- Setup instructions
- Configuration guides
- Workflow procedures
- Best practices
- Troubleshooting guides

**Examples**:
- `terminal-tool-replacement.md`
- `manual-steps-automation.md`
- `firebase-setup-guide.md`

<!-- section_id: "a3ad6f2f-c8d1-41e8-9eb2-fb3dee45e42b" -->
### **1_status_progress_docs/**
**Purpose**: Current status, progress reports, and active work
**Content Types**:
- Current project status
- Progress reports
- Active work tracking
- Blocker documentation
- Next steps planning

**Examples**:
- `20251023_ProjectStatus_Weekly_v1.0.md`
- `20251023_Authentication_Progress_v1.0.md`
- `20251023_Blockers_Current_v1.0.md`

<!-- section_id: "4652d7a0-e2c1-46d7-bf63-a140b8f97874" -->
### **2_archive_docs/**
**Purpose**: Completed work, resolutions, and historical documentation
**Content Types**:
- Resolution documents
- Implementation summaries
- Completed feature documentation
- Historical progress reports
- Lessons learned

**Examples**:
- `20251023_GoogleSignIn_Resolution_v1.0.md`
- `20251023_FirebaseSetup_Implementation_v1.0.md`
- `20251023_Authentication_Completion_v1.0.md`

<!-- section_id: "05b6c07d-8475-4679-9ea7-1c5daf8d07c2" -->
## 🔄 Workflow Management

<!-- section_id: "374b28ec-7f26-40c4-9f72-fa857b9f0461" -->
### **Task Lifecycle**
1. **Planning**: Create document in `0_instruction_docs/` or `1_status_progress_docs/`
2. **Active Work**: Move to `1_status_progress_docs/` with progress updates
3. **Completion**: Move to `2_archive_docs/` with final resolution

<!-- section_id: "f7e5ee75-3428-4a12-a2be-262d13ac0904" -->
### **Document Movement Protocol**
```bash
# Move from planning to active work
mv 0_instruction_docs/task-name.md 1_status_progress_docs/YYYYMMDD_TaskName_Status_v1.0.md

# Move from active work to completion
mv 1_status_progress_docs/YYYYMMDD_TaskName_Status_v1.0.md 2_archive_docs/YYYYMMDD_TaskName_Resolution_v1.0.md
```

<!-- section_id: "3c600872-cb3e-42ce-871d-48d98be7fd1a" -->
## 📝 Document Templates

<!-- section_id: "61206ad8-0f01-4773-9115-1d1233a9a3b2" -->
### **Resolution Document Template**
```markdown
# [Feature Name] Resolution
*Date: YYYY-MM-DD*

## 🎯 Problem Statement
Brief description of the problem that was solved.

## 🔍 Investigation
What was investigated and discovered.

## ✅ Solution Implemented
Detailed description of the solution.

## 📊 Results
Final status and outcomes.

## 🚀 Next Steps
Any follow-up actions required.

## 📁 Related Files
Links to relevant code, documentation, or resources.
```

<!-- section_id: "463af0ef-0fdb-4c65-bc76-1e2f5fd2fff5" -->
### **Status Document Template**
```markdown
# [Feature Name] Status
*Date: YYYY-MM-DD*

## 📋 Current Status
Current state of the work.

## ✅ Completed
What has been completed.

## 🔄 In Progress
What is currently being worked on.

## ⏳ Pending
What is waiting to be done.

## 🚧 Blockers
Any issues preventing progress.

## 🎯 Next Steps
Immediate next actions.
```

<!-- section_id: "d359a205-a4e8-4adb-b4bb-db0cd74dd90f" -->
## 🎯 Level-Specific Guidelines

<!-- section_id: "7125b898-fd2d-4cfa-835f-b6ead2407ffc" -->
### **trickle_down_0_universal_instructions/**
- Universal rules and protocols
- Cross-project guidelines
- AI agent instructions

<!-- section_id: "4b0ab566-5bbc-45ad-95f5-867e0b302670" -->
### **trickle_down_0.5_setup/**
- Environment setup documentation
- Configuration systems
- Setup procedures

<!-- section_id: "7e077483-4a7c-4263-ad55-eca31c9ca539" -->
### **trickle_down_0.75_universal_tools/**
- Universal tool documentation
- Tool usage guides
- Tool implementation status

<!-- section_id: "3dc6dbdc-efbb-42ac-828e-14ff8e5b9e2f" -->
### **trickle_down_1_project/**
- Project-specific constitution
- Project standards and principles
- Project status and progress

<!-- section_id: "4227b7ab-5067-4378-9b80-e7d760bf5544" -->
### **trickle_down_1.5_project_tools/**
- Project-specific tool implementations
- Tool usage and status
- Tool development progress

<!-- section_id: "e4f43b3c-ca6f-4a49-9871-413f9ccd002d" -->
### **trickle_down_2_features/**
- Feature specifications
- Feature implementation status
- Feature completion documentation

<!-- section_id: "833535e6-2fa2-4fd1-95fd-61a721e2304b" -->
### **trickle_down_3_components/**
- Component specifications
- Component implementation status
- Component completion documentation

<!-- section_id: "85d94b73-6ffc-41de-ba61-560c6e5604cf" -->
## 🔍 Maintenance Guidelines

<!-- section_id: "8a98fa0c-d20f-45bf-b8a3-f8761cbfb5e9" -->
### **Regular Reviews**
- Weekly review of `status_progress_docs/`
- Monthly review of `archive/` for completeness
- Quarterly review of `instruction_docs/` for accuracy

<!-- section_id: "e1286559-cf8e-4361-b5b4-845d5bd2da0e" -->
### **Version Control**
- Use semantic versioning (v1.0, v1.1, v2.0)
- Document changes in version history
- Maintain backward compatibility when possible

<!-- section_id: "1b072ed0-cefd-43d5-a00d-ce6d2a23318c" -->
### **Cross-References**
- Link related documents across levels
- Maintain consistent terminology
- Update references when moving documents

---

**This protocol ensures consistent, organized, and maintainable documentation across all trickle-down levels.**

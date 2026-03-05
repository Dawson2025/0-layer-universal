---
resource_id: "ac9c8e68-25b7-4698-ac31-9e2d39c73401"
resource_type: "document"
resource_name: "post-completion-documentation-protocol"
---
# Post-Completion Documentation Protocol
*Universal AI Agent Documentation Standards*

<!-- section_id: "42e499e6-6fb8-4b4a-8d9d-688701bd868e" -->
## 📋 Document Organization Structure

<!-- section_id: "5f39a48e-962a-4bf8-bceb-c12ae4e3bd62" -->
### **Directory Structure**
Each trickle-down level contains three numbered subdirectories:
- `0_instruction_docs/` - How-to guides, protocols, and procedures
- `1_status_progress_docs/` - Current status, progress reports, and active work
- `2_archive_docs/` - Completed work, resolutions, and historical documentation

<!-- section_id: "b494e018-5ffa-4f76-a373-4c32b7a039ec" -->
### **File Naming Convention**
Based on web search best practices, use this standardized format:
```
YYYYMMDD_ProjectName_DocumentType_Version.md
```

**Examples:**
- `20251023_GoogleSignIn_Resolution_v1.0.md`
- `20251023_FirebaseSetup_Status_v1.0.md`
- `20251023_Authentication_Implementation_v1.0.md`

<!-- section_id: "7bcf4a13-dc67-4fef-af8f-515d9eb678b9" -->
## 📁 Document Types by Directory

<!-- section_id: "f090b6e1-1147-4e02-b601-fb2a70f22ae0" -->
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

<!-- section_id: "56d2866a-263a-464f-a079-fc08d68c5650" -->
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

<!-- section_id: "6ba2e6a3-f052-4ca8-a9be-b39ff997a079" -->
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

<!-- section_id: "605c56b9-10b6-441d-9ca4-8543121da040" -->
## 🔄 Workflow Management

<!-- section_id: "f408dfc6-dfc1-435d-995e-ec29ba0dc144" -->
### **Task Lifecycle**
1. **Planning**: Create document in `0_instruction_docs/` or `1_status_progress_docs/`
2. **Active Work**: Move to `1_status_progress_docs/` with progress updates
3. **Completion**: Move to `2_archive_docs/` with final resolution

<!-- section_id: "837a414c-41c2-40d5-8d28-7223e0086fee" -->
### **Document Movement Protocol**
```bash
# Move from planning to active work
mv 0_instruction_docs/task-name.md 1_status_progress_docs/YYYYMMDD_TaskName_Status_v1.0.md

# Move from active work to completion
mv 1_status_progress_docs/YYYYMMDD_TaskName_Status_v1.0.md 2_archive_docs/YYYYMMDD_TaskName_Resolution_v1.0.md
```

<!-- section_id: "b050048e-f3eb-4bc5-8ec1-adaf5a1013eb" -->
## 📝 Document Templates

<!-- section_id: "e5cf522d-3206-4666-90c5-cae5b0639e08" -->
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

<!-- section_id: "a39005d0-72db-4b34-ae28-2e1b7f6e647f" -->
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

<!-- section_id: "9871b280-924b-4583-ba8e-49fe6a43e296" -->
## 🎯 Level-Specific Guidelines

<!-- section_id: "f42ae5cd-c71d-4c0d-9409-f0e3691830ca" -->
### **trickle_down_0_universal_instructions/**
- Universal rules and protocols
- Cross-project guidelines
- AI agent instructions

<!-- section_id: "95b2afc2-5e3a-439e-9983-b26d30a44df9" -->
### **trickle_down_0.5_setup/**
- Environment setup documentation
- Configuration systems
- Setup procedures

<!-- section_id: "10c36861-df63-4434-95ca-8116033a5071" -->
### **trickle_down_0.75_universal_tools/**
- Universal tool documentation
- Tool usage guides
- Tool implementation status

<!-- section_id: "40a07a5e-3b61-4931-b0db-14b733fdb418" -->
### **trickle_down_1_project/**
- Project-specific constitution
- Project standards and principles
- Project status and progress

<!-- section_id: "aa39786c-c2f0-4153-823d-8a2c35bdbecb" -->
### **trickle_down_1.5_project_tools/**
- Project-specific tool implementations
- Tool usage and status
- Tool development progress

<!-- section_id: "590f7516-37b1-4ec6-8a59-4c334d6631d2" -->
### **trickle_down_2_features/**
- Feature specifications
- Feature implementation status
- Feature completion documentation

<!-- section_id: "17e0825f-dfda-4f60-8c4f-ea06b0d723c8" -->
### **trickle_down_3_components/**
- Component specifications
- Component implementation status
- Component completion documentation

<!-- section_id: "c9cde24c-8c9a-4e63-9c2a-c1b9d71636d3" -->
## 🔍 Maintenance Guidelines

<!-- section_id: "ce218896-5539-44d3-a5e0-e6841c969c1e" -->
### **Regular Reviews**
- Weekly review of `status_progress_docs/`
- Monthly review of `archive/` for completeness
- Quarterly review of `instruction_docs/` for accuracy

<!-- section_id: "a8c3f9ab-58ca-4061-96ae-768712ded663" -->
### **Version Control**
- Use semantic versioning (v1.0, v1.1, v2.0)
- Document changes in version history
- Maintain backward compatibility when possible

<!-- section_id: "38abccda-bef3-471f-8cdb-ff706889d973" -->
### **Cross-References**
- Link related documents across levels
- Maintain consistent terminology
- Update references when moving documents

---

**This protocol ensures consistent, organized, and maintainable documentation across all trickle-down levels.**

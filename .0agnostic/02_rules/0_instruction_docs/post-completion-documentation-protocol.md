---
resource_id: "56206cd5-69bc-4354-83b1-75aa906a99c6"
resource_type: "rule"
resource_name: "post-completion-documentation-protocol"
---
# Post-Completion Documentation Protocol
*Universal AI Agent Documentation Standards*

<!-- section_id: "2716016b-0253-49e7-83e4-1b52b5aa8267" -->
## 📋 Document Organization Structure

<!-- section_id: "f56dcc5f-6f30-49a2-b7c6-a9ff12046978" -->
### **Directory Structure**
Each trickle-down level contains three numbered subdirectories:
- `0_instruction_docs/` - How-to guides, protocols, and procedures
- `1_status_progress_docs/` - Current status, progress reports, and active work
- `2_archive_docs/` - Completed work, resolutions, and historical documentation

<!-- section_id: "5aea9e34-60d5-4cce-89cc-5dc72a1c90ec" -->
### **File Naming Convention**
Based on web search best practices, use this standardized format:
```
YYYYMMDD_ProjectName_DocumentType_Version.md
```

**Examples:**
- `20251023_GoogleSignIn_Resolution_v1.0.md`
- `20251023_FirebaseSetup_Status_v1.0.md`
- `20251023_Authentication_Implementation_v1.0.md`

<!-- section_id: "e5665e4d-6c06-4319-826f-c45c5da49b7e" -->
## 📁 Document Types by Directory

<!-- section_id: "2d51799d-d31a-462b-ad83-a01f5fb41e80" -->
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

<!-- section_id: "66a5232e-ed25-4158-8c12-f595386bd721" -->
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

<!-- section_id: "f39d3e8c-3a0d-4a65-b322-ba76e2d14f85" -->
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

<!-- section_id: "34a68832-95ca-41a3-a0aa-befe22f58fb6" -->
## 🔄 Workflow Management

<!-- section_id: "0d4090b5-951f-41d7-b4c4-624c1ce867e6" -->
### **Task Lifecycle**
1. **Planning**: Create document in `0_instruction_docs/` or `1_status_progress_docs/`
2. **Active Work**: Move to `1_status_progress_docs/` with progress updates
3. **Completion**: Move to `2_archive_docs/` with final resolution

<!-- section_id: "483e3018-282c-4450-bb78-29e02f560e30" -->
### **Document Movement Protocol**
```bash
# Move from planning to active work
mv 0_instruction_docs/task-name.md 1_status_progress_docs/YYYYMMDD_TaskName_Status_v1.0.md

# Move from active work to completion
mv 1_status_progress_docs/YYYYMMDD_TaskName_Status_v1.0.md 2_archive_docs/YYYYMMDD_TaskName_Resolution_v1.0.md
```

<!-- section_id: "ac8ebade-27f9-42f3-93dc-01636b3316d8" -->
## 📝 Document Templates

<!-- section_id: "b7f252a8-7f45-4be7-941b-395381f12915" -->
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

<!-- section_id: "7ab0b861-c5a8-4fd7-8553-8a20689ae731" -->
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

<!-- section_id: "2b044e15-7f75-45ad-89f5-0c19e400f9c6" -->
## 🎯 Level-Specific Guidelines

<!-- section_id: "869d5e9a-85cc-4f2a-8118-95af93712fe1" -->
### **trickle_down_0_universal_instructions/**
- Universal rules and protocols
- Cross-project guidelines
- AI agent instructions

<!-- section_id: "43bf8f31-5a9b-4cc2-8f17-8b6767098abf" -->
### **trickle_down_0.5_setup/**
- Environment setup documentation
- Configuration systems
- Setup procedures

<!-- section_id: "86c73619-78ec-40e4-a72b-06500f7fa8ce" -->
### **trickle_down_0.75_universal_tools/**
- Universal tool documentation
- Tool usage guides
- Tool implementation status

<!-- section_id: "499d9cb4-80a1-4e61-ad0a-de36994dd580" -->
### **trickle_down_1_project/**
- Project-specific constitution
- Project standards and principles
- Project status and progress

<!-- section_id: "c22ee272-73b9-4e1b-81b8-b5fdb7c217d6" -->
### **trickle_down_1.5_project_tools/**
- Project-specific tool implementations
- Tool usage and status
- Tool development progress

<!-- section_id: "5f344fec-f3cb-49ea-89ab-4262c46d3a79" -->
### **trickle_down_2_features/**
- Feature specifications
- Feature implementation status
- Feature completion documentation

<!-- section_id: "b1f0f7e3-dd78-4b87-ac50-058e6b980392" -->
### **trickle_down_3_components/**
- Component specifications
- Component implementation status
- Component completion documentation

<!-- section_id: "356f162a-9fca-44c4-9c4c-95b2bb3acf27" -->
## 🔍 Maintenance Guidelines

<!-- section_id: "7b294859-d9ed-48e9-acfb-35a853b0d7c4" -->
### **Regular Reviews**
- Weekly review of `status_progress_docs/`
- Monthly review of `archive/` for completeness
- Quarterly review of `instruction_docs/` for accuracy

<!-- section_id: "3cc4481f-55f7-4c45-95d4-2f066357a835" -->
### **Version Control**
- Use semantic versioning (v1.0, v1.1, v2.0)
- Document changes in version history
- Maintain backward compatibility when possible

<!-- section_id: "a7f53a25-16d7-409a-8377-bb01713de53a" -->
### **Cross-References**
- Link related documents across levels
- Maintain consistent terminology
- Update references when moving documents

---

**This protocol ensures consistent, organized, and maintainable documentation across all trickle-down levels.**

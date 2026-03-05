---
resource_id: "98aa9d38-dc43-4c2e-8064-f7486d89e3b9"
resource_type: "document"
resource_name: "USAGE_GUIDE"
---
# Universal AI Context System - Usage Guide

This directory contains a universal trickle-down documentation system that can be used for any AI-assisted coding project. Follow this guide to adapt it for your specific project.

<!-- section_id: "83199d34-5b79-48d5-8c8c-a589022724b2" -->
## 🎯 Quick Start

1. **Copy the entire `0_context` directory** to your project root (or desired location)
2. **Update the core prompt file**: Edit `0_basic_prompts_throughout/what_to_do_next.md`
3. **Add project-specific documentation** as needed
4. **Update file paths** to match your project structure

<!-- section_id: "3f5c3c9a-f2a4-45f0-ba89-041ecd4f293a" -->
## 📋 Step-by-Step Setup

<!-- section_id: "bb4a2d17-b01f-47f7-af30-31d345aeb975" -->
### Step 1: Copy to Your Project

```bash
# From the location where 0_context currently exists
cp -r /path/to/0_ai_context/0_context /path/to/your/project/docs/

# Or if you want it in your project root:
cp -r /path/to/0_ai_context/0_context /path/to/your/project/
```

<!-- section_id: "77cfe275-a015-4e98-85c3-183ef8bbb746" -->
### Step 2: Customize Core Prompt

Edit `0_basic_prompts_throughout/what_to_do_next.md`:

1. **Update the project path**:
   - Replace `/PATH/TO/YOUR/PROJECT/0_context` with your actual path
   
2. **Update project overview**:
   - Replace "Your Project Name" with your actual project name
   - Describe what your project does
   - List key features
   
3. **Define technology stack**:
   - List your frontend technology
   - List your backend technology
   - Specify your database solution
   - Mention deployment platform
   
4. **Set current priorities**:
   - Define high priority tasks
   - Define medium priority tasks
   - Define low priority tasks
   
5. **Update project status**:
   - Describe current development stage
   - List technology stack
   - Specify target platform
   - Mention next milestone

<!-- section_id: "b9423ace-1f24-479d-b8aa-2d26c06bd7a3" -->
### Step 3: Add Project-Specific Documentation

Create or update files in these directories as needed:

#### `trickle_down_1_project/0_instruction_docs/`
- **constitution.md**: Project-specific coding standards, guidelines, and best practices
- **ENVIRONMENTS_AND_INTEGRATIONS.md**: Environment setup, integrations, and configurations
- **README.md**: Project-specific overview and quick start guide

#### `trickle_down_1.5_project_tools/0_instruction_docs/`
- Add project-specific tools and scripts documentation
- Document custom configurations
- Add integration guides

#### `trickle_down_2_features/0_instruction_docs/`
- Document feature specifications
- Add feature implementation guides
- Create feature testing documentation

#### `trickle_down_3_components/0_instruction_docs/`
- Document component specifications
- Add implementation guides
- Create component documentation

<!-- section_id: "387f9edc-b9cb-449b-ae30-1e22ab7e0099" -->
### Step 4: Update References

Search for and update these common patterns:

1. **Project paths**: Search for `/home/dawson/dawson-workspace/code/` and replace with your paths
2. **Project names**: Update any hardcoded project names
3. **Technology references**: Update technology stack references if different

<!-- section_id: "8da7ef66-6b4c-43a6-a8a5-3f606d26a623" -->
## 📁 Directory Structure Overview

<!-- section_id: "327a8c96-0e3f-4436-a229-60b3b5bf1657" -->
### Universal Directories (Keep As-Is)
- `trickle_down_0_universal/`: Universal AI agent instructions
- `trickle_down_0.5_setup/`: Setup and configuration (customize as needed)
- `trickle_down_0.75_universal_tools/`: Universal tools documentation

<!-- section_id: "3571fddf-93b4-452d-9cf9-fded73b2d968" -->
### Project-Specific Directories (Customize)
- `trickle_down_1_project/`: Your project's specific documentation
- `trickle_down_1.5_project_tools/`: Your project's tools
- `trickle_down_2_features/`: Your project's features
- `trickle_down_2_implementation/`: Implementation documentation
- `trickle_down_3_components/`: Component documentation
- `trickle_down_3_testing/`: Testing documentation

<!-- section_id: "4d568cf4-84dc-46bd-9f73-66cfd425f107" -->
## 🎨 Customization Examples

<!-- section_id: "6bb14aad-d7e4-4203-856d-37fa1b8d7d8f" -->
### Example 1: React/Node.js Project

```markdown
### Technology Stack
- **Frontend**: React 18 + TypeScript + Vite
- **Backend**: Node.js + Express
- **Database**: PostgreSQL + Prisma ORM
- **Deployment**: Vercel (frontend), Railway (backend)
```

<!-- section_id: "7e79036e-1fb4-445b-9916-42aa865f5cd7" -->
### Example 2: Python Django Project

```markdown
### Technology Stack
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: React (or template rendering)
- **Deployment**: Docker + AWS/GCP
```

<!-- section_id: "6d029875-278c-466c-9304-47cbae26b417" -->
### Example 3: Mobile App Project

```markdown
### Technology Stack
- **Mobile**: React Native or Flutter
- **Backend**: Node.js or Python
- **Database**: Supabase or Firebase
- **Deployment**: App Store + Google Play
```

<!-- section_id: "429c6f60-f9dc-413f-8b45-4302d7c98597" -->
## 📝 Documentation Organization

<!-- section_id: "aeddce7c-9c0b-4ad7-9f58-a972193855c7" -->
### Follow the Trickle-Down Pattern

1. **0_instruction_docs/**: How-to guides, procedures, specifications
2. **1_status_progress_docs/**: Current status, progress reports
3. **2_archive_docs/**: Completed work, resolutions, historical records
4. **2_testing_docs/**: Testing documentation, test results

<!-- section_id: "d51e44d7-5816-4c60-ad38-ba9ac23ced90" -->
### Naming Conventions

Use this pattern for dated documentation:
- `YYYY-MM-DD_description.md` for daily documentation
- `DESCRIPTION_DATE.md` for major milestones
- `CATEGORY_description.md` for category-specific docs

<!-- section_id: "68d74b02-a8c8-4601-bd52-70ef3d8cbb1e" -->
## ⚙️ Important Files to Know

<!-- section_id: "a03d44bf-acc5-4856-a920-912347192c27" -->
### Critical Files (Update These First)

1. **`0_basic_prompts_throughout/what_to_do_next.md`**
   - Primary instruction file for AI agents
   - Must be updated with your project details

2. **`README.md`**
   - Already universalized, customize as needed

3. **`MASTER_DOCUMENTATION_INDEX.md`**
   - Comprehensive index of all documentation
   - Update when adding new documentation

<!-- section_id: "41634c1c-7eb1-4991-9e63-1b9473e2973e" -->
### Reference Files (Review and Adapt)

1. **`TERMINAL_HANGING_FIX.md`**
   - Terminal execution protocol
   - Use as-is (universal)

2. **`trickle_down_0_universal/0_instruction_docs/cursor_terminal_issues.md`**
   - Cursor IDE terminal issues
   - Universal reference

<!-- section_id: "940d1b90-bfa4-4046-bc95-30057e4b7da6" -->
## 🚀 Using with AI Agents

<!-- section_id: "d1e5e5df-46c5-46f5-8982-39a1838eb5b0" -->
### For Claude/ChatGPT/Cursor AI:

Point the AI to this directory:
```
/path/to/your/project/docs/0_context
```

The AI will:
1. Read the `what_to_do_next.md` file first
2. Follow the trickle-down documentation structure
3. Use universal instructions when appropriate
4. Apply project-specific documentation when available

<!-- section_id: "7ef7adbf-d7b7-43e5-99b5-066d97b815c6" -->
### For Multiple AI Agents:

This system is designed to work with:
- **Claude** (Anthropic)
- **ChatGPT** (OpenAI)
- **Cursor AI**
- **GitHub Copilot**
- Other MCP-compatible agents

<!-- section_id: "8595d97a-d438-47b4-b3f5-fb2a658ae391" -->
## 🔧 Advanced Customization

<!-- section_id: "cebf16f2-ceca-4c99-a24b-08fcfea8f66b" -->
### Adding New Trickle-Down Levels

If you need additional organization levels:

1. Create new directory: `trickle_down_X_NAME/`
2. Mirror the standard structure:
   - `0_instruction_docs/`
   - `1_status_progress_docs/`
   - `2_archive_docs/`
3. Update `MASTER_DOCUMENTATION_INDEX.md`

<!-- section_id: "246eddb4-c021-4639-9f5a-31c043307ed3" -->
### Creating Project-Specific Tools

Document custom tools in:
- `trickle_down_1.5_project_tools/0_instruction_docs/`

Include:
- Tool descriptions
- Usage examples
- Configuration guides
- Troubleshooting

<!-- section_id: "d12125fb-d86d-467d-911e-b1f94ea05b4c" -->
## 📚 Best Practices

1. **Always update `what_to_do_next.md`** for each project
2. **Keep universal content** in `trickle_down_0_*` directories
3. **Archive old work** in `2_archive_docs/` or `3_archive_docs/`
4. **Document testing** in `2_testing_docs/` or `trickle_down_3_testing/`
5. **Maintain the index** in `MASTER_DOCUMENTATION_INDEX.md`

<!-- section_id: "cab4d412-9091-4df8-b61c-cd40fdb827db" -->
## ⚠️ Common Pitfalls

1. **Don't hardcode project paths** - Use relative paths or environment variables
2. **Don't delete universal documentation** - Keep trickle_down_0_* for reusability
3. **Don't skip the customization step** - Generic docs won't help without customization
4. **Don't ignore the master index** - Keep it updated as you add documentation

<!-- section_id: "ba586e71-e858-4d27-886f-ee4f93ed5b37" -->
## 🎯 Next Steps

1. ✅ Copy `0_context` to your project
2. ✅ Update `0_basic_prompts_throughout/what_to_do_next.md`
3. ✅ Create project constitution in `trickle_down_1_project/0_instruction_docs/constitution.md`
4. ✅ Document your stack in `README.md`
5. ✅ Start documenting features in `trickle_down_2_features/`

---

**Need Help?** Review existing documentation in the trickle_down directories for examples and best practices.


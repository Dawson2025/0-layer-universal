---
resource_id: "1d2ac45c-33f1-4ba1-8904-78b82290a88e"
resource_type: "skill
document"
resource_name: "SKILL"
name: claude-project-setup
description: "Set up a Claude Project on claude.ai with custom instructions and knowledge files via browser automation. Use when the user wants to create a practice/study project, upload context files, or configure a Claude Project from prepared materials."
---

# Claude Project Setup Skill

<!-- section_id: "2eb6bb56-6d03-4034-8932-ce1aeb40bb17" -->
## WHEN to Use
- User wants to create a Claude Project on claude.ai for study, practice, or reference
- Prepared files (system prompt, context docs) exist and need to be uploaded to a Claude Project
- User says "set up a Claude Project" or "create a practice project on claude.ai"
- After creating a `to_talk_to/` package with SYSTEM_PROMPT.md and context files

<!-- section_id: "a610a725-6494-4cf5-a916-48beb06e348d" -->
## WHEN NOT to Use
- User wants to work within Claude Code (CLI) — no browser needed
- User is asking about Claude API or SDK (not claude.ai web)
- No prepared files or system prompt exist yet — create those first

<!-- section_id: "84a88680-44c4-4885-b996-86ed67cb5d56" -->
## Prerequisites
- Claude in Chrome MCP extension active (`mcp__claude-in-chrome__*` tools available)
- User is logged into claude.ai in their browser
- Prepared files: at minimum a SYSTEM_PROMPT.md and context files
- If using GitHub integration: files must be pushed to a GitHub repo

<!-- section_id: "6e65401a-3ddc-49ad-8846-77cc086a8642" -->
## Steps

<!-- section_id: "9572ff39-e08e-4990-92ee-78c673a95511" -->
### Phase 1: Create the Project

1. **Get browser context**: Call `tabs_context_mcp` to find existing tabs
2. **Navigate to claude.ai**: Create a new tab or use existing one, navigate to `https://claude.ai/projects`
3. **Click "Create project"** button on the projects page
4. **Fill project details**:
   - Name: descriptive title
   - Description: what the project is for
5. **Click "Create project"** to submit

<!-- section_id: "2d074020-6c18-4a4f-86cd-4d19e12e786d" -->
### Phase 2: Set Custom Instructions

1. **Click "Edit Instructions"** on the project page
2. **Inject instructions via JavaScript** (React textarea workaround):
   ```javascript
   const textarea = document.querySelector('textarea');
   const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
     window.HTMLTextAreaElement.prototype, 'value'
   ).set;
   nativeInputValueSetter.call(textarea, `[SYSTEM_PROMPT content]`);
   textarea.dispatchEvent(new Event('input', { bubbles: true }));
   textarea.dispatchEvent(new Event('change', { bubbles: true }));
   ```
   **Why**: Claude.ai uses React controlled inputs. Direct `.value =` assignment doesn't trigger React's state update. The native setter + event dispatch pattern is required.
3. **Click "Save instructions"**

<!-- section_id: "85288550-63de-4e4e-b8ee-9630ec872b88" -->
### Phase 3: Add Knowledge Files via GitHub

**This is the most efficient method** when files are already in a GitHub repo.

1. **Click "Add files"** → select **"GitHub"** from the dropdown
2. **Select the repository** from the connected repos list
3. **Use the search bar** to find files by name:
   - Search for each file individually (e.g., `01_overview`, `02_results`)
   - Click the **checkbox** (left side of the row) to select each result
   - **Selections persist across searches** — previous selections are NOT lost when you search for a new term
4. **Repeat for each file**: triple-click search field → type new filename → Enter → click checkbox
5. **Click "Add files"** (black button, top right) when all files are selected

<!-- section_id: "565c59ef-29e3-4da3-bf28-a5c4be30730f" -->
### Key Learnings & Gotchas

| Issue | Solution |
|-------|----------|
| React textarea won't accept `.value =` | Use `nativeInputValueSetter` pattern (Phase 2) |
| "Upload from device" triggers native OS file dialog | Cannot be automated via browser extension — use GitHub integration instead |
| "Add text content" is tedious | One file at a time — only use as last resort |
| GitHub URL paste field | Doesn't navigate to deep folders reliably — use search instead |
| Search for folder name (e.g., `to_talk_to`) | Not useful — search only matches file names, not folder names |
| Multiple search results for same filename | Use more specific search terms (full filename) to narrow results |
| Searching for `03_discussion` returns 3 results | Use `03_discussion_answers` (full name) to get exact match |
| Clicking folder row in search | May navigate into folder instead of selecting — click the checkbox area specifically |

<!-- section_id: "756bcf51-3e27-4ab6-b6a1-8efcddec3904" -->
### Alternative: Add Text Content (Fallback)

If GitHub integration isn't available:
1. Click "Add files" → "Add text content"
2. Fill in Title and Content fields
3. Click save
4. Repeat for each file (one at a time)

<!-- section_id: "0bc8d3de-9e63-4466-89f4-55329ce39539" -->
## Output

After completion, provide:
- Project URL (e.g., `https://claude.ai/project/[uuid]`)
- Number of files added and capacity percentage
- Confirmation that instructions were saved
- Any files that couldn't be added (binary files like PDFs, images)

<!-- section_id: "a574ebba-adae-480b-9326-d0223ac1490f" -->
## Notes

- GitHub integration only imports text-based files (markdown, code, etc.)
- Binary files (PDF, PNG, IPYNB) cannot be added via GitHub — use "Upload from device" manually
- The `presentation_practice_context.md` combined file is useful as a single-file fallback
- Claude Projects use ~1% capacity per small markdown file

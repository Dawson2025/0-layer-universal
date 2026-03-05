---
resource_id: "189c09cb-d43f-4a2e-9299-e59c488a9c68"
resource_type: "rule"
resource_name: "git_repository_creation_rule"
---
# GIT REPOSITORY CREATION RULE

<!-- section_id: "0d8f8f5b-4bcd-442b-9d07-23bd64d27174" -->
## **MANDATORY REQUIREMENTS**

**ALL AI agents MUST follow these rules when creating Git repositories:**

<!-- section_id: "d4fdc35a-d567-4348-83f0-ec5d7c098569" -->
### **1. PRIVATE BY DEFAULT**

**All repositories MUST be created as PRIVATE by default.**

- **GitHub repositories**: Always select "Private" visibility
- **Local repositories**: Assume private unless explicitly instructed otherwise
- **No exceptions**: Even seemingly innocuous repos should be private by default

**Only create PUBLIC repositories when:**
- The user **explicitly** requests a public repository
- The user says something like "make it public" or "this should be public"
- The project is specifically intended for public sharing (e.g., portfolio, open source contribution)

<!-- section_id: "617aba1b-08b1-4002-9143-5b2a648b0826" -->
### **2. REPOSITORY NAMING CONVENTIONS**

When creating repositories for the layered project structure:

**Root-level projects (Layer 1):**
- Format: `<layer_num>-<project-name>`
- Example: `1-school`, `1-machine-learning`, `2-sub-project-name`
- Use hyphens, not underscores (GitHub convention)

**Sub-projects (Layer 2):**
- Format: `<parent>-<sub-project-name>`
- Example: `school-math`, `school-applied-programming`

**Nested sub-projects (Layer 3+):**
- Format: `<parent>-<sub*N-project-name>`
- Example: `school-math-applied-calculus`, `school-math-precalculus`

<!-- section_id: "9c8a0cdb-4b9c-46ad-9bf2-d9b1474607d7" -->
### **3. BEFORE CREATING A REPOSITORY**

**ALWAYS check if the repository already exists:**

1. **Via CLI (if gh is available):**
   ```bash
   gh repo list <owner> --limit 100 --json name --jq '.[].name' | grep -i "<repo-name>"
   ```

2. **Via browser:**
   - Navigate to `https://github.com/<owner>?tab=repositories`
   - Search for the repository name

3. **If repository exists:**
   - Do NOT create a duplicate
   - Verify the existing repo has correct settings (private/public)
   - Update settings if needed rather than recreating

<!-- section_id: "12215233-38bf-4d4b-8b82-0c2554af7cc6" -->
### **4. REPOSITORY CREATION CHECKLIST**

Before creating any repository:

- [ ] Confirmed repository does not already exist
- [ ] Repository will be **PRIVATE** (unless explicitly told otherwise)
- [ ] Repository name follows naming conventions
- [ ] Owner is correct (personal vs organization)
- [ ] Description is meaningful and concise

<!-- section_id: "9475037f-3ead-4aef-ba58-f8cf852d3d0e" -->
### **5. CHANGING REPOSITORY VISIBILITY**

If a repository was accidentally created as public when it should be private:

1. Go to repository Settings
2. Scroll to "Danger Zone"
3. Click "Change repository visibility"
4. Select "Make private"
5. Confirm the change

**This should be done immediately upon discovering the error.**

<!-- section_id: "350d3572-65a7-4970-9bb2-dd5a1dd56822" -->
### **6. SENSITIVE INFORMATION**

**NEVER commit sensitive information to ANY repository, regardless of visibility:**
- API keys and secrets
- Passwords and credentials
- Personal identification information
- Private configuration files with secrets

Even private repositories can become public accidentally. Treat all repositories as potentially public when deciding what to commit.

<!-- section_id: "02d503d3-63c3-483e-b34b-a12d51d94cfe" -->
## **ENFORCEMENT**

This rule is **MANDATORY** and **NON-NEGOTIABLE**.

**Key principle: When in doubt, make it private.**

The default assumption is always PRIVATE. Only deviate when the user explicitly requests otherwise.

---

**This rule is effective immediately and applies to all AI agents working on any project.**

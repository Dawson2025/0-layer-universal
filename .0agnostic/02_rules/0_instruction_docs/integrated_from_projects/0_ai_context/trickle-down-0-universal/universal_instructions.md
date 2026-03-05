---
resource_id: "d0b53c69-f55c-44eb-8f11-177c44980e37"
resource_type: "rule"
resource_name: "universal_instructions"
---
# Universal AI Agent Instructions

**Use these instructions for any project, any codebase, any task**

<!-- section_id: "6478931c-b793-4a35-ab61-e31fc8af0fc3" -->
## Core Principles

<!-- section_id: "12a77ea3-73f7-4b7a-a764-1dc0c678631f" -->
### 0. Identify Fundamental Intent First
**Before executing any request, identify and articulate the fundamental intent, purpose, or need:**

- **Surface Request**: What the user literally asked for
- **Fundamental Intent**: The underlying goal, principle, or outcome they actually need
- **Key Insight**: Users often know what they want but may not know the optimal way to achieve it
- **Your Role**: Research and implement the most effective, efficient, and best-practice solution to achieve the fundamental intent
  
**Example:**
- **Surface**: "Fix this specific test"
- **Fundamental**: "Achieve reliable, automated test coverage with minimal manual intervention"
- **Action**: Research testing best practices, analyze current approach, recommend optimal strategy

**When the fundamental intent differs from the literal request**, briefly explain what you identified and how your approach serves the deeper need.

<!-- section_id: "a79c45c1-a588-4ff8-8ebc-fde5bbcfbd9f" -->
### 1. Always Use TODO Lists
For every prompt, create a TODO list explicitly stating what you will do:
- Break down complex tasks into specific steps
- Use the `TodoWrite` tool to track progress
- Mark items as in_progress/completed as you work
- Only one item should be in_progress at a time
- Complete tasks immediately after finishing them

<!-- section_id: "519437e9-60a4-4b7c-8629-8788d51c96c0" -->
### 1b. Start With a Depth-First Prototype
- When taking on a broad or multi-phase request, implement a **small, end-to-end slice first**.
- This prototype must cover the full lifecycle (planning → implementation → integration → verification) for a representative subset.
- Use what you learn from the slice to adjust scope, tooling, and quality benchmarks before scaling to larger batches.
- Do **not** expand to additional surfaces until the initial slice is fully integrated, documented, and validated.

<!-- section_id: "2fbb385f-ddc5-45bb-a2ae-2de0095c6b57" -->
### 2. Read Before You Write
- **NEVER** make assumptions about code you haven't read
- **ALWAYS** use Read/Glob/Grep tools to understand existing code first
- Read related files to understand context and patterns
- Check imports, dependencies, and related modules
- Look for existing tests to understand expected behavior

<!-- section_id: "07db126b-f078-4641-9986-821680006668" -->
### 3. Understand the Architecture First
Before making changes:
- Identify the project structure (where are features/modules/services?)
- Understand the import patterns used
- Locate existing tests
- Find configuration files
- Identify shared infrastructure vs feature-specific code

<!-- section_id: "9405587d-7816-4b76-8a41-a74dd91594fa" -->
### 4. Test Everything
- Create tests for every feature you implement
- Run existing tests before making changes
- Run tests after your changes to verify nothing broke
- If tests fail, fix them before marking work complete
- Never mark a task complete if tests are failing

<!-- section_id: "2f727dfa-889d-40c9-832d-1036e64258b7" -->
### 5. Follow Existing Patterns
- Match the coding style of the existing codebase
- Use the same naming conventions
- Follow existing architectural patterns
- Don't introduce new patterns unless explicitly requested
- When in doubt, ask before deviating from established patterns

<!-- section_id: "18b6e050-68f6-4593-a62f-eab7e824cc3e" -->
### 6. Document As You Go
- Add clear comments for complex logic
- Update README files when adding new features
- Document new APIs or interfaces
- Keep requirements/specifications up to date
- Create or update architecture docs for significant changes

<!-- section_id: "cd64cc17-c7f0-4fca-8d32-99b648fb8f2f" -->
### 7. File Organization Best Practices
**CRITICAL:** Always organize files following this three-level hierarchy:

#### Organization Hierarchy
Files MUST be organized in this order of priority:

**1. FIRST: Best Practice Standards** (what industry says)
- Source code in `src/` or `app/`
- Configuration in `config/`
- Tests in `tests/` (or colocated)
- Documentation in `docs/`
- Scripts in `scripts/` or `bin/`
- Data in `data/`

**2. SECOND: File Type** (within best practice directories)
- Source: `src/features/`, `src/core/`, `src/services/`
- Config: `config/database/`, `config/firebase/`, `config/app/`
- Scripts: `scripts/setup/`, `scripts/migration/`, `scripts/dev/`
- Docs: `docs/api/`, `docs/setup/`, `docs/architecture/`

**3. THIRD: Module/Feature/Sub-Feature** (within file type directories)
- Features: `src/features/auth/`, `src/features/users/`
- Sub-features: `src/features/users/creation.py`, `src/features/users/editing.py`
- Services: `src/services/email/`, `src/services/payments/`

#### Example of Correct Hierarchy
```
project/
├── src/                          # 1. Best practice (source code)
│   ├── features/                 # 2. File type (feature code)
│   │   ├── auth/                # 3. Module (authentication)
│   │   │   ├── login.py        # 3b. Sub-feature
│   │   │   ├── registration.py
│   │   │   └── tests/
│   │   └── users/               # 3. Module (users)
│   │       ├── creation.py     # 3b. Sub-feature
│   │       └── editing.py
│   ├── core/                    # 2. File type (core infrastructure)
│   └── services/                # 2. File type (cross-cutting services)
├── config/                       # 1. Best practice (configuration)
│   ├── database/                # 2. File type (db config)
│   └── firebase/                # 2. File type (firebase config)
├── scripts/                      # 1. Best practice (utilities)
│   ├── setup/                   # 2. File type (setup scripts)
│   └── migration/               # 2. File type (migration scripts)
└── docs/                        # 1. Best practice (documentation)
    ├── api/                     # 2. File type (API docs)
    └── setup/                   # 2. File type (setup docs)
```

#### What Should NOT Be at Root
❌ Individual source files (move to `src/`)
❌ Configuration files (move to `config/`)
❌ Data files/databases (move to `data/`)
❌ Documentation (move to `docs/`)
❌ Utility scripts (move to `scripts/`)

#### What CAN Be at Root
✅ Entry point (app.py, main.py, run.py) - minimal
✅ Package files (requirements.txt, package.json, pyproject.toml)
✅ Build config (pytest.ini, tsconfig.json, .eslintrc)
✅ Version control (.git, .gitignore)
✅ README.md, LICENSE
✅ Environment template (.env.example)

#### AI Configuration Files
```
.claude/                   # Claude Code configuration
├── project_instructions.md
├── universal_instructions.md
└── commands/

.mcp.json                  # MCP servers (at root for Claude Code to recognize)
```

**Note:** `.mcp.json` must be at project root, not in `.claude/`, for Claude Code to recognize it.

#### When Reorganizing
If you find poor organization:
1. **Propose reorganization** before implementing
2. **Follow the hierarchy**: Best practice → File type → Module/Feature
3. **Update imports** after moving files
4. **Document the new structure**
5. **Test thoroughly**

#### Red Flags
🚩 More than 10 files in project root
🚩 No clear directory structure
🚩 Configuration scattered throughout
🚩 Tests separated from features
🚩 Files organized by feature first (should be by best practice first)

<!-- section_id: "aebd70e5-0d6f-4149-876d-571e6c6b8e91" -->
## Workflow

<!-- section_id: "eec16b06-0acb-4f18-96ef-3d52befc8dd1" -->
### For Every Task:

1. **Understand the Request**
   - Clarify ambiguous requirements
   - Ask questions if context is missing
   - Confirm scope before starting

2. **Create TODO List**
   - Break down into specific, actionable steps
   - Include investigation, implementation, testing, and documentation
   - Use TodoWrite tool to track progress

3. **Investigate First**
   - Read relevant code files
   - Search for related implementations
   - Check existing tests
   - Understand dependencies and integrations

4. **Plan the Implementation**
   - Identify which files need changes
   - Consider edge cases and error handling
   - Think about testing strategy
   - Plan for backwards compatibility if needed

5. **Implement Incrementally**
   - Make one logical change at a time
   - Test each change before moving on
   - Commit working code frequently
   - Update TODO list as you progress

6. **Verify and Test**
   - Run all relevant tests
   - Test edge cases manually if needed
   - Verify integration points work
   - Check for unintended side effects

7. **Document and Clean Up**
   - Update documentation
   - Add/update comments
   - Remove debug code
   - Clean up temporary files

8. **Final Review**
   - Review all changed files
   - Ensure TODO list is complete
   - Verify tests pass
   - Check git diff for unintended changes

<!-- section_id: "80b0ad24-8385-4aff-a8f8-7f46ee3747be" -->
## Code Quality Standards

<!-- section_id: "bbe973fe-5c9e-4ad1-a49e-bd3ee9f6a376" -->
### Readability
- Write self-documenting code with clear variable names
- Keep functions focused on single responsibilities
- Limit function/method length to ~50 lines when possible
- Use meaningful comments for "why", not "what"

<!-- section_id: "26e35079-3be9-4647-927c-299f9e124dac" -->
### Maintainability
- Avoid code duplication (DRY principle)
- Keep dependencies minimal and explicit
- Use consistent error handling patterns
- Make code easy to test

<!-- section_id: "9b00e455-c655-4498-bec2-33e8de724cec" -->
### Performance
- Don't optimize prematurely
- Profile before making performance changes
- Consider scalability for data processing
- Avoid blocking operations in async code

<!-- section_id: "f15bd642-f610-4fb1-956b-df1e97acc6de" -->
### Security
- **NEVER** commit secrets or credentials
- Validate all user inputs
- Use parameterized queries for databases
- Follow principle of least privilege
- Sanitize outputs to prevent XSS/injection

<!-- section_id: "e977c580-4725-4d75-85d3-678ec6d96043" -->
## Common Mistakes to Avoid

❌ **Don't:**
- Make changes without reading existing code first
- Skip testing because "it's a small change"
- Commit commented-out code
- Leave TODO comments without tracking them
- Ignore linter warnings
- Hard-code configuration values
- Copy code without understanding it
- Assume the requirements are complete

✅ **Do:**
- Read and understand before modifying
- Test thoroughly, including edge cases
- Remove dead code instead of commenting it out
- Track all TODOs in a proper system
- Fix linter warnings as you encounter them
- Use configuration files/environment variables
- Understand patterns before implementing them
- Ask clarifying questions about requirements

<!-- section_id: "20b73e62-1fb6-4a73-95cc-2ccc6e77c96b" -->
## Communication

<!-- section_id: "b02ad021-cf06-4dc3-894c-515db3c12c11" -->
### When to Ask Questions
- Requirements are ambiguous or incomplete
- Multiple implementation approaches are possible
- Breaking changes may be necessary
- You encounter unexpected behavior
- Dependencies need to be added
- Architecture changes are needed

<!-- section_id: "498ef21f-d6d4-4033-8a63-d463b524b1c7" -->
### How to Communicate Progress
- Update TODO list as you work
- Explain what you're doing and why
- Call out potential issues early
- Summarize changes when complete
- Highlight areas that need review
- Document decisions and trade-offs

<!-- section_id: "fbc0c0c7-9f52-400f-b2b8-fb1eaf0ba546" -->
## Git & Version Control

<!-- section_id: "27542e16-385e-4db6-8106-fdfb98eec860" -->
### Commits
- Commit working code frequently
- Write clear, descriptive commit messages
- Use conventional commit format when applicable
- Don't commit broken code
- Don't commit debugging artifacts

<!-- section_id: "4a4bea7a-41f7-47df-b803-c89e5f33669a" -->
### Branches
- Follow the project's branching strategy
- Keep branches focused on single features
- Merge/rebase from main regularly
- Clean up branches after merging

<!-- section_id: "9c4229c2-1e08-4500-b678-fc655fd15596" -->
## Error Handling

<!-- section_id: "6caa5f7f-abb6-4347-9860-9863bc01c7fd" -->
### When Things Go Wrong
1. Read the full error message carefully
2. Check the stack trace for root cause
3. Search for similar errors in codebase/docs
4. Test your assumptions with minimal examples
5. Ask for help if stuck after reasonable effort

<!-- section_id: "16892987-620c-4b27-8d24-2700fd637fcc" -->
### Debugging Strategy
- Add logging strategically
- Use debugger breakpoints
- Isolate the problem with minimal reproduction
- Check assumptions one at a time
- Document the bug and fix for future reference

<!-- section_id: "e85b1236-95f7-4667-9d06-8c962e1c65ad" -->
## Efficiency Tips

<!-- section_id: "ab360127-4750-442c-8409-8859175ae112" -->
### Use Tools Effectively
- Use Grep for code search, not manual scanning
- Use Glob for finding files by pattern
- Use Task tool for complex multi-step operations
- Run multiple independent operations in parallel
- Use specialized tools instead of bash commands when available

<!-- section_id: "79ec98c2-4702-4836-b654-d5584c0ae0af" -->
### Optimize Your Workflow
- Read documentation before experimenting
- Check for existing solutions before implementing
- Use existing libraries instead of reinventing
- Automate repetitive tasks with scripts
- Keep a mental model of the codebase structure

<!-- section_id: "e69f4e1f-d3f6-4249-ac63-57cd5c2f5f24" -->
## When Working on Unfamiliar Codebases

1. **Start with README and docs**
   - Look for architecture diagrams
   - Read setup/installation guides
   - Check for contributing guidelines
   - Review any developer documentation

2. **Explore the structure**
   - Identify main entry points
   - Map out major modules/features
   - Find the test suite
   - Locate configuration files

3. **Understand the build/run process**
   - How to install dependencies
   - How to run the application
   - How to run tests
   - How to debug

4. **Find similar examples**
   - Look for similar features already implemented
   - Follow established patterns
   - Learn from existing tests

<!-- section_id: "47dfa197-85f5-47ea-953c-daa112d6dddb" -->
## Mindset

<!-- section_id: "3703781a-acdd-4127-a625-69fd961fe0e8" -->
### Be Professional
- Take ownership of your work
- Deliver quality over speed
- Admit when you don't know something
- Learn from mistakes
- Help improve the codebase

<!-- section_id: "d61a6fda-6fc0-4b2f-815d-1c5cfc56192d" -->
### Be Thorough
- Check edge cases
- Think about failure scenarios
- Consider performance implications
- Test on different environments when relevant
- Review your own work critically

<!-- section_id: "cf94495a-e558-4710-bc0e-2be6e8652b01" -->
### Be Collaborative
- Follow team conventions
- Write code others can understand
- Document non-obvious decisions
- Accept feedback gracefully
- Share knowledge through documentation

---

<!-- section_id: "492b2d5f-bcf8-44fa-a50c-40c87da6e987" -->
## Summary Checklist

Before marking any task complete, verify:

- [ ] TODO list created and maintained
- [ ] Existing code read and understood
- [ ] Implementation follows project patterns
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] No secrets/credentials committed
- [ ] Code reviewed for quality
- [ ] Git commits are clean and descriptive
- [ ] No linter errors or warnings
- [ ] Edge cases considered and handled

---

**Remember:** The goal is not just to make code work, but to make it work reliably, maintainably, and professionally. Take the time to do it right.










---
resource_id: "6368eae1-029e-466f-849c-aa5a0e033c24"
resource_type: "rule"
resource_name: "playwright-installation-confusion-analysis"
---
# Playwright Installation Confusion - Root Cause Analysis

<!-- section_id: "7f4c5481-9ca9-4789-96c9-491bdcbd0630" -->
## The Problem

We experienced issues with Playwright MCP and Chrome DevTools MCP setup where browsers were installed using **Python Playwright** (`python3 -m playwright install`) instead of **Node.js Playwright** (`npx playwright install`), causing "Browser not installed" errors.

<!-- section_id: "8871d5b7-2768-42b0-97b7-e600f2dd0536" -->
## Root Cause: Overuse of Python Terminal Wrapper

<!-- section_id: "c5a00114-7c08-4224-99ba-835c0835d327" -->
### The Connection

**Using the Python terminal wrapper for Node.js commands may have contributed to the confusion:**

1. **Pattern Recognition Confusion**:
   - If we used: `python3 scripts/terminal_wrapper.py "npx playwright install chromium"`
   - Someone might see `python3` at the start and think: "We're using Python, so maybe I should use Python Playwright"
   - This led to: `python3 -m playwright install chromium` ❌

2. **Overly Broad "Always Use Wrapper" Rule**:
   - The rule said "always use terminal_wrapper.py for everything"
   - This made it seem like Python was the solution for all commands
   - People might have thought: "If Python wrapper is for everything, maybe Python Playwright is the right choice"

3. **Command Similarity**:
   - `python3 scripts/terminal_wrapper.py "npx playwright install"`
   - `python3 -m playwright install` (looks similar, but completely different!)

<!-- section_id: "8b7a6005-bea9-4301-8aa5-17e33a5b8918" -->
### The Actual Issue

**Python Playwright vs Node.js Playwright:**
- **Python Playwright**: `python3 -m playwright install chromium` - Installs to Python-specific cache
- **Node.js Playwright**: `npx playwright install chromium` - Installs to Node.js-specific cache
- **MCP servers use Node.js Playwright** - They can't find Python-installed browsers

<!-- section_id: "69b68948-e885-4a2c-898f-cd86f9483102" -->
### Why Using Wrapper for Node.js Commands Was Problematic

1. **Visual Confusion**: Seeing `python3` at the start of commands might suggest using Python tools
2. **Pattern Matching**: If everything uses Python wrapper, people might think Python tools are preferred
3. **Unnecessary Complexity**: Wrapping Node.js commands adds Python overhead when it's not needed
4. **Cognitive Load**: More complex commands are harder to understand and more error-prone

<!-- section_id: "df0a3d73-f012-4a84-a15e-7e1913cab5c3" -->
## The Solution

<!-- section_id: "35930a9f-9d7d-4e93-b6d4-57b4f7220ba4" -->
### Correct Approach (Now Documented)

**Node.js Commands - Use `run_terminal_cmd` directly:**
```bash
# ✅ CORRECT - Clear and direct
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
```

**NOT using Python wrapper:**
```bash
# ❌ AVOID - Unnecessary and potentially confusing
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

<!-- section_id: "1a5423e0-6402-4405-915c-d74c422cb38d" -->
### Why This Helps

1. **Clear Intent**: `npx` at the start makes it obvious this is a Node.js command
2. **No Python Confusion**: No `python3` prefix to confuse people
3. **Simpler**: Direct command is easier to understand
4. **Less Error-Prone**: Fewer layers = fewer places for mistakes

<!-- section_id: "0807841a-a7e3-4d42-b835-1ab2b1a91cd6" -->
## Prevention Strategy

<!-- section_id: "40c100b9-a51a-42f7-b3a2-4adef942a350" -->
### 1. Clear Documentation
- ✅ Document that wrapper is **only for Python scripts**
- ✅ Make it clear Node.js commands should use `run_terminal_cmd` directly
- ✅ Emphasize the difference between Python and Node.js Playwright

<!-- section_id: "3542f6e4-c790-4176-90fd-ba9b74b4504d" -->
### 2. Explicit Examples
- ✅ Show correct Node.js Playwright installation: `run_terminal_cmd("npx playwright install chromium ; exit")`
- ✅ Show wrong Python Playwright: `python3 -m playwright install chromium` ❌
- ✅ Explain why they're different

<!-- section_id: "62ccae88-cf51-4782-80dd-6ff95c7d5bce" -->
### 3. Visual Distinction
- ✅ Node.js commands: Start with `npx` or `npm`
- ✅ Python commands: Start with `python3` (and use wrapper)
- ✅ Make the distinction obvious

<!-- section_id: "6685d147-5539-41d1-880a-f2cca872ea29" -->
## Lessons Learned

1. **Don't Over-Apply Solutions**: The wrapper solves Python issues, not all terminal issues
2. **Clarity Over Consistency**: It's better to have different approaches for different command types than to force one solution everywhere
3. **Visual Cues Matter**: Command prefixes (`python3` vs `npx`) help people understand what they're using
4. **Documentation Must Be Precise**: "Always use wrapper" was too broad and led to confusion

<!-- section_id: "ec8742a3-b927-437c-ac4d-7e47b9218961" -->
## Updated Best Practices

<!-- section_id: "8c1fcd40-473c-42d3-a86d-2b1866c33713" -->
### For Playwright Installation:
```bash
# ✅ CORRECT - Node.js Playwright (for MCP servers)
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")

# ❌ WRONG - Python Playwright (won't work with MCP)
python3 -m playwright install chromium

# ❌ UNNECESSARY - Wrapping Node.js command
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

<!-- section_id: "627c3676-905f-42f8-bfdc-60c341d7ba13" -->
### For Chrome Installation:
```bash
# ✅ CORRECT - System Chrome (for Chrome DevTools MCP)
run_terminal_cmd("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; exit")
run_terminal_cmd("sudo apt install ./google-chrome-stable_current_amd64.deb ; exit")

# ❌ WRONG - Playwright Chromium (won't work for Chrome DevTools MCP)
npx playwright install chromium
```

<!-- section_id: "17170dcb-1af4-4379-892a-3441be074fd1" -->
## Summary

**Yes, using the Python wrapper for Node.js commands likely contributed to the confusion** that led to using Python Playwright instead of Node.js Playwright. The solution is to:

1. ✅ Use wrapper **only for Python scripts**
2. ✅ Use `run_terminal_cmd` directly for Node.js commands
3. ✅ Make the distinction clear in documentation
4. ✅ Use visual cues (`npx` vs `python3`) to prevent confusion

This prevents the pattern-matching confusion that led to the browser installation issues.


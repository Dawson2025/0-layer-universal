---
resource_id: "6368eae1-029e-466f-849c-aa5a0e033c24"
resource_type: "rule"
resource_name: "playwright-installation-confusion-analysis"
---
# Playwright Installation Confusion - Root Cause Analysis

## The Problem

We experienced issues with Playwright MCP and Chrome DevTools MCP setup where browsers were installed using **Python Playwright** (`python3 -m playwright install`) instead of **Node.js Playwright** (`npx playwright install`), causing "Browser not installed" errors.

## Root Cause: Overuse of Python Terminal Wrapper

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

### The Actual Issue

**Python Playwright vs Node.js Playwright:**
- **Python Playwright**: `python3 -m playwright install chromium` - Installs to Python-specific cache
- **Node.js Playwright**: `npx playwright install chromium` - Installs to Node.js-specific cache
- **MCP servers use Node.js Playwright** - They can't find Python-installed browsers

### Why Using Wrapper for Node.js Commands Was Problematic

1. **Visual Confusion**: Seeing `python3` at the start of commands might suggest using Python tools
2. **Pattern Matching**: If everything uses Python wrapper, people might think Python tools are preferred
3. **Unnecessary Complexity**: Wrapping Node.js commands adds Python overhead when it's not needed
4. **Cognitive Load**: More complex commands are harder to understand and more error-prone

## The Solution

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

### Why This Helps

1. **Clear Intent**: `npx` at the start makes it obvious this is a Node.js command
2. **No Python Confusion**: No `python3` prefix to confuse people
3. **Simpler**: Direct command is easier to understand
4. **Less Error-Prone**: Fewer layers = fewer places for mistakes

## Prevention Strategy

### 1. Clear Documentation
- ✅ Document that wrapper is **only for Python scripts**
- ✅ Make it clear Node.js commands should use `run_terminal_cmd` directly
- ✅ Emphasize the difference between Python and Node.js Playwright

### 2. Explicit Examples
- ✅ Show correct Node.js Playwright installation: `run_terminal_cmd("npx playwright install chromium ; exit")`
- ✅ Show wrong Python Playwright: `python3 -m playwright install chromium` ❌
- ✅ Explain why they're different

### 3. Visual Distinction
- ✅ Node.js commands: Start with `npx` or `npm`
- ✅ Python commands: Start with `python3` (and use wrapper)
- ✅ Make the distinction obvious

## Lessons Learned

1. **Don't Over-Apply Solutions**: The wrapper solves Python issues, not all terminal issues
2. **Clarity Over Consistency**: It's better to have different approaches for different command types than to force one solution everywhere
3. **Visual Cues Matter**: Command prefixes (`python3` vs `npx`) help people understand what they're using
4. **Documentation Must Be Precise**: "Always use wrapper" was too broad and led to confusion

## Updated Best Practices

### For Playwright Installation:
```bash
# ✅ CORRECT - Node.js Playwright (for MCP servers)
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")

# ❌ WRONG - Python Playwright (won't work with MCP)
python3 -m playwright install chromium

# ❌ UNNECESSARY - Wrapping Node.js command
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

### For Chrome Installation:
```bash
# ✅ CORRECT - System Chrome (for Chrome DevTools MCP)
run_terminal_cmd("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; exit")
run_terminal_cmd("sudo apt install ./google-chrome-stable_current_amd64.deb ; exit")

# ❌ WRONG - Playwright Chromium (won't work for Chrome DevTools MCP)
npx playwright install chromium
```

## Summary

**Yes, using the Python wrapper for Node.js commands likely contributed to the confusion** that led to using Python Playwright instead of Node.js Playwright. The solution is to:

1. ✅ Use wrapper **only for Python scripts**
2. ✅ Use `run_terminal_cmd` directly for Node.js commands
3. ✅ Make the distinction clear in documentation
4. ✅ Use visual cues (`npx` vs `python3`) to prevent confusion

This prevents the pattern-matching confusion that led to the browser installation issues.


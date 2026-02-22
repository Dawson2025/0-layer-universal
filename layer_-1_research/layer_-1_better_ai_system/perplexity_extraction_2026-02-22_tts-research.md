# Perplexity Extraction: System-Wide TTS + Claude Code TTS

**Source**: https://www.perplexity.ai/search/hey-how-s-it-going-doing-prett-VVzJDBQ9Tkq2MIwXHhxo6w
**Extracted**: 2026-02-22
**Method**: Claude in Chrome (React fiber citation extraction)

---

## Thread Summary

A multi-turn Perplexity conversation about:
1. System-wide text-to-speech (TTS) options for Ubuntu Linux
2. Claude Code CLI text-to-speech integration via community hooks/plugins

### Key Conclusions
- **System-wide TTS**: Start with **Orca** (built into GNOME/Ubuntu) — covers GUI apps, browser, and terminal
- **Claude Code TTS**: Use community TTS hooks/plugins (Kokoro-based hook or MCP TTS plugin)

---

## Answer 1: System-Wide TTS Recommendations

Initial recommendations for system-wide TTS on Ubuntu:
- **Resemble AI** — ultra-realistic, human-like voices, extensive customization
- **Piper** — open-source, fully offline, neural TTS models
- **Murf** — premium cloud-based voices with media integration
- **eSpeak NG** — longstanding, lightweight classic option

## Answer 2: Highlight-and-Speak (like Whisperflow/Vibetyper)

- **Speech Note** — flexible, works across different applications, highlight text anywhere and read aloud

## Answer 3: Orca for Desktop + Terminal Users

Recommended for users who mix normal desktop apps with terminal work:

### What Orca Covers
1. **GUI apps and browser**: reads windows, menus, buttons, dialogs, web pages; caret navigation
2. **Terminal windows**: reads command output and typed input in GNOME Terminal; screen review/flat-review to revisit previous lines
3. **Whole-window/screen review**: "Say All" and flat-review commands for active window

### Basic Setup
- Toggle Orca: `Super + Alt + S`
- Enable caret navigation in browser: `F7`
- Use Orca review commands for terminal output

### Complement with Highlight-and-Speak Scripts
- Hotkey to read only current selection via `xsel + TTS engine` (Festival, Mimic, etc.)
- Gives precision control alongside Orca's broad coverage

## Answer 4: Claude Code CLI — Agentic TTS Options

### Option 1: Existing Claude Code TTS Hooks (Recommended)
- **Kokoro-based hook** — plugs into Claude Code's hook system, auto-speaks responses using local Kokoro TTS model
- **MCP TTS plugin** — exposes TTS as an MCP tool; Claude can call it when it wants to speak

Key benefit: Claude can output full text (ASCII diagrams, code) to CLI while using a shorter "voice line" (summary) for TTS — what you hear ≠ what you see.

### Option 2: DIY with Python Helper
- Use **pyttsx3** — fully offline, wraps native engines (eSpeak/Festival)
- Have Claude output structured JSON with `spoken_summary` + `visual_output`
- Helper script sends only `spoken_summary` to TTS

### Option 3: Simple CLI Approach (No Hooks)
- Pipe specific output to `espeak` or `festival`: `echo "Short line" | espeak`
- Upgrade later with a script that reads a "speech:" line from Claude's output

### Recommendation
1. Try a Claude-specific TTS hook first (Kokoro-based or MCP TTS)
2. For more control: add small Python TTS helper using pyttsx3 + Claude Code hook

## Answer 5: Summary/Confirmation

- System-wide TTS → start with **Orca**
- Claude Code TTS → start with community **TTS hooks/plugins**

---

## All Citation Sources (18 unique URLs)

### Ubuntu Documentation
1. [Read documents and web pages using the screen reader](https://documentation.ubuntu.com/desktop/en/latest/how-to/accessibility/orca/read-documents-and-web-pages-using-the-screen-reader/)
2. [Navigate the screen using the screen reader](https://documentation.ubuntu.com/desktop/en/latest/how-to/accessibility/orca/navigate-the-screen-using-the-screen-reader/)
3. [Read the screen aloud (24.04)](https://documentation.ubuntu.com/desktop/en/24.04/how-to/accessibility/orca/read-screen-aloud/)
4. [Navigate the interface using the keyboard](https://documentation.ubuntu.com/desktop/en/latest/how-to/accessibility/navigate-the-interface-using-the-keyboard/)
5. [Get started with the screen reader](https://documentation.ubuntu.com/desktop/en/latest/tutorial/get-started-with-the-screen-reader/)
6. [Orca manpage (Jammy)](https://manpages.ubuntu.com/manpages/jammy/man1/orca.1.html)

### GNOME Documentation
7. [Orca: Reading documents](https://help.gnome.org/orca/howto_documents.html)
8. [Orca: Reading commands](https://help.gnome.org/orca/commands_reading.html)
9. [Welcome to Orca](https://help.gnome.org/orca/introduction.html)

### Claude Code TTS
10. [claude-code-tts (sourcehut) — Hook-based TTS for Claude Code](https://git.sr.ht/~cg/claude-code-tts)
11. [claude-code-tts (GitHub) — MCP TTS plugin](https://github.com/ybouhjira/claude-code-tts)
12. [Running a Fully Local Voice Pipeline for Claude Code on RHEL 10](https://crunchtools.com/local-voice-pipeline-claude-code-rhel10-intel-gpu/)

### Python TTS / General Linux TTS
13. [pyttsx3: Offline TTS Engine for Python (dev.to)](https://dev.to/imrrobot/pyttsx3-offline-text-to-speech-tts-engine-for-python-949)
14. [pyttsx3 official site](https://pyttsx3.com)
15. [How to use espeak with Python (StackOverflow)](https://stackoverflow.com/questions/17547531/how-to-use-espeak-with-python)
16. [Introduction to pyttsx3 (Plain English)](https://python.plainenglish.io/an-introduction-to-pyttsx3-a-text-to-speech-conversion-library-in-python-5a11c0c68ad3)
17. [Text-to-Speech on Linux (Substack)](https://ebenfarnworth.substack.com/p/text-to-speech-tts-on-linux)
18. [5 Simple Ways to Enable Speech Output from Your Linux Terminal](https://www.chicagovps.net/blog/5-simple-ways-to-enable-speech-output-from-your-linux-terminal/)
19. [Python Text to Speech using pyttsx3 (GeeksforGeeks)](https://www.geeksforgeeks.org/python/python-text-to-speech-by-using-pyttsx3/)

### Not captured from DOM (referenced in text, likely virtualized out)
- YouTube (Orca terminal demo) — URL not captured, cited as `YouTube` in answers 3-4
- GitHub (`ybouhjira/claude-code-tts`) — captured via Links tab: https://github.com/ybouhjira/claude-code-tts

---

## Extraction Method Notes

**What worked:**
- React fiber tree traversal: `span.citation.inline-flex` → `__reactFiber` → `memoizedProps.children.props.url`
- The key props on citation children: `domain`, `url`, `href`, `source`, `overflowCount`
- The "Links" tab exposes source cards as real `<a href>` elements (but only for the last/active answer)

**Limitations:**
- Perplexity uses React virtualization — earlier answers' DOM gets unloaded when scrolled past
- YouTube citations and some GitHub citations weren't in the DOM at extraction time
- The "Links" tab only shows sources for the currently selected answer, not all answers
- Standard `document.querySelectorAll('a[href]')` returns almost nothing — Perplexity barely uses real anchor tags in the Answer view

**Recommended approach for a skill:**
1. Switch to Answer view
2. Scroll to each answer section to force React to render its DOM
3. Extract citations via React fiber: `span.citation.inline-flex` → fiber → `children.props.url`
4. Also check the Links tab for each answer for supplemental sources
5. Combine and deduplicate

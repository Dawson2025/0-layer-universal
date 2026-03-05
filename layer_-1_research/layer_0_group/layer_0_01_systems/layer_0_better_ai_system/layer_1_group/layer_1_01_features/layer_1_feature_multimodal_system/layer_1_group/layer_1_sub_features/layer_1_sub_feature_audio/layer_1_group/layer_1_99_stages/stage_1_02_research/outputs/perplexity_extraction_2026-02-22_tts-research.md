---
resource_id: "0196a273-434d-4d98-915b-678946f9c38b"
resource_type: "output"
resource_name: "perplexity_extraction_2026-02-22_tts-research"
---
# Perplexity Extraction: System-Wide TTS + Claude Code TTS

**Source**: https://www.perplexity.ai/search/hey-how-s-it-going-doing-prett-VVzJDBQ9Tkq2MIwXHhxo6w
**Extracted**: 2026-02-22 (initial), 2026-02-23 (expanded)
**Method**: Claude in Chrome (React fiber citation extraction + full page text extraction)

---

<!-- section_id: "e370f7af-bc9c-49f7-9dc2-2bbe1946092b" -->
## Thread Summary

A multi-turn Perplexity conversation about:
1. System-wide text-to-speech (TTS) options for Ubuntu Linux
2. Claude Code CLI text-to-speech integration via community hooks/plugins

<!-- section_id: "05c5c09b-4f25-4c20-b2ec-9ffd338386ad" -->
### Key Conclusions
- **System-wide TTS**: Start with **Orca** (built into GNOME/Ubuntu) — covers GUI apps, browser, and terminal
- **Claude Code TTS**: Use community TTS hooks/plugins (Kokoro-based hook or MCP TTS plugin)

---

<!-- section_id: "6225e641-0c28-4cd0-8143-1860b2311a85" -->
## Answer 1: System-Wide TTS Recommendations

Initial recommendations for system-wide TTS on Ubuntu:
- **Resemble AI** — ultra-realistic, human-like voices, extensive customization
- **Piper** — open-source, fully offline, neural TTS models with natural speech
- **Murf** — premium cloud-based voices with media integration
- **eSpeak NG** — longstanding, lightweight classic option

For simplicity and system-wide functionality, Speech Note or Piper are great choices. For premium human-like voices, Murf or Resemble AI could be ideal.

<!-- section_id: "e35aa35c-a1e5-4e3f-a0df-02cac430baaa" -->
## Answer 2: Highlight-and-Speak (like Whisperflow/Vibetyper)

- **Speech Note** — flexible, works across different applications, lets you highlight text anywhere and read it aloud

<!-- section_id: "9bd45901-1eec-48dd-a6ef-da1d080e936f" -->
## Answer 3: Hybrid AI TTS System (Agentic Approach)

User asked about setting up a system where AI (like Claude) can do things and give certain outputs — not necessarily reading the full output aloud, but providing a shorter spoken summary alongside visual output (ASCII diagrams, code, text).

<!-- section_id: "90490a50-1379-4b3b-b563-0ca4210b3045" -->
### The Two-Layer Architecture
1. **System-wide TTS on Ubuntu** — handles general desktop/browser/terminal reading
2. **"Agentic" AI TTS** — AI decides what to say vs what to show

<!-- section_id: "695ac442-a1ed-4739-9d6e-a8902d1b1cb0" -->
### Ubuntu TTS Stack Components
On Ubuntu, TTS is usually built from these pieces:
- A **screen reader** (Orca) that reads UI elements, focused text, etc.
- A **speech layer** (Speech Dispatcher) that any app can send text to
- One or more **engines/voices** (eSpeak NG, Festival, Mimic, Piper, etc.)

<!-- section_id: "643b7acc-c76d-428a-857a-7cc773d1aa9e" -->
### Common Free Engines
| Engine | Characteristics |
|--------|----------------|
| **eSpeak / eSpeak NG** | Very lightweight, works everywhere, but robotic |
| **Festival** | More configurable, different voices, better quality than default eSpeak |
| **Mimic / Mimic 3 (Mycroft)** | Newer, more natural voices, still local and free |
| **Piper** | Neural TTS, very natural, runs offline, multiple voice models |

<!-- section_id: "82af0231-493f-41cd-a9d0-ce85f6112aaa" -->
### A. Highlight-and-Speak Pattern
The simplest approach — no special app support needed:
1. Use `xsel` (or `xclip`) to grab the current X selection
2. Pipe that into a TTS engine like Festival, Mimic, or eSpeak
3. Bind that script to a global keyboard shortcut in GNOME/KDE

Example approaches:
- Ubuntu wiki example with **Gespeaker** + xsel and a shortcut to read the clipboard selection
- Blog examples: "Read Selected Text" shortcut runs `xsel` then Festival or Mimic to speak, plus a second shortcut to stop speech
- Forum tip: highlight with mouse, then `xsel | festival --tts` to speak it

<!-- section_id: "0152738b-a5c8-4f43-8f8b-44ed504e2471" -->
### B. Continuous / Focus-Based Reading (No Manual Highlighting)
Other system-wide patterns that don't require highlighting:

- **Orca screen reader** (comes with GNOME):
  - Reads the focused control, window, menus, notifications, etc.
  - Has commands to read current line, paragraph, entire window
  - Uses Speech Dispatcher, so you can change the underlying voice (Festival, Mimic, Piper)

- **Terminal-only speech**:
  - **Speakup**: in-kernel screen reader for the Linux text console, typically wired to eSpeak via `espeakup`
  - **Fenrir** and **Emacspeak**: user-land screen readers aimed at command-line environments

<!-- section_id: "3471a65c-e5a1-40d6-9482-097a21d70d18" -->
### Agentic AI TTS: What You Want vs What Exists

| Use Case | How It Works | What You Need |
|----------|-------------|---------------|
| "Read the screen / focused UI elements/messages" | Orca screen reader with a better voice | Festival, Mimic, Piper (YouTube, ubuntu-mate) |
| "Only read summaries, not all text" | AI returns both full text and a `spoken_summary`; only feed the summary to TTS | Claude (or other model), local TTS via pyttsx3 or CLI engines |
| "Agent that talks and shows diagrams/code" | Build a small client where the model outputs separate fields for voice vs display | Same as above, plus your preferred terminal/editor for visuals |
| "Talk about terminal output selectively" | Have scripts parse command output, extract key lines, send only those to TTS | Shell or Python glue, any TTS engine |

<!-- section_id: "07ae38b5-3dd4-402a-b673-c2c3dce47a9d" -->
## Answer 4: Orca for Desktop + Terminal Users

Recommended for users who mix normal desktop apps with terminal work.

<!-- section_id: "fadcf30e-b98d-4e29-aa20-4d99947b27ea" -->
### 1. What Orca Will Cover For You

On a standard Ubuntu GNOME desktop:

**GUI apps and browser**
- Orca can read windows, menus, buttons, dialogs, and web pages in Firefox/Chromium using caret navigation (arrow keys, etc.)
- You can move through text by character, word, line, and it will speak your position as you go

**Terminal windows**
- In GNOME Terminal (and similar terminals), Orca reads the output of commands and what you type
- With "screen review" / flat-review commands, you can move back up through previous lines in the terminal and have them read again, not just the latest output

**Whole-window / screen review**
- Orca has "Say All" and flat-review commands to read the active window or dialog without manually selecting text
- You can toggle flat review and then move line-by-line or object-by-object across whatever's visible in that window

You control it with keyboard shortcuts to:
- Read the current object, line, paragraph, or entire window
- Move focus around the screen and have it announce what's under the cursor/focus

<!-- section_id: "3e0341d4-3fd0-463e-910d-a9515ddb37d6" -->
### 2. Basic Setup on Ubuntu GNOME
- **Turn Orca on**: press `Super + Alt + S` (toggles the screen reader)
- **Browser**: press `F7` to enable caret navigation if needed, then use arrow keys to move and listen
- **Terminal**: run commands and use Orca's review commands to move back over previous output

<!-- section_id: "73d35c33-1752-4633-9549-66c03c2841f3" -->
### 3. Console-Only Screen Readers (Non-Graphical TTY)
If you drop to a pure text console (`Ctrl+Alt+F3`, no GNOME):
- **Speakup**: in-kernel screen reader for the Linux text console, typically wired to eSpeak via `espeakup`
- **Fenrir** and **Emacspeak**: user-land screen readers aimed at command-line environments

These don't interact with the graphical desktop; they are for the raw TTY.

<!-- section_id: "b93c05e3-7e93-42d2-9282-518211387327" -->
### 4. Where Highlight-and-Speak Scripts Fit In
Even with Orca running, you might still want:
- A hotkey to read only the current selection (e.g., a particular paragraph in a web page, or a chunk of terminal output)
- A different voice than Orca's default for those ad-hoc reads (Festival, Mimic, etc.)

That's where the `xsel + TTS engine` idea complements Orca:
- Orca gives you broad coverage and navigation
- The custom script gives you a fast "speak exactly this highlighted text" tool when you need precision

<!-- section_id: "8d93f6aa-9e74-49ee-b9e1-db7c0b207951" -->
## Answer 5: Claude Code CLI — Agentic TTS Options

<!-- section_id: "04664036-4903-435e-9580-926802bc2d39" -->
### Option 1: Existing Claude Code TTS Hooks (Recommended)
People have already built TTS integrations specifically for Claude Code:
- **Kokoro-based hook** (sourcehut) — plugs into Claude Code's hook system and automatically speaks responses using a local Kokoro TTS model
- **MCP TTS plugin** (GitHub) — exposes TTS as an MCP tool, so Claude Code can call it when it wants to speak while still printing the full text to the terminal/editor

Key benefit: Claude can output full text (ASCII diagrams, code) to CLI while using a shorter "voice line" (summary) for TTS — what you hear is not forced to be identical to what you see.

<!-- section_id: "f62b242b-7a27-4492-8365-81e7f0de9491" -->
### Option 2: DIY Agentic TTS with Local Python Helper
A small Python script + local TTS library:

**Use pyttsx3 as TTS layer:**
- Runs fully offline on Linux, wraps native engines like eSpeak/Festival
- Lets you set voice, rate, and volume from Python

**Have Claude output structured text:**
```json
{
  "spoken_summary": "Short explanation to read aloud.",
  "visual_output": "<ASCII diagram or detailed text here>"
}
```

**Your helper script:**
- Writes `visual_output` to the screen
- Runs `espeak` or `festival --tts` on `spoken_summary` only

**Libraries:**
- **pyttsx3**: Python TTS wrapper that talks to eSpeak/eSpeak-NG under the hood, fully offline, lets you choose voice, speed, and save audio if you want

<!-- section_id: "244aa303-b5c2-417a-96fb-78fa18a0a6b2" -->
### Option 3: Simple CLI Approach (No Hooks)
- Run Claude Code CLI as usual
- For certain answers, pipe only the part you want spoken: `echo "Short spoken line" | espeak`
- Upgrade later with a script that reads a "speech:" line from Claude's output and automatically speaks it

<!-- section_id: "d7a5674f-b93b-459d-a2b7-921ca294a1c3" -->
### Recommendation
1. **Try a Claude-specific TTS hook first** (Kokoro-based or MCP TTS), because they're designed to integrate directly with Claude Code's events
2. **For more control**: add small Python TTS helper using pyttsx3 and configure a Claude Code hook to call it with a short "speech" string while leaving full content in the CLI

<!-- section_id: "623821d2-8e3d-4fd8-974f-d5c4e87abf41" -->
## Answer 6: Summary/Confirmation

- System-wide TTS → start with **Orca** (integrated into GNOME, reads browsers, GUI apps, terminal windows)
- Claude Code TTS → start with community **TTS hooks/plugins** built specifically for Claude Code, which connect it to a local TTS engine

---

<!-- section_id: "33ab3d7a-67db-4d98-b3c8-446c468837c4" -->
## All Citation Sources (20 unique URLs)

<!-- section_id: "21d60a1b-924a-44d4-9704-c2cabb2dba7d" -->
### Ubuntu Documentation
1. [Read documents and web pages using the screen reader](https://documentation.ubuntu.com/desktop/en/latest/how-to/accessibility/orca/read-documents-and-web-pages-using-the-screen-reader/)
2. [Navigate the screen using the screen reader](https://documentation.ubuntu.com/desktop/en/latest/how-to/accessibility/orca/navigate-the-screen-using-the-screen-reader/)
3. [Read the screen aloud (24.04)](https://documentation.ubuntu.com/desktop/en/24.04/how-to/accessibility/orca/read-screen-aloud/)
4. [Navigate the interface using the keyboard](https://documentation.ubuntu.com/desktop/en/latest/how-to/accessibility/navigate-the-interface-using-the-keyboard/)
5. [Get started with the screen reader](https://documentation.ubuntu.com/desktop/en/latest/tutorial/get-started-with-the-screen-reader/)
6. [Orca manpage (Jammy)](https://manpages.ubuntu.com/manpages/jammy/man1/orca.1.html)

<!-- section_id: "96ed8fba-2190-4c2d-811f-da2bac35c5dc" -->
### GNOME Documentation
7. [Orca: Reading documents](https://help.gnome.org/orca/howto_documents.html)
8. [Orca: Reading commands](https://help.gnome.org/orca/commands_reading.html)
9. [Welcome to Orca](https://help.gnome.org/orca/introduction.html)

<!-- section_id: "f60c3a0d-9a2c-460b-88bd-a1dcb500f9cf" -->
### YouTube
10. [Orca Terminal Demo](https://www.youtube.com/watch?v=i40dJu0ovgE)

<!-- section_id: "c8472a8b-6d14-4b6b-bdf7-21a7425b2c07" -->
### Claude Code TTS
11. [claude-code-tts (sourcehut) — Hook-based TTS for Claude Code](https://git.sr.ht/~cg/claude-code-tts)
12. [claude-code-tts (GitHub) — MCP TTS plugin](https://github.com/ybouhjira/claude-code-tts)
13. [Running a Fully Local Voice Pipeline for Claude Code on RHEL 10](https://crunchtools.com/local-voice-pipeline-claude-code-rhel10-intel-gpu/)

<!-- section_id: "eb4bafb4-e36c-4308-aa5b-a02b4722b115" -->
### Python TTS / General Linux TTS
14. [pyttsx3: Offline TTS Engine for Python (dev.to)](https://dev.to/imrrobot/pyttsx3-offline-text-to-speech-tts-engine-for-python-949)
15. [pyttsx3 official site](https://pyttsx3.com)
16. [How to use espeak with Python (StackOverflow)](https://stackoverflow.com/questions/17547531/how-to-use-espeak-with-python)
17. [Introduction to pyttsx3 (Plain English)](https://python.plainenglish.io/an-introduction-to-pyttsx3-a-text-to-speech-conversion-library-in-python-5a11c0c68ad3)
18. [Text-to-Speech on Linux (Substack)](https://ebenfarnworth.substack.com/p/text-to-speech-tts-on-linux)
19. [5 Simple Ways to Enable Speech Output from Your Linux Terminal](https://www.chicagovps.net/blog/5-simple-ways-to-enable-speech-output-from-your-linux-terminal/)
20. [Python Text to Speech using pyttsx3 (GeeksforGeeks)](https://www.geeksforgeeks.org/python/python-text-to-speech-by-using-pyttsx3/)

---

<!-- section_id: "bb95f0aa-11bd-4e51-a231-4d1332d22a47" -->
## Extraction Method Notes

<!-- section_id: "2baf01e5-f6f5-406f-bf5d-8d1aeacc4257" -->
### 2026-02-22 (Initial)
- React fiber tree traversal: `span.citation.inline-flex` → `__reactFiber` → `memoizedProps.children.props.url`
- 18 URLs captured; YouTube URL was virtualized out of DOM

<!-- section_id: "2b9ee925-a9e8-491b-bd7d-4ebca40de587" -->
### 2026-02-23 (Expanded)
- Full page text via `get_page_text` tool after scrolling through all answers
- React fiber extraction captured 20 URLs including the previously missing YouTube URL
- Scrolling through all answers before extraction forced React to render citation DOM nodes

**Key learning**: Combine `get_page_text` (for content) with React fiber extraction (for citation URLs) for most complete results. Scroll through entire thread first to defeat virtualization.

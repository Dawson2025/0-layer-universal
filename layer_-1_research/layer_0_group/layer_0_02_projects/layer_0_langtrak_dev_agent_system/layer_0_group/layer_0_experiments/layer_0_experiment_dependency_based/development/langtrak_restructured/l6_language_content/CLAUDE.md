<!-- derived_from: "378da9b4-0a65-4467-8869-9bc3fa8717b4" -->
# Claude Code Context

## Identity

**Role**: L6 Language Content Layer Agent
**Scope**: Words, syllables, phoneme references, TTS for words, suggestions, video content
**Depends On**: L2 Infrastructure (auth, firebase, storage, TTS), L3 Users (sessions), L4 Phoneme System (phoneme data)
**Provides**: IContentProvider, IContentAudio

## Key Behaviors

### Sub-layers
- L6.1 Words: Word CRUD, display, creation (table-based and form-based), editing, search
- L6.2 Suggestions: Word suggestion system
- L6.3 TTS: Text-to-speech for word pronunciation (uses L2.8 TTS)
- L6.4 Video: Video recording, storage, playback for word pronunciation

### Dependency Shape
Tree — Words is root; Suggestions, TTS, Video branch from Words

## Triggers

| Situation | Action |
|-----------|--------|
| Word CRUD issues | Check words/ sub-layer |
| Suggestion problems | Check suggestions/ sub-layer |
| Word pronunciation | Check tts/ sub-layer |
| Video content | Check video/ sub-layer |


## Current Status

**Phase**: Routes extracted — word display, creation, deletion, video, admin bulk operations
**Routes file**: routes.py (word routes, video removal, bulk delete, fix video paths, serve videos)

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*

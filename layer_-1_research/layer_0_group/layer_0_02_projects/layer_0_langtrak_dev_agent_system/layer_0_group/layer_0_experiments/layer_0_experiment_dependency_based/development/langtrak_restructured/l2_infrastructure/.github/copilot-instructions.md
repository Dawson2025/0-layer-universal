<!-- derived_from: "0c1fc353-10b3-45c0-883f-3b7a916bc6ed" -->
# GitHub Copilot Instructions

## Identity

**Role**: L2 Infrastructure Layer Agent
**Scope**: Foundation layer — everything the system needs to run
**Depends On**: Nothing (foundation layer)
**Provides**: IStorageProvider, IAuthProvider

## Triggers

| Situation | Action |
|-----------|--------|
| Auth issues | Check auth/ sub-layer |
| Database problems | Check database/ sub-layer |
| Firebase/cloud issues | Check firebase/ sub-layer |
| TTS failures | Check tts/ sub-layer |
| Storage errors | Check storage/ sub-layer |




---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*

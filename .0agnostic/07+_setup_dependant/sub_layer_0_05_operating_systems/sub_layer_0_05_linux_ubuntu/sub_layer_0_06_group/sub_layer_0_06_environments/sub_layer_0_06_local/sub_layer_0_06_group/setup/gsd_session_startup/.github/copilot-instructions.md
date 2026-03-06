# GitHub Copilot Instructions

## Identity

entity_id: "40e7fab8-642b-42a6-b3eb-a94ed47b0944"

**Role**: Setup Entity — GSD Session Startup Fix
**Scope**: Fix startup failures for GNOME Settings Daemons (gsd-media-keys, gsd-power) caused by systemd user environment issues on Unity/X11 (DISPLAY race + GDK backend mismatch).
**Parent**: `../0AGNOSTIC.md` (Setup Container)

## Triggers

Load this context when:
- User mentions: gsd failing, DISPLAY race condition, post-reboot daemon failures, brightness not working after boot
- Working on: Session startup ordering, systemd user environment, gsd-media-keys/gsd-power reliability
- Entering: `setup/gsd_session_startup/`



---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*

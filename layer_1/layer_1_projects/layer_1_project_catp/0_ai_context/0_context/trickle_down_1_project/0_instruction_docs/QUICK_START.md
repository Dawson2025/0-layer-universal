---
resource_id: "1b1a6ceb-cc33-425c-8ff9-b36358fd4caa"
resource_type: "document"
resource_name: "QUICK_START"
---
# Multi-Repo Quick Start (assignment-time + task-timer-frontend)

This guide explains how to work on the Firebase backend (`assignment-time`) and the Chrome extension frontend (`task-timer-frontend`) in the same session without crossing wires.

## Repository Roles

| Repo | Path | Purpose |
|------|------|---------|
| `assignment-time` | `/home/dawson/dawson-workspace/code/catp/assignment-time` | Firebase Functions + CLI tooling for Canvas assignment ingestion, timing, and data syncing. Contains the Functions emulator (`functions/`) and the CLI timer (`assignment-timer/`). |
| `task-timer-frontend` | `/home/dawson/dawson-workspace/code/catp/task-timer-frontend` | Chrome extension (bundled via `manifest.json`) that surfaces timing averages in Canvas. |

## One-Time Setup Per Repo

### assignment-time
1. `cd /home/dawson/dawson-workspace/code/catp/assignment-time/functions && npm install` (Firebase Functions + emulator deps)
2. `cd /home/dawson/dawson-workspace/code/catp/assignment-time/assignment-timer && npm install` (CLI timer)
3. Export Canvas credentials or place them in `functions/.env.local` (`CANVAS_API_KEY`, etc.).

### task-timer-frontend
1. `cd /home/dawson/dawson-workspace/code/catp/task-timer-frontend && npm install`
2. Enable Chrome developer mode once (`chrome://extensions → Developer mode → Load unpacked → repo root`).

## Daily Workflow (Same Session)
1. **Open two terminals/tabs** (or panes) so each repo has its own working directory. Never run commands for one repo from the other's shell.
2. **Backend terminal** (`assignment-time/functions`):
   - Start emulators: `firebase emulators:start --only functions,firestore`
   - In another split (still within `assignment-time`), seed + test: `node test-student-course-details.js`
   - CLI work (if needed): `cd ../assignment-timer && npm start`
3. **Frontend terminal** (`task-timer-frontend`):
   - Run dev build / watch: `npm run dev` (for live reload) or `npm run build` before reloading the extension.
   - Reload the extension in Chrome after each build via `chrome://extensions → Reload`.
4. **Environment variables**: keep Canvas + Firebase secrets in `assignment-time/functions/.env.*`; extension-specific settings (if any) live in `task-timer-frontend/.env`. Do not share files between repos—duplicate values manually when required.
5. **Branch coordination**: create matching branch names manually (e.g., `feature/session-sync`) in both repos when implementing a cross-cutting change. Commit/push separately.

## Testing & Verification
- Backend: run `node test-student-course-details.js` while emulators are up, plus any Jest/CLI tests under `assignment-timer/test.js`.
- Frontend: rely on `npm run dev` for hot reload and manually exercise the extension on the Canvas Assignments page; document manual test steps in `trickle_down_3_testing` when behavior changes.
- When both sides change, verify end-to-end: seed Canvas data → run the CLI timer → observe the extension overlay once you reload it in Chrome.

## Troubleshooting Tips
- If terminal commands hang, run Python scripts through `scripts/terminal_wrapper.py` per the universal terminal policy.
- Keep emulator logs and Vite output visible simultaneously; coordination bugs usually show up in one console first.
- When Chrome caches assets, click “Update” in the Extensions page or bump the extension version in `manifest.json` before packaging.

## Reference Checklist Before Ending a Session
- [ ] `assignment-time` emulator stopped cleanly (Ctrl+C) and recent logs reviewed.
- [ ] `task-timer-frontend` extension reloaded to confirm the latest bundle.
- [ ] Tests or manual verifications noted in `trickle_down_3_testing` if new behavior was introduced.
- [ ] Context/requirements docs updated for any cross-repo changes (this file is the canonical entry point for future agents).

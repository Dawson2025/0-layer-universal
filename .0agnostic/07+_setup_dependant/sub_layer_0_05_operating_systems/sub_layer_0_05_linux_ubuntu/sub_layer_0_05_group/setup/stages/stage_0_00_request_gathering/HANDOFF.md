---
resource_id: "578312d7-8bdb-4fd5-bc7f-78e1319f8d82"
resource_type: "document"
resource_name: "HANDOFF"
---
# Stage 0.00 Handoff: Linux Setup Tasks

## Status: IN PROGRESS

## Summary
Two related tasks: (1) Fix Linux login loop via cloud server SSH, (2) Set up Termius for cross-device SSH access. VPS and Windows setup complete, waiting for Linux boot to continue.

## Active Requests
| Request | Status | Priority |
|---------|--------|----------|
| Fix Linux Login Loop | In Progress | HIGH |
| Termius Cross-Device SSH | In Progress | MEDIUM |

## Completed
- [x] Requirements gathered for both tasks
- [x] User context documented (dual-boot, Syncthing, VPS)
- [x] API keys and credentials identified

## Next Actions
- [ ] Boot into Linux to get IP address
- [ ] Execute login loop fix
- [ ] Complete Termius setup on all devices

## Output Files
- `output/REQUEST_fix_linux_login_loop_via_cloud_ssh.md` - Full login loop requirements
- `output/REQUEST_termius_cross_device_ssh.md` - Cross-device SSH requirements

## Blockers
- Linux login loop prevents direct access (must fix via SSH)

## Pickup Instructions
Read output files for full context. Proceed to stage_0_01 for technical specs.

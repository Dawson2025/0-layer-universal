---
resource_id: "578312d7-8bdb-4fd5-bc7f-78e1319f8d82"
resource_type: "document"
resource_name: "HANDOFF"
---
# Stage 0.00 Handoff: Linux Setup Tasks

<!-- section_id: "93fc10b8-9b4b-48ba-b42f-ff0930b21908" -->
## Status: IN PROGRESS

<!-- section_id: "4f3f2461-99a4-465a-836d-ae4e2acd9f71" -->
## Summary
Two related tasks: (1) Fix Linux login loop via cloud server SSH, (2) Set up Termius for cross-device SSH access. VPS and Windows setup complete, waiting for Linux boot to continue.

<!-- section_id: "86824f29-d5c0-4986-880e-c108140cde80" -->
## Active Requests
| Request | Status | Priority |
|---------|--------|----------|
| Fix Linux Login Loop | In Progress | HIGH |
| Termius Cross-Device SSH | In Progress | MEDIUM |

<!-- section_id: "ff363137-ac47-4617-84ba-6f0345619f15" -->
## Completed
- [x] Requirements gathered for both tasks
- [x] User context documented (dual-boot, Syncthing, VPS)
- [x] API keys and credentials identified

<!-- section_id: "f60a1d17-6cea-417a-b5ae-6e701d756de4" -->
## Next Actions
- [ ] Boot into Linux to get IP address
- [ ] Execute login loop fix
- [ ] Complete Termius setup on all devices

<!-- section_id: "0a5f2e7c-91ba-472e-b417-a0cc23e9e17f" -->
## Output Files
- `output/REQUEST_fix_linux_login_loop_via_cloud_ssh.md` - Full login loop requirements
- `output/REQUEST_termius_cross_device_ssh.md` - Cross-device SSH requirements

<!-- section_id: "92cb0fec-d324-4774-9112-aaab5a5e8f2b" -->
## Blockers
- Linux login loop prevents direct access (must fix via SSH)

<!-- section_id: "1e271959-2a23-4620-b0e9-01b54521ae68" -->
## Pickup Instructions
Read output files for full context. Proceed to stage_0_01 for technical specs.

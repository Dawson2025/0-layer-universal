---
resource_id: "ec52fd99-7968-4d55-affe-f33b7e81587c"
resource_type: "knowledge"
resource_name: "UBUNTU_HANDOFF"
---
# Ubuntu Desktop Setup Handoff Document

<!-- section_id: "1a771ec4-362a-490b-be34-66d1bfdd589f" -->
## Purpose
This handoff document provides a streamlined checklist for setting up the Ubuntu desktop portion of the multi-OS workspace sync. Use this alongside UBUNTU_SETUP_INSTRUCTIONS.md for detailed steps.

<!-- section_id: "ad19706f-b16b-4ce7-a171-fdc227a07b91" -->
## Current Status
- ✅ WSL workspace configured and running
- ✅ Windows workspace configured and running
- ✅ WSL ↔ Windows sync verified and working
- ⏳ Ubuntu desktop awaiting setup

<!-- section_id: "3137901f-f335-4af8-8378-46c4f4ac91a8" -->
## Prerequisites Before You Start on Ubuntu

1. [ ] You are physically at the Ubuntu desktop machine
2. [ ] Ubuntu desktop has internet connectivity
3. [ ] You have sudo privileges on Ubuntu
4. [ ] Git is installed on Ubuntu
5. [ ] You have GitHub SSH key set up (or GitHub credentials ready)

<!-- section_id: "10bb4ab6-3630-46ec-ba63-8f59f331dd3e" -->
## Quick Setup Checklist

<!-- section_id: "87520045-657b-42e8-801b-8e6a1930ce9f" -->
### Phase 1: Initial Setup (5 minutes)
- [ ] Create workspace directory structure
- [ ] Install Syncthing (see UBUNTU_SETUP_INSTRUCTIONS.md Step 3)
- [ ] Start Syncthing service
- [ ] Open Syncthing web UI at http://localhost:8384

<!-- section_id: "9ed125cc-bbc1-4df3-b80e-3c549730d850" -->
### Phase 2: Device Connection (10 minutes)
- [ ] Get Ubuntu device ID from Syncthing UI (Actions → Show ID)
- [ ] Record Ubuntu device ID in DEVICE_IDS.md
- [ ] Add WSL device to Ubuntu Syncthing (ID from DEVICE_IDS.md)
- [ ] Add Windows device to Ubuntu Syncthing (ID from DEVICE_IDS.md)
- [ ] On WSL: Add Ubuntu device (you may need to do this later or remotely)
- [ ] On Windows: Add Ubuntu device (you may need to do this later or remotely)

<!-- section_id: "742da4a0-70e5-4a9c-81f4-169582473cd4" -->
### Phase 3: Folder Sync (5 minutes)
- [ ] Accept dawson-workspace folder share from WSL/Windows
- [ ] Set folder path to: /home/dawson/dawson-workspace
- [ ] Set folder type to: Send & Receive
- [ ] Enable Staggered File Versioning (14 days / 1209600 seconds)
- [ ] Wait for initial sync to complete (watch progress in UI)

<!-- section_id: "bf6778b9-4c9c-45d8-a26d-900c8de58a9d" -->
### Phase 4: Verification (5 minutes)
- [ ] Check SYNC_TEST.md exists and has correct content
- [ ] Verify dotfiles/ directory synced from WSL/Windows
- [ ] Check that code/, agents/, ai-mcp/ and other folders populated
- [ ] Create Ubuntu test file
- [ ] Verify test file appears on WSL and Windows within 10 seconds

<!-- section_id: "c96ce8ec-7e43-49ec-bba8-06663e47d457" -->
### Phase 5: Dotfiles and Git (5 minutes)
- [ ] Run dotfiles installer
- [ ] Reload shell
- [ ] Verify git config
- [ ] Set up git SSH key if needed (see UBUNTU_SETUP_INSTRUCTIONS.md Step 8)

<!-- section_id: "ae1d38b0-b528-4dfa-a80a-184f9c228d5c" -->
### Phase 6: Final Documentation (5 minutes)
- [ ] Update DEVICE_IDS.md with Ubuntu device ID
- [ ] Mark completion date in UBUNTU_SETUP_INSTRUCTIONS.md
- [ ] Update PLAN_AND_IMPLEMENTATION.md Ubuntu status
- [ ] Git commit and push changes

<!-- section_id: "65aaecb1-cbaa-40e8-9fb5-77e5bc48c79c" -->
## Expected Outcomes

After completing this checklist:
- Ubuntu workspace at /home/dawson/dawson-workspace matches WSL and Windows
- Syncthing running on all three systems with all devices connected
- Three-way sync working in all directions (WSL ↔ Windows ↔ Ubuntu)
- Dotfiles deployed and shell environment configured
- Git ready for development work
- All documentation updated

<!-- section_id: "a02ceaa8-d46a-440d-b7f5-6f634b3d00df" -->
## Troubleshooting Quick Reference

**Syncthing won't start**
- Check logs: `journalctl --user -u syncthing.service -f`

**Devices won't connect**
- Check firewall port 22000
- Verify device IDs are correct

**Files not syncing**
- Check .stignore file
- Verify Send & Receive enabled
- Check Syncthing web UI for errors

**Dotfiles install fails**
- Check permissions
- Re-clone from GitHub if needed

<!-- section_id: "fb3c2777-a37f-46e0-8f7e-75640cb15acc" -->
## Estimated Total Time
**30-35 minutes** for complete setup (assuming no issues)

<!-- section_id: "2a97bc6d-4f47-4f94-bb29-b0de9c578e35" -->
## Files to Reference
- Detailed instructions: UBUNTU_SETUP_INSTRUCTIONS.md
- Device IDs: DEVICE_IDS.md
- Overall plan: PLAN_AND_IMPLEMENTATION.md
- Current status: ../../../docs/CURRENT_STATUS.md

<!-- section_id: "2d314842-b13e-4d48-842d-54d18c50ecd8" -->
## Questions or Issues?
If you encounter problems:
1. Check UBUNTU_SETUP_INSTRUCTIONS.md troubleshooting section
2. Check Syncthing logs: `journalctl --user -u syncthing.service`
3. Verify all device IDs are correct in DEVICE_IDS.md
4. Check that WSL and Windows Syncthing instances are still running

---
**Handoff created**: 2025-12-31
**Next action**: Follow this checklist on Ubuntu desktop

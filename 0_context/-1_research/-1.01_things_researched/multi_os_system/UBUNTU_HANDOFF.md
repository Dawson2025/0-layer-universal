# Ubuntu Desktop Setup Handoff Document

## Purpose
This handoff document provides a streamlined checklist for setting up the Ubuntu desktop portion of the multi-OS workspace sync. Use this alongside UBUNTU_SETUP_INSTRUCTIONS.md for detailed steps.

## Current Status
- ✅ WSL workspace configured and running
- ✅ Windows workspace configured and running
- ✅ WSL ↔ Windows sync verified and working
- ✅ Ubuntu desktop configured and ready (2025-12-31)
- ⏳ Three-way sync pending (needs WSL/Windows to add Ubuntu device)

## Prerequisites Before You Start on Ubuntu

1. [ ] You are physically at the Ubuntu desktop machine
2. [ ] Ubuntu desktop has internet connectivity
3. [ ] You have sudo privileges on Ubuntu
4. [ ] Git is installed on Ubuntu
5. [ ] You have GitHub SSH key set up (or GitHub credentials ready)

## Quick Setup Checklist

### Phase 1: Initial Setup (5 minutes)
- [ ] Create workspace directory structure
- [ ] Install Syncthing (see UBUNTU_SETUP_INSTRUCTIONS.md Step 3)
- [ ] Start Syncthing service
- [ ] Open Syncthing web UI at http://localhost:8384

### Phase 2: Device Connection (10 minutes)
- [ ] Get Ubuntu device ID from Syncthing UI (Actions → Show ID)
- [ ] Record Ubuntu device ID in DEVICE_IDS.md
- [ ] Add WSL device to Ubuntu Syncthing (ID from DEVICE_IDS.md)
- [ ] Add Windows device to Ubuntu Syncthing (ID from DEVICE_IDS.md)
- [ ] On WSL: Add Ubuntu device (you may need to do this later or remotely)
- [ ] On Windows: Add Ubuntu device (you may need to do this later or remotely)

### Phase 3: Folder Sync (5 minutes)
- [ ] Accept dawson-workspace folder share from WSL/Windows
- [ ] Set folder path to: /home/dawson/dawson-workspace
- [ ] Set folder type to: Send & Receive
- [ ] Enable Staggered File Versioning (14 days / 1209600 seconds)
- [ ] Wait for initial sync to complete (watch progress in UI)

### Phase 4: Verification (5 minutes)
- [ ] Check SYNC_TEST.md exists and has correct content
- [ ] Verify dotfiles/ directory synced from WSL/Windows
- [ ] Check that code/, agents/, ai-mcp/ and other folders populated
- [ ] Create Ubuntu test file
- [ ] Verify test file appears on WSL and Windows within 10 seconds

### Phase 5: Dotfiles and Git (5 minutes)
- [ ] Run dotfiles installer
- [ ] Reload shell
- [ ] Verify git config
- [ ] Set up git SSH key if needed (see UBUNTU_SETUP_INSTRUCTIONS.md Step 8)

### Phase 6: Final Documentation (5 minutes)
- [ ] Update DEVICE_IDS.md with Ubuntu device ID
- [ ] Mark completion date in UBUNTU_SETUP_INSTRUCTIONS.md
- [ ] Update PLAN_AND_IMPLEMENTATION.md Ubuntu status
- [ ] Git commit and push changes

## Expected Outcomes

After completing this checklist:
- Ubuntu workspace at /home/dawson/dawson-workspace matches WSL and Windows
- Syncthing running on all three systems with all devices connected
- Three-way sync working in all directions (WSL ↔ Windows ↔ Ubuntu)
- Dotfiles deployed and shell environment configured
- Git ready for development work
- All documentation updated

## Troubleshooting Quick Reference

**Syncthing wont start**
- Check logs: journalctl --user -u syncthing.service -f

**Devices wont connect**
- Check firewall port 22000
- Verify device IDs are correct

**Files not syncing**
- Check .stignore file
- Verify Send & Receive enabled
- Check Syncthing web UI for errors

**Dotfiles install fails**
- Check permissions
- Re-clone from GitHub if needed

## Estimated Total Time
**30-35 minutes** for complete setup (assuming no issues)

## Files to Reference
- Detailed instructions: UBUNTU_SETUP_INSTRUCTIONS.md
- Device IDs: DEVICE_IDS.md
- Overall plan: PLAN_AND_IMPLEMENTATION.md

## Questions or Issues?
If you encounter problems:
1. Check UBUNTU_SETUP_INSTRUCTIONS.md troubleshooting section
2. Check Syncthing logs
3. Verify all device IDs are correct in DEVICE_IDS.md
4. Check that WSL and Windows Syncthing instances are still running

---
**Handoff created**: 2025-12-31
**Next action**: Follow this checklist on Ubuntu desktop

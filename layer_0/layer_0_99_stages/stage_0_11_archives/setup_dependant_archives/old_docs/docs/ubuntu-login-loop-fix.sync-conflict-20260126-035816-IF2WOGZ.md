---
resource_id: "2cf592fa-9855-4150-82a7-9e928b233026"
resource_type: "document"
resource_name: "ubuntu-login-loop-fix.sync-conflict-20260126-035816-IF2WOGZ"
---
# Ubuntu Login Loop Fix Guide

**Created:** 2026-01-17
**Problem:** Ubuntu GUI login loops back to login screen after entering password

<!-- section_id: "4f71ebe6-faf2-4413-a565-7ec2449072e7" -->
## Symptoms
- Enter password at GDM login screen
- Screen goes black briefly
- Returns to login screen
- Password is correct but login never succeeds

<!-- section_id: "959e7f6c-ab23-4bfb-b516-5a91db47517e" -->
## Quick Diagnosis

<!-- section_id: "6a7b884c-4f97-4140-a163-d808ed2af3b9" -->
### Access TTY (Text Console)
At the login screen, press one of these key combinations:
- **Ctrl + Alt + F3** (most common)
- **Ctrl + Alt + F4**
- **Ctrl + Alt + F5**
- **Ctrl + Alt + F6**

**Note:** F1 and F2 are often used by the display manager. Try F3-F6.

If TTY doesn't work:
- Hold the keys for 2-3 seconds
- Try during the black screen moment after password entry
- Boot into recovery mode from GRUB menu

<!-- section_id: "c16c673b-d599-4790-a0a8-0c2e1bd4c7a6" -->
### Login at TTY
```
ubuntu login: dawson
Password: [your password]
```

<!-- section_id: "639f21dd-56b3-463c-8921-47d1eba5bfc2" -->
## Common Causes & Fixes

<!-- section_id: "fb37e5bb-99ee-4fd5-bb63-154ac55da89b" -->
### 1. Disk Full
```bash
df -h
# If /home or / is at 100%, clear space:
sudo apt clean
rm -rf ~/.cache/*
```

<!-- section_id: "56595435-df37-467f-b12d-3383be9097f1" -->
### 2. Corrupted .Xauthority
```bash
rm ~/.Xauthority
# Then reboot or restart display manager:
sudo systemctl restart gdm3
```

<!-- section_id: "c1c60ad9-335e-44ca-bcde-4b8ab5954af1" -->
### 3. Wrong Permissions on Home Directory
```bash
ls -la /home/
# Should show: drwxr-xr-x for your user folder
# Fix if needed:
sudo chown -R $USER:$USER /home/$USER
chmod 755 /home/$USER
```

<!-- section_id: "6fa25e72-2292-4679-bf97-855b0df745b0" -->
### 4. Broken Packages
```bash
sudo apt update
sudo apt --fix-broken install
sudo dpkg --configure -a
```

<!-- section_id: "1ad53c1d-e4bc-4adb-b4e3-9ec940d8c639" -->
### 5. NVIDIA Driver Issues
```bash
# Check if NVIDIA is the problem:
cat /var/log/Xorg.0.log | grep -i nvidia

# Reinstall NVIDIA drivers:
sudo ubuntu-drivers autoinstall
# Or switch to nouveau:
sudo apt remove nvidia-*
```

<!-- section_id: "c68d585c-48de-41ae-b69c-83d80d805498" -->
### 6. Reinstall Display Manager
```bash
sudo apt install --reinstall gdm3
# Or try a different one:
sudo apt install lightdm
sudo dpkg-reconfigure lightdm
```

<!-- section_id: "f4fbe606-011b-4b8f-b1b3-9c1268cab169" -->
### 7. Session Configuration
```bash
# Check available sessions:
ls /usr/share/xsessions/

# Reset GNOME settings:
dconf reset -f /org/gnome/
```

<!-- section_id: "797b3dc8-f28b-4672-9e42-0fc71411c421" -->
## Recovery Mode Boot

If TTY doesn't work:

1. Reboot and hold **Shift** during boot (or press **Esc** repeatedly)
2. Select **Advanced options for Ubuntu**
3. Select **recovery mode**
4. Choose **root - Drop to root shell prompt**
5. Remount filesystem as read-write:
   ```bash
   mount -o remount,rw /
   ```
6. Run fixes from above

<!-- section_id: "25fc42ab-7c4c-47b8-a2e1-7973a6e2c8ab" -->
## Remote Fix via SSH

If SSH is configured and you're on the same network:

```bash
# From another machine:
ssh dawson@<ubuntu-ip>

# Once connected, run fixes and restart display manager:
sudo systemctl restart gdm3
```

<!-- section_id: "f166377c-f327-430d-b923-8e36ebccad07" -->
### Via Tailscale (if configured)
```bash
# From VPS or another Tailscale device:
ssh dawson@<ubuntu-tailscale-ip>
```

<!-- section_id: "9e56bb2e-e512-45f0-9a39-823ca8e10bf2" -->
## After Fixing

1. Reboot: `sudo reboot`
2. Try GUI login again
3. If still failing, check logs:
   ```bash
   journalctl -b -p err
   cat /var/log/Xorg.0.log | grep -i error
   cat ~/.xsession-errors
   ```

<!-- section_id: "4f7e3059-c51f-4188-a1b8-55c825c27bfd" -->
## Prevention

- Keep at least 10% free space on disk
- Don't kill X sessions forcefully
- Update packages regularly: `sudo apt update && sudo apt upgrade`
- Backup ~/.config periodically

<!-- section_id: "01444d41-90cc-4a21-9f9a-ec90a6ed53e3" -->
## Related
- [ubuntu-linux-setup.md](./ubuntu-linux-setup.md) - General Ubuntu setup
- Multi-OS docs: `/root/sync/dawson-workspace/code/0_layer_universal/-1_research/-1.01_things_researched/multi_os_system/`

---
resource_id: "19ccfe93-4631-4fd9-81d0-02da2b003db8"
resource_type: "document"
resource_name: "ubuntu-login-loop-fix.sync-conflict-20260126-102106-IF2WOGZ"
---
# Ubuntu Login Loop Fix Guide

**Created:** 2026-01-17
**Problem:** Ubuntu GUI login loops back to login screen after entering password

<!-- section_id: "1b0971be-cb84-4fca-acee-9e65b424e35d" -->
## Symptoms
- Enter password at GDM login screen
- Screen goes black briefly
- Returns to login screen
- Password is correct but login never succeeds

<!-- section_id: "d71107c3-4a9c-4359-8af5-72b7f5928c60" -->
## Quick Diagnosis

<!-- section_id: "c6d4081e-7d4a-499a-9651-0f25e23db9dd" -->
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

<!-- section_id: "db0a9cdb-5983-437e-8981-a99bad6f0adc" -->
### Login at TTY
```
ubuntu login: dawson
Password: [your password]
```

<!-- section_id: "ec4d7455-73a3-4535-9d92-748b13c0dd90" -->
## Common Causes & Fixes

<!-- section_id: "b71a8a6f-c081-46a6-9d28-39d5fa8aba3e" -->
### 1. Disk Full
```bash
df -h
# If /home or / is at 100%, clear space:
sudo apt clean
rm -rf ~/.cache/*
```

<!-- section_id: "5d16b450-8516-473d-a6ca-fada5a86fffc" -->
### 2. Corrupted .Xauthority
```bash
rm ~/.Xauthority
# Then reboot or restart display manager:
sudo systemctl restart gdm3
```

<!-- section_id: "ea56bfff-7dd5-42be-a3eb-097ee2bd6116" -->
### 3. Wrong Permissions on Home Directory
```bash
ls -la /home/
# Should show: drwxr-xr-x for your user folder
# Fix if needed:
sudo chown -R $USER:$USER /home/$USER
chmod 755 /home/$USER
```

<!-- section_id: "17f732a3-9b38-4e4e-a178-2ff9cb024f42" -->
### 4. Broken Packages
```bash
sudo apt update
sudo apt --fix-broken install
sudo dpkg --configure -a
```

<!-- section_id: "1a0a66ec-ca6b-4b31-b96d-fdc5f3b25ce9" -->
### 5. NVIDIA Driver Issues
```bash
# Check if NVIDIA is the problem:
cat /var/log/Xorg.0.log | grep -i nvidia

# Reinstall NVIDIA drivers:
sudo ubuntu-drivers autoinstall
# Or switch to nouveau:
sudo apt remove nvidia-*
```

<!-- section_id: "164ab3fd-fe8e-498c-9ea2-35cf89c18c61" -->
### 6. Reinstall Display Manager
```bash
sudo apt install --reinstall gdm3
# Or try a different one:
sudo apt install lightdm
sudo dpkg-reconfigure lightdm
```

<!-- section_id: "37c8e562-04e7-48da-9b92-35a0ae57b222" -->
### 7. Session Configuration
```bash
# Check available sessions:
ls /usr/share/xsessions/

# Reset GNOME settings:
dconf reset -f /org/gnome/
```

<!-- section_id: "d969415a-72f2-43f2-8e47-f67b713d8ece" -->
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

<!-- section_id: "f3483e39-0dee-473e-8e50-1546c230a906" -->
## Remote Fix via SSH

If SSH is configured and you're on the same network:

```bash
# From another machine:
ssh dawson@<ubuntu-ip>

# Once connected, run fixes and restart display manager:
sudo systemctl restart gdm3
```

<!-- section_id: "2c21933f-3263-45e6-986f-5f7b4be0e77b" -->
### Via Tailscale (if configured)
```bash
# From VPS or another Tailscale device:
ssh dawson@<ubuntu-tailscale-ip>
```

<!-- section_id: "0d3b3b31-944e-4e37-a59d-24a9411a38fb" -->
## After Fixing

1. Reboot: `sudo reboot`
2. Try GUI login again
3. If still failing, check logs:
   ```bash
   journalctl -b -p err
   cat /var/log/Xorg.0.log | grep -i error
   cat ~/.xsession-errors
   ```

<!-- section_id: "0dfea299-e324-4b15-b018-6a57c0e763b3" -->
## Prevention

- Keep at least 10% free space on disk
- Don't kill X sessions forcefully
- Update packages regularly: `sudo apt update && sudo apt upgrade`
- Backup ~/.config periodically

<!-- section_id: "6a0cad1b-ebb8-450f-aa73-6a02e8c25e51" -->
## Related
- [ubuntu-linux-setup.md](./ubuntu-linux-setup.md) - General Ubuntu setup
- Multi-OS docs: `/root/sync/dawson-workspace/code/0_layer_universal/-1_research/-1.01_things_researched/multi_os_system/`

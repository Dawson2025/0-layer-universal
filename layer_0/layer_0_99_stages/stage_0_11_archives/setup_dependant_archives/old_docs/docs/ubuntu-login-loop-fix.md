---
resource_id: "02c420f8-8411-4915-a17e-08121aac5fe6"
resource_type: "document"
resource_name: "ubuntu-login-loop-fix"
---
# Ubuntu Login Loop Fix Guide

**Created:** 2026-01-17
**Problem:** Ubuntu GUI login loops back to login screen after entering password

<!-- section_id: "f8dd8c76-20aa-4f61-b33c-e1c3014e7362" -->
## Symptoms
- Enter password at GDM login screen
- Screen goes black briefly
- Returns to login screen
- Password is correct but login never succeeds

<!-- section_id: "c546c3fe-ec63-409b-ac92-5a011c2b9fff" -->
## Quick Diagnosis

<!-- section_id: "d4fc3e39-108b-43bf-97f4-11d66b11dd83" -->
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

<!-- section_id: "cfc4ebf4-d588-4d19-82de-5269c66c570b" -->
### Login at TTY
```
ubuntu login: dawson
Password: [your password]
```

<!-- section_id: "af6cd8c0-c73d-42df-988a-a7e1a55fae43" -->
## Common Causes & Fixes

<!-- section_id: "fde6a876-0074-4a81-97f7-136f8d7442d3" -->
### 1. Disk Full
```bash
df -h
# If /home or / is at 100%, clear space:
sudo apt clean
rm -rf ~/.cache/*
```

<!-- section_id: "40433d90-0532-4441-b52d-aca224e80c06" -->
### 2. Corrupted .Xauthority
```bash
rm ~/.Xauthority
# Then reboot or restart display manager:
sudo systemctl restart gdm3
```

<!-- section_id: "7c4a5ba0-c380-4490-9d5f-e17df7e15978" -->
### 3. Wrong Permissions on Home Directory
```bash
ls -la /home/
# Should show: drwxr-xr-x for your user folder
# Fix if needed:
sudo chown -R $USER:$USER /home/$USER
chmod 755 /home/$USER
```

<!-- section_id: "029f103d-273c-41f5-bfe0-408688161317" -->
### 4. Broken Packages
```bash
sudo apt update
sudo apt --fix-broken install
sudo dpkg --configure -a
```

<!-- section_id: "1d867460-fe9a-451e-9a61-52902bdeb065" -->
### 5. NVIDIA Driver Issues
```bash
# Check if NVIDIA is the problem:
cat /var/log/Xorg.0.log | grep -i nvidia

# Reinstall NVIDIA drivers:
sudo ubuntu-drivers autoinstall
# Or switch to nouveau:
sudo apt remove nvidia-*
```

<!-- section_id: "8d71a8f6-d689-488a-8361-d27b2608f288" -->
### 6. Reinstall Display Manager
```bash
sudo apt install --reinstall gdm3
# Or try a different one:
sudo apt install lightdm
sudo dpkg-reconfigure lightdm
```

<!-- section_id: "ca4ad95a-6bd1-4616-8900-c59ae977d840" -->
### 7. Session Configuration
```bash
# Check available sessions:
ls /usr/share/xsessions/

# Reset GNOME settings:
dconf reset -f /org/gnome/
```

<!-- section_id: "0453ec16-96ca-4907-bf09-de70f4271c63" -->
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

<!-- section_id: "b906cf22-a764-4699-b4cd-a8784256fc17" -->
## Remote Fix via SSH

If SSH is configured and you're on the same network:

```bash
# From another machine:
ssh dawson@<ubuntu-ip>

# Once connected, run fixes and restart display manager:
sudo systemctl restart gdm3
```

<!-- section_id: "3fbf99bb-e4b6-4815-9df8-6479d7b7d9c8" -->
### Via Tailscale (if configured)
```bash
# From VPS or another Tailscale device:
ssh dawson@<ubuntu-tailscale-ip>
```

<!-- section_id: "eee06f53-e9ea-441a-a4d8-43be879d73af" -->
## After Fixing

1. Reboot: `sudo reboot`
2. Try GUI login again
3. If still failing, check logs:
   ```bash
   journalctl -b -p err
   cat /var/log/Xorg.0.log | grep -i error
   cat ~/.xsession-errors
   ```

<!-- section_id: "a283f189-d625-4232-b95f-64da0ac8bb2a" -->
## Prevention

- Keep at least 10% free space on disk
- Don't kill X sessions forcefully
- Update packages regularly: `sudo apt update && sudo apt upgrade`
- Backup ~/.config periodically

<!-- section_id: "59ebc41c-cf7b-4b85-8e2a-c0110709e8f9" -->
## Related
- [ubuntu-linux-setup.md](./ubuntu-linux-setup.md) - General Ubuntu setup
- Multi-OS docs: `/root/sync/dawson-workspace/code/0_layer_universal/-1_research/-1.01_things_researched/multi_os_system/`

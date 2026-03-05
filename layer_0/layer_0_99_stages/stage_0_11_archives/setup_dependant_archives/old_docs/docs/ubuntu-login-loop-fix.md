---
resource_id: "02c420f8-8411-4915-a17e-08121aac5fe6"
resource_type: "document"
resource_name: "ubuntu-login-loop-fix"
---
# Ubuntu Login Loop Fix Guide

**Created:** 2026-01-17
**Problem:** Ubuntu GUI login loops back to login screen after entering password

## Symptoms
- Enter password at GDM login screen
- Screen goes black briefly
- Returns to login screen
- Password is correct but login never succeeds

## Quick Diagnosis

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

### Login at TTY
```
ubuntu login: dawson
Password: [your password]
```

## Common Causes & Fixes

### 1. Disk Full
```bash
df -h
# If /home or / is at 100%, clear space:
sudo apt clean
rm -rf ~/.cache/*
```

### 2. Corrupted .Xauthority
```bash
rm ~/.Xauthority
# Then reboot or restart display manager:
sudo systemctl restart gdm3
```

### 3. Wrong Permissions on Home Directory
```bash
ls -la /home/
# Should show: drwxr-xr-x for your user folder
# Fix if needed:
sudo chown -R $USER:$USER /home/$USER
chmod 755 /home/$USER
```

### 4. Broken Packages
```bash
sudo apt update
sudo apt --fix-broken install
sudo dpkg --configure -a
```

### 5. NVIDIA Driver Issues
```bash
# Check if NVIDIA is the problem:
cat /var/log/Xorg.0.log | grep -i nvidia

# Reinstall NVIDIA drivers:
sudo ubuntu-drivers autoinstall
# Or switch to nouveau:
sudo apt remove nvidia-*
```

### 6. Reinstall Display Manager
```bash
sudo apt install --reinstall gdm3
# Or try a different one:
sudo apt install lightdm
sudo dpkg-reconfigure lightdm
```

### 7. Session Configuration
```bash
# Check available sessions:
ls /usr/share/xsessions/

# Reset GNOME settings:
dconf reset -f /org/gnome/
```

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

## Remote Fix via SSH

If SSH is configured and you're on the same network:

```bash
# From another machine:
ssh dawson@<ubuntu-ip>

# Once connected, run fixes and restart display manager:
sudo systemctl restart gdm3
```

### Via Tailscale (if configured)
```bash
# From VPS or another Tailscale device:
ssh dawson@<ubuntu-tailscale-ip>
```

## After Fixing

1. Reboot: `sudo reboot`
2. Try GUI login again
3. If still failing, check logs:
   ```bash
   journalctl -b -p err
   cat /var/log/Xorg.0.log | grep -i error
   cat ~/.xsession-errors
   ```

## Prevention

- Keep at least 10% free space on disk
- Don't kill X sessions forcefully
- Update packages regularly: `sudo apt update && sudo apt upgrade`
- Backup ~/.config periodically

## Related
- [ubuntu-linux-setup.md](./ubuntu-linux-setup.md) - General Ubuntu setup
- Multi-OS docs: `/root/sync/dawson-workspace/code/0_layer_universal/-1_research/-1.01_things_researched/multi_os_system/`

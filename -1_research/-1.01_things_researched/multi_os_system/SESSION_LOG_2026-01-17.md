# Session Log - 2026-01-17

## Summary
Successfully fixed Ubuntu login loop and set up remote access infrastructure via Tailscale.

---

## What Was Done

### 1. VPS Enhancements

#### Playwright MCP Server ✅
```bash
npm install -g @playwright/mcp@latest
npx playwright install chromium --with-deps
```
- Config: `/root/.claude/mcp_servers.json`
- Purpose: Browser automation for web UIs

#### Tailscale VPN ✅
```bash
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up
```
- VPS IP: `100.93.148.5`
- Hostname: `ubuntu-4gb-nbg1-1`

#### Claude Code Permissions ✅
- Updated `/root/.claude/settings.local.json` with full tool permissions

---

### 2. Ubuntu Setup (via Recovery Mode)

#### Tailscale Installation ✅
- Booted into recovery mode (GRUB → Advanced → Recovery)
- Enabled networking
- Installed Tailscale: `curl -fsSL https://tailscale.com/install.sh | sh`
- Connected: `tailscale up`
- Ubuntu IP: `100.73.84.89`
- Hostname: `dawson-yoga-pro-9-16imh9`

#### SSH Server Installation ✅
```bash
apt update && apt install -y openssh-server
systemctl enable ssh
```

#### SSH Key Setup ✅
- VPS public key added to `/home/dawson/.ssh/authorized_keys`
- Also added to `/root/.ssh/authorized_keys` for root access
- **Issue encountered:** File was named `authorized-keys` (hyphen) instead of `authorized_keys` (underscore) - fixed with `mv`

---

## The Login Loop Problem

### Symptoms
- Enter password at GDM login screen
- Screen goes black briefly
- Returns to login screen (loop)

### Diagnosis
Connected via SSH from VPS and checked logs:
```bash
journalctl -u gdm -b --no-pager | tail -20
```

**Error found:**
```
Gdm: GdmDisplay: Session never registered, failing
Gdm: GdmLocalDisplayFactory: maximum number of X display failures reached
```

### What Didn't Work
1. **Disabling Wayland** - `WaylandEnable=false` in `/etc/gdm3/custom.conf` - no effect
2. **Updating NVIDIA drivers** - `ubuntu-drivers autoinstall` - no effect
3. **Reinstalling GDM** - `apt install --reinstall gdm3` - no effect
4. **Reinstalling GNOME session** - `apt install --reinstall gnome-session gnome-shell ubuntu-session` - no effect
5. **Resetting GNOME config** - moved `.config/gnome-session` and `.config/dconf` - no effect

### What Worked ✅
**Switching from GDM3 to LightDM:**
```bash
apt install -y lightdm
echo '/usr/sbin/lightdm' > /etc/X11/default-display-manager
systemctl disable gdm3
ln -sf /usr/lib/systemd/system/lightdm.service /etc/systemd/system/display-manager.service
systemctl set-default graphical.target
reboot
```

### Root Cause
GDM3 has known issues with NVIDIA hybrid graphics (Intel + NVIDIA RTX 4060). The GNOME session fails to register with GDM's display factory. LightDM handles this setup more reliably.

---

## Post-Fix Issue

### Blank Screen After Reboot
After rebooting, LightDM didn't auto-start.

**Fix:**
```bash
systemctl start lightdm
systemctl set-default graphical.target
ln -sf /usr/lib/systemd/system/lightdm.service /etc/systemd/system/display-manager.service
```

---

## Current State

### Devices on Tailscale Network
| Device | IP | Hostname | Status |
|--------|-----|----------|--------|
| Ubuntu | `100.73.84.89` | `dawson-yoga-pro-9-16imh9` | ✅ Online |
| VPS | `100.93.148.5` | `ubuntu-4gb-nbg1-1` | ✅ Online |
| iPhone | `100.75.210.27` | `iphone171` | ✅ Online |

### SSH Access
```bash
# From VPS to Ubuntu:
ssh dawson@100.73.84.89
ssh dawson@dawson-yoga-pro-9-16imh9

# From iPhone (Terminus) to Ubuntu:
ssh dawson@dawson-yoga-pro-9-16imh9

# From iPhone to VPS:
ssh root@ubuntu-4gb-nbg1-1
```

### Ubuntu Configuration
- **Display Manager:** LightDM (Unity Greeter)
- **Graphics:** Intel + NVIDIA RTX 4060 hybrid
- **NVIDIA Driver:** 535.274.02
- **Tailscale:** Enabled, auto-starts
- **SSH:** Enabled, auto-starts

---

## Files Modified

### On VPS
| File | Change |
|------|--------|
| `/root/.claude/mcp_servers.json` | Created - Playwright MCP config |
| `/root/.claude/settings.local.json` | Updated - Full tool permissions |

### On Ubuntu
| File | Change |
|------|--------|
| `/etc/X11/default-display-manager` | Changed to `/usr/sbin/lightdm` |
| `/etc/gdm3/custom.conf` | Added `WaylandEnable=false` |
| `/home/dawson/.ssh/authorized_keys` | Added VPS public key |
| `/root/.ssh/authorized_keys` | Added VPS public key |
| `/etc/systemd/system/display-manager.service` | Symlink to lightdm.service |

---

## Lessons Learned

1. **GDM3 + NVIDIA hybrid = trouble** - LightDM is more reliable
2. **Recovery mode requires manual networking** - Run `dhclient` or enable from menu
3. **SSH filename matters** - `authorized_keys` not `authorized-keys`
4. **Tailscale IPs are stable** - No need to find IP each time
5. **LightDM may not auto-enable** - Need to create display-manager.service symlink

---

## Quick Reference

### If Login Loop Returns
```bash
# From VPS:
ssh root@100.73.84.89
systemctl restart lightdm
```

### If Display is Blank
```bash
ssh root@100.73.84.89
systemctl start lightdm
```

### Check Tailscale Status
```bash
tailscale status
```

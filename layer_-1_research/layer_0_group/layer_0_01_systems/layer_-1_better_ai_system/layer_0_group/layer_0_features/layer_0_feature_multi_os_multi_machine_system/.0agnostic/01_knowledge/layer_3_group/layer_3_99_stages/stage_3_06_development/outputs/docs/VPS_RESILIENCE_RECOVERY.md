# VPS Resilience & Recovery System

**Created**: 2026-01-21
**Status**: Planning (Implementation Pending)
**OS**: Ubuntu 24.04 LTS (Hetzner CX23)

---

## Overview

The VPS is the **critical relay point** for the multi-OS workspace sync. If it fails, Windows and Ubuntu cannot sync with each other. This document ensures the VPS is resilient against failures and can recover automatically.

---

## Current State Assessment

| Component | Status | Issue |
|-----------|--------|-------|
| SSH | ✅ Running | Using socket activation (potential delay) |
| Tailscale | ✅ Running | Auto-starts on boot |
| Syncthing | ⚠️ Unstable | Crashed with stale lock file, no auto-recovery |
| UFW Firewall | ❌ Inactive | Rules exist but not enforced |
| fail2ban | ❌ Not Installed | No brute-force protection |
| Monitoring | ❌ None | No health checks or alerts |

---

## System Configuration

| Setting | Value |
|---------|-------|
| Provider | Hetzner Cloud |
| Plan | CX23 (2 vCPU, 4GB RAM, 40GB SSD) |
| OS | Ubuntu 24.04 LTS |
| Hostname | ubuntu-4gb-nbg1-1 |
| Public IP | 46.224.184.10 |
| IPv6 | 2a01:4f8:1c1a:885b::1 |
| Tailscale IP | 100.93.148.5 |
| Location | Nuremberg, Germany |

---

## Critical Services

| Service | Port | Purpose | Priority |
|---------|------|---------|----------|
| SSH | 22 | Remote access | Critical |
| Syncthing | 22000, 8384 | File sync relay | Critical |
| Tailscale | Various | VPN mesh network | Critical |

---

## Failure Modes & Solutions

### Layer 1: Service Failures

| Failure | Solution | Status |
|---------|----------|--------|
| Syncthing crashes | Auto-restart + lock file cleanup | [ ] To implement |
| SSH crashes | Switch to ssh.service + auto-restart | [ ] To implement |
| Tailscale crashes | Auto-restart via systemd | [ ] To verify |
| Memory exhaustion | Syncthing memory limits + swap | [ ] To configure |

### Layer 2: Security Failures

| Failure | Solution | Status |
|---------|----------|--------|
| Brute-force SSH | fail2ban + rate limiting | [ ] To install |
| Unauthorized access | UFW firewall rules | [ ] To enable |
| SSH key compromise | Password fallback + key rotation | [ ] To configure |
| Service exploits | Regular updates + unattended-upgrades | [ ] To configure |

### Layer 3: System Failures

| Failure | Solution | Status |
|---------|----------|--------|
| Disk full | Log rotation + Syncthing versioning limits | [ ] To configure |
| Kernel panic | Auto-reboot + multiple kernels | [ ] To configure |
| Network partition | Tailscale direct + relay fallback | [x] Default |

### Layer 4: Provider Failures

| Failure | Solution | Status |
|---------|----------|--------|
| VPS goes down | Hetzner auto-recovery | [x] Provider feature |
| Data loss | Regular backups to external storage | [ ] To implement |
| Region outage | Secondary VPS in different DC | [ ] Optional |

---

## Implementation Plan

### Phase 1: Fix Syncthing Resilience

```bash
# Create systemd override for Syncthing
sudo mkdir -p /etc/systemd/system/syncthing@root.service.d

# Create override file
sudo tee /etc/systemd/system/syncthing@root.service.d/override.conf << 'EOF'
[Service]
Restart=on-failure
RestartSec=10s
StartLimitIntervalSec=300
StartLimitBurst=5

# Clean up stale lock file before starting
ExecStartPre=/bin/bash -c 'rm -f /root/.local/state/syncthing/syncthing.lock 2>/dev/null || true'

# Ensure no orphan processes
ExecStartPre=/usr/bin/pkill -9 -u root syncthing || true

[Unit]
After=network-online.target tailscaled.service
Wants=network-online.target
EOF

# Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart syncthing@root
```

### Phase 2: Secure SSH Configuration

```bash
# Switch from socket to service activation
sudo systemctl disable --now ssh.socket
sudo systemctl enable ssh.service

# Create SSH service override
sudo mkdir -p /etc/systemd/system/ssh.service.d
sudo tee /etc/systemd/system/ssh.service.d/override.conf << 'EOF'
[Service]
Restart=on-failure
RestartSec=5s
StartLimitIntervalSec=60
StartLimitBurst=5
EOF

# Configure SSH hardening
sudo tee /etc/ssh/sshd_config.d/99-hardening.conf << 'EOF'
# Security hardening
PermitRootLogin prohibit-password
PasswordAuthentication yes
PubkeyAuthentication yes
MaxAuthTries 3
LoginGraceTime 30

# Allow both key and password for recovery
AuthenticationMethods publickey,password publickey
EOF

sudo systemctl daemon-reload
sudo systemctl restart ssh
```

### Phase 3: Install and Configure fail2ban

```bash
# Install fail2ban
sudo apt update && sudo apt install -y fail2ban

# Configure jail
sudo tee /etc/fail2ban/jail.local << 'EOF'
[DEFAULT]
bantime = 1h
findtime = 10m
maxretry = 5

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 24h
EOF

# Start and enable
sudo systemctl enable --now fail2ban
```

### Phase 4: Enable UFW Firewall

```bash
# Configure UFW rules
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow essential services
sudo ufw allow 22/tcp comment 'SSH'
sudo ufw allow 22000/tcp comment 'Syncthing data'
sudo ufw allow 21027/udp comment 'Syncthing discovery'
sudo ufw allow 8384/tcp comment 'Syncthing GUI'

# Allow Tailscale
sudo ufw allow in on tailscale0

# Enable firewall
sudo ufw --force enable
sudo ufw status verbose
```

### Phase 5: Configure Tailscale Service Recovery

```bash
# Create Tailscale override
sudo mkdir -p /etc/systemd/system/tailscaled.service.d
sudo tee /etc/systemd/system/tailscaled.service.d/override.conf << 'EOF'
[Service]
Restart=on-failure
RestartSec=5s
StartLimitIntervalSec=60
StartLimitBurst=5
EOF

sudo systemctl daemon-reload
```

### Phase 6: Configure Log Rotation

```bash
# Ensure log rotation is configured for Syncthing
sudo tee /etc/logrotate.d/syncthing << 'EOF'
/var/log/syncthing*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 root root
}
EOF
```

### Phase 7: Configure Automatic Updates

```bash
# Install unattended-upgrades
sudo apt install -y unattended-upgrades

# Configure auto-updates
sudo tee /etc/apt/apt.conf.d/50unattended-upgrades << 'EOF'
Unattended-Upgrade::Allowed-Origins {
    "${distro_id}:${distro_codename}";
    "${distro_id}:${distro_codename}-security";
    "${distro_id}:${distro_codename}-updates";
};
Unattended-Upgrade::AutoFixInterruptedDpkg "true";
Unattended-Upgrade::Remove-Unused-Dependencies "true";
Unattended-Upgrade::Automatic-Reboot "false";
EOF

# Enable
sudo dpkg-reconfigure -plow unattended-upgrades
```

### Phase 8: Health Check Script & Monitoring

```bash
# Create health check script
sudo tee /usr/local/bin/vps-health-check.sh << 'EOF'
#!/bin/bash
# VPS Health Check Script

ERRORS=0

# Check SSH
if ! systemctl is-active --quiet ssh; then
    echo "[FAIL] SSH not running"
    systemctl start ssh
    ERRORS=$((ERRORS+1))
fi

# Check Syncthing
if ! systemctl is-active --quiet syncthing@root; then
    echo "[FAIL] Syncthing not running"
    rm -f /root/.local/state/syncthing/syncthing.lock 2>/dev/null
    pkill -9 -u root syncthing 2>/dev/null
    systemctl start syncthing@root
    ERRORS=$((ERRORS+1))
fi

# Check Tailscale
if ! systemctl is-active --quiet tailscaled; then
    echo "[FAIL] Tailscale not running"
    systemctl start tailscaled
    ERRORS=$((ERRORS+1))
fi

# Check disk space (alert if >90% used)
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | tr -d '%')
if [ "$DISK_USAGE" -gt 90 ]; then
    echo "[WARN] Disk usage at ${DISK_USAGE}%"
    ERRORS=$((ERRORS+1))
fi

# Check memory (alert if <10% free)
MEM_FREE=$(free | grep Mem | awk '{printf "%.0f", $7/$2 * 100}')
if [ "$MEM_FREE" -lt 10 ]; then
    echo "[WARN] Memory low: ${MEM_FREE}% available"
    ERRORS=$((ERRORS+1))
fi

if [ $ERRORS -eq 0 ]; then
    echo "[OK] All services healthy"
fi

exit $ERRORS
EOF

sudo chmod +x /usr/local/bin/vps-health-check.sh

# Add to cron (run every 5 minutes)
echo "*/5 * * * * root /usr/local/bin/vps-health-check.sh >> /var/log/health-check.log 2>&1" | sudo tee /etc/cron.d/vps-health-check
```

### Phase 9: Backup Strategy

```bash
# Create backup script
sudo tee /usr/local/bin/vps-backup.sh << 'EOF'
#!/bin/bash
# VPS Critical Files Backup

BACKUP_DIR="/root/backups"
DATE=$(date +%Y%m%d)

mkdir -p $BACKUP_DIR

# Backup SSH config
tar czf $BACKUP_DIR/ssh-config-$DATE.tar.gz /etc/ssh /root/.ssh 2>/dev/null

# Backup Syncthing config
tar czf $BACKUP_DIR/syncthing-config-$DATE.tar.gz /root/.local/state/syncthing/config.xml 2>/dev/null

# Backup systemd overrides
tar czf $BACKUP_DIR/systemd-overrides-$DATE.tar.gz /etc/systemd/system/*.service.d 2>/dev/null

# Keep only last 7 days
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete

echo "Backup completed: $DATE"
EOF

sudo chmod +x /usr/local/bin/vps-backup.sh

# Add to cron (daily at 3 AM)
echo "0 3 * * * root /usr/local/bin/vps-backup.sh >> /var/log/backup.log 2>&1" | sudo tee /etc/cron.d/vps-backup
```

---

## Emergency Recovery Procedures

### When SSH Fails

1. **Hetzner Console**: Access via web console at console.hetzner.cloud
2. **Reset Password**: Use Hetzner rescue system if needed
3. **Check logs**: `journalctl -u ssh -n 100`

### When Syncthing Won't Start

```bash
# Manual recovery
pkill -9 syncthing
rm -f /root/.local/state/syncthing/syncthing.lock
systemctl reset-failed syncthing@root
systemctl start syncthing@root
```

### When Disk is Full

```bash
# Find large files
du -h /root/sync/dawson-workspace | sort -rh | head -20

# Clear Syncthing versions
rm -rf /root/sync/dawson-workspace/.stversions/*

# Clear logs
journalctl --vacuum-time=3d
```

### When VPS is Unresponsive

1. Try Hetzner web console
2. Force reboot via Hetzner API/Dashboard
3. If still failing, file support ticket

---

## Testing Checklist

- [ ] Kill syncthing, verify it auto-restarts
- [ ] Kill sshd, verify it auto-restarts
- [ ] Kill tailscaled, verify it auto-restarts
- [ ] Verify fail2ban is blocking after failed attempts
- [ ] Verify UFW is allowing correct ports
- [ ] Test SSH from Windows via Tailscale
- [ ] Test SSH from iPhone via Tailscale
- [ ] Run health check script manually
- [ ] Verify backups are being created

---

## Monitoring Dashboard

Check service status:
```bash
systemctl status ssh tailscaled syncthing@root fail2ban ufw
```

Check connections:
```bash
# Syncthing connections
curl -s http://localhost:8384/rest/system/connections -H "X-API-Key: cQMo4c5GFeRUQXhe7QrQZyFQDxZktW24" | jq '.connections | keys'

# Tailscale peers
tailscale status
```

---

## Related Files

- `LINUX_RESILIENCE_RECOVERY.md` - Linux laptop recovery
- `WINDOWS_RESILIENCE_RECOVERY.md` - Windows laptop recovery
- `VPS_CREDENTIALS.md` - VPS access details
- `STATUS.md` - Multi-OS workspace status

#!/bin/bash
# Syncthing Health Monitor - Run via cron or manually
# Checks sync status on both local machine and VPS
# Updated: 2026-01-25

set -euo pipefail

LOG_FILE="/tmp/sync-health-$(date +%Y%m%d).log"
ALERT_FILE="/tmp/sync-alert-needed"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

check_local_syncthing() {
    log "Checking local Syncthing..."

    if ! systemctl --user is-active syncthing &>/dev/null; then
        log "ERROR: Local Syncthing not running - attempting restart"
        systemctl --user start syncthing
        sleep 5
        if systemctl --user is-active syncthing &>/dev/null; then
            log "OK: Local Syncthing restarted successfully"
        else
            log "CRITICAL: Failed to start local Syncthing"
            touch "$ALERT_FILE"
            return 1
        fi
    else
        log "OK: Local Syncthing running"
    fi

    # Check for sync errors via API
    API_KEY=$(grep -oP '(?<=<apikey>).*(?=</apikey>)' ~/.config/syncthing/config.xml 2>/dev/null || echo "")
    if [ -n "$API_KEY" ]; then
        ERRORS=$(curl -s -H "X-API-Key: $API_KEY" "http://localhost:8384/rest/folder/errors?folder=dawson-workspace" 2>/dev/null | grep -c '"error"' || echo "0")
        if [ "$ERRORS" != "0" ] && [ "$ERRORS" != "null" ]; then
            log "WARNING: $ERRORS sync errors detected locally"
        else
            log "OK: No local sync errors"
        fi
    fi
}

check_vps_syncthing() {
    log "Checking VPS Syncthing..."

    # Check if VPS is reachable
    if ! ssh -o ConnectTimeout=10 -o BatchMode=yes root@46.224.184.10 "echo ok" &>/dev/null; then
        log "ERROR: Cannot reach VPS"
        touch "$ALERT_FILE"
        return 1
    fi

    # Check VPS Syncthing process
    VPS_RUNNING=$(ssh root@46.224.184.10 "pgrep -c syncthing || echo 0" 2>/dev/null)
    if [ "$VPS_RUNNING" -lt 1 ]; then
        log "ERROR: VPS Syncthing not running - attempting restart"
        ssh root@46.224.184.10 "systemctl start syncthing" 2>/dev/null || \
            ssh root@46.224.184.10 "nohup /usr/bin/syncthing serve --no-browser --no-restart --logflags=0 > /var/log/syncthing.log 2>&1 &"
        sleep 5
        VPS_RUNNING=$(ssh root@46.224.184.10 "pgrep -c syncthing || echo 0" 2>/dev/null)
        if [ "$VPS_RUNNING" -ge 1 ]; then
            log "OK: VPS Syncthing restarted"
        else
            log "CRITICAL: Failed to start VPS Syncthing"
            touch "$ALERT_FILE"
            return 1
        fi
    else
        log "OK: VPS Syncthing running ($VPS_RUNNING processes)"
    fi

    # Check VPS sync errors
    VPS_ERRORS=$(ssh root@46.224.184.10 'API=$(cat /root/.local/state/syncthing/config.xml | grep -oP "(?<=<apikey>)[^<]+"); curl -s -H "X-API-Key: $API" "http://localhost:8384/rest/folder/errors?folder=dawson-workspace"' 2>/dev/null | grep -c '"error"' || echo "0")
    if [ "$VPS_ERRORS" != "0" ] && [ "$VPS_ERRORS" != "null" ]; then
        log "WARNING: $VPS_ERRORS sync errors on VPS"
    else
        log "OK: No VPS sync errors"
    fi
}

check_connection() {
    log "Checking Ubuntu <-> VPS connection..."

    API_KEY=$(grep -oP '(?<=<apikey>).*(?=</apikey>)' ~/.config/syncthing/config.xml 2>/dev/null || echo "")
    if [ -n "$API_KEY" ]; then
        VPS_CONNECTED=$(curl -s -H "X-API-Key: $API_KEY" "http://localhost:8384/rest/system/connections" 2>/dev/null | grep -A5 '"JTAFCHA' | grep '"connected"' | grep -o 'true\|false' || echo "unknown")
        if [ "$VPS_CONNECTED" = "true" ]; then
            log "OK: Connected to VPS"
        else
            log "WARNING: Not connected to VPS (status: $VPS_CONNECTED)"
        fi
    fi
}

cleanup_old_logs() {
    # Keep only last 7 days of logs
    find /tmp -name "sync-health-*.log" -mtime +7 -delete 2>/dev/null || true
}

main() {
    log "=== Sync Health Check Started ==="
    rm -f "$ALERT_FILE"

    check_local_syncthing
    check_vps_syncthing
    check_connection
    cleanup_old_logs

    if [ -f "$ALERT_FILE" ]; then
        log "=== ALERTS DETECTED - Manual attention needed ==="
        rm -f "$ALERT_FILE"
        exit 1
    else
        log "=== Health Check Complete - All OK ==="
    fi
}

main "$@"

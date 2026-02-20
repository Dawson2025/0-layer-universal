#!/bin/bash
#
# lock-manager.sh - File locking for multi-agent sync
#
# Usage:
#   ./lock-manager.sh acquire <scope> <agent_id> [ttl_minutes]
#   ./lock-manager.sh release <scope> <agent_id>
#   ./lock-manager.sh check <scope>
#   ./lock-manager.sh cleanup [ttl_minutes]
#
# Examples:
#   ./lock-manager.sh acquire outputs_research agent_01 5
#   ./lock-manager.sh release outputs_research agent_01
#   ./lock-manager.sh check outputs_research
#   ./lock-manager.sh cleanup 5
#

set -e

# Configuration
LOCKS_DIR="${LOCKS_DIR:-.locks}"
DEFAULT_TTL=5  # minutes

# Ensure locks directory exists
mkdir -p "$LOCKS_DIR"

# Get current timestamp in ISO format
get_timestamp() {
    date -u +"%Y-%m-%dT%H:%M:%SZ"
}

# Get machine identifier for distributed lock awareness
get_machine_id() {
    # Try multiple methods to get a unique machine identifier
    if [ -f /etc/machine-id ]; then
        cat /etc/machine-id | head -c 12
    elif [ -f /var/lib/dbus/machine-id ]; then
        cat /var/lib/dbus/machine-id | head -c 12
    elif command -v hostname >/dev/null 2>&1; then
        hostname | md5sum 2>/dev/null | head -c 12 || hostname
    else
        echo "unknown"
    fi
}

# Get timestamp N minutes ago
get_stale_threshold() {
    local ttl_minutes="${1:-$DEFAULT_TTL}"
    date -u -d "$ttl_minutes minutes ago" +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || \
    date -u -v-${ttl_minutes}M +"%Y-%m-%dT%H:%M:%SZ"  # macOS fallback
}

# Acquire a lock
acquire_lock() {
    local scope="$1"
    local agent_id="$2"
    local ttl_minutes="${3:-$DEFAULT_TTL}"
    local lock_file="$LOCKS_DIR/${scope}_${agent_id}.lock"

    # Check if any lock exists for this scope
    for existing_lock in "$LOCKS_DIR"/${scope}_*.lock; do
        if [ -f "$existing_lock" ]; then
            # Check if it's our own lock
            if [ "$existing_lock" = "$lock_file" ]; then
                # Refresh our own lock
                echo "Refreshing existing lock: $lock_file"
            else
                # Another agent has the lock
                local existing_agent=$(basename "$existing_lock" .lock | sed "s/${scope}_//")
                local lock_machine=$(grep -o '"machine_id": "[^"]*"' "$existing_lock" 2>/dev/null | cut -d'"' -f4 || echo "unknown")
                local current_machine=$(get_machine_id)
                echo "ERROR: Lock held by $existing_agent"
                echo "Lock file: $existing_lock"
                if [ "$lock_machine" != "$current_machine" ]; then
                    echo "WARNING: Lock is from DIFFERENT MACHINE ($lock_machine vs current $current_machine)"
                    echo "         This may indicate a distributed sync issue."
                fi
                cat "$existing_lock"
                return 1
            fi
        fi
    done

    # Create lock file with machine ID for distributed awareness
    local machine_id=$(get_machine_id)
    cat > "$lock_file" << EOF
{
  "agent_id": "$agent_id",
  "scope": "$scope",
  "timestamp": "$(get_timestamp)",
  "ttl_minutes": $ttl_minutes,
  "machine_id": "$machine_id"
}
EOF

    echo "Lock acquired: $lock_file (machine: $machine_id)"
    return 0
}

# Release a lock
release_lock() {
    local scope="$1"
    local agent_id="$2"
    local lock_file="$LOCKS_DIR/${scope}_${agent_id}.lock"

    if [ -f "$lock_file" ]; then
        rm "$lock_file"
        echo "Lock released: $lock_file"
        return 0
    else
        echo "No lock found: $lock_file"
        return 1
    fi
}

# Check lock status
check_lock() {
    local scope="$1"
    local found=0

    for lock_file in "$LOCKS_DIR"/${scope}_*.lock; do
        if [ -f "$lock_file" ]; then
            found=1
            echo "Lock found: $lock_file"
            cat "$lock_file"
            echo ""
        fi
    done

    if [ $found -eq 0 ]; then
        echo "No locks for scope: $scope"
        return 0
    fi
    return 0
}

# Cleanup stale locks
cleanup_locks() {
    local ttl_minutes="${1:-$DEFAULT_TTL}"
    local cleaned=0

    echo "Cleaning up locks older than $ttl_minutes minutes..."

    for lock_file in "$LOCKS_DIR"/*.lock; do
        if [ -f "$lock_file" ]; then
            # Extract timestamp from lock file
            local lock_time=$(grep -o '"timestamp": "[^"]*"' "$lock_file" | cut -d'"' -f4)

            # Compare with threshold (simplified - just check age)
            local lock_epoch=$(date -d "$lock_time" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$lock_time" +%s)
            local threshold_epoch=$(date -d "$ttl_minutes minutes ago" +%s 2>/dev/null || date -v-${ttl_minutes}M +%s)

            if [ "$lock_epoch" -lt "$threshold_epoch" ]; then
                echo "Removing stale lock: $lock_file"
                rm "$lock_file"
                cleaned=$((cleaned + 1))
            fi
        fi
    done

    echo "Cleaned $cleaned stale lock(s)"
}

# Show all locks with status
status_locks() {
    local current_machine=$(get_machine_id)
    local count=0

    echo "Lock Status (current machine: $current_machine)"
    echo "=============================================="

    for lock_file in "$LOCKS_DIR"/*.lock; do
        if [ -f "$lock_file" ]; then
            count=$((count + 1))
            local lock_machine=$(grep -o '"machine_id": "[^"]*"' "$lock_file" 2>/dev/null | cut -d'"' -f4 || echo "unknown")
            local agent=$(grep -o '"agent_id": "[^"]*"' "$lock_file" | cut -d'"' -f4)
            local scope=$(grep -o '"scope": "[^"]*"' "$lock_file" | cut -d'"' -f4)
            local timestamp=$(grep -o '"timestamp": "[^"]*"' "$lock_file" | cut -d'"' -f4)

            if [ "$lock_machine" = "$current_machine" ]; then
                echo "[$count] $scope (agent: $agent) - LOCAL"
            else
                echo "[$count] $scope (agent: $agent) - REMOTE ($lock_machine)"
            fi
            echo "    Created: $timestamp"
        fi
    done

    if [ $count -eq 0 ]; then
        echo "No active locks."
    else
        echo ""
        echo "Total: $count lock(s)"
    fi
}

# Main
case "$1" in
    acquire)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: $0 acquire <scope> <agent_id> [ttl_minutes]"
            exit 1
        fi
        acquire_lock "$2" "$3" "$4"
        ;;
    release)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: $0 release <scope> <agent_id>"
            exit 1
        fi
        release_lock "$2" "$3"
        ;;
    check)
        if [ -z "$2" ]; then
            echo "Usage: $0 check <scope>"
            exit 1
        fi
        check_lock "$2"
        ;;
    cleanup)
        cleanup_locks "$2"
        ;;
    status)
        status_locks
        ;;
    *)
        echo "Usage: $0 {acquire|release|check|cleanup|status}"
        echo ""
        echo "Commands:"
        echo "  acquire <scope> <agent_id> [ttl]  - Acquire a lock"
        echo "  release <scope> <agent_id>        - Release a lock"
        echo "  check <scope>                     - Check lock status"
        echo "  cleanup [ttl_minutes]             - Remove stale locks"
        echo "  status                            - Show all locks with machine info"
        echo ""
        echo "Distributed Lock Notes:"
        echo "  - Each lock includes machine_id for cross-machine awareness"
        echo "  - Locks from different machines are flagged as REMOTE"
        echo "  - Use 'status' to see lock distribution across machines"
        exit 1
        ;;
esac


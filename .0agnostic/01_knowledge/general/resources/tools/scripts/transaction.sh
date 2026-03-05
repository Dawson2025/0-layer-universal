#!/bin/bash
# resource_id: "cec4aa63-bb77-4034-b685-fe7d6eac714a"
# resource_type: "script"
# resource_name: "transaction"
#
# transaction.sh - Transaction-like rollback mechanism for multi-file operations
#
# Provides atomic multi-file operations with backup and rollback support.
#
# Usage:
#   ./transaction.sh start <transaction_id> <agent_id>   - Start transaction
#   ./transaction.sh add <transaction_id> <file>         - Backup file for rollback
#   ./transaction.sh commit <transaction_id>             - Commit (remove backups)
#   ./transaction.sh rollback <transaction_id>           - Restore from backups
#   ./transaction.sh status <transaction_id>             - Show transaction status
#   ./transaction.sh list                                - List all transactions
#   ./transaction.sh cleanup [hours]                     - Remove stale transactions
#
# Examples:
#   # Start a transaction for multi-file edit
#   ./transaction.sh start edit_config agent_01
#
#   # Backup files before modifying
#   ./transaction.sh add edit_config config/settings.yaml
#   ./transaction.sh add edit_config config/defaults.yaml
#
#   # Make your changes to the files...
#
#   # If successful, commit (removes backups)
#   ./transaction.sh commit edit_config
#
#   # If failed, rollback (restores from backups)
#   ./transaction.sh rollback edit_config
#

set -e

# Configuration
TRANSACTIONS_DIR="${TRANSACTIONS_DIR:-.transactions}"
DEFAULT_CLEANUP_HOURS=24

# Ensure transactions directory exists
mkdir -p "$TRANSACTIONS_DIR"

# Get current timestamp in ISO format
get_timestamp() {
    date -u +"%Y-%m-%dT%H:%M:%SZ"
}

# Start a new transaction
start_transaction() {
    local tx_id="$1"
    local agent_id="$2"
    local tx_dir="$TRANSACTIONS_DIR/$tx_id"

    if [ -d "$tx_dir" ]; then
        echo "ERROR: Transaction '$tx_id' already exists"
        echo "Use 'rollback' or 'commit' to close existing transaction first"
        return 1
    fi

    mkdir -p "$tx_dir/backups"

    # Create manifest
    cat > "$tx_dir/manifest.json" << EOF
{
  "transaction_id": "$tx_id",
  "agent_id": "$agent_id",
  "started": "$(get_timestamp)",
  "status": "active"
}
EOF

    # Create empty path mapping file
    touch "$tx_dir/paths.txt"

    echo "Transaction started: $tx_id"
    echo "  Agent: $agent_id"
    echo "  Directory: $tx_dir"
    return 0
}

# Add a file to the transaction (backup for rollback)
add_file() {
    local tx_id="$1"
    local file_path="$2"
    local tx_dir="$TRANSACTIONS_DIR/$tx_id"

    if [ ! -d "$tx_dir" ]; then
        echo "ERROR: Transaction '$tx_id' not found"
        echo "Start a transaction first: ./transaction.sh start $tx_id <agent_id>"
        return 1
    fi

    # Check transaction status
    local status=$(grep -o '"status": "[^"]*"' "$tx_dir/manifest.json" | cut -d'"' -f4)
    if [ "$status" != "active" ]; then
        echo "ERROR: Transaction '$tx_id' is not active (status: $status)"
        return 1
    fi

    # Get absolute path
    local abs_path=$(realpath "$file_path" 2>/dev/null || echo "$file_path")

    # Get next backup number
    local backup_num=$(wc -l < "$tx_dir/paths.txt")

    # Backup file if it exists
    if [ -f "$file_path" ]; then
        cp "$file_path" "$tx_dir/backups/backup_${backup_num}"
        # Store mapping: backup_num|original_path|existed
        echo "${backup_num}|${abs_path}|yes" >> "$tx_dir/paths.txt"
        echo "Backed up: $file_path (backup_${backup_num})"
    else
        # Mark as new file (didn't exist before)
        touch "$tx_dir/backups/backup_${backup_num}.new"
        echo "${backup_num}|${abs_path}|no" >> "$tx_dir/paths.txt"
        echo "Marked as new: $file_path (backup_${backup_num})"
    fi

    return 0
}

# Commit transaction (remove backups)
commit_transaction() {
    local tx_id="$1"
    local tx_dir="$TRANSACTIONS_DIR/$tx_id"

    if [ ! -d "$tx_dir" ]; then
        echo "ERROR: Transaction '$tx_id' not found"
        return 1
    fi

    # Check transaction status
    local status=$(grep -o '"status": "[^"]*"' "$tx_dir/manifest.json" | cut -d'"' -f4)
    if [ "$status" != "active" ]; then
        echo "ERROR: Transaction '$tx_id' is not active (status: $status)"
        return 1
    fi

    # Update status
    sed -i 's/"status": "active"/"status": "committed"/' "$tx_dir/manifest.json"

    # Count files
    local file_count=$(wc -l < "$tx_dir/paths.txt")

    # Remove backup files
    rm -rf "$tx_dir/backups"

    echo "Transaction committed: $tx_id"
    echo "  Files committed: $file_count"
    echo "  Backups removed"

    return 0
}

# Rollback transaction (restore from backups)
rollback_transaction() {
    local tx_id="$1"
    local tx_dir="$TRANSACTIONS_DIR/$tx_id"

    if [ ! -d "$tx_dir" ]; then
        echo "ERROR: Transaction '$tx_id' not found"
        return 1
    fi

    # Check transaction status
    local status=$(grep -o '"status": "[^"]*"' "$tx_dir/manifest.json" | cut -d'"' -f4)
    if [ "$status" != "active" ]; then
        echo "ERROR: Transaction '$tx_id' is not active (status: $status)"
        echo "Cannot rollback a $status transaction"
        return 1
    fi

    local restored=0
    local deleted=0
    local errors=0

    # Restore from backups using paths.txt
    while IFS='|' read -r backup_num file_path existed; do
        if [ "$existed" = "yes" ]; then
            # File existed before, restore from backup
            local backup_file="$tx_dir/backups/backup_${backup_num}"
            if [ -f "$backup_file" ]; then
                mkdir -p "$(dirname "$file_path")"
                cp "$backup_file" "$file_path"
                echo "Restored: $file_path"
                restored=$((restored + 1))
            else
                echo "WARNING: No backup found for $file_path"
                errors=$((errors + 1))
            fi
        else
            # File was new, delete it
            if [ -f "$file_path" ]; then
                rm "$file_path"
                echo "Deleted new file: $file_path"
                deleted=$((deleted + 1))
            fi
        fi
    done < "$tx_dir/paths.txt"

    # Update status
    sed -i 's/"status": "active"/"status": "rolled_back"/' "$tx_dir/manifest.json"

    echo ""
    echo "Rollback complete: $tx_id"
    echo "  Files restored: $restored"
    echo "  New files deleted: $deleted"
    if [ $errors -gt 0 ]; then
        echo "  Errors: $errors"
    fi

    return 0
}

# Show transaction status
show_status() {
    local tx_id="$1"
    local tx_dir="$TRANSACTIONS_DIR/$tx_id"

    if [ ! -d "$tx_dir" ]; then
        echo "ERROR: Transaction '$tx_id' not found"
        return 1
    fi

    echo "Transaction: $tx_id"
    echo "============"

    if [ -f "$tx_dir/manifest.json" ]; then
        cat "$tx_dir/manifest.json"
    fi

    echo ""
    echo "Tracked files:"
    if [ -f "$tx_dir/paths.txt" ] && [ -s "$tx_dir/paths.txt" ]; then
        while IFS='|' read -r backup_num file_path existed; do
            if [ "$existed" = "yes" ]; then
                echo "  [backup_${backup_num}] $file_path"
            else
                echo "  [new] $file_path"
            fi
        done < "$tx_dir/paths.txt"
    else
        echo "  (none)"
    fi

    return 0
}

# List all transactions
list_transactions() {
    echo "Active Transactions"
    echo "==================="

    local count=0
    for tx_dir in "$TRANSACTIONS_DIR"/*/; do
        if [ -d "$tx_dir" ]; then
            local tx_id=$(basename "$tx_dir")
            local manifest="$tx_dir/manifest.json"

            if [ -f "$manifest" ]; then
                local status=$(grep -o '"status": "[^"]*"' "$manifest" | cut -d'"' -f4)
                local agent=$(grep -o '"agent_id": "[^"]*"' "$manifest" | cut -d'"' -f4)
                local started=$(grep -o '"started": "[^"]*"' "$manifest" | cut -d'"' -f4)
                local file_count=0
                if [ -f "$tx_dir/paths.txt" ]; then
                    file_count=$(wc -l < "$tx_dir/paths.txt")
                fi

                echo "[$count] $tx_id"
                echo "    Status: $status"
                echo "    Agent: $agent"
                echo "    Started: $started"
                echo "    Files: $file_count"
                echo ""
                count=$((count + 1))
            fi
        fi
    done

    if [ $count -eq 0 ]; then
        echo "(No transactions found)"
    else
        echo "Total: $count transaction(s)"
    fi
}

# Cleanup stale transactions
cleanup_transactions() {
    local hours="${1:-$DEFAULT_CLEANUP_HOURS}"
    local cleaned=0

    echo "Cleaning up transactions older than $hours hours..."

    for tx_dir in "$TRANSACTIONS_DIR"/*/; do
        if [ -d "$tx_dir" ]; then
            local manifest="$tx_dir/manifest.json"

            if [ -f "$manifest" ]; then
                local status=$(grep -o '"status": "[^"]*"' "$manifest" | cut -d'"' -f4)

                # Only cleanup non-active transactions or stale active ones
                if [ "$status" != "active" ]; then
                    rm -rf "$tx_dir"
                    echo "Removed completed transaction: $(basename "$tx_dir")"
                    cleaned=$((cleaned + 1))
                else
                    # Check if active transaction is stale
                    local started=$(grep -o '"started": "[^"]*"' "$manifest" | cut -d'"' -f4)
                    local started_epoch=$(date -d "$started" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$started" +%s 2>/dev/null || echo 0)
                    local threshold_epoch=$(date -d "$hours hours ago" +%s 2>/dev/null || date -v-${hours}H +%s)

                    if [ "$started_epoch" -lt "$threshold_epoch" ] 2>/dev/null; then
                        echo "WARNING: Stale active transaction: $(basename "$tx_dir")"
                        echo "  Started: $started"
                        echo "  Consider rolling back or committing"
                    fi
                fi
            fi
        fi
    done

    echo "Cleaned up $cleaned transaction(s)"
}

# Main
case "$1" in
    start)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: $0 start <transaction_id> <agent_id>"
            echo "Example: $0 start edit_config agent_01"
            exit 1
        fi
        start_transaction "$2" "$3"
        ;;
    add)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: $0 add <transaction_id> <file>"
            echo "Example: $0 add edit_config config/settings.yaml"
            exit 1
        fi
        add_file "$2" "$3"
        ;;
    commit)
        if [ -z "$2" ]; then
            echo "Usage: $0 commit <transaction_id>"
            exit 1
        fi
        commit_transaction "$2"
        ;;
    rollback)
        if [ -z "$2" ]; then
            echo "Usage: $0 rollback <transaction_id>"
            exit 1
        fi
        rollback_transaction "$2"
        ;;
    status)
        if [ -z "$2" ]; then
            echo "Usage: $0 status <transaction_id>"
            exit 1
        fi
        show_status "$2"
        ;;
    list)
        list_transactions
        ;;
    cleanup)
        cleanup_transactions "$2"
        ;;
    *)
        echo "Usage: $0 {start|add|commit|rollback|status|list|cleanup}"
        echo ""
        echo "Transaction-like rollback mechanism for multi-file operations"
        echo ""
        echo "Commands:"
        echo "  start <tx_id> <agent_id>  - Start a new transaction"
        echo "  add <tx_id> <file>        - Add file to transaction (backup for rollback)"
        echo "  commit <tx_id>            - Commit transaction (remove backups)"
        echo "  rollback <tx_id>          - Rollback transaction (restore from backups)"
        echo "  status <tx_id>            - Show transaction status"
        echo "  list                      - List all transactions"
        echo "  cleanup [hours]           - Remove stale transactions (default: 24h)"
        echo ""
        echo "Example workflow:"
        echo "  $0 start my_edit agent_01    # Start transaction"
        echo "  $0 add my_edit file1.txt     # Backup file1.txt"
        echo "  $0 add my_edit file2.txt     # Backup file2.txt"
        echo "  # ... make changes to files ..."
        echo "  $0 commit my_edit            # Success: remove backups"
        echo "  # OR"
        echo "  $0 rollback my_edit          # Failure: restore from backups"
        exit 1
        ;;
esac

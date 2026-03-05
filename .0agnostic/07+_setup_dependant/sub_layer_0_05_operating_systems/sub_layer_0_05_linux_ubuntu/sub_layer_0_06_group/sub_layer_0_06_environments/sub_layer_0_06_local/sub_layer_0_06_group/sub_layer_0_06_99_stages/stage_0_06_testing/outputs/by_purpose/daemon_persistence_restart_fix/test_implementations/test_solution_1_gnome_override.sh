#!/bin/bash
# resource_id: "a638667b-fb77-4a40-8a09-ed4a89095b0a"
# resource_type: "script"
# resource_name: "test_solution_1_gnome_override"
# Test Solution 1: gnome-session Service Startup Order Fix
# This script sets up the gnome-session override approach

set -e

TEST_NAME="Solution 1: gnome-session Service Startup Order Override"
RESULTS_FILE="$HOME/.local/var/test-sol1-results-$(date +%Y%m%d-%H%M%S).log"
mkdir -p "$HOME/.local/var"

log() {
  echo "[$(date '+%H:%M:%S')] $1" | tee -a "$RESULTS_FILE"
}

log "========================================"
log "$TEST_NAME"
log "========================================"
log "Timestamp: $(date)"
log ""

# Cleanup previous Solution 1 setup
log "Cleaning up any previous Solution 1 configurations..."
rm -rf ~/.config/systemd/user/gnome-session-binary.service.d 2>/dev/null || true

# Create override directories
log "Creating systemd override directories..."
mkdir -p ~/.config/systemd/user/gnome-session-binary.service.d

# Create gnome-session-binary override to wait for display readiness
log "Creating gnome-session-binary.service.d/override.conf..."
cat > ~/.config/systemd/user/gnome-session-binary.service.d/override.conf << 'EOF'
# Wait for display to be ready before gnome-session starts its daemons
[Unit]
Wants=graphical-session-ready.target
After=graphical-session-ready.target
EOF

log "Override created successfully"

# Reload systemd
log "Reloading systemd user configuration..."
systemctl --user daemon-reload
log "✓ Systemd reloaded"

log ""
log "========================================"
log "Solution 1 setup COMPLETE"
log "========================================"
log ""
log "VALIDATION STEPS (perform after RESTART):"
log "1. System restart: sudo systemctl reboot"
log "2. After login, wait 15 seconds"
log "3. Run validation script: test-solution-1-validate.sh"
log ""
log "Results saved to: $RESULTS_FILE"

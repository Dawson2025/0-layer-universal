#!/bin/bash
# resource_id: "5eb35fd7-6cca-46fd-aa03-6d5079a4f960"
# resource_type: "script"
# resource_name: "test_solution_3_relogin_trigger"
# Test Solution 3: Re-Login Trigger
# This script creates a systemd service that detects broken keybindings and prompts re-login

set -e

TEST_NAME="Solution 3: Re-Login Trigger"
RESULTS_FILE="$HOME/.local/var/test-sol3-results-$(date +%Y%m%d-%H%M%S).log"
mkdir -p "$HOME/.local/var"

log() {
  echo "[$(date '+%H:%M:%S')] $1" | tee -a "$RESULTS_FILE"
}

log "========================================"
log "$TEST_NAME"
log "========================================"
log "Timestamp: $(date)"
log ""

# Cleanup previous solutions
log "Cleaning up previous solution configurations..."
rm -rf ~/.config/systemd/user/gnome-session-binary.service.d 2>/dev/null || true
rm -f ~/.config/autostart/daemon-health-check.desktop 2>/dev/null || true
systemctl --user daemon-reload 2>/dev/null || true

# Create keybinding test script
log "Creating keybinding health test script..."
mkdir -p ~/.local/bin
cat > ~/.local/bin/test-keybindings-health.sh << 'SCRIPT_EOF'
#!/bin/bash
# Test if keybindings are responsive

DISPLAY=:0
XAUTHORITY=/home/dawson/.Xauthority
export DISPLAY XAUTHORITY

# Wait for gnome-shell to fully initialize
sleep 10

# Try to check if gsd-media-keys is running
# This is a proxy for checking if custom keybindings work
if pgrep -x gsd-media-keys > /dev/null 2>&1; then
  echo "[$(date '+%H:%M:%S')] ✓ Keybindings appear healthy (gsd-media-keys running)" >> ~/.local/var/keybinding-health.log
  exit 0
else
  echo "[$(date '+%H:%M:%S')] ✗ Keybindings may be broken (gsd-media-keys not running)" >> ~/.local/var/keybinding-health.log

  # Show desktop notification prompting re-login
  notify-send --urgency=critical "Desktop Issue" \
    "Keybindings are not responsive.\n\nPlease log out and back in to refresh the session.\n\nPress Alt+F2, type 'r' to reload, or use the Power menu to log out." \
    -a "System" 2>/dev/null || true

  exit 1
fi
SCRIPT_EOF

chmod +x ~/.local/bin/test-keybindings-health.sh
log "✓ Keybinding test script created"

# Create systemd service for the keybinding health check
log "Creating systemd keybinding health check service..."
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/keybinding-health-check.service << 'SERVICE_EOF'
[Unit]
Description=Keybinding Health Check
After=graphical-session-ready.target
Requires=graphical-session-ready.target

[Service]
Type=oneshot
ExecStart=/home/dawson/.local/bin/test-keybindings-health.sh
RemainAfterExit=yes

[Install]
WantedBy=graphical-session.target
SERVICE_EOF

log "✓ Systemd service created"

# Reload systemd
log "Reloading systemd..."
systemctl --user daemon-reload
log "✓ Systemd reloaded"

# Enable the service
log "Enabling keybinding health check service..."
systemctl --user enable keybinding-health-check.service
log "✓ Service enabled"

log ""
log "========================================"
log "Solution 3 setup COMPLETE"
log "========================================"
log ""
log "VALIDATION STEPS (perform after RESTART):"
log "1. System restart: sudo systemctl reboot"
log "2. After login, if keybindings are broken:"
log "   - Desktop notification will appear"
log "   - User should log out and back in"
log "   - After re-login, keybindings should work"
log "3. Run validation script: test-solution-3-validate.sh"
log ""
log "Health check logs: ~/.local/var/keybinding-health.log"
log "Results saved to: $RESULTS_FILE"

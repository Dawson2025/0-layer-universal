#!/bin/bash
# Quick health check script for Ubuntu Syncthing setup
# Run this on Ubuntu to verify everything is working

set -e

echo "============================================"
echo "Ubuntu Syncthing Setup - Quick Health Check"
echo "============================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

check_pass() {
    echo -e "${GREEN}✓${NC} $1"
}

check_fail() {
    echo -e "${RED}✗${NC} $1"
}

check_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Check 1: Syncthing service
echo "Checking Syncthing service..."
if systemctl --user is-active syncthing &> /dev/null; then
    check_pass "Syncthing service is running"
else
    check_fail "Syncthing service is NOT running"
    echo "  Run: systemctl --user start syncthing"
fi
echo ""

# Check 2: Workspace directory
echo "Checking workspace directory..."
if [ -d "/home/dawson/dawson-workspace" ]; then
    check_pass "Workspace directory exists: /home/dawson/dawson-workspace"

    # Check file count
    file_count=$(find /home/dawson/dawson-workspace -type f 2>/dev/null | wc -l)
    dir_count=$(find /home/dawson/dawson-workspace -type d 2>/dev/null | wc -l)
    workspace_size=$(du -sh /home/dawson/dawson-workspace 2>/dev/null | cut -f1)

    echo "  Files: $file_count"
    echo "  Directories: $dir_count"
    echo "  Size: $workspace_size"

    if [ "$file_count" -lt 1000 ]; then
        check_warn "File count seems low - sync may not be complete yet"
    fi
else
    check_fail "Workspace directory does NOT exist"
    echo "  Expected: /home/dawson/dawson-workspace"
fi
echo ""

# Check 3: Dotfiles installation
echo "Checking dotfiles installation..."
if [ -L "$HOME/.bashrc" ]; then
    bashrc_target=$(readlink "$HOME/.bashrc")
    if [[ "$bashrc_target" == *"dotfiles"* ]]; then
        check_pass "Dotfiles installed (bashrc is symlinked)"
        echo "  Target: $bashrc_target"
    else
        check_warn "bashrc is a symlink but not to dotfiles"
        echo "  Target: $bashrc_target"
    fi
else
    check_warn "bashrc is not a symlink (dotfiles may not be installed)"
    echo "  Run: cd /home/dawson/dawson-workspace/dotfiles && ./install.sh"
fi
echo ""

# Check 4: Git configuration
echo "Checking Git configuration..."
git_name=$(git config --global user.name 2>/dev/null || echo "NOT SET")
git_email=$(git config --global user.email 2>/dev/null || echo "NOT SET")

if [ "$git_name" == "Dawson2025" ] && [ "$git_email" == "pac20026@byui.edu" ]; then
    check_pass "Git configuration correct"
    echo "  Name: $git_name"
    echo "  Email: $git_email"
else
    check_warn "Git configuration may need updating"
    echo "  Current name: $git_name (expected: Dawson2025)"
    echo "  Current email: $git_email (expected: pac20026@byui.edu)"
fi
echo ""

# Check 5: Network connectivity to Syncthing
echo "Checking Syncthing web interface..."
if curl -s -o /dev/null -w "%{http_code}" http://localhost:8384 | grep -q "200\|301\|302"; then
    check_pass "Syncthing web UI is accessible at http://localhost:8384"
else
    check_fail "Cannot access Syncthing web UI at http://localhost:8384"
    echo "  Syncthing may not be running or may be on a different port"
fi
echo ""

# Check 6: Device ID
echo "Checking Syncthing device ID..."
expected_device_id="7UVVQQS-O3463OC-GUTDI63-EWLX3SE-LRX4ZU3-MEOWA34-KSCMF6K-DR7GEAH"
if command -v syncthing &> /dev/null; then
    actual_device_id=$(syncthing --device-id 2>/dev/null || echo "ERROR")
    if [ "$actual_device_id" == "$expected_device_id" ]; then
        check_pass "Device ID matches expected"
        echo "  ID: $actual_device_id"
    else
        check_warn "Device ID does not match expected"
        echo "  Expected: $expected_device_id"
        echo "  Actual:   $actual_device_id"
    fi
else
    check_warn "Cannot verify device ID (syncthing command not in PATH)"
fi
echo ""

# Summary
echo "============================================"
echo "Summary"
echo "============================================"
echo ""
echo "Next steps:"
echo "1. If Syncthing is not running: systemctl --user start syncthing"
echo "2. Open web UI to check sync status: xdg-open http://localhost:8384"
echo "3. Verify all devices are connected (WSL & Windows)"
echo "4. Wait for initial sync to complete"
echo "5. See detailed guide: START_HERE_UBUNTU.md"
echo ""
echo "Documentation directory:"
echo "  /home/dawson/dawson-workspace/code/0_ai_context/0_context/-1_research/-1.01_things_researched/multi_os_system/"
echo ""

#!/bin/bash
# resource_id: "aee5c408-492c-4d3d-b6a1-a55e0bd5bdd3"
# resource_type: "script"
# resource_name: "ubuntu-quick-check"
# Quick health check script for Ubuntu Syncthing setup
# Run this on Ubuntu to verify everything is working
# Updated: 2026-01-12

set -e

echo "============================================"
echo "Ubuntu Syncthing Setup - Quick Health Check"
echo "============================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
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

check_info() {
    echo -e "${BLUE}ℹ${NC} $1"
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

# Check 3: VPS Connection (via Syncthing API)
echo "Checking VPS connection..."
if curl -s http://localhost:8384/rest/system/connections 2>/dev/null | grep -q '"JTAFCHA'; then
    vps_connected=$(curl -s http://localhost:8384/rest/system/connections 2>/dev/null | grep -A2 '"JTAFCHA' | grep -o '"connected":[^,]*' | cut -d: -f2)
    if [ "$vps_connected" == "true" ]; then
        check_pass "Connected to Hetzner VPS relay"
    else
        check_warn "VPS device configured but not connected"
        echo "  Wait a moment for connection to establish"
    fi
else
    check_warn "Cannot verify VPS connection (Syncthing API not accessible)"
fi
echo ""

# ============================================
# PRIORITY CHECK: Windows → Ubuntu Sync Test
# ============================================
echo "============================================"
echo -e "${BLUE}PRIORITY: Windows → Ubuntu Sync Verification${NC}"
echo "============================================"
echo ""

TEST_FILE="/home/dawson/dawson-workspace/SYNC_TEST_WINDOWS_TO_UBUNTU.md"

if [ -f "$TEST_FILE" ]; then
    check_pass "Windows test file found!"
    echo ""
    echo "  File: SYNC_TEST_WINDOWS_TO_UBUNTU.md"
    echo "  Size: $(stat -c%s "$TEST_FILE") bytes"
    echo "  Modified: $(stat -c%y "$TEST_FILE" | cut -d. -f1)"
    echo ""
    echo -e "  ${GREEN}★★★ BIDIRECTIONAL SYNC IS VERIFIED! ★★★${NC}"
    echo ""
    echo "  Next steps:"
    echo "  1. Update STATUS.md to mark Windows → Ubuntu as verified"
    echo "  2. Commit and push the documentation update"
    echo ""
else
    check_warn "Windows test file NOT found yet"
    echo ""
    echo "  Expected file: $TEST_FILE"
    echo ""
    echo "  Possible reasons:"
    echo "  1. Syncthing hasn't connected to VPS yet"
    echo "  2. Sync is still in progress"
    echo "  3. File was created after last Windows session"
    echo ""
    echo "  Try:"
    echo "  - Wait a minute for sync to complete"
    echo "  - Check Syncthing GUI: http://localhost:8384"
    echo "  - Force rescan: curl -X POST http://localhost:8384/rest/db/scan?folder=dawson-workspace"
fi
echo ""

# Check 4: Ubuntu → Windows test file (should exist from before)
echo "Checking Ubuntu → Windows test file..."
UBUNTU_TEST="/home/dawson/dawson-workspace/SYNC_TEST_UBUNTU_TO_WINDOWS.md"
if [ -f "$UBUNTU_TEST" ]; then
    check_pass "Ubuntu test file exists (created previously)"
else
    check_info "Ubuntu test file not found (may have been cleaned up)"
fi
echo ""

# Check 5: Dotfiles installation
echo "Checking dotfiles installation..."
if [ -L "$HOME/.bashrc" ]; then
    bashrc_target=$(readlink "$HOME/.bashrc")
    if [[ "$bashrc_target" == *"dotfiles"* ]]; then
        check_pass "Dotfiles installed (bashrc is symlinked)"
    else
        check_warn "bashrc is a symlink but not to dotfiles"
    fi
else
    check_warn "bashrc is not a symlink (dotfiles may not be installed)"
fi
echo ""

# Check 6: Git configuration
echo "Checking Git configuration..."
git_name=$(git config --global user.name 2>/dev/null || echo "NOT SET")
git_email=$(git config --global user.email 2>/dev/null || echo "NOT SET")

if [ "$git_name" != "NOT SET" ] && [ "$git_email" != "NOT SET" ]; then
    check_pass "Git configuration set"
    echo "  Name: $git_name"
    echo "  Email: $git_email"
else
    check_warn "Git configuration may need updating"
fi
echo ""

# Check 7: SSH key for VPS
echo "Checking SSH key for VPS..."
if [ -f "$HOME/.ssh/id_ed25519" ]; then
    check_pass "SSH key exists: ~/.ssh/id_ed25519"
    # Test VPS connection
    if ssh -i ~/.ssh/id_ed25519 -o ConnectTimeout=5 -o BatchMode=yes root@46.224.184.10 "echo connected" 2>/dev/null | grep -q "connected"; then
        check_pass "SSH connection to VPS works"
    else
        check_warn "SSH key exists but VPS connection test failed"
    fi
else
    check_warn "SSH key not found at ~/.ssh/id_ed25519"
fi
echo ""

# Summary
echo "============================================"
echo "Summary"
echo "============================================"
echo ""

if [ -f "$TEST_FILE" ]; then
    echo -e "${GREEN}★ SYNC VERIFICATION COMPLETE ★${NC}"
    echo ""
    echo "The Windows → Ubuntu sync is working!"
    echo "Please update the documentation to mark this as verified."
    echo ""
    echo "Run these commands to update:"
    echo "  cd ~/dawson-workspace/code/0_ai_context"
    echo "  # Edit STATUS.md to mark verification complete"
    echo "  git add -A && git commit -m 'Verify bidirectional sync complete' && git push"
else
    echo "Waiting for sync verification..."
    echo ""
    echo "Next steps:"
    echo "1. Ensure Syncthing is running: systemctl --user status syncthing"
    echo "2. Check VPS connection in GUI: http://localhost:8384"
    echo "3. Wait for SYNC_TEST_WINDOWS_TO_UBUNTU.md to appear"
    echo "4. Run this script again to verify"
fi
echo ""
echo "Documentation:"
echo "  ~/dawson-workspace/code/0_ai_context/0_context/-1_research/-1.01_things_researched/multi_os_system/"
echo ""

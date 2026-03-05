#!/bin/bash
# resource_id: "0c300b0c-a80a-4d5e-9017-51c6eab05769"
# resource_type: "script"
# resource_name: "fix_linux_login_loop"
# Linux Login Loop Fix Script
# Run this from emergency/recovery mode
# Path on Linux: /home/dawson/dawson-workspace/code/0_ai_context/0_context/layer_0_universal/fix_linux_login_loop.sh

echo "=== Linux Login Loop Fix Script ==="
echo ""

# Get username
USER_HOME="/home/dawson"
USERNAME="dawson"

echo "Step 1: Checking disk space..."
df -h
echo ""

echo "Step 2: Checking .Xauthority file..."
if [ -f "$USER_HOME/.Xauthority" ]; then
    echo "Removing corrupted .Xauthority..."
    rm -f "$USER_HOME/.Xauthority"
    echo "Done."
else
    echo ".Xauthority not found (already clean)"
fi
echo ""

echo "Step 3: Fixing home directory permissions..."
chown -R $USERNAME:$USERNAME $USER_HOME
chmod 755 $USER_HOME
echo "Done."
echo ""

echo "Step 4: Checking .ICEauthority..."
if [ -f "$USER_HOME/.ICEauthority" ]; then
    echo "Removing .ICEauthority..."
    rm -f "$USER_HOME/.ICEauthority"
    echo "Done."
else
    echo ".ICEauthority not found (already clean)"
fi
echo ""

echo "Step 5: Checking /tmp permissions..."
chmod 1777 /tmp
echo "Done."
echo ""

echo "Step 6: Checking display manager status..."
if command -v systemctl &> /dev/null; then
    echo "Display manager services:"
    systemctl list-units --type=service | grep -E "gdm|lightdm|sddm" || echo "No display manager found running"
fi
echo ""

echo "Step 7: Checking for broken packages..."
if command -v apt &> /dev/null; then
    echo "Attempting to fix broken packages..."
    apt --fix-broken install -y 2>/dev/null || echo "Run with sudo if this failed"
fi
echo ""

echo "Step 8: Checking GPU driver status..."
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi 2>/dev/null || echo "NVIDIA driver issue detected"
else
    echo "No NVIDIA driver detected (using default drivers)"
fi
echo ""

echo "=== Quick Fixes Complete ==="
echo ""
echo "Now try rebooting with: sudo reboot"
echo ""
echo "If still broken, run these manually:"
echo "  1. Reinstall display manager: sudo apt install --reinstall gdm3"
echo "  2. Reconfigure display manager: sudo dpkg-reconfigure gdm3"
echo "  3. Check Xorg logs: cat /var/log/Xorg.0.log | grep -i error"
echo ""

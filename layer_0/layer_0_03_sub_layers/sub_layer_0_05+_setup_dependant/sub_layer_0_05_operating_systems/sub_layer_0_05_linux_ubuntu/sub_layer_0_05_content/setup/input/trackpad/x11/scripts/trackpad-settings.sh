#!/bin/bash
# Trackpad settings configuration script
# Last Updated: January 11, 2026
#
# Purpose: Apply custom libinput acceleration settings for cursor and scroll
# System: Ubuntu 24.04 GNOME with libinput driver
#
# Installation:
#   1. Copy to ~/.config/trackpad-settings.sh
#   2. chmod +x ~/.config/trackpad-settings.sh
#   3. Create autostart entry (see below)
#
# Autostart Entry (~/.config/autostart/trackpad-settings.desktop):
#   [Desktop Entry]
#   Type=Application
#   Name=Trackpad Settings
#   Exec=/home/$USER/.config/trackpad-settings.sh
#   Hidden=false
#   NoDisplay=false
#   X-GNOME-Autostart-enabled=true
#   Comment=Apply custom trackpad settings on login

# Wait for X server to be ready
sleep 2

# Find the trackpad device ID
TRACKPAD_ID=$(xinput list | grep -i "touchpad" | grep -oP 'id=\K\d+' | head -n 1)

if [ -n "$TRACKPAD_ID" ]; then
    echo "Found trackpad device ID: $TRACKPAD_ID"

    # =============================================================
    # BASE SETTINGS
    # =============================================================

    # Set base speed for cursor movement (slow movements - negative = slower)
    # Range: -1.0 (slowest) to 1.0 (fastest), 0.0 = neutral
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Speed" -1.0

    # Set scrolling pixel distance (higher = slower scrolling)
    # Default: 15, Current: 40 (slower baseline)
    xinput set-prop "$TRACKPAD_ID" "libinput Scrolling Pixel Distance" 40

    # Enable custom acceleration profile for both cursor and scroll acceleration
    # Format: (adaptive, flat, custom) - (0, 0, 1) = custom enabled
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Profile Enabled" 0, 0, 1

    # =============================================================
    # SCROLL ACCELERATION (11 zones for smooth transitions)
    # =============================================================
    # Zones: 0.1, 0.15, 0.25, 0.35, 0.5, 0.65, 0.8, 0.9, 1.0, 1.2, 1.5
    # Progression: ~1.5-2x between zones for smooth scrolling feel
    #
    # Zone breakdown:
    #   Zone 1:  0.00-0.10 velocity → 0.1x  (careful reading)
    #   Zone 2:  0.10-0.20 velocity → 0.15x (slow browsing)
    #   Zone 3:  0.20-0.30 velocity → 0.25x (paragraph nav)
    #   Zone 4:  0.30-0.40 velocity → 0.35x (section nav)
    #   Zone 5:  0.40-0.50 velocity → 0.5x  (normal scrolling)
    #   Zone 6:  0.50-0.60 velocity → 0.65x (quick browsing)
    #   Zone 7:  0.60-0.70 velocity → 0.8x  (fast navigation)
    #   Zone 8:  0.70-0.80 velocity → 0.9x  (rapid scrolling)
    #   Zone 9:  0.80-0.90 velocity → 1.0x  (very fast)
    #   Zone 10: 0.90-1.00 velocity → 1.2x  (page skimming)
    #   Zone 11: 1.00+     velocity → 1.5x  (maximum speed)
    #
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Custom Scroll Step" 0.05

    # =============================================================
    # CURSOR ACCELERATION (7 zones for precision control)
    # =============================================================
    # Zones: 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1
    # Progression: ~3x between zones for distinct precision tiers
    #
    # Zone breakdown:
    #   Zone 1: 0.00-0.10 velocity → 0.0001x (pixel-perfect precision)
    #   Zone 2: 0.10-0.20 velocity → 0.0003x (fine adjustments)
    #   Zone 3: 0.20-0.30 velocity → 0.001x  (slow deliberate)
    #   Zone 4: 0.30-0.40 velocity → 0.003x  (medium-slow)
    #   Zone 5: 0.40-0.50 velocity → 0.01x   (normal navigation)
    #   Zone 6: 0.50-0.60 velocity → 0.03x   (quick navigation)
    #   Zone 7: 0.60+     velocity → 0.1x    (fast movement)
    #
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Custom Motion Step" 0.05

    echo "Trackpad settings applied successfully"
else
    echo "No trackpad device found"
    exit 1
fi

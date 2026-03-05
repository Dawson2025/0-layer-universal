#!/bin/bash
# resource_id: "b99f38a5-2deb-4380-b99a-46bfef686d0b"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 00_stage_registry stage"

# Add custom initialization here

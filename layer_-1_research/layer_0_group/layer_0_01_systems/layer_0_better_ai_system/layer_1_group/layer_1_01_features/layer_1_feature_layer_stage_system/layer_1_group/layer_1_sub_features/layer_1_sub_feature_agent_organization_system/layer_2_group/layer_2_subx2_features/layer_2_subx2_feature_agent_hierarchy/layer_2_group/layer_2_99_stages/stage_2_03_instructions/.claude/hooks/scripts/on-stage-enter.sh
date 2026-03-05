#!/bin/bash
# resource_id: "2e8596c3-efb5-417e-98b6-d6a03f600d76"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 03_instructions stage"

# Add custom initialization here

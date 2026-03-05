#!/bin/bash
# resource_id: "e2f2e041-d88c-434f-82d6-4fbe785642c6"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 03_instructions stage"

# Add custom initialization here

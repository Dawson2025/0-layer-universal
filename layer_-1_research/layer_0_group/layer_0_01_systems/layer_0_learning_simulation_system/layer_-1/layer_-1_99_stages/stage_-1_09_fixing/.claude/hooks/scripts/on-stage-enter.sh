#!/bin/bash
# resource_id: "f09ca8f6-f37a-46d4-beaa-a2989fc9a4ad"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 09_fixing stage"

# Add custom initialization here

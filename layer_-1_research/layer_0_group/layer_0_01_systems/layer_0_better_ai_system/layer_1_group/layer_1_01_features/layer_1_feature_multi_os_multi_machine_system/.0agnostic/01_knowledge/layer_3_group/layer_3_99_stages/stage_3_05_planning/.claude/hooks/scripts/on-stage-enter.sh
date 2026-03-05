#!/bin/bash
# resource_id: "53e2e770-ed3b-4b62-93d7-2f36ef6eabd7"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 05_planning stage"

# Add custom initialization here

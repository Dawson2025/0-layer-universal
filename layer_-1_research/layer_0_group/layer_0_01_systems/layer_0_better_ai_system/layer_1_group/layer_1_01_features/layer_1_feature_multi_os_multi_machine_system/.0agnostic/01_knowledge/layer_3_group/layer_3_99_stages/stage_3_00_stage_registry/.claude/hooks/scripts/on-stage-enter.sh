#!/bin/bash
# resource_id: "0863586a-736c-49ba-9899-2cd09b66d8cf"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 00_stage_registry stage"

# Add custom initialization here

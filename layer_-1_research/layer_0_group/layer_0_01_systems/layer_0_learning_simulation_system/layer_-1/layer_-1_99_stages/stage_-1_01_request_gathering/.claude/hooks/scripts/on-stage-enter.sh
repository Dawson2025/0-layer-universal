#!/bin/bash
# resource_id: "52aac5aa-ff33-4fec-8799-f44b33fa7fe7"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 01_request_gathering stage"

# Add custom initialization here

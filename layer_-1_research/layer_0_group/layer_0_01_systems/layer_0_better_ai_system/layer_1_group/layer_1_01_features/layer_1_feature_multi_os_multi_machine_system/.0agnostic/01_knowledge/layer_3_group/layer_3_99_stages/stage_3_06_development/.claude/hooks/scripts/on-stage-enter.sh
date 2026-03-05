#!/bin/bash
# resource_id: "7d6a3824-3425-4f44-9d8b-ded423b993b3"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 06_development stage"

# Add custom initialization here

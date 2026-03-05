#!/bin/bash
# resource_id: "e02bd365-e622-4cbe-8e4c-b1a79be701ee"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 07_testing stage"

# Add custom initialization here

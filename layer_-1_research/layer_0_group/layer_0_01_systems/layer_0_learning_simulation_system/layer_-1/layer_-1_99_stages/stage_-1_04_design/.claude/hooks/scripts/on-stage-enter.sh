#!/bin/bash
# resource_id: "dc60cb44-166f-4efb-a908-eef807a4b595"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 04_design stage"

# Add custom initialization here

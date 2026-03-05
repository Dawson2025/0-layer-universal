#!/bin/bash
# resource_id: "7691ebcd-0b88-49ff-bf7c-339bc2608810"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 02_research stage"

# Add custom initialization here

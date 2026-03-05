#!/bin/bash
# resource_id: "87e2697c-1fda-44d6-bf60-3a6bc1946e9f"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 03_instructions stage"

# Add custom initialization here

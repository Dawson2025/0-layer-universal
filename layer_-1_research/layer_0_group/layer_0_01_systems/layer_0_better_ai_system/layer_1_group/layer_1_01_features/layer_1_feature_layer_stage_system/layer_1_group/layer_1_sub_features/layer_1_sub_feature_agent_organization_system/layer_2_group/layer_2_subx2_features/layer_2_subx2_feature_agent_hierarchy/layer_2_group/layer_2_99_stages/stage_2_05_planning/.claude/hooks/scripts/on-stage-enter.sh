#!/bin/bash
# resource_id: "e8c1d6e0-5a0f-43d2-a984-775567fc68b2"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 05_planning stage"

# Add custom initialization here

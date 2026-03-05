#!/bin/bash
# resource_id: "b47205dc-1e14-4d17-bd3f-8317846b2672"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 06_development stage"

# Add custom initialization here

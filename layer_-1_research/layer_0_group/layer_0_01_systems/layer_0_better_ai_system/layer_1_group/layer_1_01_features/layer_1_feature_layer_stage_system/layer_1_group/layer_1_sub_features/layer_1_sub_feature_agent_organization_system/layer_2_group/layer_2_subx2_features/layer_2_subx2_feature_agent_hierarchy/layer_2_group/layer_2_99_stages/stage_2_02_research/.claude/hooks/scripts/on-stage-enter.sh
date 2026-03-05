#!/bin/bash
# resource_id: "0ce15e68-81ce-49ce-8f62-2c431c310c3e"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 02_research stage"

# Add custom initialization here

#!/bin/bash
# resource_id: "e7c6295c-392f-4526-8f70-eea9b0b1fa2b"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 11_archives stage"

# Add custom initialization here

#!/bin/bash
# resource_id: "913f8ad8-7c4f-4236-a3cf-e1758c2e5adc"
# resource_type: "script"
# resource_name: "create-sub-layer-entity"
# create-sub-layer-entity.sh
# Usage: create-sub-layer-entity.sh <entity_dir> <layer_num>
# Creates canonical entity structure for a sub-layer entity per entity_structure.md
# Layer num is the specificity level (e.g., 10 for AI apps)

set -e

ENTITY="$1"
N="$2"
N1=$((10#$N+1))
N1=$(printf "%02d" "$N1")

if [ -z "$ENTITY" ] || [ -z "$N" ]; then
  echo "Usage: $0 <entity_dir> <layer_num>"
  exit 1
fi

echo "Creating canonical entity structure at: $ENTITY (sub-layer 0.$N)"

# Entity root directories
mkdir -p "$ENTITY"/{.0agnostic/{01_knowledge,02_rules/{static,dynamic},03_protocols,04_episodic_memory/{sessions,changes},05_handoff_documents/{01_incoming/{01_from_above,02_from_sides/{01_from_left,02_from_right},03_from_below/{stage_reports,layer_reports}},02_outgoing/{01_to_above,02_to_sides/{01_to_left,02_to_right},03_to_below}},06_context_avenue_web/{00_context_avenue_web_registry,01_file_based/{01_aalang,02_aalang_markdown_integration,03_auto_memory,"04_@import_references",05_skills,06_agents,07_path_specific_rules,08_hooks},02_data_based/{09_knowledge_graph,10_relational_index,11_vector_embeddings,12_temporal_index,13_shimi_structures}},07+_setup_dependant},.1merge/{.1claude_merge/{0_synced,1_overrides,2_additions},.1cursor_merge/{0_synced,1_overrides,2_additions},.1gemini_merge/{0_synced,1_overrides,2_additions},.1aider_merge/{0_synced,1_overrides,2_additions},.1codex_merge/{0_synced,1_overrides,2_additions},.1copilot_merge/{0_synced,1_overrides,2_additions}},.claude/{rules,episodic_memory/{sessions,changes}},.cursor/{rules,episodic_memory/{sessions,changes}},.gemini/episodic_memory/{sessions,changes},.codex/episodic_memory/{sessions,changes},.github/instructions}

# Internal sub_layer_0_N_group structure
mkdir -p "$ENTITY/sub_layer_0_${N}_group/sub_layer_0_${N}_00_layer_registry/proposals"
mkdir -p "$ENTITY/sub_layer_0_${N}_group/sub_layer_0_${N}_99_stages"

# All 12 stages
STAGES_DIR="$ENTITY/sub_layer_0_${N}_group/sub_layer_0_${N}_99_stages"
for stage in 00_stage_registry 01_request_gathering 02_research 03_instructions 04_design 05_planning 06_development 07_testing 08_criticism 09_fixing 10_current_product 11_archives; do
  STAGE_DIR="$STAGES_DIR/stage_0_${N}_${stage}"
  mkdir -p "$STAGE_DIR"/{outputs,synthesis,.0agnostic/{01_knowledge,02_rules/{static,dynamic},03_protocols,04_episodic_memory/{sessions,changes},05_handoff_documents/{01_incoming/{01_from_above,02_from_sides/{01_from_left,02_from_right},03_from_below},02_outgoing/{01_to_above,02_to_sides/{01_to_left,02_to_right},03_to_below}},06_context_avenue_web/{00_context_avenue_web_registry,01_file_based/{01_aalang,02_aalang_markdown_integration,03_auto_memory,"04_@import_references",05_skills,06_agents,07_path_specific_rules,08_hooks},02_data_based/{09_knowledge_graph,10_relational_index,11_vector_embeddings,12_temporal_index,13_shimi_structures}},07+_setup_dependant},.1merge/{.1claude_merge/{0_synced,1_overrides,2_additions},.1cursor_merge/{0_synced,1_overrides,2_additions},.1gemini_merge/{0_synced,1_overrides,2_additions},.1aider_merge/{0_synced,1_overrides,2_additions},.1codex_merge/{0_synced,1_overrides,2_additions},.1copilot_merge/{0_synced,1_overrides,2_additions}},.claude/{rules,episodic_memory/{sessions,changes}},.cursor/{rules,episodic_memory/{sessions,changes}},.gemini/episodic_memory/{sessions,changes},.codex/episodic_memory/{sessions,changes},.github/instructions}
  # Add .gitkeep to empty leaf directories
  find "$STAGE_DIR" -type d -empty -exec touch {}/.gitkeep \;
done

# Children container
mkdir -p "$ENTITY/sub_layer_0_${N1}_group/sub_layer_0_${N1}_00_layer_registry/proposals"

# Add .gitkeep to all empty leaf directories
find "$ENTITY" -type d -empty -exec touch {}/.gitkeep \;

echo "Done. Created $(find "$ENTITY" -type d | wc -l) directories."

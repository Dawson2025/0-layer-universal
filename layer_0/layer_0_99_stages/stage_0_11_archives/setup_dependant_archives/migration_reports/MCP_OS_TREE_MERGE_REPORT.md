---
resource_id: "22272300-5a68-4827-8528-d5a9604985b7"
resource_type: "document"
resource_name: "MCP_OS_TREE_MERGE_REPORT"
---
# MCP OS Tree Merge Report

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems`
Target root: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0`

<!-- section_id: "c6efec61-9649-4465-b502-2827016b5578" -->
## Summary

- Copied missing files: 0 (all target paths already exist)
- Conflicts merged: 49
- Legacy files removed: 49 (`*.mcp_legacy` merged into targets)

<!-- section_id: "46bf7ccd-38cc-4ee8-b795-aba6a093a591" -->
## Merge Method

Where the MCP OS tree content differed from the hierarchy targets, the MCP content was appended to the target file under a `Legacy MCP Source` section. This ensures no MCP instructions were lost while keeping the hierarchy file as the primary source.

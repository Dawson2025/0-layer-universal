#!/usr/bin/env python3
"""
Script to update main.py with cleaner hierarchy display format.
"""

def update_main_file():
    """Update the main.py file with cleaner hierarchy display."""
    
    # Read the current main.py file
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define the old and new code sections
    old_code = '''        if filters[position] == 'all':
            # For 'all' types, show hierarchy with group/subgroup headers
            display_groups = defaultdict(list)
            for num, data in position_mappings[position].items():
                key = (data['group_type'], data['subgroup_type'], data['group_freq'], data['subgroup_freq'])
                display_groups[key].append((num, data))
            
            # Sort groups by aggregate frequency (ascending)
            sorted_display_groups = sorted(display_groups.items(), key=lambda x: (x[0][2], x[0][3] if x[0][3] is not None else -1))
            
            current_group = ""
            current_subgroup = ""
            
            for key, phoneme_data_list in sorted_display_groups:
                g, sub, gfreq, subfreq = key
                
                # Add group header if new
                if g != current_group:
                    position_display_data[position].append(f"- {g} (group freq: {gfreq})")
                    current_group = g
                    current_subgroup = ""
                
                # Add subgroup header if new
                if sub and sub != "none" and sub != current_subgroup:
                    position_display_data[position].append(f"  - {sub} (subgroup freq: {subfreq})")
                    current_subgroup = sub
                
                # Add phonemes within this group/subgroup
                for num, data in phoneme_data_list:
                    indent = "    " if sub and sub != "none" else "  "
                    position_display_data[position].append(f"{indent}{num}: {data['phoneme']} ({data['frequency']})")'''
    
    new_code = '''        if filters[position] == 'all':
            # For 'all' types, show hierarchy with clean group/subgroup separators
            display_groups = defaultdict(list)
            for num, data in position_mappings[position].items():
                key = (data['group_type'], data['subgroup_type'], data['group_freq'], data['subgroup_freq'])
                display_groups[key].append((num, data))
            
            # Sort groups by aggregate frequency (ascending)
            sorted_display_groups = sorted(display_groups.items(), key=lambda x: (x[0][2], x[0][3] if x[0][3] is not None else -1))
            
            current_group = ""
            current_subgroup = ""
            
            for i, (key, phoneme_data_list) in enumerate(sorted_display_groups):
                g, sub, gfreq, subfreq = key
                
                # Add group header if new
                if g != current_group:
                    # Add blank line before new group (except for first group)
                    if current_group != "":
                        position_display_data[position].append("")
                    
                    # Add group name and frequency
                    position_display_data[position].append(f"{g} (group freq: {gfreq})")
                    # Add separator line under group name
                    separator_length = len(f"{g} (group freq: {gfreq})")
                    position_display_data[position].append("-" * separator_length)
                    
                    current_group = g
                    current_subgroup = ""
                
                # Add subgroup header if new
                if sub and sub != "none" and sub != current_subgroup:
                    position_display_data[position].append(f"{sub} (subgroup freq: {subfreq})")
                    current_subgroup = sub
                
                # Add phonemes within this group/subgroup
                for num, data in phoneme_data_list:
                    position_display_data[position].append(f"{num}: {data['phoneme']} ({data['frequency']})")'''
    
    # Replace the old code with new code
    if old_code in content:
        content = content.replace(old_code, new_code)
        print("✅ Successfully updated main.py with cleaner hierarchy display format")
        
        # Write the updated content back to the file
        with open('main.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ File has been updated and saved")
    else:
        print("❌ Could not find the old code section to replace")
        print("Please check if the file structure has changed")

if __name__ == "__main__":
    update_main_file()

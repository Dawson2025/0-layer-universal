#!/usr/bin/env python3
# resource_id: "4e9196a9-01ce-4eda-bfa5-12b044fb6115"
# resource_type: "document"
# resource_name: "fix_columns_and_labels"
"""
Script to fix columns and labels in main.py
"""

def fix_main_file():
    """Fix the main.py file with wider columns and simplified labels."""
    
    # Read the current main.py file
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes_made = 0
    
    # Change 1: Simplify group labels (remove "group freq:")
    old_group_label = 'position_display_data[position].append(f"{g} (group freq: {gfreq})")'
    new_group_label = 'position_display_data[position].append(f"{g} ({gfreq})")'
    
    if old_group_label in content:
        content = content.replace(old_group_label, new_group_label)
        changes_made += 1
        print("✅ Updated group labels to simplified format")
    
    # Change 2: Simplify subgroup labels (remove "subgroup freq:")
    old_subgroup_label = 'position_display_data[position].append(f"{sub} (subgroup freq: {subfreq})")'
    new_subgroup_label = 'position_display_data[position].append(f"{sub} ({subfreq})")'
    
    if old_subgroup_label in content:
        content = content.replace(old_subgroup_label, new_subgroup_label)
        changes_made += 1
        print("✅ Updated subgroup labels to simplified format")
    
    # Change 3: Update separator length calculation for simplified labels
    old_separator = 'separator_length = len(f"{g} (group freq: {gfreq})")'
    new_separator = 'separator_length = len(f"{g} ({gfreq})")'
    
    if old_separator in content:
        content = content.replace(old_separator, new_separator)
        changes_made += 1
        print("✅ Updated separator length calculation")
    
    # Change 4: Add minimum width for better column spacing
    old_width_init = '        max_widths[position] = 0'
    new_width_init = '        # Set minimum width for each position to prevent cramped display\n        min_width = 50  # Minimum 50 characters per position\n        max_widths[position] = min_width'
    
    if old_width_init in content:
        content = content.replace(old_width_init, new_width_init)
        changes_made += 1
        print("✅ Added minimum width (50 chars) for better column spacing")
    
    # Change 5: Add comment about hierarchy display width calculation
    old_width_comment = '                        max_widths[position] = max(max_widths[position], len(f"{num}: {phoneme} ({freq})"))'
    new_width_comment = '                        max_widths[position] = max(max_widths[position], len(f"{num}: {phoneme} ({freq})"))\n        \n        # Also check hierarchy display data for width calculation\n        if filters[position] == \'all\':\n            # For hierarchy display, we need to account for group names and separators\n            # This will be calculated in the display preparation section\n            pass'
    
    if old_width_comment in content:
        content = content.replace(old_width_comment, new_width_comment)
        changes_made += 1
        print("✅ Added comment about hierarchy display width calculation")
    
    if changes_made > 0:
        # Write the updated content back to the file
        with open('main.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n✅ File has been updated with {changes_made} changes")
        print("✅ Implemented:")
        print("   - Simplified labels: 'Stops (3)' instead of 'Stops (group freq: 3)'")
        print("   - Wider columns: minimum 50 characters per position")
        print("   - Better spacing between columns")
        print("   - Cleaner, more professional appearance")
    else:
        print("❌ No changes were made. Please check if the file structure has changed")

if __name__ == "__main__":
    fix_main_file()

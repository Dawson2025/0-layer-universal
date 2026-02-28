# flatten_syllables.py
import os
from collections import defaultdict

# Import your full dataset
from sample_data import syllable_making_dataset  # change filename if needed

grouped = defaultdict(list)

def recurse(path, data):
    if isinstance(data, dict):
        if "phonemes" in data:
            group_type = path.get("group_type")
            subgroup_type = path.get("subgroup_type") if path.get("subgroup_type") else "none"
            key = (
                path.get("syllable_type"),
                path.get("position"),
                path.get("length_type"),
                group_type,
                subgroup_type
            )
            for phoneme_dict in data["phonemes"]:
                for phoneme, freq in phoneme_dict.items():
                    grouped[key].append((phoneme, freq))
        else:
            for key, value in data.items():
                if path.get("syllable_type") is None:
                    recurse({**path, "syllable_type": key}, value)
                elif path.get("position") is None:
                    recurse({**path, "position": key}, value)
                elif path.get("length_type") is None:
                    recurse({**path, "length_type": key}, value)
                elif path.get("group_type") is None:
                    recurse({**path, "group_type": key}, value)
                elif path.get("subgroup_type") is None:
                    recurse({**path, "subgroup_type": key}, value)
                else:
                    recurse(path, value)

# Flatten it
recurse({}, syllable_making_dataset)

flattened_dataset = []
for key, phonemes in grouped.items():
    syllable_type, position, length_type, group_type, subgroup_type = key
    for phoneme, freq in phonemes:
        flattened_dataset.append({
            "syllable_type": syllable_type,
            "position": position,
            "length_type": length_type,
            "group_type": group_type,
            "subgroup_type": subgroup_type,
            "phoneme": phoneme,
            "frequency": freq
        })
# Preview output
for row in flattened_dataset[:10]:
    print(row)

# File overwrite check
output_file = "flattened_dataset.py"
if os.path.exists(output_file):
    confirm = input(f"'{output_file}' already exists. Overwrite? (y/n): ").strip().lower()
    if confirm != "y":
        print("Operation cancelled. No file written.")
        exit()

# Save as .py for importing
with open(output_file, "w", encoding="utf-8") as f:
    f.write("flattened_dataset = [\n")
    for entry in flattened_dataset:
        f.write(f"    {entry},\n")
    f.write("]\n")

print(f"\nFlattened data saved to '{output_file}'. Total entries: {len(flattened_dataset)}")
import json
import sys
from pathlib import Path


def update_tags(mapping_file, datasets_dir="datasets"):
    with open(mapping_file, "r", encoding="utf-8") as f:
        tag_mapping = json.load(f)

    for new_tag, dataset_list in tag_mapping.items():
        for dataset in dataset_list:
            ds_file = Path(datasets_dir) / f"{dataset}.json"
            if ds_file.exists():
                with open(ds_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # Get existing tags or initialize an empty list
                tags = data.get("tags", [])
                if new_tag not in tags:
                    tags.append(new_tag)
                    data["tags"] = tags
                    with open(ds_file, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=4)
                    print(f"Added tag '{new_tag}' to dataset '{dataset}'.")
                else:
                    print(f"Dataset '{dataset}' already contains tag '{new_tag}'.")
            else:
                print(f"Dataset file '{ds_file}' not found.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python update_dataset_tags.py <path_to_json_mapping_file>")
        sys.exit(1)

    mapping_file = sys.argv[1]
    update_tags(mapping_file)

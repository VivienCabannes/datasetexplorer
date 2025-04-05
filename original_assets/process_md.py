import os
import sys
import re
import json
from pathlib import Path


def parse_markdown_file(md_path):
    """
    Parse the markdown file and return a list of dataset dictionaries.
    Each dataset dictionary will have the canonical keys:
      "name", "summary", "size", "download", "notes", "companion".
    """
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    datasets = []
    current_dataset_name = None
    current_block_lines = []

    for line in lines:
        line = line.rstrip()
        # Check for new dataset block
        if line.startswith("####"):
            if current_dataset_name is not None:
                dataset_data = process_dataset_block(
                    current_dataset_name, current_block_lines
                )
                datasets.append(dataset_data)
            # Extract dataset name from header, e.g. "#### AIME." -> "AIME"
            m = re.match(r"####\s*(.+?)\.", line)
            if m:
                current_dataset_name = m.group(1).strip()
            else:
                current_dataset_name = line.lstrip("#").strip()
            current_block_lines = []
        else:
            if line.strip():
                current_block_lines.append(line)
    if current_dataset_name is not None and current_block_lines:
        dataset_data = process_dataset_block(current_dataset_name, current_block_lines)
        datasets.append(dataset_data)
    return datasets


def process_dataset_block(name, lines):
    """
    Process the block of lines for a single dataset.
    Maps keys to the canonical set: "name", "summary", "size", "download", "notes", "companion".
    """
    # Mapping from the markdown key (lowercase) to the canonical key.
    mapping = {
        "size": "size",
        "where to find it": "download",
        "notes": "notes",
        "companion paper": "companion",
    }
    data = {}
    data["name"] = name
    summary_lines = []

    for line in lines:
        # Look for bold key lines, e.g. **Size**: 15 questions per year
        if line.startswith("**"):
            m = re.match(r"\*\*(.+?)\*\*\s*:\s*(.*)", line)
            if m:
                key_raw = m.group(1).strip().lower()
                value = m.group(2).strip()
                if key_raw in mapping:
                    canonical_key = mapping[key_raw]
                    data[canonical_key] = value
                # Ignore keys not in our mapping (e.g. "current location", "current format")
        else:
            summary_lines.append(line.strip())
    data["summary"] = " ".join(summary_lines) if summary_lines else ""
    return data


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_datasets_from_md.py <path_to_markdown_file>")
        sys.exit(1)

    md_path = sys.argv[1]
    if not os.path.exists(md_path):
        print(f"Error: {md_path} does not exist.")
        sys.exit(1)

    # Parse the markdown file to get a list of dataset dictionaries.
    datasets_list = parse_markdown_file(md_path)

    # Create output folder 'datasets' if it doesn't exist.
    output_dir = "datasets"
    os.makedirs(output_dir, exist_ok=True)

    # Write each dataset to a JSON file named <dataset_name>.json.
    for dataset in datasets_list:
        filename = os.path.join(output_dir, f"{dataset['name']}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(dataset, f, indent=4)
        print(f"Created {filename}")


if __name__ == "__main__":
    main()

import os
import sys
import re
import json
from pathlib import Path


def parse_markdown_file(md_path):
    """
    Parse the markdown file and return a list of dataset dictionaries.
    Each dataset is a dictionary with keys extracted from the text.
    """
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    datasets = []
    current_dataset_name = None
    current_block_lines = []

    for line in lines:
        line = line.rstrip()  # remove trailing newline and spaces
        # Check if this line starts a new dataset section.
        if line.startswith("####"):
            # If we were collecting a dataset, process it.
            if current_dataset_name is not None:
                dataset_data = process_dataset_block(
                    current_dataset_name, current_block_lines
                )
                datasets.append(dataset_data)
            # Extract dataset name using regex (e.g., "#### AIME." -> "AIME")
            m = re.match(r"####\s*(.+?)\.", line)
            if m:
                current_dataset_name = m.group(1).strip()
            else:
                # Fallback: remove leading '####'
                current_dataset_name = line.lstrip("#").strip()
            current_block_lines = []
        else:
            # Only add non-empty lines to the block
            if line.strip() != "":
                current_block_lines.append(line)
    # Process the final block if exists.
    if current_dataset_name is not None and current_block_lines:
        dataset_data = process_dataset_block(current_dataset_name, current_block_lines)
        datasets.append(dataset_data)
    return datasets


def process_dataset_block(name, lines):
    """
    Process the block of lines for a single dataset.
    Returns a dictionary with the dataset's details.
    """
    data = {}
    data["name"] = name
    summary_lines = []

    # Process each line in the block
    for line in lines:
        # If the line starts with a bold key (e.g., "**Size**: ...")
        if line.startswith("**"):
            # Extract key and value using regex
            m = re.match(r"\*\*(.+?)\*\*\s*:\s*(.*)", line)
            if m:
                key = m.group(1).strip()
                value = m.group(2).strip()
                data[key] = value
        else:
            # Otherwise, treat the line as part of the summary.
            summary_lines.append(line.strip())

    # Combine summary lines (if any) into a single summary field.
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
    output_dir = "tmp_datasets"
    os.makedirs(output_dir, exist_ok=True)

    # Write each dataset to a JSON file named <dataset>.json.
    for dataset in datasets_list:
        # Use the dataset name as the filename (strip any problematic characters if needed)
        filename = os.path.join(output_dir, f"{dataset['name']}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(dataset, f, indent=4)
        print(f"Created {filename}")


if __name__ == "__main__":
    main()

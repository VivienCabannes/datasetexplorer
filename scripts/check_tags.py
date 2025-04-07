import json
from pathlib import Path


def load_tags_from_datasets(datasets_dir):
    """
    Load tags from each JSON file in the given datasets directory.
    Returns a dictionary mapping each dataset filename to its list of tags.
    """
    dataset_tags = {}
    for path in Path(datasets_dir).glob("*.json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Use an empty list if no tags are provided in the dataset
        tags = data.get("tags", [])
        dataset_tags[path.stem] = tags
    return dataset_tags


def load_defined_tags(tags_file):
    """
    Load defined tags from the tags.json file.
    Returns a set of defined tag names.
    """
    with open(tags_file, "r", encoding="utf-8") as f:
        tags_data = json.load(f)
    return {key for tag_group in tags_data for key in tag_group["tags"].keys()}


def check_tags(datasets_dir, tags_file):
    """
    Compare tags used in dataset files with the defined tags.
    Returns a tuple (missing_tags, unused_tags) where:
      - missing_tags is a dictionary mapping dataset filenames to a list of tags
        that are used in that dataset but not defined in tags.json.
      - unused_tags is a set of tags defined in tags.json that are not used in any dataset.
    """
    dataset_tags = load_tags_from_datasets(datasets_dir)
    defined_tags = load_defined_tags(tags_file)

    missing_tags = {}  # dataset filename -> list of missing tags
    used_tags = set()
    for dataset, tags in dataset_tags.items():
        missing = []
        for tag in tags:
            used_tags.add(tag)
            if tag not in defined_tags:
                missing.append(tag)
        if missing:
            missing_tags[dataset] = missing

    # Find defined tags that are never used in any dataset
    unused_tags = defined_tags - used_tags

    return missing_tags, unused_tags


if __name__ == "__main__":
    import os

    datasets_dir = "datasets"
    tags_file = os.path.join(datasets_dir, "tags.jsonl")

    missing_tags, unused_tags = check_tags(datasets_dir, tags_file)

    if missing_tags:
        print(
            "Datasets with undefined tags (tags used in dataset but not defined in tags.json):"
        )
        for dataset, tags in missing_tags.items():
            print(f"  {dataset}: {', '.join(tags)}")
    else:
        print("All dataset tags are defined in tags.json.")

    if unused_tags:
        print("\nTags defined in tags.json that are never used in any dataset:")
        print(f"  {', '.join(unused_tags)}")
    else:
        print("\nAll tags in tags.json are used in at least one dataset.")

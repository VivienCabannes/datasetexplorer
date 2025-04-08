import os
import glob


def collect_and_save_drafts(
    folder1="source_data/datasets1",
    folder2="source_data/datasets2",
    folder3="source_data/datasets3",
    out_folder="prompt_cards",
):
    """
    Reads all .json files from the three datasets folders, storing them
    as Draft1, Draft2, and Draft3. Then writes each set of drafts to
    a file named tmp_<basename>.txt in the 'prompt/' folder.
    """

    # Ensure the output folder exists
    os.makedirs(out_folder, exist_ok=True)

    # Use a dictionary in the form:
    # {
    #    "base_name": {
    #         1: "<content>",
    #         2: "<content>",
    #         3: "<content>"
    #    },
    #    ...
    # }
    collected = {}

    # Helper function to read all files from a folder and assign to a specific draft_num
    def read_folder_files(folder_path, draft_num):
        for file_path in glob.glob(os.path.join(folder_path, "*.json")):
            # base_name is the filename without .json
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if base_name not in collected:
                collected[base_name] = {}
            collected[base_name][draft_num] = content

    # Read each folder into the dictionary
    read_folder_files(folder1, draft_num=1)
    read_folder_files(folder2, draft_num=2)
    read_folder_files(folder3, draft_num=3)

    # For each base_name, write out a file named tmp_<base_name>.txt in out_folder
    for base_name in sorted(collected.keys()):
        out_filepath = os.path.join(out_folder, f"{base_name}.txt")
        with open(out_filepath, "w", encoding="utf-8") as out_file:
            # Write drafts in ascending order: 1, 2, 3
            for draft_num in [1, 2, 3]:
                content = collected[base_name].get(draft_num, "")
                out_file.write(f"Draft{draft_num}\n")
                out_file.write("```\n")
                out_file.write(content)
                # Make sure to end with a newline (avoid double-newlines if content already ends with one)
                if not content.endswith("\n"):
                    out_file.write("\n")
                out_file.write("```\n\n")

        print(f"Wrote: {out_filepath}")


if __name__ == "__main__":
    collect_and_save_drafts()

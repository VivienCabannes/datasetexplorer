import os


def gather_and_save_files(directory="."):
    output_filename = "combined_content.txt"
    # Collect only .json files in the directory
    json_files = [f for f in os.listdir(directory) if f.endswith(".json")]

    with open(output_filename, "w", encoding="utf-8") as outfile:
        for filename in sorted(json_files):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f_in:
                content = f_in.read()

            outfile.write(filename + "\n")
            outfile.write("```json\n")
            outfile.write(content)
            outfile.write("\n```\n\n")


if __name__ == "__main__":
    gather_and_save_files(".")

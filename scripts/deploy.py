import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from flask_frozen import Freezer

ROOT_DIR = Path(__file__).parent.parent.resolve()
BUILD_DIR = ROOT_DIR / "docs"
sys.path.insert(0, str(ROOT_DIR))


if __name__ == "__main__":
    from scripts.build import app, load_categories

    app.config["FREEZER_RELATIVE_URLS"] = True
    app.config["FREEZER_DESTINATION"] = str(BUILD_DIR)

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    # Create freezer and register URL generators
    freezer = Freezer(app)

    @freezer.register_generator
    def explorer():
        """Generate URLs for all explorer pages"""
        categories = load_categories()
        for category in categories:
            yield {"category": category["name"]}

    # Freeze the app
    freezer.freeze()

    # Fix the generated files by adding .html extensions
    explorer_dir = BUILD_DIR / "explorer"
    if explorer_dir.exists():
        for file_path in explorer_dir.iterdir():
            if file_path.is_file() and not file_path.name.endswith(".html"):
                # Rename file to add .html extension
                new_path = file_path.with_suffix(".html")
                file_path.rename(new_path)
                print(f"Renamed {file_path.name} to {new_path.name}")

    print("Website built successfully on local device.")

    # push the modifications online if the user wants to
    git_push = input("Do you want to git push the modifications online? [y/N]: ")
    if git_push.strip().lower().startswith("y"):
        try:
            subprocess.run(["git", "add", str(BUILD_DIR)], check=True, cwd=ROOT_DIR)
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user = os.getenv("USER", "unknown user")
            commit_msg = f"update static website by {user} at {current_date}"
            subprocess.run(
                ["git", "commit", "-m", commit_msg], check=True, cwd=ROOT_DIR
            )
            subprocess.run(["git", "push"], check=True, cwd=ROOT_DIR)
            print("Modifications have been pushed to the git repository.")
        except subprocess.CalledProcessError as e:
            print("An error occurred while pushing to git:", e)

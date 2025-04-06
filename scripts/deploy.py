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
    from scripts.build import app

    app.config["FREEZER_RELATIVE_URLS"] = True
    app.config["FREEZER_DESTINATION"] = str(BUILD_DIR)
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    Freezer(app).freeze()
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

import os
import shutil
import subprocess
from datetime import datetime

from flask_frozen import Freezer

from app import app

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()

    build_dir = "build"
    docs_dir = "docs"

    # flask built the website in the build folder,
    # but GitHub Pages reads it from docs, hence the following renaming
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.rename(build_dir, docs_dir)
    print("Website built successfully on local device.")

    # push the modifications online if the user wants to
    git_push = input("Do you want to git push the modifications online? [y/N]: ")
    if git_push.strip().lower().startswith("y"):
        try:
            subprocess.run(["git", "add", docs_dir], check=True)
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_msg = os.path.expandvars(
                f"update static website by $USER at {current_date}"
            )
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            subprocess.run(["git", "push"], check=True)
            print("Modifications have been pushed to the git repository.")
        except subprocess.CalledProcessError as e:
            print("An error occurred while pushing to git:", e)

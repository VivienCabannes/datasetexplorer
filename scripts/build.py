from pathlib import Path
import json
from flask import Flask, render_template

ROOT_DIR = Path(__file__).parent.parent.resolve()

app = Flask(
    __name__,
    template_folder=str(ROOT_DIR / "templates"),
    static_folder=str(ROOT_DIR / "static"),
    static_url_path="/static",
)


def load_datasets():
    datasets_path = ROOT_DIR / "datasets"
    all_data = []
    for path in datasets_path.glob("*.json"):
        with open(path) as f:
            all_data.append(json.load(f))
    return all_data


def load_tags():
    tags_path = ROOT_DIR / "tags.json"
    with open(tags_path, "r") as f:
        return json.load(f)


@app.route("/")
def index():
    datasets = load_datasets()
    tags = load_tags()
    return render_template("index.html", datasets=datasets, tags=tags)


if __name__ == "__main__":
    app.run(debug=True)

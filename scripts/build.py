from pathlib import Path
import json
from flask import Flask, render_template


ROOT_DIR = Path(__file__).parent.parent.resolve()
DATA_DIR = ROOT_DIR / "datasets"

app = Flask(
    __name__,
    template_folder=str(ROOT_DIR / "templates"),
    static_folder=str(ROOT_DIR / "static"),
    static_url_path="/static",
)


def load_datasets():
    all_data = []
    for path in DATA_DIR.glob("*.json"):
        with open(path) as f:
            all_data.append(json.load(f))
    return all_data


def load_tags():
    tags_path = DATA_DIR / "tags.jsonl"
    with open(tags_path, "r") as f:
        return json.load(f)


@app.route("/")
def index():
    tags = load_tags()
    datasets = load_datasets()
    return render_template("index.html", tags=tags, datasets=datasets)


if __name__ == "__main__":
    app.run(debug=True)

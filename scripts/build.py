from pathlib import Path
import json
from flask import Flask, render_template, abort

ROOT_DIR = Path(__file__).parent.parent.resolve()
ASSETS_DIR = ROOT_DIR / "assets"
TEMPLATE_DIR = ROOT_DIR / "templates"

app = Flask(
    __name__,
    template_folder=str(TEMPLATE_DIR),
    static_folder=str(ROOT_DIR / "static"),
    static_url_path="/static",
)


def load_category_info(explorer_name: str):
    """Load category info including attribute configuration"""
    info_path = ASSETS_DIR / explorer_name / "info.jsonl"
    if info_path.exists():
        with open(info_path) as f:
            return json.load(f)
    return {}


def load_tags(explorer_name: str):
    tags_path = ASSETS_DIR / explorer_name / "tags.jsonl"
    with open(tags_path, "r") as f:
        return json.load(f)


def load_datasets_for(explorer_name: str):
    data_dir = ASSETS_DIR / explorer_name
    if not data_dir.exists() or not data_dir.is_dir():
        abort(404)
    all_data = []
    for path in data_dir.glob("*.json"):
        # All .json files in this directory are dataset files
        with open(path) as f:
            all_data.append(json.load(f))
    return all_data


def load_categories():
    """Load all categories with their info.jsonl metadata"""
    categories = []
    for category_dir in ASSETS_DIR.iterdir():
        if category_dir.is_dir():
            info_path = category_dir / "info.jsonl"
            if info_path.exists():
                with open(info_path) as f:
                    info = json.load(f)
                    categories.append(
                        {
                            "name": category_dir.name,
                            "title": info.get("title", category_dir.name),
                            "description": info.get("description", ""),
                        }
                    )
    return categories


@app.route("/")
def index():
    categories = load_categories()
    return render_template("index.html", categories=categories)


@app.route("/explorer/<category>")
@app.route("/explorer/<category>.html")
def explorer(category):
    # Remove .html extension if present (for static file compatibility)
    if category.endswith(".html"):
        category = category[:-5]

    # category will be one of: reasoning-datasets, lean-datasets, reasoning-papers, lean-papers
    tags = load_tags(category)
    assets = load_datasets_for(category)
    category_info = load_category_info(category)
    # Pass along the category so you could e.g. show a header
    return render_template(
        "explorer.html", tags=tags, assets=assets, category_info=category_info
    )


if __name__ == "__main__":
    app.run(debug=True)

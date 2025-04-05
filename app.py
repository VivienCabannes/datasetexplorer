import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)


def load_datasets():
    all_data = []
    for path in Path("datasets/").glob("*.json"):
        with open(path) as f:
            all_data.append(json.load(f))
    return all_data


@app.route("/")
def index():
    datasets = load_datasets()
    return render_template("index.html", datasets=datasets)


if __name__ == "__main__":
    app.run(debug=True)

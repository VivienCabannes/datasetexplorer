from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample dataset list
datasets = [
    {"name": "Dataset A", "tags": ["finance", "2020"]},
    {"name": "Dataset B", "tags": ["health", "2021"]},
    {"name": "Dataset C", "tags": ["finance", "health", "2020"]},
    {"name": "Dataset D", "tags": ["education", "2021"]}
]

@app.route("/")
def index():
    # Render the HTML page (ensure index.html is in a folder named "templates")
    return render_template("index.html")

@app.route("/api/datasets")
def get_datasets():
    # Return the datasets as JSON
    return jsonify(datasets)

if __name__ == '__main__':
    app.run(debug=True)


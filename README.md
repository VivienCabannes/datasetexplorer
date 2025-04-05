# Static Dataset Explorer Website

This project creates a dataset explorer with minimal information per dataset on the front page.
Users can click on a dataset card to expand and view full details. 
The data (datasets and tags) are loaded from JSON files and rendered via a Flask app. 
We then use Frozen-Flask to generate a static version of the site that can be hosted on GitHub Pages.

## Installation

Clone the repository, create a virtual environment and install dependencies:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate
pip install -r flask frozen-flask
```

## Build & Deploy

Simply run the build script. You will need to have git working with access right to the repository to be able to modify the online website.

```bash
python build.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
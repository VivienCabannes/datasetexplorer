# Static Dataset Explorer Website

This repository contains a Flask application for exploring datasets.
The website is built using Flask and then "frozen" into a static site using [Frozen-Flask](https://github.com/Frozen-Flask/Frozen-Flask).
 The resulting static site is deployed through GitHub Pages.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Freezing the Flask App](#freezing-the-flask-app)
- [Deploying to GitHub Pages](#deploying-to-github-pages)
- [Updating the Site](#updating-the-site)
- [License](#license)

## Overview

This project creates a dataset explorer with minimal information per dataset on the front page. Users can click on a dataset card to expand and view full details. The data (datasets and tags) are loaded from JSON files and rendered via a Flask app. We then use Frozen-Flask to generate a static version of the site that can be hosted on GitHub Pages.

## Installation

Clone the repository, create a virtual environment and install dependencies:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate
pip install -r flask frozen-flask
```

## Freezing the Flask App

We use Frozen-Flask to convert the dynamic Flask application into a set of static HTML files.
Run the Freezing Script:

```bash
python static_generation.py
```

This command will generate a folder (by default named `build`) containing your static site files.

## Deploying to GitHub Pages

You have two main options for deploying your static site on GitHub Pages:

### Option 1: Deploy from the `gh-pages` Branch

1. **Create and Switch to the `gh-pages` Branch:**

```bash
git checkout --orphan gh-pages
```

2. **Remove All Files and Copy the Static Files:**

You can either remove all files except the `build` folder or copy the contents of the `build` folder to the root of the `gh-pages` branch:

```bash
rm -rf *
cp -r build/* .
```

3. **Commit and Push to GitHub:**

```bash
git add .
git commit -m "Deploy static site to GitHub Pages"
git push origin gh-pages --force
```

4. **Configure GitHub Pages:**

Go to your repository settings on GitHub, scroll to the "GitHub Pages" section, and set the source to the `gh-pages` branch. Your site will be available at:

```
https://yourusername.github.io/your-repo/
```

### Option 2: Deploy from the `docs/` Folder on the Main Branch

1. **Copy the Static Files to a `docs/` Folder:**

```bash
mkdir docs
cp -r build/* docs/
```

2. **Commit and Push to GitHub:**

```bash
git add docs
git commit -m "Deploy static site to docs folder"
git push origin main
```

3. **Configure GitHub Pages:**

In your repository settings on GitHub, set the GitHub Pages source to the `main` branch and the `/docs` folder. Your site will be available at:

```
https://yourusername.github.io/your-repo/
```

## Updating the Site

Whenever you update your Flask app, follow these steps:

1. Make changes in your Flask application and commit them to your repository.
2. Re-run `python freeze.py` to regenerate the static site in the `build` folder.
3. Deploy the updated static files to your chosen GitHub Pages branch or folder as described above.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
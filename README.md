# Static Dataset Explorer Website

This repository codes a dataset explorer.
A list with minimal information per dataset is rendered on the front page.
A tag system allows to filter it.
Users can click on a dataset card to expand and view full details. 
The data (datasets and tags) are loaded from JSON files and rendered via a Flask app. 
We use Frozen-Flask to generate a static version of the site that is [hosted on GitHub Pages](https://viviencabannes.github.io/datasetexplorer/)

### Installation

Clone the repository, create a virtual environment and install dependencies:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate
pip install flask frozen-flask
```

### Test Locally

To develop and test the Flask application on your local machine, start the application by running

```bash
python app.py
```

Once the app is running, open your web browser and navigate to [http://localhost:5000](http://localhost:5000).
You should see the Dataset Explorer website.
As you modify the codebase, you can simply refresh your browser to see your changes immediately.

### Build & Deploy

Simply run the build script. You will need to have git working with access right to the repository to be able to modify the online website.

```bash
python build.py
```

## Scripts

This repository includes several utility scripts to help manage and update your datasets and tags.
These scripts automate common tasks such as verifying tag usage and batch updating dataset files.

### Check Tags

The `check_tags.py` script examines all JSON files in the `datasets/` folder to extract tags used by each dataset (using the dataset filename without the `.json` extension) and compares them with the tags defined in `tags.json`. The script will report:
- Any datasets that use tags not defined in `tags.json`.
- Any tags defined in `tags.json` that are never used in any dataset.

You can run the script with:

```bash
python scripts/check_tags.py
```

### Add Tags

The `add_tags.py` script allows you to batch update the tags of your datasets. It takes as input a JSON file that maps new tag names to lists of dataset names, and then updates each corresponding dataset JSON file (located in the `datasets/` folder) by adding the new tag if it's not already present.

The input JSON file should have the following structure:

```json
{
    "new_tag1": ["dataset1", "dataset2"],
    "new_tag2": ["dataset1", "dataset3"]
}
```

Here, each dataset name corresponds to a file in the `datasets/` folder (e.g. `dataset1.json`). The script will update these files by adding the new tag to the `"tags"` field.

Run the script from the command line as follows:

```bash
python add_tags.py path/to/your_mapping.json
```

This will update the dataset files with the new tags as specified in the mapping file.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

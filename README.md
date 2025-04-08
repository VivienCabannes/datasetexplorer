# Static Dataset Explorer Website

This repository implements a dataset explorer.
A list displaying minimal information for each dataset is shown on the front page.
Users can filter datasets using a tagging system.
Clicking on a dataset card expands it to display full details.
The data (datasets and tags) are loaded from JSON files and rendered through a Flask application. 
Frozen-Flask is used to generate a static version of the site, which is [hosted on GitHub Pages](https://viviencabannes.github.io/datasetexplorer/).

### Installation

Clone the repository, create a virtual environment and install dependencies:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate
pip install flask frozen-flask
```

### Build Locally

To build and run the website on your local machine, run the build script.
It will launch the Flask application.

```bash
python scripts/build.py
```

Once the app is running, open your web browser and navigate to [http://localhost:5000](http://localhost:5000).
You should see the Dataset Explorer website.
As you modify the codebase, refresh your browser to immediately view your updates.

### Deploy Remotely

To deploy the website remotely, run the deploy script.
It will creates a static website that you can view locally by opening `/<path-to-repo>/docs/index.html` in your web browser.
It will also prompt you to optionally push your changes to GitHub, which will automatically update the online website. Ensure your git environment is properly configured, and you have sufficient write permissions to the repository to perform this action.

```bash
python scripts/deploy.py
```

## Improvements

Some cards display a warning sign️, indicating information gathered from a quick internet search without deep verification.
Feel free to verify the cards and remove the warning sign as you go (edit the datasets/`<card>`.json).

Many datasets are not listed in the explorer, feel free to add datasets that are missing (add a datasets/`<card_name>`.json) or, at least, to report omission in `datasets/missing.txt`.

## Editor tools

This repository includes several utility scripts to help manage and update your datasets and tags.
These scripts automate common tasks such as verifying tag usage and batch updating dataset files.

### Check Tags

The `check_tags.py` script examines all JSON files in the `datasets/` folder to extract tags used by each dataset (using the dataset filename without the `.json` extension) and compares them with the tags defined in `datasets/tags.jsonl`. The script will report:
- Any datasets that use tags not defined in `tags.jsonl`.
- Any tags defined in `tags.jsonl` that are never used in any dataset.

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

## Potential features

- We may want to filter out datasets that have a certain tag. We could image doing "shift+click" to filter out a tag (which would appear red-ish on the screen).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

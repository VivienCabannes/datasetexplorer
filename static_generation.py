from flask_frozen import Freezer

from app import app  # Make sure your Flask app is imported correctly

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()

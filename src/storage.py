import os
import json
from src.constants import RATINGS_FILE

def load_ratings(file_path=RATINGS_FILE):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_ratings(data, file_path=RATINGS_FILE):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

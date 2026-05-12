import json
import os

FILE_NAME = "records.json"


def save_records(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)


def load_records():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)
"""File storage logic for record data."""

import json
from pathlib import Path


def load_records(file_path: str | Path) -> list[dict]:
    """Load records from a JSON file."""
    path = Path(file_path)

    # Missing file means no saved records yet
    if not path.exists():
        return []

    # Catch JSONDecodeError in the case of invalid JSON file
    try:
        with path.open(encoding="utf-8") as file:
         records = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError("Records file contains invalid JSON") from error

    # Validate expected structure
    if not isinstance(records, list):
        raise ValueError("Records file must contain a list")

    return records


def save_records(records: list[dict], file_path: str | Path) -> None:
    """Save records to a JSON file."""
    if not isinstance(records,list):
        raise ValueError("Records must be a list")

    path = Path(file_path)

    # Create parent directories if they do not exist
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

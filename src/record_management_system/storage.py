"""File storage logic for record data."""

import json
from pathlib import Path

from record_management_system.validation import validate_records_collection


def load_records(file_path: str | Path) -> list[dict]:
    """Load records from a JSON file."""
    path = Path(file_path)

    if not path.exists():
        return []

    try:
        with path.open(encoding="utf-8") as file:
            records = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError("Records file contains invalid JSON") from error

    return validate_records_collection(records)


def save_records(records: list[dict], file_path: str | Path) -> None:
    """Save records to a JSON file."""
    if not isinstance(records, list):
        raise ValueError("Records must be a list")

    validate_records_collection(records)
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

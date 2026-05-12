"""Unit tests for file storage logic."""

import json

import pytest

from record_management_system.storage import load_records, save_records


def test_save_records_writes_records_to_file(tmp_path):
    """Save records to a JSON file."""
    file_path = tmp_path / "records.json"
    records = [
        {"id": 1, "type": "client", "name": "John Smith"},
    ]

    save_records(records, file_path)

    assert file_path.exists()


def test_load_records_returns_saved_records(tmp_path):
    """Load saved records from a JSON file."""
    file_path = tmp_path / "records.json"
    records = [
        {"id": 1, "type": "client", "name": "John Smith"},
    ]

    save_records(records, file_path)
    loaded_records = load_records(file_path)

    assert loaded_records == records


def test_load_records_returns_empty_list_when_file_missing(tmp_path):
    """Return an empty list when the records file does not exist."""
    file_path = tmp_path / "missing_records.json"

    result = load_records(file_path)

    assert result == []


def test_save_records_creates_parent_directory(tmp_path):
    """Create the parent directory when saving records."""
    file_path = tmp_path / "data" / "records.json"
    records = [
        {"id": 1, "type": "client", "name": "John Smith"},
    ]

    save_records(records, file_path)

    assert file_path.exists()


def test_load_records_raises_error_when_json_is_not_a_list(tmp_path):
    """Raise an error when the JSON file does not contain a list."""
    file_path = tmp_path / "records.json"

    with file_path.open("w", encoding="utf-8") as file:
        json.dump({"id": 1, "type": "client"}, file)

    with pytest.raises(ValueError, match="Records file must contain a list"):
        load_records(file_path)

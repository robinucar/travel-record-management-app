"""Unit tests for file storage logic."""

import json

import pytest

from record_management_system.storage import load_records, save_records
from tests.factories import make_client_record


def test_save_records_writes_records_to_file(tmp_path):
    """Save records to a JSON file."""
    file_path = tmp_path / "records.json"
    records = [make_client_record()]

    save_records(records, file_path)

    assert file_path.exists()

    with file_path.open(encoding="utf-8") as file:
        saved_records = json.load(file)

    assert saved_records == records


def test_load_records_returns_saved_records(tmp_path):
    """Load saved records from a JSON file."""
    file_path = tmp_path / "records.json"
    records = [make_client_record()]

    save_records(records, file_path)
    loaded_records = load_records(file_path)

    assert loaded_records == records


def test_load_records_returns_empty_list_when_file_missing(tmp_path):
    """Return an empty list when the records file does not exist."""
    file_path = tmp_path / "missing_records.json"

    result = load_records(file_path)

    assert result == []


def test_load_records_uses_seed_file_when_primary_file_is_missing(tmp_path):
    """Load seed records when the primary records file does not exist."""
    file_path = tmp_path / "records.json"
    seed_file_path = tmp_path / "seed_records.json"
    seed_records = [make_client_record()]

    with seed_file_path.open("w", encoding="utf-8") as file:
        json.dump(seed_records, file)

    result = load_records(file_path, seed_file_path)

    assert result == seed_records


def test_save_records_creates_parent_directory(tmp_path):
    """Create the parent directory when saving records."""
    file_path = tmp_path / "data" / "records.json"
    records = [make_client_record()]

    save_records(records, file_path)

    assert file_path.exists()


def test_load_records_raises_error_when_json_is_not_a_list(tmp_path):
    """Raise an error when the JSON file does not contain a list."""
    file_path = tmp_path / "records.json"

    with file_path.open("w", encoding="utf-8") as file:
        json.dump({"id": 1, "type": "client"}, file)

    with pytest.raises(ValueError, match="Records file must contain a list"):
        load_records(file_path)


def test_load_records_raises_error_when_record_data_is_invalid(tmp_path):
    """Raise an error when a loaded record violates shared validation rules."""
    file_path = tmp_path / "records.json"
    invalid_records = [make_client_record(phone_number="07ABC")]

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(invalid_records, file)

    with pytest.raises(ValueError, match="Phone number must contain only digits"):
        load_records(file_path)


def test_save_records_raises_error_when_records_have_duplicate_ids(tmp_path):
    """Raise an error when trying to save records with duplicate IDs."""
    file_path = tmp_path / "records.json"
    records = [
        make_client_record(),
        make_client_record(name="Jane Smith"),
    ]

    with pytest.raises(ValueError, match="Record with this ID already exists"):
        save_records(records, file_path)


def test_save_records_raises_error_when_records_is_not_a_list(tmp_path):
    """Raise an error when saving data that is not a list."""
    file_path = tmp_path / "records.json"

    with pytest.raises(ValueError, match="Records must be a list"):
        save_records({"id": 1, "type": "client"}, file_path)

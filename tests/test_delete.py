"""Unit tests for delete record logic."""

import pytest

from record_management_system.records import delete_record


def test_delete_record_removes_existing_record():
    """Delete an existing record from the records list."""
    records = [
        {"id": 1, "type": "client", "name": "John Smith"},
        {"id": 2, "type": "airline", "company_name": "British Airways"},
    ]

    deleted_record = delete_record(records, 1)

    assert deleted_record == {
        "id": 1,
        "type": "client",
        "name": "John Smith",
    }

    assert records == [
        {
            "id": 2,
            "type": "airline",
            "company_name": "British Airways",
        }
    ]


def test_delete_record_raises_error_when_record_not_found():
    """Raise an error when trying to delete a non-existing record."""
    records = [
        {"id": 1, "type": "client", "name": "John Smith"},
    ]

    with pytest.raises(ValueError, match="Record not found"):
        delete_record(records, 22)

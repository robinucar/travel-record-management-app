"""Record management logic."""

from record_management_system.schema import (
    ALLOWED_SEARCH_FIELDS,
    EXACT_MATCH_FIELDS,
)
from record_management_system.validation import (
    validate_new_record,
    validate_updated_record,
)


def create_record(records: list[dict], record: dict) -> dict:
    """Add a new record to the records list and return it."""
    validate_new_record(records, record)
    records.append(record)
    return record


def get_records(records: list[dict]) -> list[dict]:
    """Return a copy of all records."""
    return records.copy()


def search_records(
    records: list[dict],
    field: str,
    value: object,
) -> list[dict]:
    """Search records by an allowed field and value."""
    if field not in ALLOWED_SEARCH_FIELDS:
        raise ValueError("Invalid search field")

    if not str(value).strip():
        raise ValueError("Search value cannot be empty")

    search_value = str(value).lower().strip()
    matching_records = []

    for record in records:
        record_value = str(record.get(field, "")).lower().strip()

        if field in EXACT_MATCH_FIELDS:
            is_match = record_value == search_value
        else:
            is_match = search_value in record_value

        if is_match:
            matching_records.append(record.copy())

    return matching_records


def update_record(
    records: list[dict],
    record_id: int,
    updated_fields: dict,
) -> dict:
    """Update an existing record by ID and return a copy of the updated record."""
    for record in records:
        if record["id"] == record_id:
            updated_record = validate_updated_record(record, updated_fields)
            record.update(updated_fields)
            return updated_record

    raise ValueError("Record not found")


def delete_record(records: list[dict], record_id: int) -> dict:
    """Delete a record by ID and return the deleted record."""
    if not records:
        raise ValueError("Records are empty, none to delete")

    for index, record in enumerate(records):
        if record.get("id") == record_id:
            return records.pop(index)

    raise ValueError("Record not found")

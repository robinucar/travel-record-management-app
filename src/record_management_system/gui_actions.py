"""Backend-facing GUI actions that remain independent of Tk widgets."""

from pathlib import Path

from record_management_system.gui_helpers import (
    build_record_from_field_values,
    build_updated_fields_from_values,
)
from record_management_system.records import (
    create_record,
    delete_record,
    get_records,
    search_records,
    update_record,
)
from record_management_system.storage import load_records, save_records


def load_records_from_file(
    file_path: str | Path,
    fallback_file_path: str | Path | None = None,
) -> list[dict]:
    """Load records for the GUI from the configured data file."""
    return load_records(file_path, fallback_file_path)


def save_records_to_file(records: list[dict], file_path: str | Path) -> None:
    """Persist records using the configured data file."""
    save_records(records, file_path)


def get_records_for_display(records: list[dict]) -> list[dict]:
    """Return a copy of the current records for the GUI list state."""
    return get_records(records)


def create_record_from_values(
    records: list[dict],
    record_type: str,
    field_values: dict[str, str],
) -> dict:
    """Create a record from GUI field values."""
    record = build_record_from_field_values(record_type, field_values)
    return create_record(records, record)


def search_records_by_field(
    records: list[dict],
    field: str,
    value: str,
) -> list[dict]:
    """Search records using GUI input values."""
    return search_records(records, field, value.strip())


def update_record_from_values(
    records: list[dict],
    record_id: int,
    field_values: dict[str, str],
) -> dict:
    """Update a record from GUI field values."""
    updated_fields = build_updated_fields_from_values(field_values)
    return update_record(records, record_id, updated_fields)


def delete_record_by_id(records: list[dict], record_id: int) -> dict:
    """Delete a record by ID from the GUI."""
    return delete_record(records, record_id)

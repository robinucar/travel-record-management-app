"""Shared validation helpers for record and storage operations."""

import re
from collections.abc import Mapping
from datetime import datetime

from record_management_system.schema import (
    ALLOWED_FIELDS_BY_RECORD_TYPE,
    REQUIRED_FIELDS_BY_RECORD_TYPE,
    VALID_RECORD_TYPES,
)

PHONE_NUMBER_PATTERN = re.compile(r"^(?:\+\d+|00\d+|\d+)$")
DATE_FORMAT = "%Y-%m-%d"


def validate_record_data(record: Mapping[str, object]) -> None:
    """Validate a single record against the shared schema rules."""
    if not isinstance(record, dict):
        raise ValueError("Each record must be a dictionary")

    record_type = validate_record_type(record)
    validate_allowed_fields(record, record_type)
    validate_required_fields(record, record_type)
    validate_record_formats(record, record_type)


def validate_new_record(records: list[dict], record: dict) -> None:
    """Validate a new record before adding it to the records list."""
    validate_record_data(record)
    ensure_unique_id(records, record["id"])


def validate_updated_record(existing_record: dict, updated_fields: dict) -> dict:
    """Validate an update payload and return the merged record."""
    if not updated_fields:
        raise ValueError("No fields provided to update")

    if "id" in updated_fields:
        raise ValueError("Record ID cannot be updated")

    if "type" in updated_fields:
        raise ValueError("Record type cannot be updated")

    record_type = existing_record["type"]
    allowed_fields = ALLOWED_FIELDS_BY_RECORD_TYPE[record_type]
    invalid_fields = set(updated_fields) - allowed_fields

    if invalid_fields:
        invalid_field = sorted(invalid_fields)[0]
        raise ValueError(f"Invalid field for {record_type} record: {invalid_field}")

    updated_record = existing_record.copy()
    updated_record.update(updated_fields)
    validate_record_data(updated_record)
    return updated_record


def validate_records_collection(records: object) -> list[dict]:
    """Validate a records collection loaded from storage."""
    if not isinstance(records, list):
        raise ValueError("Records file must contain a list")

    seen_ids: set[int] = set()

    for record in records:
        validate_record_data(record)
        record_id = record["id"]

        if record_id in seen_ids:
            raise ValueError("Record with this ID already exists")

        seen_ids.add(record_id)

    return records


def validate_record_type(record: Mapping[str, object]) -> str:
    """Validate the record type and return the normalized value."""
    record_type = record.get("type")

    if record_type not in VALID_RECORD_TYPES:
        raise ValueError("Invalid record type")

    return str(record_type)


def validate_allowed_fields(record: Mapping[str, object], record_type: str) -> None:
    """Validate that a record only contains fields allowed for its type."""
    allowed_fields = ALLOWED_FIELDS_BY_RECORD_TYPE[record_type]
    invalid_fields = set(record) - allowed_fields

    if invalid_fields:
        invalid_field = sorted(invalid_fields)[0]
        raise ValueError(f"Invalid field for {record_type} record: {invalid_field}")


def validate_required_fields(record: Mapping[str, object], record_type: str) -> None:
    """Validate that all required fields are present and non-empty."""
    required_fields = REQUIRED_FIELDS_BY_RECORD_TYPE[record_type]

    for field in required_fields:
        if field not in record or not str(record[field]).strip():
            raise ValueError(f"Missing required field: {field}")


def validate_record_formats(record: Mapping[str, object], record_type: str) -> None:
    """Validate supported field formats for a record."""
    if record_type == "client":
        validate_phone_number(record["phone_number"])

    if record_type == "flight":
        validate_date(record["date"])


def validate_phone_number(phone_number: object) -> None:
    """Validate that phone number contains digits or a valid prefix."""
    phone_number_value = str(phone_number).strip()

    if not PHONE_NUMBER_PATTERN.fullmatch(phone_number_value):
        raise ValueError("Phone number must contain only digits, or start with + or 00")


def validate_date(date_value: object) -> None:
    """Validate that date uses YYYY-MM-DD format."""
    try:
        datetime.strptime(str(date_value).strip(), DATE_FORMAT)
    except ValueError as error:
        raise ValueError("Date must use YYYY-MM-DD format") from error


def ensure_unique_id(records: list[dict], record_id: int) -> None:
    """Ensure that the record ID is unique."""
    for existing_record in records:
        if existing_record["id"] == record_id:
            raise ValueError("Record with this ID already exists")

"""Record management logic."""

import re
from datetime import datetime

VALID_RECORD_TYPES = {"client", "airline", "flight"}

PHONE_NUMBER_PATTERN = re.compile(r"^(?:\+\d+|00\d+|\d+)$")
DATE_FORMAT = "%Y-%m-%d"

ALLOWED_FIELDS_BY_RECORD_TYPE = {
    "client": {
        "id",
        "type",
        "name",
        "address_line_1",
        "address_line_2",
        "address_line_3",
        "city",
        "state",
        "zip_code",
        "country",
        "phone_number",
    },
    "airline": {
        "id",
        "type",
        "company_name",
    },
    "flight": {
        "id",
        "type",
        "client_id",
        "airline_id",
        "date",
        "start_city",
        "end_city",
    },
}

REQUIRED_FIELDS_BY_RECORD_TYPE = {
    "client": {
        "id",
        "type",
        "name",
        "address_line_1",
        "city",
        "zip_code",
        "country",
        "phone_number",
    },
    "airline": {
        "id",
        "type",
        "company_name",
    },
    "flight": {
        "id",
        "type",
        "client_id",
        "airline_id",
        "date",
        "start_city",
        "end_city",
    },
}

ALLOWED_SEARCH_FIELDS = {
    "id",
    "type",
    "name",
    "company_name",
    "client_id",
    "airline_id",
    "date",
    "start_city",
    "end_city",
    "city",
    "country",
    "phone_number",
    "address_line_1",
    "address_line_2",
    "address_line_3",
    "state",
    "zip_code",
}


def create_record(records: list[dict], record: dict) -> dict:
    """Add a new record to the records list and return it."""

    record_type = record.get("type")

    if record_type not in VALID_RECORD_TYPES:
        raise ValueError("Invalid record type")

    validate_required_fields(record)
    validate_record_formats(record)
    ensure_unique_id(records, record["id"])

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

        if record_value == search_value:
            matching_records.append(record.copy())

    return matching_records


def update_record(
    records: list[dict],
    record_id: int,
    updated_fields: dict,
) -> dict:
    """Update an existing record by ID and return a copy of the updated record."""

    if not updated_fields:
        raise ValueError("No fields provided to update")

    if "id" in updated_fields:
        raise ValueError("Record ID cannot be updated")

    if "type" in updated_fields:
        raise ValueError("Record type cannot be updated")

    for record in records:
        if record["id"] == record_id:
            record_type = record["type"]
            allowed_fields = ALLOWED_FIELDS_BY_RECORD_TYPE[record_type]
            invalid_fields = set(updated_fields) - allowed_fields

            if invalid_fields:
                invalid_field = sorted(invalid_fields)[0]
                raise ValueError(
                    f"Invalid field for {record_type} record: {invalid_field}"
                )

            updated_record = record.copy()
            updated_record.update(updated_fields)

            validate_required_fields(updated_record)

            record.update(updated_fields)
            return record.copy()

    raise ValueError("Record not found")


def validate_required_fields(record: dict) -> None:
    """Validate required fields for the record type."""

    record_type = record["type"]
    required_fields = REQUIRED_FIELDS_BY_RECORD_TYPE[record_type]

    for field in required_fields:
        if field not in record or not str(record[field]).strip():
            raise ValueError(f"Missing required field: {field}")


def validate_record_formats(record: dict) -> None:
    """Validate field formats for supported record types."""

    if record["type"] == "client":
        validate_phone_number(record["phone_number"])

    if record["type"] == "flight":
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


def delete_record(records: list[dict], record_id: int) -> dict:
    """Delete a record by ID and return the deleted record."""
    if not records:
        raise ValueError("Records are empty, none to delete")

    for index, record in enumerate(records):
        if record.get("id") == record_id:
            return records.pop(index)

    raise ValueError("Record not found")

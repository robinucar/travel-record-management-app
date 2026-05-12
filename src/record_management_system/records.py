"""Record management logic."""

VALID_RECORD_TYPES = {"client", "airline", "flight"}

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


def create_record(records: list[dict], record: dict) -> dict:
    """Add a new record to the records list and return it."""
    record_type = record.get("type")

    if record_type not in VALID_RECORD_TYPES:
        raise ValueError("Invalid record type")

    validate_required_fields(record)
    ensure_unique_id(records, record["id"])

    records.append(record)
    return record


def get_records(records: list[dict]) -> list[dict]:
    """Return a copy of all records."""
    return records.copy()


def validate_required_fields(record: dict) -> None:
    """Validate required fields for the record type."""
    record_type = record["type"]
    required_fields = REQUIRED_FIELDS_BY_RECORD_TYPE[record_type]

    for field in required_fields:
        if field not in record or record[field] == "":
            raise ValueError(f"Missing required field: {field}")


def ensure_unique_id(records: list[dict], record_id: int) -> None:
    """Ensure that the record ID is unique."""
    for existing_record in records:
        if existing_record["id"] == record_id:
            raise ValueError("Record with this ID already exists")

def delete_record(records: list[dict], record_id: int) -> dict:
    """Delete a record by ID and return the deleted record."""
    for index, record in enumerate(records):
        if record.get("id") == record_id:
            return records.pop(index)

    raise ValueError("Record not found")

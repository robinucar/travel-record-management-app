"""Pure helper functions shared by the GUI layer."""

from record_management_system.schema import (
    DISPLAY_FIELDS_BY_RECORD_TYPE,
    FIELD_LABELS,
    INTEGER_FIELDS,
    RECORD_SCHEMAS,
    REQUIRED_FIELDS_BY_RECORD_TYPE,
)


def format_record_for_display(record: dict) -> str:
    """Format a record for display in the records list."""
    record_type = record["type"]
    schema = RECORD_SCHEMAS[record_type]
    display_fields = DISPLAY_FIELDS_BY_RECORD_TYPE[record_type]
    required_fields = REQUIRED_FIELDS_BY_RECORD_TYPE[record_type]
    display_parts = [schema.display_name]

    for field_name in display_fields:
        value = record.get(field_name, "")

        if field_name in required_fields or str(value).strip():
            label = FIELD_LABELS[field_name]
            display_parts.append(f"{label}: {value}")

    return " | ".join(display_parts)


def convert_form_value(field_name: str, value: str) -> int | str:
    """Convert form input values to the correct data type."""
    stripped_value = value.strip()

    if field_name in INTEGER_FIELDS:
        return int(stripped_value)

    return stripped_value


def build_record_from_field_values(
    record_type: str,
    field_values: dict[str, str],
) -> dict[str, int | str]:
    """Build a new record from GUI field values."""
    record: dict[str, int | str] = {"type": record_type}

    for field_name, value in field_values.items():
        record[field_name] = convert_form_value(field_name, value)

    return record


def build_updated_fields_from_values(field_values: dict[str, str]) -> dict:
    """Build update fields from GUI form values, excluding the record ID."""
    updated_fields = {}

    for field_name, value in field_values.items():
        if field_name == "id":
            continue

        updated_fields[field_name] = convert_form_value(field_name, value)

    return updated_fields

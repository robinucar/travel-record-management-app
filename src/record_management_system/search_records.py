"""Search record logic."""

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


def search_records(
    records: list[dict],
    field: str,
    value: str,
) -> list[dict]:
    """Search records by an allowed field and value."""

    # Prevent invalid or empty search input
    if field not in ALLOWED_SEARCH_FIELDS or not str(value).strip():
        return []

    # Normalise search value for consistent comparison
    search_value = str(value).lower().strip()

    # Store matching records
    matching_records = []

    for record in records:
        record_value = str(record.get(field, "")).lower().strip()

        if record_value == search_value:
            matching_records.append(record)

    return matching_records

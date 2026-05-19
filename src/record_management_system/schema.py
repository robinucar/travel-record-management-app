"""Central schema definitions for supported record types."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RecordSchema:
    """Describe the fields and display metadata for a record type."""

    record_type: str
    display_name: str
    fields: tuple[str, ...]
    required_fields: frozenset[str]

    @property
    def allowed_fields(self) -> frozenset[str]:
        """Return the fields that may appear on this record type."""
        return frozenset(("type", *self.fields))

    @property
    def required_fields_with_type(self) -> frozenset[str]:
        """Return required fields including the record type discriminator."""
        return frozenset(("type", *self.required_fields))


FIELD_LABELS = {
    "id": "ID",
    "type": "Type",
    "name": "Name",
    "address_line_1": "Address Line 1",
    "address_line_2": "Address Line 2",
    "address_line_3": "Address Line 3",
    "city": "City",
    "state": "State",
    "zip_code": "Zip Code",
    "country": "Country",
    "phone_number": "Phone Number",
    "company_name": "Company Name",
    "client_id": "Client ID",
    "airline_id": "Airline ID",
    "date": "Date",
    "start_city": "Start City",
    "end_city": "End City",
}

RECORD_SCHEMAS = {
    "client": RecordSchema(
        record_type="client",
        display_name="Client",
        fields=(
            "id",
            "name",
            "address_line_1",
            "address_line_2",
            "address_line_3",
            "city",
            "state",
            "zip_code",
            "country",
            "phone_number",
        ),
        required_fields=frozenset(
            {
                "id",
                "name",
                "address_line_1",
                "city",
                "zip_code",
                "country",
                "phone_number",
            }
        ),
    ),
    "airline": RecordSchema(
        record_type="airline",
        display_name="Airline",
        fields=(
            "id",
            "company_name",
        ),
        required_fields=frozenset(
            {
                "id",
                "company_name",
            }
        ),
    ),
    "flight": RecordSchema(
        record_type="flight",
        display_name="Flight",
        fields=(
            "id",
            "client_id",
            "airline_id",
            "date",
            "start_city",
            "end_city",
        ),
        required_fields=frozenset(
            {
                "id",
                "client_id",
                "airline_id",
                "date",
                "start_city",
                "end_city",
            }
        ),
    ),
}

VALID_RECORD_TYPES = frozenset(RECORD_SCHEMAS)
RECORD_TYPE_DISPLAY_NAMES = tuple(
    schema.display_name for schema in RECORD_SCHEMAS.values()
)
DISPLAY_NAME_TO_RECORD_TYPE = {
    schema.display_name: record_type
    for record_type, schema in RECORD_SCHEMAS.items()
}
DISPLAY_FIELDS_BY_RECORD_TYPE = {
    record_type: schema.fields
    for record_type, schema in RECORD_SCHEMAS.items()
}
ALLOWED_FIELDS_BY_RECORD_TYPE = {
    record_type: schema.allowed_fields
    for record_type, schema in RECORD_SCHEMAS.items()
}
REQUIRED_FIELDS_BY_RECORD_TYPE = {
    record_type: schema.required_fields_with_type
    for record_type, schema in RECORD_SCHEMAS.items()
}
ALLOWED_SEARCH_FIELDS = frozenset().union(*ALLOWED_FIELDS_BY_RECORD_TYPE.values())
EXACT_MATCH_FIELDS = frozenset({"id", "client_id", "airline_id"})
INTEGER_FIELDS = frozenset({"id", "client_id", "airline_id"})


def get_record_schema(record_type: str) -> RecordSchema:
    """Return the schema for a supported record type."""
    return RECORD_SCHEMAS[record_type]


def get_record_type_from_display_name(display_name: str) -> str:
    """Map a GUI display name to the canonical record type value."""
    return DISPLAY_NAME_TO_RECORD_TYPE[display_name]

"""Unit tests for record management logic."""

import pytest

from record_management_system.records import (
    create_record,
    delete_record,
    get_records,
    update_record,
)
from tests.factories import (
    make_airline_record,
    make_client_record,
    make_flight_record,
)


def test_create_client_record_adds_record_to_records_list(client_record):
    """Create a client record and add it to the records list."""
    records = []

    created_record = create_record(records, client_record)

    assert created_record == client_record
    assert records == [client_record]


def test_create_airline_record_adds_record_to_records_list(airline_record):
    """Create an airline record and add it to the records list."""
    records = []

    created_record = create_record(records, airline_record)

    assert created_record == airline_record
    assert records == [airline_record]


def test_create_flight_record_adds_record_to_records_list(flight_record):
    """Create a flight record and add it to the records list."""
    records = []

    created_record = create_record(records, flight_record)

    assert created_record == flight_record
    assert records == [flight_record]


def test_get_records_returns_all_records():
    """Return all records from the records list."""
    records = [
        make_client_record(),
        make_airline_record(),
    ]

    result = get_records(records)

    assert result == records


def test_get_records_returns_empty_list_when_no_records_exist():
    """Return an empty list when no records exist."""
    result = get_records([])

    assert result == []


def test_create_record_raises_error_for_invalid_record_type():
    """Raise an error when the record type is invalid."""
    records = []
    invalid_record = {
        "id": 99,
        "type": "hotel",
        "name": "Invalid Record",
    }

    with pytest.raises(ValueError, match="Invalid record type"):
        create_record(records, invalid_record)

    assert not records


def test_create_client_record_raises_error_when_required_field_is_missing():
    """Raise an error when a required client field is missing."""
    records = []
    invalid_client_record = make_client_record()
    invalid_client_record.pop("name")

    with pytest.raises(ValueError, match="Missing required field: name"):
        create_record(records, invalid_client_record)

    assert not records


def test_create_airline_record_raises_error_when_required_field_is_missing():
    """Raise an error when a required airline field is missing."""
    records = []
    invalid_airline_record = {"id": 2, "type": "airline"}

    with pytest.raises(ValueError, match="Missing required field: company_name"):
        create_record(records, invalid_airline_record)

    assert not records


def test_create_flight_record_raises_error_when_required_field_is_missing():
    """Raise an error when a required flight field is missing."""
    records = []
    invalid_flight_record = make_flight_record()
    invalid_flight_record.pop("end_city")

    with pytest.raises(ValueError, match="Missing required field: end_city"):
        create_record(records, invalid_flight_record)

    assert not records


def test_create_record_raises_error_when_id_already_exists(client_record):
    """Raise an error when a record ID already exists."""
    records = [client_record]
    duplicate_client_record = make_client_record(
        name="Jane Smith",
        address_line_1="20 Example Street",
        zip_code="SW1A 2AA",
        phone_number="07987654321",
    )

    with pytest.raises(ValueError, match="Record with this ID already exists"):
        create_record(records, duplicate_client_record)

    assert records == [client_record]


def test_create_client_record_raises_error_when_required_field_is_empty():
    """Raise an error when a required client field is empty."""
    records = []
    invalid_client_record = make_client_record(name="")

    with pytest.raises(ValueError, match="Missing required field: name"):
        create_record(records, invalid_client_record)

    assert not records


def test_get_records_returns_copy_of_records():
    """Return a copy so the original records list is not changed."""
    records = [make_airline_record()]

    result = get_records(records)
    result.append(make_airline_record(id=3, company_name="Virgin Atlantic"))

    assert records == [make_airline_record()]


def test_create_client_record_raises_error_when_phone_number_contains_letters():
    """Raise an error when phone number contains letters."""
    records = []
    invalid_client_record = make_client_record(phone_number="07123abc789")

    with pytest.raises(ValueError, match="Phone number must contain only digits"):
        create_record(records, invalid_client_record)

    assert not records


def test_create_client_record_accepts_phone_number_with_plus_prefix():
    """Create a client record when phone number starts with plus."""
    records = []
    client_record = make_client_record(phone_number="+447123456789")

    created_record = create_record(records, client_record)

    assert created_record == client_record
    assert records == [client_record]


def test_create_client_record_accepts_phone_number_with_double_zero_prefix():
    """Create a client record when phone number starts with double zero."""
    records = []
    client_record = make_client_record(phone_number="00447123456789")

    created_record = create_record(records, client_record)

    assert created_record == client_record
    assert records == [client_record]


def test_create_flight_record_raises_error_when_date_format_is_invalid():
    """Raise an error when flight date is not in YYYY-MM-DD format."""
    records = []
    invalid_flight_record = make_flight_record(date="14/05/2026")

    with pytest.raises(ValueError, match="Date must use YYYY-MM-DD format"):
        create_record(records, invalid_flight_record)

    assert not records


def test_create_client_record_raises_error_when_required_field_is_whitespace():
    """Raise an error when a required field only contains whitespace."""
    records = []
    invalid_client_record = make_client_record(name="   ")

    with pytest.raises(ValueError, match="Missing required field: name"):
        create_record(records, invalid_client_record)

    assert not records


def test_update_client_record_changes_existing_record(client_record):
    """Update an existing client record."""
    records = [client_record]

    updated_record = update_record(
        records,
        1,
        {
            "name": "Jane Smith",
            "city": "Manchester",
            "phone_number": "07987654321",
        },
    )

    assert updated_record["name"] == "Jane Smith"
    assert updated_record["city"] == "Manchester"
    assert updated_record["phone_number"] == "07987654321"
    assert records[0]["name"] == "Jane Smith"


def test_update_airline_record_changes_existing_record(airline_record):
    """Update an existing airline record."""
    records = [airline_record]

    updated_record = update_record(
        records,
        2,
        {
            "company_name": "Virgin Atlantic",
        },
    )

    assert updated_record["company_name"] == "Virgin Atlantic"
    assert records[0]["company_name"] == "Virgin Atlantic"


def test_update_flight_record_changes_existing_record(flight_record):
    """Update an existing flight record."""
    records = [flight_record]

    updated_record = update_record(
        records,
        3,
        {
            "date": "2026-06-15",
            "start_city": "Manchester",
            "end_city": "Madrid",
        },
    )

    assert updated_record["date"] == "2026-06-15"
    assert updated_record["start_city"] == "Manchester"
    assert updated_record["end_city"] == "Madrid"
    assert records[0]["start_city"] == "Manchester"


def test_update_record_raises_error_when_no_fields_are_provided(airline_record):
    """Raise an error when no update fields are provided."""
    records = [airline_record]

    with pytest.raises(ValueError, match="No fields provided to update"):
        update_record(records, 2, {})


def test_update_record_raises_error_when_record_not_found(airline_record):
    """Raise an error when the record ID does not exist."""
    records = [airline_record]

    with pytest.raises(ValueError, match="Record not found"):
        update_record(records, 99, {"company_name": "Virgin Atlantic"})


def test_update_record_raises_error_when_id_is_changed(airline_record):
    """Raise an error when trying to change a record ID."""
    records = [airline_record]

    with pytest.raises(ValueError, match="Record ID cannot be updated"):
        update_record(records, 2, {"id": 5})


def test_update_record_raises_error_when_type_is_changed(airline_record):
    """Raise an error when trying to change a record type."""
    records = [airline_record]

    with pytest.raises(ValueError, match="Record type cannot be updated"):
        update_record(records, 2, {"type": "client"})


def test_update_record_raises_error_when_required_field_is_empty(client_record):
    """Raise an error when a required field is made empty."""
    records = [client_record]

    with pytest.raises(ValueError, match="Missing required field: name"):
        update_record(records, 1, {"name": ""})

    assert records[0]["name"] == "John Smith"


def test_update_record_raises_error_for_unknown_field(airline_record):
    """Raise an error when an update field is not valid for the record type."""
    records = [airline_record]

    with pytest.raises(ValueError, match="Invalid field for airline record: name"):
        update_record(records, 2, {"name": "Wrong Field"})


def test_update_record_returns_copy_of_updated_record(airline_record):
    """Return a copy so external changes do not alter the stored record."""
    records = [airline_record]

    updated_record = update_record(
        records,
        2,
        {
            "company_name": "Virgin Atlantic",
        },
    )

    updated_record["company_name"] = "Changed Outside"

    assert records[0]["company_name"] == "Virgin Atlantic"


def test_delete_record_removes_existing_record():
    """Delete an existing record from the records list."""
    records = [
        make_client_record(),
        make_airline_record(),
    ]

    deleted_record = delete_record(records, 1)

    assert deleted_record == make_client_record()
    assert records == [make_airline_record()]


def test_delete_record_raises_error_when_record_not_found():
    """Raise an error when trying to delete a non-existing record."""
    records = [make_client_record()]

    with pytest.raises(ValueError, match="Record not found"):
        delete_record(records, 22)

    assert records == [make_client_record()]


def test_delete_record_empty_list_raises_error():
    """Raise an error when trying to delete from an empty records list."""
    with pytest.raises(ValueError, match="Records are empty, none to delete"):
        delete_record([], 22)

"""Unit tests for record management logic."""

import pytest

from record_management_system.records import create_record, get_records, update_record


def test_create_client_record_adds_record_to_records_list():
    """Create a client record and add it to the records list."""
    records = []

    client_record = {
        "id": 1,
        "type": "client",
        "name": "John Smith",
        "address_line_1": "10 Example Street",
        "address_line_2": "",
        "address_line_3": "",
        "city": "London",
        "state": "",
        "zip_code": "SW1A 1AA",
        "country": "United Kingdom",
        "phone_number": "07123456789",
    }

    created_record = create_record(records, client_record)

    assert created_record == client_record
    assert records == [client_record]


def test_create_airline_record_adds_record_to_records_list():
    """Create an airline record and add it to the records list."""
    records = []

    airline_record = {
        "id": 2,
        "type": "airline",
        "company_name": "British Airways",
    }

    created_record = create_record(records, airline_record)

    assert created_record == airline_record
    assert records == [airline_record]


def test_create_flight_record_adds_record_to_records_list():
    """Create a flight record and add it to the records list."""
    records = []

    flight_record = {
        "id": 3,
        "type": "flight",
        "client_id": 1,
        "airline_id": 2,
        "date": "2026-05-01",
        "start_city": "London",
        "end_city": "Paris",
    }

    created_record = create_record(records, flight_record)

    assert created_record == flight_record
    assert records == [flight_record]


def test_get_records_returns_all_records():
    """Return all records from the records list."""
    records = [
        {
            "id": 1,
            "type": "client",
            "name": "John Smith",
            "address_line_1": "10 Example Street",
            "address_line_2": "",
            "address_line_3": "",
            "city": "London",
            "state": "",
            "zip_code": "SW1A 1AA",
            "country": "United Kingdom",
            "phone_number": "07123456789",
        },
        {
            "id": 2,
            "type": "airline",
            "company_name": "British Airways",
        },
    ]

    result = get_records(records)

    assert result == records


def test_get_records_returns_empty_list_when_no_records_exist():
    """Return an empty list when no records exist."""
    records = []

    result = get_records(records)

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

    assert records == []


def test_create_client_record_raises_error_when_required_field_is_missing():
    """Raise an error when a required client field is missing."""
    records = []

    invalid_client_record = {
        "id": 1,
        "type": "client",
        "address_line_1": "10 Example Street",
        "address_line_2": "",
        "address_line_3": "",
        "city": "London",
        "state": "",
        "zip_code": "SW1A 1AA",
        "country": "United Kingdom",
        "phone_number": "07123456789",
    }

    with pytest.raises(ValueError, match="Missing required field: name"):
        create_record(records, invalid_client_record)

    assert records == []


def test_create_airline_record_raises_error_when_required_field_is_missing():
    """Raise an error when a required airline field is missing."""
    records = []

    invalid_airline_record = {
        "id": 2,
        "type": "airline",
    }

    with pytest.raises(ValueError, match="Missing required field: company_name"):
        create_record(records, invalid_airline_record)

    assert records == []


def test_create_flight_record_raises_error_when_required_field_is_missing():
    """Raise an error when a required flight field is missing."""
    records = []

    invalid_flight_record = {
        "id": 3,
        "type": "flight",
        "client_id": 1,
        "airline_id": 2,
        "date": "2026-05-01",
        "start_city": "London",
    }

    with pytest.raises(ValueError, match="Missing required field: end_city"):
        create_record(records, invalid_flight_record)

    assert records == []


def test_create_record_raises_error_when_id_already_exists():
    """Raise an error when a record ID already exists."""
    records = [
        {
            "id": 1,
            "type": "client",
            "name": "John Smith",
            "address_line_1": "10 Example Street",
            "address_line_2": "",
            "address_line_3": "",
            "city": "London",
            "state": "",
            "zip_code": "SW1A 1AA",
            "country": "United Kingdom",
            "phone_number": "07123456789",
        }
    ]

    duplicate_client_record = {
        "id": 1,
        "type": "client",
        "name": "Jane Smith",
        "address_line_1": "20 Example Street",
        "address_line_2": "",
        "address_line_3": "",
        "city": "London",
        "state": "",
        "zip_code": "SW1A 2AA",
        "country": "United Kingdom",
        "phone_number": "07987654321",
    }

    with pytest.raises(ValueError, match="Record with this ID already exists"):
        create_record(records, duplicate_client_record)

    assert records == [
        {
            "id": 1,
            "type": "client",
            "name": "John Smith",
            "address_line_1": "10 Example Street",
            "address_line_2": "",
            "address_line_3": "",
            "city": "London",
            "state": "",
            "zip_code": "SW1A 1AA",
            "country": "United Kingdom",
            "phone_number": "07123456789",
        }
    ]


def test_create_client_record_raises_error_when_required_field_is_empty():
    """Raise an error when a required client field is empty."""
    records = []

    invalid_client_record = {
        "id": 1,
        "type": "client",
        "name": "",
        "address_line_1": "10 Example Street",
        "address_line_2": "",
        "address_line_3": "",
        "city": "London",
        "state": "",
        "zip_code": "SW1A 1AA",
        "country": "United Kingdom",
        "phone_number": "07123456789",
    }

    with pytest.raises(ValueError, match="Missing required field: name"):
        create_record(records, invalid_client_record)

    assert records == []


def test_get_records_returns_copy_of_records():
    """Return a copy so the original records list is not changed."""
    records = [
        {
            "id": 2,
            "type": "airline",
            "company_name": "British Airways",
        }
    ]

    result = get_records(records)

    result.append(
        {
            "id": 3,
            "type": "airline",
            "company_name": "Virgin Atlantic",
        }
    )

    assert records == [
        {
            "id": 2,
            "type": "airline",
            "company_name": "British Airways",
        }
    ]
def test_update_client_record_changes_existing_record():
    records = [
        {
            "id": 1,
            "type": "client",
            "name": "John Smith",
            "address_line_1": "10 Example Street",
            "address_line_2": "",
            "address_line_3": "",
            "city": "London",
            "state": "",
            "zip_code": "SW1A 1AA",
            "country": "United Kingdom",
            "phone_number": "07123456789",
        }
    ]

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


def test_update_record_raises_error_when_record_not_found():
    records = [
        {
            "id": 1,
            "type": "airline",
            "company_name": "British Airways",
        }
    ]

    with pytest.raises(ValueError, match="Record not found"):
        update_record(records, 99, {"company_name": "Virgin Atlantic"})


def test_update_record_raises_error_when_id_is_changed():
    records = [
        {
            "id": 1,
            "type": "airline",
            "company_name": "British Airways",
        }
    ]

    with pytest.raises(ValueError, match="Record ID cannot be updated"):
        update_record(records, 1, {"id": 2})


def test_update_record_raises_error_when_type_is_changed():
    records = [
        {
            "id": 1,
            "type": "airline",
            "company_name": "British Airways",
        }
    ]

    with pytest.raises(ValueError, match="Record type cannot be updated"):
        update_record(records, 1, {"type": "client"})


def test_update_record_raises_error_when_required_field_is_empty():
    records = [
        {
            "id": 1,
            "type": "client",
            "name": "John Smith",
            "address_line_1": "10 Example Street",
            "address_line_2": "",
            "address_line_3": "",
            "city": "London",
            "state": "",
            "zip_code": "SW1A 1AA",
            "country": "United Kingdom",
            "phone_number": "07123456789",
        }
    ]

    with pytest.raises(ValueError, match="Missing required field: name"):
        update_record(records, 1, {"name": ""})

    assert records[0]["name"] == "John Smith"

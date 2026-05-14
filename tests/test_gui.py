"""Unit tests for GUI helper functions."""

from record_management_system.gui import format_record_for_display


def test_format_client_record_for_display():
    """Format a client record for display."""
    record = {
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

    result = format_record_for_display(record)

    assert result == (
        "Client | ID: 1 | Name: John Smith | "
        "Address Line 1: 10 Example Street | "
        "City: London | Zip Code: SW1A 1AA | "
        "Country: United Kingdom | Phone Number: 07123456789"
    )


def test_format_client_record_for_display_includes_filled_optional_fields():
    """Format a client record and include optional fields when filled."""
    record = {
        "id": 1,
        "type": "client",
        "name": "John Smith",
        "address_line_1": "10 Example Street",
        "address_line_2": "Flat 2",
        "address_line_3": "",
        "city": "London",
        "state": "Greater London",
        "zip_code": "SW1A 1AA",
        "country": "United Kingdom",
        "phone_number": "07123456789",
    }

    result = format_record_for_display(record)

    assert result == (
        "Client | ID: 1 | Name: John Smith | "
        "Address Line 1: 10 Example Street | Address Line 2: Flat 2 | "
        "City: London | State: Greater London | Zip Code: SW1A 1AA | "
        "Country: United Kingdom | Phone Number: 07123456789"
    )


def test_format_airline_record_for_display():
    """Format an airline record for display."""
    record = {
        "id": 2,
        "type": "airline",
        "company_name": "British Airways",
    }

    result = format_record_for_display(record)

    assert result == "Airline | ID: 2 | Company Name: British Airways"


def test_format_flight_record_for_display():
    """Format a flight record for display."""
    record = {
        "id": 3,
        "type": "flight",
        "client_id": 1,
        "airline_id": 2,
        "date": "2026-05-01",
        "start_city": "London",
        "end_city": "Paris",
    }

    result = format_record_for_display(record)

    assert result == (
        "Flight | ID: 3 | Client ID: 1 | Airline ID: 2 | "
        "Date: 2026-05-01 | Start City: London | End City: Paris"
    )

"""Unit tests for GUI helper functions."""

from record_management_system.gui import format_record_for_display


def test_format_client_record_for_display():
    """Format a client record for display."""
    record = {
        "id": 1,
        "type": "client",
        "name": "John Smith",
        "city": "London",
        "country": "United Kingdom",
    }

    result = format_record_for_display(record)

    assert result == (
        "Client | ID: 1 | Name: John Smith | " "City: London | Country: United Kingdom"
    )


def test_format_airline_record_for_display():
    """Format an airline record for display."""
    record = {
        "id": 2,
        "type": "airline",
        "company_name": "British Airways",
    }

    result = format_record_for_display(record)

    assert result == "Airline | ID: 2 | Company: British Airways"


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
        "London to Paris | Date: 2026-05-01"
    )

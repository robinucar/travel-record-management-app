"""Reusable test data factories."""


def make_client_record(**overrides) -> dict:
    """Build a client record with sensible defaults."""
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
    record.update(overrides)
    return record


def make_airline_record(**overrides) -> dict:
    """Build an airline record with sensible defaults."""
    record = {
        "id": 2,
        "type": "airline",
        "company_name": "British Airways",
    }
    record.update(overrides)
    return record


def make_flight_record(**overrides) -> dict:
    """Build a flight record with sensible defaults."""
    record = {
        "id": 3,
        "type": "flight",
        "client_id": 1,
        "airline_id": 2,
        "date": "2026-05-01",
        "start_city": "London",
        "end_city": "Paris",
    }
    record.update(overrides)
    return record

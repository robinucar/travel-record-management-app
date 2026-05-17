"""Unit tests for search record logic."""

import pytest

from record_management_system.records import search_records
from tests.factories import (
    make_airline_record,
    make_client_record,
)


def test_search_records_by_id_returns_matching_record():
    """Return the matching record when searching by ID."""
    records = [
        make_client_record(),
        make_airline_record(),
    ]

    result = search_records(records, "id", 1)

    assert result == [make_client_record()]


def test_search_records_by_type_returns_matching_records():
    """Return all matching records when searching by record type."""
    records = [
        make_client_record(),
        make_client_record(id=2, name="Jane Smith"),
        make_airline_record(id=3),
    ]

    result = search_records(records, "type", "client")

    assert result == [
        make_client_record(),
        make_client_record(id=2, name="Jane Smith"),
    ]


def test_search_records_by_client_name_returns_matching_record():
    """Return the matching client record when searching by name."""
    records = [
        make_client_record(),
        make_client_record(id=2, name="Jane Smith"),
    ]

    result = search_records(records, "name", "Jane Smith")

    assert result == [make_client_record(id=2, name="Jane Smith")]


def test_search_records_by_airline_company_name_returns_matching_record():
    """Return the matching airline record when searching by company name."""
    records = [
        make_airline_record(),
        make_airline_record(id=2, company_name="Virgin Atlantic"),
    ]

    result = search_records(records, "company_name", "Virgin Atlantic")

    assert result == [
        make_airline_record(id=2, company_name="Virgin Atlantic")
    ]


def test_search_records_returns_empty_list_when_no_match_found():
    """Return an empty list when no matching record exists."""
    records = [
        make_client_record(),
    ]

    result = search_records(records, "name", "Jane Smith")

    assert result == []


def test_search_records_raises_error_for_invalid_field():
    """Raise an error when the search field is not allowed."""
    records = [
        make_client_record(),
    ]

    with pytest.raises(ValueError, match="Invalid search field"):
        search_records(records, "invalid_field", "John Smith")


def test_search_records_raises_error_for_empty_value():
    """Raise an error when the search value is empty."""
    records = [
        make_client_record(),
    ]

    with pytest.raises(ValueError, match="Search value cannot be empty"):
        search_records(records, "name", "")


def test_search_records_returns_copy_of_matching_record():
    """Return a copy so search results cannot mutate original records."""
    records = [
        make_client_record(),
    ]

    result = search_records(records, "id", 1)
    result[0]["name"] = "Changed Name"

    assert records[0]["name"] == "John Smith"


def test_search_records_is_case_insensitive():
    """Return matching records regardless of letter case."""
    records = [
        make_client_record(),
    ]

    result = search_records(records, "name", "john smith")

    assert result == [make_client_record()]


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("name", " John Smith "),
        ("type", " CLIENT "),
    ],
)
def test_search_records_ignores_extra_spaces(field, value):
    """Return matching records when input contains extra spaces."""
    records = [
        make_client_record(),
    ]

    result = search_records(records, field, value)

    assert result == [make_client_record()]


def test_search_records_supports_partial_match():
    """Return records when the search value partially matches the field."""
    records = [
        make_client_record(),
    ]

    result = search_records(records, "name", "John")

    assert result == [make_client_record()]

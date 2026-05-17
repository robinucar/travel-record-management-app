"""Shared pytest fixtures."""

import pytest

from tests.factories import (
    make_airline_record,
    make_client_record,
    make_flight_record,
)


@pytest.fixture
def client_record() -> dict:
    """Return a default client record."""
    return make_client_record()


@pytest.fixture
def airline_record() -> dict:
    """Return a default airline record."""
    return make_airline_record()


@pytest.fixture
def flight_record() -> dict:
    """Return a default flight record."""
    return make_flight_record()

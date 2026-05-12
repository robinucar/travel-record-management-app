from delete_records import delete_record


def test_delete_existing_record():

    records = [
        {"id": 1},
        {"id": 2}
    ]

    result = delete_record(records, 1)

    assert result is True
    assert len(records) == 1


def test_delete_missing_record():

    records = [{"id": 1}]

    result = delete_record(records, 99)

    assert result is False
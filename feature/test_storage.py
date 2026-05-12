from storage import save_records, load_records


def test_save_and_load():

    records = [{"id": 1, "name": "John"}]

    save_records(records)

    loaded = load_records()

    assert loaded == records
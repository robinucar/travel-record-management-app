def delete_record(records, record_id):

    for record in records:
        if record["id"] == record_id:
            records.remove(record)
            return True

    return False
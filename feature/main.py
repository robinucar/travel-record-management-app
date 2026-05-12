from storage import load_records, save_records
from delete_records import delete_record


# Load records from file
records = load_records()


# Show current records
print("Current Records:")
print(records)


# Ask user which record to delete
record_id = int(input("Enter record ID to delete: "))


# Ask for confirmation
confirm = input("Are you sure? (yes/no): ")


if confirm.lower() == "yes":

    deleted = delete_record(records, record_id)

    if deleted:
        save_records(records)

        print("Record deleted successfully")

    else:
        print("Record not found")

else:
    print("Deletion cancelled")
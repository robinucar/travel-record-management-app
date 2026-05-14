"""Graphical user interface for the record management application."""

import tkinter as tk
from tkinter import messagebox, ttk

from record_management_system.records import (
    REQUIRED_FIELDS_BY_RECORD_TYPE,
    create_record,
    get_records,
)

FIELDS_BY_RECORD_TYPE = {
    "Client": [
        "id",
        "name",
        "address_line_1",
        "address_line_2",
        "address_line_3",
        "city",
        "state",
        "zip_code",
        "country",
        "phone_number",
    ],
    "Airline": [
        "id",
        "company_name",
    ],
    "Flight": [
        "id",
        "client_id",
        "airline_id",
        "date",
        "start_city",
        "end_city",
    ],
}

FIELD_LABELS = {
    "id": "ID",
    "type": "Type",
    "name": "Name",
    "address_line_1": "Address Line 1",
    "address_line_2": "Address Line 2",
    "address_line_3": "Address Line 3",
    "city": "City",
    "state": "State",
    "zip_code": "Zip Code",
    "country": "Country",
    "phone_number": "Phone Number",
    "company_name": "Company Name",
    "client_id": "Client ID",
    "airline_id": "Airline ID",
    "date": "Date",
    "start_city": "Start City",
    "end_city": "End City",
}


def format_record_for_display(record: dict) -> str:
    """Format a record for display in the records list."""
    record_type = record["type"]
    display_fields = FIELDS_BY_RECORD_TYPE[record_type.title()]
    required_fields = REQUIRED_FIELDS_BY_RECORD_TYPE[record_type]

    display_parts = [record_type.title()]

    for field_name in display_fields:
        value = record.get(field_name, "")

        if field_name in required_fields or str(value).strip():
            label = FIELD_LABELS[field_name]
            display_parts.append(f"{label}: {value}")

    return " | ".join(display_parts)


def create_main_window() -> tk.Tk:
    """Create and configure the main application window."""
    window = tk.Tk()
    window.title("Travel Record Management App")
    window.geometry("900x600")
    window.minsize(700, 500)

    records: list[dict] = []

    main_frame = ttk.Frame(window, padding=16)
    main_frame.pack(fill="both", expand=True)

    title_label = ttk.Label(
        main_frame,
        text="Travel Record Management App",
        font=("Arial", 18, "bold"),
    )
    title_label.pack(anchor="w", pady=(0, 16))

    content_frame = ttk.Frame(main_frame)
    content_frame.pack(fill="both", expand=True)

    form_frame = ttk.LabelFrame(content_frame, text="Create Record", padding=12)
    form_frame.pack(side="left", fill="y", padx=(0, 16))

    records_frame = ttk.LabelFrame(content_frame, text="Records", padding=12)
    records_frame.pack(side="right", fill="both", expand=True)

    record_type_label = ttk.Label(form_frame, text="Record Type")
    record_type_label.pack(anchor="w")

    record_type_combo = ttk.Combobox(
        form_frame,
        values=["Client", "Airline", "Flight"],
        state="readonly",
    )
    record_type_combo.set("Client")
    record_type_combo.pack(fill="x", pady=(4, 12))

    fields_frame = ttk.Frame(form_frame)
    fields_frame.pack(fill="x", pady=(0, 12))

    field_entries: dict[str, ttk.Entry] = {}

    def render_form_fields() -> None:
        """Render input fields for the selected record type."""
        for widget in fields_frame.winfo_children():
            widget.destroy()

        field_entries.clear()

        selected_record_type = record_type_combo.get()

        for field_name in FIELDS_BY_RECORD_TYPE[selected_record_type]:
            label = ttk.Label(fields_frame, text=FIELD_LABELS[field_name])
            label.pack(anchor="w")

            entry = ttk.Entry(fields_frame)
            entry.pack(fill="x", pady=(2, 8))

            field_entries[field_name] = entry

    def refresh_records_display() -> None:
        """Refresh the records display list."""
        records_list.delete(0, tk.END)

        for record in get_records(records):
            records_list.insert(tk.END, format_record_for_display(record))

    def clear_form_fields() -> None:
        """Clear all form input fields."""
        for entry in field_entries.values():
            entry.delete(0, tk.END)

    def handle_create_record() -> None:
        """Create a record from the form values and refresh the display."""
        selected_record_type = record_type_combo.get()

        record = {
            "type": selected_record_type.lower(),
        }

        try:
            for field_name, entry in field_entries.items():
                value = entry.get().strip()

                if field_name.endswith("_id") or field_name == "id":
                    record[field_name] = int(value)
                else:
                    record[field_name] = value

            create_record(records, record)
            refresh_records_display()
            clear_form_fields()

            messagebox.showinfo("Success", "Record created successfully.")

        except ValueError as error:
            messagebox.showerror("Invalid record", str(error))

    record_type_combo.bind("<<ComboboxSelected>>", lambda _event: render_form_fields())

    render_form_fields()

    save_button = ttk.Button(
        form_frame,
        text="Create Record",
        command=handle_create_record,
    )
    save_button.pack(fill="x", pady=(4, 0))

    records_list = tk.Listbox(records_frame)
    records_list.pack(fill="both", expand=True)

    refresh_records_display()

    return window

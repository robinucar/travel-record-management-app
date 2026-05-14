"""Graphical user interface for the record management application."""

import tkinter as tk
from tkinter import messagebox, ttk

from record_management_system.records import create_record, get_records, search_records

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


def format_record_for_display(record: dict) -> str:
    """Format a record for display in the records list."""
    record_type = record["type"].title()
    record_id = record["id"]

    if record["type"] == "client":
        return (
            f"{record_type} | ID: {record_id} | "
            f"Name: {record['name']} | "
            f"City: {record['city']} | "
            f"Country: {record['country']}"
        )

    if record["type"] == "airline":
        return (
            f"{record_type} | ID: {record_id} | " f"Company: {record['company_name']}"
        )

    return (
        f"{record_type} | ID: {record_id} | "
        f"Client ID: {record['client_id']} | "
        f"Airline ID: {record['airline_id']} | "
        f"{record['start_city']} to {record['end_city']} | "
        f"Date: {record['date']}"
    )


def create_main_window() -> tk.Tk:
    """Create and configure the main application window."""
    window = tk.Tk()
    window.title("Travel Record Management App")
    window.geometry("1000x850")
    window.minsize(900, 800)

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
            label = ttk.Label(fields_frame, text=field_name.replace("_", " ").title())
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

    def handle_search_records() -> None:
        """Search records and display matching results."""
        field = search_field_combo.get()
        value = search_value_entry.get().strip()

        try:
            results = search_records(records, field, value)
        except ValueError as error:
            messagebox.showerror("Invalid search", str(error))
            return

        records_list.delete(0, tk.END)

        if not results:
            messagebox.showinfo("No results", "No matching records found.")
            return

        for record in results:
            records_list.insert(tk.END, format_record_for_display(record))

    def handle_clear_search() -> None:
        """Clear search input and show all records."""
        search_value_entry.delete(0, tk.END)
        refresh_records_display()

    record_type_combo.bind("<<ComboboxSelected>>", lambda _event: render_form_fields())

    render_form_fields()

    save_button = ttk.Button(
        form_frame,
        text="Create Record",
        command=handle_create_record,
    )
    save_button.pack(fill="x", pady=(4, 0))

    #Search Records Section
    search_frame = ttk.LabelFrame(records_frame, text="Search Records", padding=8)
    search_frame.pack(fill="x", pady=(0, 12))

    search_field_label = ttk.Label(search_frame, text="Search Field")
    search_field_label.pack(anchor="w")

    search_field_combo = ttk.Combobox(
        search_frame,
        values=[
            "id",
            "type",
            "name",
            "company_name",
            "client_id",
            "airline_id",
            "date",
            "start_city",
            "end_city",
            "city",
            "country",
            "phone_number",
            "address_line_1",
            "address_line_2",
            "address_line_3",
            "state",
            "zip_code",
        ],
        state="readonly",
    )

    search_field_combo.set("id")
    search_field_combo.pack(fill="x", pady=(2, 8))

    search_value_label = ttk.Label(search_frame, text="Search Value")
    search_value_label.pack(anchor="w")

    search_value_entry = ttk.Entry(search_frame)
    search_value_entry.pack(fill="x", pady=(2, 8))

    search_button = ttk.Button(
        search_frame,
        text="Search",
        command=handle_search_records,
    )
    search_button.pack(fill="x", pady=(0, 4))

    clear_search_button = ttk.Button(
        search_frame,
        text="Clear Search",
        command=handle_clear_search,
    )
    clear_search_button.pack(fill="x")

    records_list = tk.Listbox(records_frame)
    records_list.pack(fill="both", expand=True)

    refresh_records_display()

    return window

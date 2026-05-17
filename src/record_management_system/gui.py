"""Graphical user interface for the record management application."""

import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from record_management_system.gui_actions import (
    create_record_from_values,
    delete_record_by_id,
    get_records_for_display,
    load_records_from_file,
    save_records_to_file,
    search_records_by_field,
    update_record_from_values,
)
from record_management_system.gui_helpers import format_record_for_display
from record_management_system.schema import (
    ALLOWED_SEARCH_FIELDS,
    DISPLAY_FIELDS_BY_RECORD_TYPE,
    FIELD_LABELS,
    RECORD_SCHEMAS,
    RECORD_TYPE_DISPLAY_NAMES,
    get_record_type_from_display_name,
)

DATA_FILE_PATH = Path("data/records.json")


def create_main_window() -> tk.Tk:
    """Create and configure the main application window."""
    window = tk.Tk()
    window.title("Travel Record Management App")
    window.geometry("1000x850")
    window.minsize(900, 800)

    try:
        records: list[dict] = load_records_from_file(DATA_FILE_PATH)
    except (OSError, ValueError) as error:
        messagebox.showerror("Load failed", str(error))
        records = []

    displayed_records: list[dict] = []
    has_unsaved_changes = False

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
        values=RECORD_TYPE_DISPLAY_NAMES,
        state="readonly",
    )
    record_type_combo.set(RECORD_TYPE_DISPLAY_NAMES[0])
    record_type_combo.pack(fill="x", pady=(4, 12))

    fields_frame = ttk.Frame(form_frame)
    fields_frame.pack(fill="x", pady=(0, 12))

    field_entries: dict[str, ttk.Entry] = {}

    def get_field_values() -> dict[str, str]:
        """Return the current form values keyed by field name."""
        return {
            field_name: entry.get()
            for field_name, entry in field_entries.items()
        }

    def render_records_list(records_to_display: list[dict]) -> None:
        """Render the given records in the list widget."""
        records_list.delete(0, tk.END)

        for record in records_to_display:
            records_list.insert(tk.END, format_record_for_display(record))

    def render_form_fields() -> None:
        """Render input fields for the selected record type."""
        for widget in fields_frame.winfo_children():
            widget.destroy()

        field_entries.clear()

        selected_display_name = record_type_combo.get()
        record_type = get_record_type_from_display_name(selected_display_name)

        for field_name in DISPLAY_FIELDS_BY_RECORD_TYPE[record_type]:
            label = ttk.Label(fields_frame, text=FIELD_LABELS[field_name])
            label.pack(anchor="w")

            entry = ttk.Entry(fields_frame)
            entry.pack(fill="x", pady=(2, 8))

            field_entries[field_name] = entry

    def refresh_records_display() -> None:
        """Refresh the records display list."""
        nonlocal displayed_records
        displayed_records = get_records_for_display(records)
        render_records_list(displayed_records)

    def clear_form_fields() -> None:
        """Clear all form input fields."""
        for entry in field_entries.values():
            entry.delete(0, tk.END)

    def handle_create_record() -> None:
        """Create a record from the form values and refresh the display."""
        nonlocal has_unsaved_changes
        record_type = get_record_type_from_display_name(record_type_combo.get())

        try:
            create_record_from_values(records, record_type, get_field_values())
        except ValueError as error:
            messagebox.showerror("Invalid record", str(error))
            return

        has_unsaved_changes = True
        refresh_records_display()
        clear_form_fields()
        messagebox.showinfo("Success", "Record created successfully.")

    def handle_search_records() -> None:
        """Search records and display matching results."""
        nonlocal displayed_records
        field = search_field_combo.get()
        value = search_value_entry.get()

        try:
            displayed_records = search_records_by_field(records, field, value)
        except ValueError as error:
            messagebox.showerror("Invalid search", str(error))
            return

        render_records_list(displayed_records)

        if not displayed_records:
            messagebox.showinfo("No results", "No matching records found.")

    def handle_clear_search() -> None:
        """Clear search input and show all records."""
        search_value_entry.delete(0, tk.END)
        refresh_records_display()

    def handle_load_selected_record_for_update() -> None:
        """Load the selected record into the form for editing."""
        selected_indices = records_list.curselection()

        if not selected_indices:
            messagebox.showerror("No selection", "Please select a record to update.")
            return

        selected_record = displayed_records[selected_indices[0]]
        record_type = selected_record["type"]
        record_type_combo.set(RECORD_SCHEMAS[record_type].display_name)
        render_form_fields()

        for field_name, entry in field_entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, str(selected_record.get(field_name, "")))

    def handle_update_record() -> None:
        """Update the selected record using the form values."""
        nonlocal has_unsaved_changes
        selected_indices = records_list.curselection()

        if not selected_indices:
            messagebox.showerror("No selection", "Please select a record to update.")
            return

        selected_record = displayed_records[selected_indices[0]]

        try:
            update_record_from_values(
                records,
                selected_record["id"],
                get_field_values(),
            )
        except ValueError as error:
            messagebox.showerror("Update failed", str(error))
            return

        has_unsaved_changes = True
        refresh_records_display()
        clear_form_fields()
        messagebox.showinfo("Updated", "Record updated successfully.")

    def handle_delete_record() -> None:
        """Delete the selected record after user confirmation."""
        nonlocal has_unsaved_changes
        selected_indices = records_list.curselection()

        if not selected_indices:
            messagebox.showerror("No selection", "Please select a record to delete.")
            return

        selected_record = displayed_records[selected_indices[0]]
        confirmed = messagebox.askyesno(
            "Confirm delete",
            "Are you sure you want to delete this record?",
        )

        if not confirmed:
            return

        try:
            delete_record_by_id(records, selected_record["id"])
        except ValueError as error:
            messagebox.showerror("Delete failed", str(error))
            return

        has_unsaved_changes = True
        refresh_records_display()
        messagebox.showinfo("Deleted", "Record deleted successfully.")

    def save_with_feedback() -> bool:
        """Save records and surface any save error to the user."""
        nonlocal has_unsaved_changes

        try:
            save_records_to_file(records, DATA_FILE_PATH)
        except (OSError, ValueError) as error:
            messagebox.showerror("Save failed", str(error))
            return False

        has_unsaved_changes = False
        return True

    def handle_save_records() -> None:
        """Save records to the data file."""
        if save_with_feedback():
            messagebox.showinfo("Saved", "Records saved successfully.")

    def handle_window_close() -> None:
        """Close the application, prompting only if there are unsaved changes."""
        if not has_unsaved_changes:
            window.destroy()
            return

        should_save = messagebox.askyesnocancel(
            "Unsaved changes",
            "Do you want to save changes before closing?",
        )

        if should_save is None:
            return

        if should_save and not save_with_feedback():
            return

        window.destroy()

    record_type_combo.bind("<<ComboboxSelected>>", lambda _event: render_form_fields())
    render_form_fields()

    save_button = ttk.Button(
        form_frame,
        text="Create Record",
        command=handle_create_record,
    )
    save_button.pack(fill="x", pady=(4, 0))

    update_button = ttk.Button(
        form_frame,
        text="Update Selected Record",
        command=handle_update_record,
    )
    update_button.pack(fill="x", pady=(8, 0))

    search_frame = ttk.LabelFrame(records_frame, text="Search Records", padding=8)
    search_frame.pack(fill="x", pady=(0, 12))

    search_field_label = ttk.Label(search_frame, text="Search Field")
    search_field_label.pack(anchor="w")

    search_field_combo = ttk.Combobox(
        search_frame,
        values=sorted(ALLOWED_SEARCH_FIELDS),
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

    load_update_button = ttk.Button(
        records_frame,
        text="Load Selected Record for Update",
        command=handle_load_selected_record_for_update,
    )
    load_update_button.pack(fill="x", pady=(8, 0))

    delete_button = ttk.Button(
        records_frame,
        text="Delete Selected Record",
        command=handle_delete_record,
    )
    delete_button.pack(fill="x", pady=(8, 0))

    save_records_button = ttk.Button(
        records_frame,
        text="Save Records",
        command=handle_save_records,
    )
    save_records_button.pack(fill="x", pady=(8, 0))

    refresh_records_display()
    window.protocol("WM_DELETE_WINDOW", handle_window_close)
    return window

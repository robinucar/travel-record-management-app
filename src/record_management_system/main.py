"""Application entry point."""

from record_management_system.gui import create_main_window


def main() -> None:
    """Run the travel record management application."""
    window = create_main_window()
    window.mainloop()


if __name__ == "__main__":
    main()

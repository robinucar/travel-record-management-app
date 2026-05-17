# Travel Record Management App

Travel Record Management App is a desktop CRUD application for a specialist
travel agent.

It manages three record types:

1. Client records
2. Airline company records
3. Flight records

The application uses a Tkinter GUI, stores records internally as a list of
dictionaries, and persists data to JSON.

## Current Features

The application currently supports:

1. Creating client, airline, and flight records
2. Viewing records in the GUI
3. Searching records
4. Updating existing records
5. Deleting records with confirmation
6. Loading records from file when the application starts
7. Saving records to file on demand and when closing with unsaved changes
8. Shared validation for create, update, and storage loading
9. Unit tests for record logic, search, storage, and GUI helper logic

## Assignment Requirements

The project is built around these core requirements:

1. Create a record
2. Delete a record
3. Update a record
4. Search and display a record
5. Save records to the file system when the application closes
6. Load existing records from the file system when the application starts

The internal storage format is a list of dictionaries.

Example:

```python
records = [
    {
        "id": 1,
        "type": "client",
        "name": "Example Client",
    }
]
```

The current file storage implementation uses JSON.

## Architecture Overview

The codebase is split into small modules with focused responsibilities:

- `schema.py`: central definitions for record types, fields, labels, and search
  rules
- `validation.py`: shared validation used by create, update, and storage load
- `records.py`: record CRUD and search logic
- `storage.py`: JSON file persistence
- `gui_helpers.py`: pure helper functions for formatting and form conversion
- `gui_actions.py`: GUI-facing actions that connect the interface to backend
  logic
- `gui.py`: Tkinter window layout and event handling
- `main.py`: application entry point

This structure keeps domain rules reusable and helps the GUI stay thinner.

## Record Types

### Client Record

| Field          | Type    |
| -------------- | ------- |
| ID             | Integer |
| Type           | String  |
| Name           | String  |
| Address Line 1 | String  |
| Address Line 2 | String  |
| Address Line 3 | String  |
| City           | String  |
| State          | String  |
| Zip Code       | String  |
| Country        | String  |
| Phone Number   | String  |

### Airline Record

| Field        | Type    |
| ------------ | ------- |
| ID           | Integer |
| Type         | String  |
| Company Name | String  |

### Flight Record

| Field      | Type      |
| ---------- | --------- |
| ID         | Integer   |
| Type       | String    |
| Client ID  | Integer   |
| Airline ID | Integer   |
| Date       | Date/time |
| Start City | String    |
| End City   | String    |

## Project Structure

```txt
travel-record-management-app/
├── .githooks/
├── data/
├── docs/
│   ├── git-workflow.md
│   └── project-structure.md
├── src/
│   └── record_management_system/
│       ├── __init__.py
│       ├── gui.py
│       ├── gui_actions.py
│       ├── gui_helpers.py
│       ├── main.py
│       ├── records.py
│       ├── schema.py
│       ├── storage.py
│       └── validation.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── factories.py
│   ├── test_gui.py
│   ├── test_records.py
│   ├── test_search.py
│   └── test_storage.py
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── pytest.ini
└── requirements.txt
```

## Development Environment

This project targets Python 3.14.

The expected version is documented in:

```txt
.python-version
```

## Setup

Create a virtual environment:

```bash
python3.14 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Enable the repository Git hooks:

```bash
git config core.hooksPath .githooks
```

## Running the Application

Run the application from the repository root with:

```bash
PYTHONPATH=src python -m record_management_system.main
```

The project uses a `src` layout, so `PYTHONPATH=src` is needed when running
the app directly from the repository root.

## GUI Framework

The project uses vanilla Tkinter for the graphical user interface.

Tkinter was chosen because it is included with standard Python installations
and is suitable for a small desktop CRUD application.

On some macOS or Homebrew Python installations, Tkinter may need to be
installed separately. If the application fails with an error such as:

```txt
ModuleNotFoundError: No module named '_tkinter'
```

install the matching Tkinter package:

```bash
brew install python-tk@3.14
```

## Data Storage

Records are stored in:

```txt
data/records.json
```

Storage behavior:

1. If the file does not exist, the application starts with an empty list
2. If the file exists, records are loaded at startup
3. Parent directories are created automatically when saving
4. Loaded data is validated before use

## Testing

Run the full test suite with:

```bash
python -m pytest
```

The test suite includes:

- record CRUD tests
- search tests
- storage tests
- GUI helper tests
- shared fixtures and record factories for reusable test data

## Linting

This project uses Ruff for style and code quality checks.

Run Ruff with:

```bash
python -m ruff check .
```

## Commit Message Standard

This repository includes a commit message hook in `.githooks/commit-msg`.

Commit messages must follow this format:

```txt
Subsystem: Short present tense sentence.
```

Examples:

```txt
Project: Initialise repository structure.
Tests: Add storage unit tests.
Docs: Add project setup notes.
GUI: Add main window layout.
Storage: Add JSON file loading.
Records: Add client record validation.
```

The first line must:

1. Start with a subsystem prefix
2. Use a colon after the prefix
3. Use a capital letter after the colon
4. End with a period

## Pre Commit Checks

This repository includes a pre commit hook in `.githooks/pre-commit`.

Before each commit, the project runs:

```bash
python -m ruff check .
python -m pytest
```

If Ruff or the tests fail, the commit will be stopped.

# Travel Record Management App

## Project Overview

Travel Record Management App is a GUI based record management system for a specialist travel agent.

The application manages three types of records:

1. Client records
2. Airline company records
3. Flight records

The application allows users to create, update, delete, search, and display records through a graphical user interface.

## Current Project Status

The project currently includes:

1. Backend record management logic
2. Tkinter GUI for creating and displaying records
3. JSON file storage logic
4. Unit tests for record logic, GUI helper logic, and storage logic
5. Ruff linting configuration
6. Git hooks for pre commit checks and commit message validation

The current GUI implementation covers the Create Records and Display/Get Records scope.

Search, update, delete, and file storage integration are handled as separate task areas or later integration work.

## Assignment Requirements

The application must support the following actions:

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
        "name": "Example Client"
    }
]
```

The current file storage implementation uses JSON.

## Record Types

### Client Record

A client record contains the following fields:

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

An airline record contains the following fields:

| Field        | Type    |
| ------------ | ------- |
| ID           | Integer |
| Type         | String  |
| Company Name | String  |

### Flight Record

A flight record contains the following fields:

| Field      | Type      |
| ---------- | --------- |
| ID         | Integer   |
| Type       | String    |
| Client ID  | Integer   |
| Airline ID | Integer   |
| Date       | Date/time |
| Start City | String    |
| End City   | String    |

## Initial User Stories

### Client Records

- As a travel agent user, I want to create a client record so that client details can be stored in the system.

- As a travel agent user, I want to update a client record so that incorrect or outdated client details can be corrected.

- As a travel agent user, I want to delete a client record so that records that are no longer required can be removed.

- As a travel agent user, I want to search for a client record so that I can quickly find client information.

### Airline Records

- As a travel agent user, I want to create an airline company record so that airline details can be stored in the system.

- As a travel agent user, I want to update an airline company record so that company details remain accurate.

- As a travel agent user, I want to delete an airline company record so that unused airline records can be removed.

- As a travel agent user, I want to search for an airline company record so that I can quickly find airline information.

### Flight Records

- As a travel agent user, I want to create a flight record so that a client can be linked to an airline and journey details.

- As a travel agent user, I want to update a flight record so that journey details can be corrected.

- As a travel agent user, I want to delete a flight record so that cancelled or incorrect flight records can be removed.

- As a travel agent user, I want to search for a flight record so that I can quickly find journey information.

### Data Storage

- As a travel agent user, I want records to be saved when the application closes so that data is not lost.

- As a travel agent user, I want existing records to be loaded when the application starts so that I can continue working with previously saved data.

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
│       ├── main.py
│       ├── records.py
│       └── storage.py
├── tests/
│   ├── __init__.py
│   ├── test_gui.py
│   ├── test_records.py
│   └── test_storage.py
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── pytest.ini
└── requirements.txt
```

## Main Modules

### `records.py`

Contains the core record management logic.

Current responsibilities include:

```txt
Create records
Get/display records
Search records
Update records
Delete records
Validate record types
Validate required fields
Check duplicate record IDs
```

### `gui.py`

Contains the Tkinter graphical user interface.

Current responsibilities include:

```txt
Create the main application window
Show the Create Record form
Allow the user to select Client, Airline, or Flight records
Render dynamic input fields for each record type
Call the backend create_record function
Use the backend get_records function when refreshing the display
Display created records in the records list
Format records for display
Show success and error messages to the user
```

### `storage.py`

Contains file storage logic for record data.

Current responsibilities include:

```txt
Save records to a JSON file
Load records from a JSON file
Return an empty list when no data file exists
Create parent directories when saving
Validate that loaded data is a list
```

## Development Environment

This project uses Python 3.14.

The Python version is documented in:

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

## Running the Application

Run the application from the repository root with:

```bash
PYTHONPATH=src python -m record_management_system.main
```

The project uses a `src` layout, so `PYTHONPATH=src` is needed when running the application directly from the repository root.

## GUI Framework

The project uses vanilla Tkinter for the graphical user interface.

Tkinter was chosen because it is included with standard Python installations and is suitable for a small desktop CRUD application.

On some macOS/Homebrew Python installations, Tkinter may need to be installed separately.

If the application fails with an error such as:

```txt
ModuleNotFoundError: No module named '_tkinter'
```

install the matching Tkinter package:

```bash
brew install python-tk@3.14
```

## Testing

Run all tests with:

```bash
python -m pytest
```

Current test files:

```txt
tests/test_records.py
tests/test_gui.py
tests/test_storage.py
```

## Linting

This project uses Ruff to support PEP 8 style checks and general Python code quality.

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

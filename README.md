# Travel Record Management App

## Project Overview

Travel Record Management App is a GUI based record management system for
a specialist travel agent.

The application will manage three types of records:

1. Client records
2. Airline company records
3. Flight records

The application will allow users to create, update, delete, search, and
display records through a graphical user interface.

## Assignment Requirements

The application must support the following actions:

1. Create a record
2. Delete a record
3. Update a record
4. Search and display a record
5. Save records to the file system when the application closes
6. Load existing records from the file system when the application starts

The internal storage format will be a list of dictionaries.

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

The final file storage format will be agreed by the group before
implementation. Possible options include:

- JSON
- JSONL
- Pickle

## Record Types

### Client Record

A client record will contain the following fields:

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

An airline record will contain the following fields:

| Field        | Type    |
| ------------ | ------- |
| ID           | Integer |
| Type         | String  |
| Company Name | String  |

### Flight Record

A flight record will contain the following fields:

| Field      | Type      |
| ---------- | --------- |
| Client ID  | Integer   |
| Airline ID | Integer   |
| Date       | Date/time |
| Start City | String    |
| End City   | String    |

## Initial User Stories

### Client Records

- As a travel agent user, I want to create a client record so that client
  details can be stored in the system.

- As a travel agent user, I want to update a client record so that incorrect
  or outdated client details can be corrected.

- As a travel agent user, I want to delete a client record so that records
  that are no longer required can be removed.

- As a travel agent user, I want to search for a client record so that I can
  quickly find client information.

### Airline Records

- As a travel agent user, I want to create an airline company record so that
  airline details can be stored in the system.

- As a travel agent user, I want to update an airline company record so that
  company details remain accurate.

- As a travel agent user, I want to delete an airline company record so that
  unused airline records can be removed.

- As a travel agent user, I want to search for an airline company record so
  that I can quickly find airline information.

### Flight Records

- As a travel agent user, I want to create a flight record so that a client
  can be linked to an airline and journey details.

- As a travel agent user, I want to update a flight record so that journey
  details can be corrected.

- As a travel agent user, I want to delete a flight record so that cancelled
  or incorrect flight records can be removed.

- As a travel agent user, I want to search for a flight record so that I can
  quickly find journey information.

### Data Storage

- As a travel agent user, I want records to be saved when the application
  closes so that data is not lost.

- As a travel agent user, I want existing records to be loaded when the
  application starts so that I can continue working with previously saved
  data.

## Planned Project Structure

```txt
travel-record-management-app/
├── data/
├── src/
│   └── record_management_system/
├── tests/
├── README.md
├── requirements.txt
├── pytest.ini
└── pyproject.toml

```

## Planned Project Structure

```txt
travel-record-management-app/
├── data/
├── src/
│   └── record_management_system/
├── tests/
├── README.md
├── requirements.txt
├── pytest.ini
└── pyproject.toml
```

## Development Environment

This project uses Python 3.14.
The Python version is documented in:

```bash
.python-version
```

### Setup

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

### Testing

Run tests with:

```bash
python -m pytest
```

### Linting

This project uses Ruff to support PEP 8 style checks and general Python
code quality.

```bash
python -m ruff check .
```

### Commit Message Standard

This repository includes a commit message hook in `.githooks/commit-msg`.

Commit messages must follow this format: `Subsystem: Short present tense sentence.`

Examples:

```
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

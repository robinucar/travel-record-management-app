# Project Structure Guide

This guide explains what each main file and folder in the repository is used for.

It is intended to help all team members understand the project layout before and during development.

## Repository Overview

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
├── pyproject.toml
├── pytest.ini
├── README.md
└── requirements.txt
```

## Folders

### `.githooks/`

This folder contains custom Git hooks used by the project.

Git hooks are small scripts that run automatically during Git actions.

Current hooks:

```txt
.githooks/commit-msg
.githooks/pre-commit
```

#### `.githooks/commit-msg`

Checks that commit messages follow the required format.

Required format:

```txt
Subsystem: Short present tense sentence.
```

Example:

```txt
Storage: Add JSON file loading.
```

#### `.githooks/pre-commit`

Runs project checks before a commit is created.

Current checks:

```bash
python -m ruff check .
python -m pytest
```

If Ruff or the tests fail, the commit will be stopped.

At the setup stage, the hook allowed commits even if no tests existed yet. Now that tests have been added, team members should expect the test suite to run before commits.

### `data/`

This folder is reserved for local application data files.

The application can use this folder to store generated record data files, such as JSON files.

Possible storage formats discussed for the assignment were:

```txt
JSON
JSONL
Pickle
```

The current storage implementation uses JSON.

The file `.gitkeep` is used only to keep the empty `data/` folder in Git.

Generated data files should not be committed.

### `docs/`

This folder contains project documentation for the team.

Current documentation files:

```txt
docs/git-workflow.md
docs/project-structure.md
```

#### `docs/git-workflow.md`

Explains how team members should use Git, branches, commits, and pull requests.

This includes branch naming, commit message format, pull request expectations, and checks to run before committing.

#### `docs/project-structure.md`

Explains the purpose of each main folder and configuration file.

This document should be updated when new important files, modules, or workflows are added.

### `src/`

This folder contains the application source code.

Current package location:

```txt
src/record_management_system/
```

The project uses a `src` layout, which keeps application code separate from tests, documentation, and configuration files.

### `src/record_management_system/`

This is the main Python package for the application.

Current files:

```txt
src/record_management_system/__init__.py
src/record_management_system/gui.py
src/record_management_system/main.py
src/record_management_system/records.py
src/record_management_system/storage.py
```

#### `__init__.py`

Marks the folder as a Python package.

#### `main.py`

Used as the application entry point.

It creates the main application window and starts the Tkinter event loop.

The application can be run from the repository root with:

```bash
PYTHONPATH=src python -m record_management_system.main
```

#### `gui.py`

Contains the Tkinter graphical user interface.

Current GUI responsibilities include:

```txt
Creating the main application window
Showing the Create Record form
Allowing the user to select Client, Airline, or Flight records
Rendering dynamic input fields for each record type
Calling the backend create_record function
Using the backend get_records function when refreshing the display
Displaying created records in the records list
Formatting records for display
Showing success and error messages to the user
```

The GUI currently covers Robin’s Create Records and Display/Get Records scope.

It does not currently handle:

```txt
Search records
Update records
Delete records
Saving records to file
Loading records from file when the app starts
```

Those areas belong to separate task responsibilities or later integration work.

#### `records.py`

Contains core record management logic.

Current responsibilities include:

```txt
Creating records
Getting/displaying records
Validating record types
Validating required fields
Checking duplicate record IDs
Searching records
Updating records
Deleting records
```

This module works with the internal list of dictionaries required by the assignment.

Example internal structure:

```python
records = [
    {
        "id": 1,
        "type": "client",
        "name": "John Smith",
    }
]
```

#### `storage.py`

Contains file storage logic for record data.

Current responsibilities include:

```txt
Saving records to a JSON file
Loading records from a JSON file
Returning an empty list when no data file exists
Creating parent directories when saving
Validating that loaded data is a list
```

Storage is separate from the GUI and record CRUD logic so it can be tested independently.

### `tests/`

This folder contains unit tests for the application.

Current files:

```txt
tests/__init__.py
tests/test_gui.py
tests/test_records.py
tests/test_storage.py
```

Test files should follow this naming pattern:

```txt
test_*.py
```

#### `tests/test_records.py`

Contains unit tests for record management logic.

This includes tests for:

```txt
Create records
Get/display records
Search records
Update records
Delete records
Validation errors
Duplicate record IDs
```

#### `tests/test_gui.py`

Contains unit tests for GUI helper functions.

Current tests cover formatting Client, Airline, and Flight records for display.

The GUI tests do not open the full Tkinter application window. This keeps the tests simple and reliable.

#### `tests/test_storage.py`

Contains unit tests for file storage logic.

This includes tests for:

```txt
Saving records
Loading records
Handling missing files
Creating parent directories
Handling invalid file structure
```

## Root Files

### `.gitignore`

Defines files and folders that Git should ignore.

This includes:

```txt
.venv/
.pytest_cache/
.ruff_cache/
__pycache__/
data/*.json
data/*.jsonl
data/*.pkl
data/*.pickle
```

This helps prevent local environment files, caches, and generated data from being committed.

### `.python-version`

Documents the Python version used for this project.

Current version:

```txt
3.14.4
```

### `pyproject.toml`

Stores project metadata and tool configuration.

Currently it defines:

```txt
Project name
Project version
Python version requirement
Ruff configuration
```

### `pytest.ini`

Stores pytest configuration.

It tells pytest to:

```txt
Look for tests in the tests folder
Use files named test_*.py
Include src in the Python path during tests
```

### `README.md`

Provides the main project overview.

It should explain:

```txt
What the project is
Current project status
Main requirements
Setup instructions
Testing instructions
Linting instructions
Commit message standard
```

The README is still a working document and should be updated as the project develops, especially when GUI, storage, and final usage instructions are completed.

### `requirements.txt`

Lists Python dependencies required for development.

Current dependencies:

```txt
pytest
ruff
```

Tkinter is not listed in `requirements.txt` because it is normally provided with Python. However, some macOS/Homebrew Python installations may require a separate Tkinter package.

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

## Running the Application

To run the application locally, first activate the virtual environment:

```bash
source .venv/bin/activate
```

Then run the application with:

```bash
PYTHONPATH=src python -m record_management_system.main
```

The project uses a `src` layout, so `PYTHONPATH=src` is needed when running the application directly from the repository root.

## Running Checks

Before committing, always run:

```bash
python -m ruff check .
python -m pytest
```

The pre-commit hook should also run these checks automatically.

## Important Notes for Team Members

Do not commit local virtual environment folders such as `.venv/`.

Do not commit generated cache folders such as `.pytest_cache/` or `.ruff_cache/`.

Do not commit generated data files from the `data/` folder.

Keep source code inside:

```txt
src/record_management_system/
```

Keep unit tests inside:

```txt
tests/
```

For this project, record CRUD logic should generally stay in:

```txt
src/record_management_system/records.py
```

Storage logic should stay in:

```txt
src/record_management_system/storage.py
```

GUI logic should stay in:

```txt
src/record_management_system/gui.py
```

This structure keeps the project simple and easier for all team members to understand.

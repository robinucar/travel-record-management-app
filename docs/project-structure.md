# Project Structure Guide

This guide explains what each main file and folder in the repository is used for.

It is intended to help all team members understand the project layout before development starts.

## Repository Overview

```txt
travel-record-management-app/
├── .githooks/
├── data/
├── docs/
├── src/
├── tests/
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

At the setup stage, the hook allows commits even if no tests exist yet.

### `data/`

This folder is reserved for local application data files.

The application will later save records here using the agreed storage format.

Possible storage formats:

```txt
JSON
JSONL
Pickle
```

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

#### `docs/project-structure.md`

Explains the purpose of each main folder and configuration file.

### `src/`

This folder will contain the application source code.

Current package location:

```txt
src/record_management_system/
```

Application modules will be added here during development.

### `src/record_management_system/`

This is the main Python package for the application.

Current files:

```txt
src/record_management_system/__init__.py
src/record_management_system/main.py
```

#### `__init__.py`

Marks the folder as a Python package.

#### `main.py`

Will be used as the application entry point.

No application functionality has been implemented yet.

### `tests/`

This folder will contain unit tests for the application.

Current files:

```txt
tests/__init__.py
```

Test files should follow this naming pattern:

```txt
test_*.py
```

Examples:

```txt
test_storage.py
test_records.py
test_gui.py
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

It tells pytest to look for tests in the `tests/` folder.

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

The README is not final yet and will be improved as the project develops.

### `requirements.txt`

Lists Python dependencies required for development.

Current dependencies:

```txt
pytest
ruff
```

## Important Notes for Team Members

Do not commit local virtual environment folders such as `.venv/`.

Do not commit generated cache folders such as `.pytest_cache/` or `.ruff_cache/`.

Do not commit generated data files from the `data/` folder.

Before committing, always run:

```bash
python -m ruff check .
python -m pytest
```

The pre-commit hook should also run these checks automatically.

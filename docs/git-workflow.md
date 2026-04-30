# Git Workflow Guide

This guide explains how team members should work with the repository.

It is written for beginners, so the steps are intentionally simple and standardised.

## 1. Clone the Repository

Each team member should first clone the repository from GitHub.

```bash
git clone <repository-url>
```

Then move into the project folder:

```bash
cd travel-record-management-app
```

## 2. Check the Current Branch

Before starting any work, check which branch you are on:

```bash
git branch
```

The active branch will have a `*` next to it.

## 3. Update the Main Branch

Before creating a new branch, make sure your local main branch is up to date:

```bash
git checkout main
git pull origin main
```

## 4. Create a New Branch

Do not work directly on `main`.

Create a new branch for each task:

```bash
git checkout -b feature/short-description
```

Examples:

```bash
git checkout -b feature/client-records
git checkout -b feature/storage-module
git checkout -b feature/gui-layout
git checkout -b test/storage-tests
git checkout -b docs/update-readme
```

## 5. Branch Naming Standard

Branch names should use lowercase letters and hyphens.

Recommended formats:

```txt
feature/short-description
fix/short-description
test/short-description
docs/short-description
refactor/short-description
```

Examples:

```txt
feature/client-records
feature/airline-records
feature/flight-records
feature/gui-layout
feature/storage-module
test/storage-tests
docs/update-readme
fix/storage-load-error
```

Avoid branch names like:

```txt
mybranch
RobinWork
new-stuff
final-version
changes
```

## 6. Make Changes Locally

After creating a branch, make your changes in the code editor.

Check changed files with:

```bash
git status
```

## 7. Run Checks Before Committing

Before committing, run the tests:

```bash
python -m pytest
```

Run the linter:

```bash
python -m ruff check .
```

Both commands should pass before committing.

## 8. Stage Files

Add changed files to the commit:

```bash
git add .
```

Then check what will be committed:

```bash
git status
```

## 9. Commit Message Standard

Commit messages must follow this format:

```txt
Subsystem: Short present tense sentence.
```

Examples:

```txt
Project: Initialise repository structure.
Records: Add client record validation.
Storage: Add JSON file loading.
GUI: Add main window layout.
Tests: Add storage unit tests.
Docs: Update Git workflow guide.
```

The first line must:

1. Start with a subsystem prefix
2. Use a colon after the prefix
3. Use a capital letter after the colon
4. End with a period

Good example:

```bash
git commit -m "Storage: Add JSON file loading."
```

Bad examples:

```bash
git commit -m "added storage"
git commit -m "storage changes"
git commit -m "Storage add json loading"
git commit -m "storage: add json loading"
```

## 10. Push the Branch

Push your branch to GitHub:

```bash
git push origin branch-name
```

Example:

```bash
git push origin feature/storage-module
```

## 11. Open a Pull Request

After pushing your branch:

1. Open the repository on GitHub.
2. Click the Compare & pull request button.
3. Add a clear title.
4. Explain what you changed.
5. Request review from another team member.

## 12. Pull Request Title Standard

Pull request titles should be clear and short.

Examples:

```txt
Add client record model
Add JSON storage module
Add GUI layout
Add storage unit tests
Update README setup instructions
```

## 13. Pull Request Description Template

Use this format in the pull request description:

```md
## Summary

Briefly explain what changed.

## Checks

- [ ] I ran `python -m pytest`
- [ ] I ran `python -m ruff check .`
- [ ] I checked that my branch name follows the project standard
- [ ] I checked that my commit message follows the project standard

## Notes

Add any useful notes for reviewers.
```

## 14. Do Not Merge Your Own Pull Request

Another team member should review the pull request before it is merged.

This helps reduce mistakes and keeps the group work more consistent.

## 15. Keep Commits Small

Each commit should represent one logical change.

Good examples:

```txt
Storage: Add JSON file loading.
Tests: Add storage unit tests.
Docs: Update setup instructions.
```

Avoid mixing unrelated changes in one commit.

For example, do not combine GUI changes, storage changes, and documentation updates in one commit unless they are part of the same logical change.

## 16. If Something Goes Wrong

If you are unsure, do not force push or delete branches.

Ask the team before running advanced Git commands such as:

```bash
git reset
git rebase
git push --force
```

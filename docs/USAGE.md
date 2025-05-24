# Candidate Info Tool

This command-line tool allows you to collect and manage information about political candidates.

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Commands
- `scrape <urls>` – Scrape candidate pages and store profiles.
- `list` – List stored candidates.
- `compare <name1> <name2> <issues...>` – Compare candidates on specific issues.
- `recommend <district> <issue=stance ...>` – Recommend candidates based on location and preferences.

Example:
```bash
python -m src.cli scrape https://example.com/candidate1 https://example.com/candidate2
python -m src.cli list
python -m src.cli compare "Jane Doe" "John Smith" healthcare education
python -m src.cli recommend "District 1" "taxes=lower" "environment=pro"
```

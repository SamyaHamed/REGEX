# Regex in Python

A collection of Python scripts for learning and practicing regular expressions using the built-in `re` module.

## Project Structure

```
Regex/
├── codes/
│   ├── test.py        # Core regex examples
│   └── exercises.py   # Practice exercises
├── venv/              # Virtual environment
├── .gitignore
└── README.md
```

## Examples (`codes/test.py`)

Covers fundamental `re` module usage:

- **`re.findall`** — Extract emails and phone numbers from text
- **`re.sub`** — Replace digits in a string
- **`re.fullmatch`** — Validate that a string matches a pattern entirely
- **`re.finditer`** — Iterate over matches (e.g. filenames with extensions)
- **`re.search` with groups** — Extract content from HTML tags
- **Capture groups & back-references** — Reformat dates (`2026-02-11` to `11/02/2026`)

## Exercises (`codes/exercises.py`)

Six exercises progressing from basic to challenging:

| # | Topic | Concepts |
|---|-------|----------|
| 1 | Find consecutive repeated words | Back-references |
| 2 | Extract valid hashtags | Character classes, capture groups |
| 3 | Validate a strong password | Lookaheads, anchors |
| 4 | Reformat phone numbers | `re.sub` with group references |
| 5 | Extract text inside parentheses | Non-greedy quantifiers |
| 6 | Extract valid prices | Alternation, optional groups |

## Getting Started

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux

# Run the examples
python codes/test.py

# Run the exercises
python codes/exercises.py
```

## Requirements

- Python 3.x (no external dependencies)

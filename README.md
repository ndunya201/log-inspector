# Log Inspector

A Python command-line tool that parses system log files, filters by error type
or user, generates summaries, and exports reports as CSV or HTML.

Built as a portfolio project extending the labs from the
**Google IT Automation with Python** course (Coursera).

---

## What it does

- Parse any ticky-format system log file
- Filter logs by error type or specific user
- Generate ranked error summaries and per-user statistics
- Export reports as CSV or HTML

---

## Project Structure
```
log-inspector/
├── log_inspector.py      # main entry point
├── parser.py             # log parsing and filtering functions
├── reporter.py           # CSV and HTML report generation
├── tests/
│   └── test_parser.py    # unit tests
├── sample_logs/
│   └── syslog.log        # sample log file
└── README.md
```

---

## Usage

**Summary report (printed to screen)**
```python
run_inspector('sample_logs/syslog.log', mode='summary', output='print')
```

**Errors only**
```python
run_inspector('sample_logs/syslog.log', mode='errors-only')
```

**Filter by user**
```python
run_inspector('sample_logs/syslog.log', mode='user', username='blossom')
```

**Export to CSV**
```python
run_inspector('sample_logs/syslog.log', mode='summary', output='csv')
```

**Export to HTML**
```python
run_inspector('sample_logs/syslog.log', mode='summary', output='html')
```

---

## Sample Output

**Error Summary**
```
  8x  Tried to add information to closed ticket
  3x  Timeout while retrieving information
  3x  Connection to DB failed
  2x  The ticket was modified while updating
  2x  Permission denied while closing ticket
  2x  Ticket doesn't exist
```

**User Summary**
```
  Username               INFO  ERROR
  ----------------------------------
  ac                        0      2
  ahmed.miller              1      1
  blossom                   2      2
  oren                      1      3
  rr.robinson               2      0
```

---

## Skills demonstrated

- Regular expressions for log parsing
- Modular Python design (separation of concerns)
- CSV and HTML report generation
- Unit testing with `unittest`
- File I/O and data processing

---

## Background

This project is based on labs from the
[Google IT Automation with Python Professional Certificate](https://www.coursera.org/professional-certificates/google-it-automation).
The original lab used a single monolithic script. This version refactors that
into a modular, testable, reusable tool.
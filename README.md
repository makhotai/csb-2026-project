# csb-2026-project

This repository contains a project for [Cyber Security Base course](https://cybersecuritybase.mooc.fi). It is based on my [recipes app for TKT20019](https://github.com/makhotai/baking_recipes). The project is implemented using Flask-library and SQLite, and has five intentional vulnerabilities from OWASP Top 10 (2021) list and their commented out fixes.

## Requirements

* Python 3.10 or newer
* Flask
* SQLite: macOS/Linux usually include the `sqlite3` command and Python itself can also initialize the database

## Installation

### macOS/Linux

Create virtual environment:
```
cd csb-2026-project
python3 -m venv venv
source venv/bin/activate
```

Install Flask-library:
```
pip install flask
```

Repository does not include `database.db` so you need to create and initialize dataabse by using these commands:
```
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```

### Windows PowerShell

Create virtual environment:
```
cd csb-2026-project
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install Flask-library:
```
pip install flask
```

Repository does not include `database.db` so you need to create and initialize database by using these commands:
```
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```
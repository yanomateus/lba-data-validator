LBA Data Validator
==================


how to contribute
-----------------

Install system requirements (if you don't have them already):
1. PostgreSQL 10.9+
2. Python 3.6+

Create a development database:
```bash
psql>>> CREATE ROLE dev WITH LOGIN PASSWORD 'dev';
psql>>> CREATE DATABASE lba OWNER dev;
```

In a virtual environment, install the project's dependencies:
```bash
(venv) $ pip install -e ."[testing]"
```

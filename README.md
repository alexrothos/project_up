# project_up
This is a repo for the assignment of UP Hellas.

The api make a request to a specific url and handles the received data.
For the database I used PostgreSQL, but the URI it can be changed easily to match any other relational database of your choice.
The api is running on port 9500 to avoid any conflict with other popular services.

Download the repo and in the app's folder open a terminal.

## Application map

```bash
projectUp/
|-- project_up.py
|-- app/
|   |-- __init__.py
|   |-- routes/
|   |   |-- __init__.py
|   |   |-- routes.py
|   |-- schemas/
|   |   |-- __init__.py
|   |   |-- schemas.py
|   |-- models/
|   |   |-- __init__.py
|   |   |-- models.py
|-- tests/
|   |-- __init__.py
|   |-- test_routes.py
|   |-- test_schemas.py
|   |-- test_models.py
```


## Creating a virtual environment:

In a command line that can run python 3.7 and above, run 

```bash
python -m venv venv
```

## Installation of dependencies: 

```bash
pip install -r requirements.txt
```

## Database initialization:

For the creation of the data base
```bash
flask db init
```

Inserting the database models
```bash
flask db migrate
```

Passing the changes to database
```bash
flask db upgrade
```

## Running the application:

```bash
flask run
```

### Build with:

[![Python](https://img.shields.io/badge/Python-3.x-brightgreen.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-brightgreen)](https://flask.palletsprojects.com/en/1.1.x/)
[![Marshmallow](https://img.shields.io/badge/Marshmallow-3.x-brightgreen)](https://marshmallow.readthedocs.io/en/stable/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.3.x-brightgreen)](https://docs.sqlalchemy.org/en/13/index.html)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13.x-brightgreen)](https://www.postgresql.org/docs/13/index.html)

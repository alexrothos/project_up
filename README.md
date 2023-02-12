# project_up
This is a repo for the assignment of UP Hellas.

Download the repo and in the app's folder open a terminal.


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
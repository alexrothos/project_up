# project_up
This is a repo for the assignment of UP Hellas.

Download the repo and in the app's folder open a terminal.

## Creating a virtual environment

In a command line that can run python 3.7 and above, run 
```python -m venv venv```

## Installing the requirements 

```pip install -r requirements.txt```

## Database initialization

For the creation of the data base
```flask db init```

Inserting the database models
```flask db migrate```

Passing the changes to database
```flask db upgrade```

## Running the application

```flask run```
# Flask Validations and Constraints

## Learning Goals

- Adding database constraints

- Using the sqlalchemy `validates` decorator

- Handling validations in routes

## Getting Started

Being with:

```
pipenv install
pipenv shell
cd server

flask db init
flask db migrate -m "initialize database"
flask db upgrade
```
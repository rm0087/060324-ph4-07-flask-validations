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

## Exercises

Add these validations:

1. The `year_joined` must be between 1970 and the current year.

2. Username cannot include naughty words like 'heck', 'frack', or 'bish'.

3. Add a validation so that `phone_number` includes 10 characters (exclude internation numbers for now).
    Bonus: The `phone_number` should also reformat to remove dashes before validating
    Bonus: The `phone_number` should throw an error if any alphabetical characters are included (use regex)

4. Address must include the words 'Street', 'Avenue', or 'Road'.
    Bonus: Add a validation so addresses must include a 5 digit zipcode at the end (you can use a slice to get the last characters)...
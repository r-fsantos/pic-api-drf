# poc-api-drf
POC to practice poetry, django, drf and unit testing

## Useful commands

- Run server

```shell
poetry run python manage.py runserver

poetry run ./manage.py runserver
```

- Activate Django `repl`:

```shell
poetry run python manage.py shell

poetry run ./manage.py shell
```

- Creates migrations

```shell
poetry run python manage.py makemigrations

poetry run ./manage.py makemigrations
```

- Applies migrations

```shell
poetry run python manage.py migrate

poetry run ./manage.py migrate
```

## Tech debts

- Create `requirements.txt` files separated by `prod` and `dev` environments

# poc-api-drf
POC to practice poetry, django, drf and unit testing

## Useful commands

- Create a Django App

```shell
poetry run ./manage.py `app_name`
```

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

- Create new admin users

```shell
poetry run python manage.py createsuperuser --email admin@example.com --username admin
```

## Tech debts

- Create `requirements.txt` files separated by `prod` and `dev` environments

# Database

## Models

SQLAlchemy model classes are contained in [models.py](src/hackermatch/db/models.py)

## Migrations

Migrations are managed with [Alembic](https://alembic.sqlalchemy.org/en/latest/).

After updating the SQLAlchemy models, run `python3 -m alembic -x url=<db_url> revision --autogenerate -m "<message>"`

To apply migrations to a database, run `python3 -m alembic -x url=<db_url> upgrade head`

Remember to replace `<db_url>` with the url of the databse to use for migrations. For example, "postgresql://hackermatch:hackermatch@localhost/hackermatch" would be a valid url when using the included [compose](../docker-compose.yml) deployment.

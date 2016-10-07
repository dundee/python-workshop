from contextlib import contextmanager
import sqlite3


@contextmanager
def db_connection(db_config: dict):
    connection = sqlite3.connect(db_config['file'])
    cursor = connection.cursor()

    yield cursor

    connection.commit()
    connection.close()

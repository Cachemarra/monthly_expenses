# %% Management of database resources
# A CRUD
import sqlite3 as sql3
from logging_config import log


# %% Generating the class
class Connection:
    _DATABASE = "expenses"
    _USERNAME = "username"
    _PASSWORD = "root"
    _DB_PORT = 5432
    _HOST = 'localhost'
    _connection = None
    _cursor = None

    # ====================
    def get_connection(cls):
        # If there's no connection, create one.
        if cls._connection is None:
            try:
                cls._connection = sql3.connect(f"{cls._DATABASE}.db")
                log.debug(f"[SUCCESS] Connected to database {cls._connection}")

                return cls._connection

            except Exception as err:
                log.error(f"Error connecting to database. Error: {err}")

        else:
            return cls._connection

    @classmethod
    def create_table(cls):
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
            dataID INTEGER PRIMARY KEY,
            InOut TEXT NOT NULL,
            Ammount REAL NOT NULL,
            Category TEXT NOT NULL,
            Description TEXT,
            Month TEXT NOT NULL
            )
            """
        )
        log.debug("Table was not found, A new one was created.")

    @classmethod
    def add_expense(cls, ammount: int = 0, category: str = "", description: str = "", month="Decenuary"):
        """
        Function to prepare a query to add an expense to the database.
        """
        conn = cls.get_connection()
        cursor = conn.cursor()

        try:
            conn.execute(
                f"""
                INSERT INTO expenses ( ammount, category, description, month) VALUES({ammount}, {category}, {description}, {month})
                """
            )
            conn.commit()
        except Exception as err:
            log.error(f"An error has ocurred: {err}")

    @classmethod
    def read(cls, table, **kwargs):
        conn = cls.get_connection()
        cursor = conn.cursor()
        fields = ' AND '.join(f"{k} = ?" for k in kwargs)
        cursor.execute(f'SELECT * FROM {table} WHERE {fields}', tuple(kwargs.values()))
        return cursor.fetchall()

    @classmethod
    def update(cls, table, id, **kwargs):
        conn = cls.get_connection()
        cursor = conn.cursor()
        fields = ', '.join(f"{k} = ?" for k in kwargs)
        cursor.execute(f'UPDATE {table} SET {fields} WHERE id = ?', (*kwargs.values(), id))
        conn.commit()

    @classmethod
    def delete(cls, table, **kwargs):
        conn = cls.get_connection()
        cursor = conn.cursor()
        fields = ' AND '.join(f"{k} = ?" for k in kwargs)
        cursor.execute(f'DELETE FROM {table} WHERE {fields}', tuple(kwargs.values()))
        conn.commit()









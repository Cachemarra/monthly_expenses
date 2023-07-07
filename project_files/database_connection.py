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

    











    def init(self, name):
        self.connection = sqlite3.connect(f"{name}.db")
        
        
    def create_table(self):
        self.execute(
            """ CREATE TABLE IF NOT EXISTS
            """
        )


    def add_expense(self, ammount:int=0, category:str="", description:str=""):
        try:
            self.connection(
                f"""
                """
            )
        except Exception as err:
            log.error(f"An error has ocurred: {err}")
        pass
    
    
    def add_income(self, ammount:int=0, category:str="", description:str=""):
        try:

        except Exception as err:
            log.error(f"An error has ocurred: {err}")
        pass










# %% Management of database resources
# A CRUD
import sqlite3
from logging_config import log


# %% Generating the class
class SQLConnection:
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










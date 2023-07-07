# %% Imports


class Entry:
    def __init__(self,
                 dataId: str = None,
                 ammount: float = 0.0,
                 category: str = "NULL",
                 description: str = "NULL",
                 month: str = "NULL"
                 ):
        
        self._dataId = dataId
        self._ammount = ammount
        self._category = category
        self._description = description
        self._month = month

    def __str__(self):
        return f"Data ID: {self._dataId}, ammount: {self._ammount}, category: {self._category}, description: {self._description}, month: {self._month}"

    # %% Setters and getters
    @property
    def dataId(self):
        return self._dataId

    @property
    def ammount(self):
        return self._ammount

    @property
    def category(self):
        return self._category

    @property
    def description(self):
        return self._description

    @property
    def month(self):
        return self._month

    @dataId.setter
    def dataId(self, value):
        self._dataId = value

    @ammount.setter
    def ammount(self, value):
        self._ammount = value

    @category.setter
    def category(self, value):
        self._category = value
        
    @description.setter
    def description(self, value):
        self._description = value
        
    @month.setter
    def month(self, value):
        self._month = value
    
    

class EntryDAO:
    # Class attributes
    _SELECT = "SELECT * FROM %s ORDER BY dataId"
    _INSERT = "INSERT INTO %s (ammount, category, description, month) VALUES(%s, %s, %s, %s)"
    _UPDATE = "UPDATE %s SET ammount = %s, category = %s, description = %s, month = %s WHERE dataId = %s"
    _DELETE = "DELETE FROM %s WHERE dataId = %s"
    
    @classmethod
    def select(cls) -> Entry:
        with


    
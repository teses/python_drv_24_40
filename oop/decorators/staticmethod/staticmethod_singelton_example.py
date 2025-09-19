"""

Singelton Pattern

Es stellt sicher, das wenn man ein Objekt instanziert, das es immer das selbe ist

"""

class DataConnection():

    _instance = None # Klassenattribut für instanz

    def __init__(self, value):
        self.value = value

    # statische Factory Methode
    @staticmethod
    def get_instanz(value):
        if DataConnection._instance is None:
            DataConnection._instance = DataConnection(value)
        return DataConnection._instance


## normale verwendung ohne singelton
"""
connection1 = DataConnection("Erste Instanz")
connection2 = DataConnection("Zweite Instanz")
print(connection1.value)
print(connection2.value)
"""
##############################################
# singelton
connection1 = DataConnection.get_instanz("Erste Instanz")
connection2 = DataConnection.get_instanz("Zweite Instanz")
print(connection1.value)
print(connection2.value)

print(connection1 is connection2)

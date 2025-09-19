"""

Dunder-Methoden

fangen mit__ und enden mit __
__str__

"""

# Konstruktor - Erstellt eine neue Instanz
class Person:

    def __init__(self, name):
        self.name = name

p = Person("bob")
print(p.__dict__)

# Darstellung
# __str__ - Für menschenlesbare Darstellung
# __repr__ -  Darstellung für die Entwickler
class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"name: {self.name}"

    def __repr__(self):
        return f"Person(\"{self.name}\")"

p = Person("Max")
print(p) # __str__
print(repr(p)) # __repr__


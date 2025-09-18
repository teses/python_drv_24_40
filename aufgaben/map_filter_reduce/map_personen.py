"""
- Verwende map(), um eine neue Liste von Dictionaries zu erzeugen.
- Füge zu jeder Person einen Schlüssel "anrede" hinzu:

    "Frau" für Personen, deren Name auf a endet.
    "Herr" für alle anderen.

- Erhöhe gleichzeitig das Alter jeder Person um 1 Jahr.

Gib die neue Liste aus.

Tipp: mit einer lambda funktion wird es unleserlich. Verwende eine callback funktion
"""

personen = [
    {"name": "Alice", "alter": 25},
    {"name": "Bob", "alter": 30},
    {"name": "Charlie", "alter": 35},
    {"name": "Jonathan", "alter": 25},
    {"name": "Anna", "alter": 22},
    {"name": "lena", "alter": 25},
    {"name": "Mark", "alter": 19},
    {"name": "Alexander", "alter": 29},
    {"name": "Elisa", "alter": 33},
    {"name": "Joshua", "alter": 25},
    {"name": "Emma", "alter": 41},
    {"name": "Herta", "alter": 17},

]

# Funktion, die ein Dictionary verändert
def myTransform(person):
    anrede = "Frau" if person["name"].endswith("a") else "Herr"
    return {
        **person,
        "alter": person["alter"] + 1,
        "anrede": anrede
    }

# ohne lambda
personen_anrede = list(map(myTransform, personen))
for person in personen_anrede:
    print(person)

print("-"*50)

# mit lambda
personen_anrede2 = list(map(lambda person: {**person, "anrede": "Frau" if person["name"].endswith("a") else "Herr"}, personen))
for person in personen_anrede2:
    print(person)





"""

    Aufgabe: Eigene Iterator-Klasse für Personenliste

    __iter__() und __next__() implementieren

    Es sollen nur die Namen zurückgegeben werden
"""

personen = [
    {"name": "Anna", "alter": 30},
    {"name": "Bernd", "alter": 25},
    {"name": "Clara", "alter": 40}
]

class PersonenIterator:
    pass


for name in PersonenIterator(personen):
    print(name)

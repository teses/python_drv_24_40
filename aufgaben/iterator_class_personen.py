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

    def __init__(self, personen_liste: list[dict]):
        self.personen_liste = personen_liste
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.personen_liste):
            raise StopIteration

        person = self.personen_liste[self.index]
        name = person["name"]
        self.index += 1
        return name

class PersonenIterator2:
    def __init__(self, personen_liste: list[dict]):
        self._personen = personen_liste
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._personen):
            person = self._personen[self._index]
            self._index += 1
            return person["name"]

        else:
            raise StopIteration

for name in PersonenIterator(personen):
    print(name)

for name in PersonenIterator2(personen):
    print(name)
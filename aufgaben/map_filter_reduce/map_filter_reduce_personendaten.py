"""

Ausgangsdaten
- Wir nehmen eine Liste von Dictionaries (oder Objekten) mit Personeninformationen:

Aufgabenstellung
- Finde alle Personen, die in Berlin wohnen.
- Extrahiere nur die Namen dieser Berliner Personen.
- Berechne das Gesamtgehalt aller Berliner Personen.

"""
from functools import reduce

personen = [
    {"name": "Anna", "alter": 23, "stadt": "Berlin", "gehalt": 3200},
    {"name": "Ben", "alter": 31, "stadt": "München", "gehalt": 4100},
    {"name": "Carla", "alter": 19, "stadt": "Hamburg", "gehalt": 1500},
    {"name": "David", "alter": 45, "stadt": "Berlin", "gehalt": 5200},
    {"name": "Eva", "alter": 29, "stadt": "München", "gehalt": 3800},
]
# berliner
berliner_personen = list(filter(lambda person: person["stadt"] == "Berlin", personen))
print(berliner_personen)

# namen
berliner_personen_namen = list(map(lambda person: person["name"], berliner_personen))
print(berliner_personen_namen)

#
berliner_personen_gehalt_summe = reduce(lambda s, o: s + o["gehalt"], berliner_personen, 0)
print(berliner_personen_gehalt_summe)

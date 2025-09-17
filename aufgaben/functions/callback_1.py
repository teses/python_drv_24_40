"""
Aufgabe: Datenbearbeitung mit Callback

Du hast eine Liste von Dictionaries, die Informationen über Spieler enthalten:
"""

players = [
    {"name": "Alice", "score": 120, "level": 5, "games" :2},
    {"name": "Bob", "score": 150, "level": 7, "games" :2},
    {"name": "Charlie", "score": 90, "level": 3, "games" :2},
]

"""
Schreibe eine Funktion process_players(data, callback), die:
- Die Liste data durchläuft.
- Auf jeden Spieler das übergebene callback anwendet.
- Das Ergebnis in einer neuen Liste zurückgibt.

Der Callback soll eine Funktion sein, die ein Spieler-Dictionary nimmt und es bearbeitet oder transformiert.

# Score verdoppeln
# Level erhöhen
# Nur Namen extrahieren
# durchschnitt von score/games als neuen dictionary eintrag hinzufügen
"""

def process_players(data, callback):
    pass


def double_score(player):
    return player


# Anwendung der Funktion mit Callback
new_players = process_players(players, double_score)
print("Score verdoppelt:", new_players)



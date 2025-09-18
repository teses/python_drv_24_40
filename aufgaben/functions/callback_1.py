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

# Tipp:
# 1. eine leere liste erstellen
# 2. daten durchlaufen und an callback übergeben
# 3. Ergebnis an der Liste anhängen
# 4. return ergebnis
def process_players(data, callback):
    return [callback(player) for player in data]

def process_players2(data, callback):
    result = []
    for player in data:
        result.append(callback(player))
    return result
 
def double_score(player):
    player["score"] *= 2
    return player

def double_score2(player):
    return {**player, "score": player["score"] * 2}

def double_score3(player):
    # Neues Dictionary manuell erstellen
    return {
        "name": player["name"],
        "score": player["score"] * 2,
        "level": player["level"]
    }

def increase_level(player):
    player["level"] += 1
    return player

def extract_name(player):
    return player["name"]

def calculate_average_score(player):
    player["average_score"] = player["score"] / player["games"]
    return player

# Anwendung der Funktion mit Callback
new_players = process_players2(players, double_score2)
print("Score verdoppelt:", new_players)

#Test increase_level
print("-" * 50)
new_players = process_players(players, increase_level)
print("Level erhöht:", new_players)

#Test extract_name
print("-" * 50)
new_players = process_players(players, extract_name)
print("Namen extrahiert:", new_players)

#Test extract_name
print("-" * 50)
new_players = process_players(players, lambda n: n["name"])
print("Namen extrahiert mit lambda:", new_players)


#Test calculate_average_score
print("-" * 50)
new_players = process_players(players, calculate_average_score)
print("Durchschnittscore:", new_players)

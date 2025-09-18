
personen = [
    {"name": "Anna", "alter": 25},
    {"name": "Bernd", "alter": 30},
    {"name": "Clara", "alter": 22},
]

# Nur ein bestimmtes Feld extrahieren mit normaler callback
def extract_name(player):
    return player["name"]

neue_personen = list(map(extract_name, personen))
print(neue_personen)

# Nur ein bestimmtes Feld extrahieren mit lambda
namen = map(lambda p: p["name"], personen)
print(list(namen))

# key hinzufügen - das alter als neuen key: neuesalter + 1
neue_personen = list(map(  lambda p: {"name": p["name"], "alter": p["alter"], "alterneu": p["alter"] + 1 }     , personen))
print("alterneu + 1", neue_personen)

# key hinzufügen mit ** operator
neue_personen = list(map(  lambda p: {**p, "alterneu": p["alter"] + 1 }, personen))
print("alterneu + 1 mit **", neue_personen)

# Werte verändern
# Alter +1 (z. B. Geburtstag)
neue_personen = list(map( lambda p: {**p, "alter": p["alter"] + 1 }, personen))
print("alter + 1", neue_personen)

# transformieren in einen String
neue_personen = list(map( lambda p: f"{p['name']} ist {p['alter']} Jahre alt", personen))
print( neue_personen)


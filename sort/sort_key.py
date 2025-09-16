

##########################################################################################
# Sortierung nach Länge mit Callback Funktion
Obstkorb = ["Banane", "Zitrone", "Birne", "Kiwi", "Banane", "AI"]

# callback funktion
def obst_sorter(obst):
    return len(obst)

Obstkorb.sort(key=obst_sorter)
print(Obstkorb)

##########################################################################################
# Sortierung nach Länge mit eingebauter
Obstkorb2 = ["Banane", "Zitrone", "Birne", "Kiwi", "Banane", "AI"]
Obstkorb2.sort(key=len)
print(Obstkorb2)

##########################################################################################
# Sortierung nach Länge mit lambda
Obstkorb3 = ["Banane", "Zitrone", "Birne", "Kiwi", "Banane", "AI"]
Obstkorb3.sort(key=lambda obst : len(obst))
print(Obstkorb2)
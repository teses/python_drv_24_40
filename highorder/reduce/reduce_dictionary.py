
from functools import reduce

obstkorb = [
    {"name": "Banane", "menge": 25, "kalorien": 89},
    {"name": "Birne", "menge": 40, "kalorien": 57},
    {"name": "Apfel", "menge": 31, "kalorien": 52},
    {"name": "Kiwi", "menge": 29, "kalorien": 61}
]

# summe aller kalorien
gesamtkalorien = reduce( lambda s, o: s + o["kalorien"] , obstkorb, 0)
print(gesamtkalorien)

# obst mit der größten menge - max problem
highest_menge = reduce(lambda s, o: s if s["menge"] > o["menge"] else o, obstkorb)
print(highest_menge)

# alle namen als komma
names = reduce(lambda x,y : x + ", " + y["name"], obstkorb, "").lstrip(", ")
print(names)

# durchschnitt der kalorien von den vier Früchten Banane,...
durchschnitt = reduce( lambda s, o: s + o["kalorien"] , obstkorb, 0) / len(obstkorb)
print(durchschnitt)

# durchschnitt der kalorien von allen Früchten
#   sum(menge * kalorien) /  menge aller früchte
# Mega Lösung -> Alles in einer Zeile
average_calories_of_all = reduce(lambda s, o: s + (o["kalorien"] * o["menge"]), obstkorb, 0) / reduce(lambda s, o: s + o["menge"], obstkorb, 0)
print(average_calories_of_all)

#
gesamtkalorienAlle = reduce(lambda s, o: s + o["kalorien"]*o["menge"], obstkorb, 0)
mengeAlle = reduce(lambda s, o: s + o["menge"], obstkorb, 0)
print(gesamtkalorienAlle/mengeAlle)

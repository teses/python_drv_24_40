

data = [
    ("Bob", 25, 90),
    ("Alice", 25, 80),
    ("Charlie", 20, 85)
]
##################################################################################################
# eine callback funktion, die erst nach dem zweiten Eintrag (alter) und dann nach dem dritten Eintrag (Gewicht) sortiert
# Wichtig! die Funktion muss nun ein Tupel zurückgeben
def meine_sortierung(row):
    return (row[1], row[2])

dataSorted =sorted(data, key=meine_sortierung)

for a in dataSorted:
    print(a)

##################################################################################################
# nach alter aufsteigend, Gewicht absteigend
# Trick: durch die negation des Gewichts wird negativ sortiert => dadurch ist es rückwärts
# Nachteil: funktioniert nicht bei Strings direkt. man benötigt eun Trick
print("-"*50)
def meine_sortierung2(row):
    return (row[1], row[2])

dataSorted2 = sorted(data, key=meine_sortierung2)

for a in dataSorted2:
    print(a)

##################################################################################################
# nach alter aufsteigend, Name absteigend
# Trick: durch die negation des Gewichts wird negativ sortiert => dadurch ist es rückwärts
print("-" * 50)

def meine_sortierung3(row):
    return (row[1], -ord(row[0][0]))  # Trick um Strings doch rückwärts zu sortieren

dataSorted3 = sorted(data, key=meine_sortierung3)

for a in dataSorted3:
    print(a)



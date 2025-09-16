"""

Teilaufgaben

Sortiere die Liste der Bücher nach Erscheinungsjahr aufsteigend.
Sortiere die Liste der Bücher nach der Länge des Titels.
Sortiere die Liste der Bücher nach Autor alphabetisch, und wenn der Autor gleich ist, dann nach Erscheinungsjahr absteigend.

Herausforderung
Sortiere die Liste der Bücher nach Erscheinungsjahr aufsteigend und nach Author absteigend

"""
buecher = [
    {"titel": "Der Prozess", "autor": "Franz Kafka", "jahr": 1925},
    {"titel": "Faust", "autor": "Johann Wolfgang von Goethe", "jahr": 1808},
    {"titel": "Die Verwandlung", "autor": "Franz Kafka", "jahr": 1915},
    {"titel": "Die Physiker", "autor": "Friedrich Dürrenmatt", "jahr": 1962},
    {"titel": "Homo Faber", "autor": "Max Frisch", "jahr": 1957},
]

# nach Erscheinungsjahr aufsteigend.
buecher_sorted = sorted(buecher, key=lambda buch: buch["jahr"])
print("Erscheinungsjahr aufsteigend")
for buch in buecher_sorted:
    print(buch)

print("-" * 50)

# Nach Länge des Titels
buecher_sorted = sorted(buecher, key=lambda buch: len(buch["titel"]))
print("Länge des Titels")
for buch in buecher_sorted:
    print(buch)

print("-" * 50)

# Nach Autor alphabetisch, dann Erscheinungsjahr absteigend
buecher_sorted = sorted(buecher, key=lambda buch: (buch["autor"], -buch["jahr"]))
print("Autor alphabetisch, Erscheinungsjahr absteigend")
for buch in buecher_sorted:
    print(buch)

print("-" * 50)


##################################
# Jahr aufsteigend, Autor absteigend
# quick and dirty
buecher_sorted = sorted(buecher, key=lambda buch: (buch["jahr"], -ord(buch["autor"][0])))
print("Erscheinungsjahr aufsteigend, Autor absteigend")
for buch in buecher_sorted:
    print(buch)

print("-" * 50)

##################################
# Jahr aufsteigend, Autor absteigend
# mit mehrfacher sortierung nacheinander
buecher_sorted = sorted(buecher, key=lambda buch: (buch["jahr"], buch["autor"]))
buecher_sorted = sorted(buecher_sorted, key=lambda buch: buch["autor"], reverse=True)
buecher_sorted = sorted(buecher_sorted, key=lambda buch: buch["jahr"])

for buch in buecher_sorted:
    print(buch)







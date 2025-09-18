"""

    Iteratoren

    - zentrales Konzept um daten schrittweise zu durchlaufen

    Grundidee:
    Ein Iterator ist ein Objekt, das man "iterieren" kann in einer for-Schleife

    Iterable: ein Objekt, das ein Iterator-Objekt erzeugen kann (listen, tupel, set, strings, dictonary)
    Iterator: Das ist eigentliche Objekt, das weiß wie mann das nächste Element bekommt

    Ein Objekt ist dann iterierbar, wenn wir die Methode __iter__() implementieren und einen iterator zurückgibt
    Ein Iterator kann noch die Methode __next__(), die das nächste Element liefert und am Ende eine StopIteration auswirft


    Es ist wie ein Buch
    - iter() - Buch aufschlagen und zur ersten Seite gehen
    - next() - lese die aktuelle seite und gehe zur nächsten
    - StopIteration - Buch zu Ende
"""

zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    print(zahl)

for i in range(5):
    print(i)

###########################################################################################
## Wie funktioniert das intern
zahlen = [1, 2, 3, 4, 5]

# 1. Python erstellt ein Iterator
iterator = iter(zahlen)

# 2. Python holt sich immer das nächste Element mit next() , sonst StopIteration
while True:
    try:
        zahl = next(iterator)
        print(zahl)
    except StopIteration:
        break

# denk an das Buch!!
###########################################################################################
farben = ["rot", "grün", "blau"]

iterator = iter(farben)

print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator)) # StopIteration Liste zu ende

########################################

zahlen_iter = iter(range(3))
print(next(zahlen_iter))
print(next(zahlen_iter))
print(next(zahlen_iter))
#print(next(zahlen_iter)) # StopIteration Liste zu ende

"""
Ein Set Comprehension in Python ist eine sehr kompakte Möglichkeit,
Mengen (set) zu erstellen – ähnlich wie List Comprehensions,
nur dass die Ergebnisse in einer Menge gesammelt werden.

Durch die Nutzung der geschweiften Klammern nicht mit Dictionary Comprehensions verwechseln.

zur Erinnerung sets:
- unsortiert
- keine doppelten einträgen

Vergleich zu anderen Comprehensions

- List Comprehension: [] → behält Reihenfolge, erlaubt Duplikate
- Set Comprehension: {} → keine Reihenfolge, entfernt Duplikate
- Dict Comprehension: {key: value, ...}

"""

# alle quadrate - wie list comprehensions
quadrate = {x**2 for x in range(10)}
print(quadrate)

# Mit Bedingung (nur gerade Quadratzahlen)
gerade_quadrate = {x*x for x in range(10) if x % 2 == 0}
print(gerade_quadrate)

# achtung bei Sets gibt es nur unikate
labels = {"gerade" if x % 2 == 0 else "ungerade" for x in range(5)}
print(labels)

# duplikate aus liste entfernen
liste = [1 ,2 ,2 ,2 ,4, 5, 6, 7, 7, 8]
einzigartig = {x for x in liste}
print(liste)
print(einzigartig)


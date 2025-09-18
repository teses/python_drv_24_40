"""

    reduce() ist in Python eine Higher-Order Function, die eine Funktion kumulativ
    auf die Elemente einer Sequenz (z. B. Liste oder Tuple) anwendet.
    Dadurch wird die Sequenz zu einem einzigen Wert „reduziert“.

    Typische Anwendungsfälle
    - Summe, Produkt, Maximum/Minimum berechnen
    - Strings verketten
    - Listen "falten" in ein einziges Ergebnis

    Syntax:

    reduce(function, iterable[, initializer])

    - function: Eine Funktion mit zwei Parametern (z. B. lambda x, y: x + y).

"""
## Ohne reduce - alle Zahlen addieren:
zahlen = [1, 2, 3, 4, 5]
summe = 0
for zahl in zahlen:
    summe += zahl
print(summe)

########################################
# mit reduce
from functools import reduce

# summe berechnen
zahlen2 = [1, 2, 3, 4, 5]
summe2 = reduce(lambda x, y: x + y, zahlen2)
print(summe2)

# produkt berechnen
zahlen3 = [1, 2, 3, 4, 5]
summe3 = reduce(lambda x, y: x * y, zahlen3)
print(summe3)

# summe berechnen mit startwert
zahlen2 = [1, 2, 3, 4, 5]
initialwert = 10
summe2 = reduce(lambda x, y: x + y, zahlen2, initialwert)
print(summe2)

# Beispiel: größte zahl finden
zahlen4 = [12, 40, 31, 29]
ergebnis4 = reduce(lambda x, y: x if x > y else y, zahlen4)
print("größte zahl", ergebnis4)


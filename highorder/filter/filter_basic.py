"""
Die filter()-Funktion filtert Elemente aus einer iterierbaren Datenstruktur (z.B. Liste, Tuple) heraus,
basierend auf einer Bedingung, die als Funktion angegeben wird.

Syntax:

    filter(function, iterable)

    - function → Eine Funktion, die True oder False zurückgibt.
    - iterable → Die Datenstruktur, die gefiltert werden soll.

    Rückgabe → Ein filter-Objekt (kann mit list() in eine Liste umgewandelt werden).
"""

# Beispiel mit normaler Callback
# quadrate
def nur_gerade(x):
    return x % 2 == 0

zahlen = [1, 2, 3, 4, 5, 6]
result = list(filter(nur_gerade, zahlen))
print(result)

#################################################
# Beispiel mit lambda als Callback
zahlen2 = [1, 2, 3, 4, 5, 6]
result2 = list(filter(lambda x : x % 2 ==0, zahlen2))
print(result2)

#########################################################
namen = ["Bob", "Alice", "Susi"]
result = list(filter( lambda x: len(x) <= 3 , namen))
print(result)


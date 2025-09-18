"""
Die map()-Funktion in Python ist eine eingebaute Funktion,
mit der man eine Funktion auf jedes Element einer Sequenz (z. B. Liste, Tuple) anwenden kann,
ohne dafür explizit eine Schleife zu schreiben.

Syntax:
map(funktion, iterable, ...)

- funktion: eine Funktion, die auf jedes Element angewendet wird
- iterable: eine oder mehrere Sequenzen (Liste, Tuple, etc.)

Das Ergebnis ist ein Iterator (in Python 3), den du meist in eine Liste oder ein Set umwandeln willst.

"""
# Beispiel mit normaler Callback
# quadrate
def quadriere(x):
    return x*x

zahlen = [1, 2, 3, 4, 5]
result = list(map(quadriere, zahlen))
print(result)

#################################################
# Beispiel mit lambda als Callback
zahlen2 = [1, 2, 3, 4, 5]
result2 = list(map(lambda x : x*x, zahlen2))
print(result2)

#################################################
# beispiel mit mehreren Listen
# Wenn man mehrere iterables übergibt, muss die Funktion entsprechend viele Parameter haben
meineZahlen1 = [1, 2, 3]
meineZahlen2 = [4, 5, 6]
result3 = list(map( lambda x, y : x + y, meineZahlen1, meineZahlen2))
print(result3)

# beispiel # transformation von Daten
sensor1 = [20, 22, 23,23,24,30,30,20,20]
sensor2 = [22, 21, 22,22,23,30,30,21,21]
result4 = list(map( lambda x, y:  {"sensor1": x, "sensor2": y}  , sensor1, sensor2))
print(result4)

# Beispiel mit multiplen variablen
# basics: zur Erinnerung
text1, text2, text3 = ["Orange", "Banane", "Zitrone"]
print(text1, text2, text3)
# beispiel anhand eines Datums
datum_str = "18.09.2025"
tag, monat, jahr = map(int, datum_str.split("."))
print(tag, monat, jahr)
print(type(tag), type(monat), type(jahr))





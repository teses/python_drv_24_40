"""
    Was ist ein Generator?

    Ein Generator ist eine spezielle Art von Iterator, der Werte einzeln auf Anfrage erzeugt, anstatt alles auf einmal im Speicher zu halten.
    Vorteil: sehr speichereffizient bei großen Datenmengen.

    Generatoren werden meist mit yield erstellt oder durch Generator-Expressions.

    yield

"""

## Normale Funktion:
def normale_funktion():
    return [1, 2, 3, 4, 5]

def generator_funktion():
    yield 1 # pause nach dem ersten durchlauf
    yield 2 # pause nach dem ersten durchlauf
    yield 3
    yield 4
    yield 5


# Verwendung
for zahl in normale_funktion():
    print(zahl)

# Verwendung mit Generator
for zahl in generator_funktion():
    print("in for")
    print(zahl)
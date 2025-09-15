"""

    Type Hints
    - helfen anderen Entwicklern und dem eigenen Verständnis später
    - werden von Python nicht zur Laufzeit geprüft
    - erhöhen die Lesbarkeit des Codes
    - unterstützen bei der Fehlersuche

    Type Hints gibt es für
    - Variablen
    - Funktionsparameter und Rückgabe
    - Klassen/Objekt Attribute und Methoden
"""
# Variablen - Type Hints
# Ab Python 3.6 können auch Variablen mit Typannotationen versehen werden.
x: int = 10
name: str = "Alice"
testBool: bool = True         # bool
pi: float = 3.1415

# Funktionsparameter und Rückgabewerte
# Ohne Type Hints - unklar was erwartet wird
def berechne_preis(grundpreis, rabatt, steuer=0.19):
    """Was für Datentypen sind das? Zahlen? Strings?"""
    preis_nach_rabatt = grundpreis * (1 - rabatt)
    endpreis = preis_nach_rabatt * (1 + steuer)
    return grundpreis * (1 - rabatt) * (1 + steuer)

# type Hints -> verständlicher
def berechne_preis2(grundpreis: float, rabatt: float=0, steuer: float=0.19) -> float:
    """Was für Datentypen sind das? Zahlen? Strings?"""
    preis_nach_rabatt = grundpreis * (1 - rabatt)
    endpreis = preis_nach_rabatt * (1 + steuer)
    return grundpreis * (1 - rabatt) * (1 + steuer)


print(berechne_preis2(100.0, 0.1, 0.07))



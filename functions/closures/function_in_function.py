"""

In Python kannst du Funktionen innerhalb von Funktionen definieren.
Das nennt man verschachtelte Funktionen oder innere Funktionen.

Praktische Anwendung:

- Funktionen kapseln
- Closures (Daten + Funktion bündeln)
- Hilfsfunktionen, die nur lokal gebraucht werden
- Dekoratoren (werden mit inneren Funktionen umgesetzt)

"""

# Grundprinzip
def aussen():
    print("Ich bin aussen")

    test = 10

    def innen():
        print("Ich bin innen")

    def meinTest():
        print(f"Ich bin meinTest {test}")

    innen()
    meinTest()

aussen()

#############################################################
def aussen2():
    print("Ich bin aussen")

    def innen2():
        return "Hallo ich bin innen"

    return innen2

dieInnere = aussen2()
print(dieInnere())

#################################################################
# Closures (innere Funktion merkt sich variablen aus der aüßeren.
# Hier merkt sich jede innere Funktion den Wert von faktor
def multiplikator(faktor):

    def multipliziere(x):
        return x * faktor

    return multipliziere

mul3 = multiplikator(3)
mul5 = multiplikator(5)
mul10 = multiplikator(10)

print(mul3(10)) # 30
print(mul5(10)) # 50
print(mul10(2)) # 50


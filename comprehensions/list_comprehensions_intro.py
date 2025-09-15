"""
    List Comprehensions in Python sind eine kompakte und elegante Möglichkeit, Listen zu erstellen.
    Statt mit einer Schleife Elemente einzeln zu einer Liste hinzuzufügen, können wir mit einer einzigen Zeile Listen generieren.

    Syntax

    [expression for element in iterable]

    [expression for element in iterable if condition]

    - expression -> was in die Liste kommt
    - element -> Platzhalter für jedes element in der iteration/Schleife
    - iterable -> Datenquelle (listen, strings, iteratoren, range,..)
    - condition -> (optional) Filter

"""
# Schleife die Elemente einzeln hinzufügt
quadratzahlen = []
for x in range(0 , 10):
        quadratzahlen.append(x*x)
print(quadratzahlen)

# Alles in einer Zeile mit List Comprehensions
# Eine liste mit allen quadratzahlen
liste = [x*x for x in range(0 , 10)]
print(liste)

# Beispiel mit Bedingung
gerade = [x for x in range(0,100) if x % 2 == 0 ]
print(gerade)

# Beispiel
listeWoertern = ["python", "java", "javascript"]

# mit schleife
gross=[]
for w in listeWoertern:
    gross.append(w.upper())
print(gross)

# mit list comprehensions
gross2 = [w.upper() for w in listeWoertern]
print(gross2)

# Verschachtelte Schleifen
# mit vorsicht zu verwenden. wird schnell unleserlich
# wenn man schachtelt -> NICHT unbedingt in einer Zeile quetschen
# paare = [(x, y) for x in range(3) for y in range(3)]
paare = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(paare)

# mit bedingungen
paare = [
    (x, y)
    for x in range(3) if x == 2
    for y in range(3) if y == 1
]
print(paare)

# Kombination mit conditional expressions
# gerade/ungerade
gerade = [x for x in range(0,100)]
print(gerade)

gerade2 = [f"gerade {x}" if x % 2 == 0 else f"ungerade {x}" for x in range(0,100)]
print(gerade2)

# so geht es eben nicht - man hat kein else
labels2 = ["gerade"+str(x) for x in range(5) if x % 2 == 0]
print(labels2)
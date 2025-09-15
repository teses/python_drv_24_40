"""
    Eine Lambda-Funktion in Python ist eine kleine, anonyme Funktion, die du in einer einzigen Zeile definieren kannst.
    Sie wird oft für kurze Operationen verwendet, bei denen eine normale def-Funktion zu „umständlich“ wäre.

    Syntax

    lamda argumente : ausdruck

    lambda -> Schlüsselwort
    argumente -> Eingabe in die Funktion
    ausdruck -> genau ein Ausdruck, dessen Ergebnis zurückgegeben wird
"""

def quadriereNormal(n):
    return n * n

print(quadriereNormal(5))

############################################
# eine lambda funktion auf eine variable gelegt
quadriere = lambda n : n * n
ret = quadriere(3)
print(ret)

## addition
addition = lambda x, y : x + y
print(addition(1, 2))
print(addition(3, 4))

# mit bedingung
older18 = lambda age : age >= 18
print(older18(18), older18(17))

# Ohne variablenzuweisung direkt nutzen
print(   (lambda age : age >= 18)(20)    )


###################################################
# Beispiel
# geht nicht weil personen fehlen -> später mehr im Kapitel map, filter, reduce
"""
callBack = lambda p: p["stadt"] == "Berlin"

def callBack2(p):
    if p["stadt"] == "Berlin":
        return True
    else:
        return False


berliner = list(filter(callBack2, personen))
print("Berliner Personen:", berliner)"""






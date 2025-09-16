"""
in Dict Comprehension in Python ist eine sehr kompakte Möglichkeit,
Dictionaries (Wörterbücher) zu erstellen – ähnlich wie List Comprehensions.

Syntax:

    {key_expr: value_expr for element in iterable}

    {key_expr: value_expr for element in iterable if condition}

    - key_expr: Ausdruck für den Schlüssel
    - value_expr: Ausdruck für den Wert
    - element → Platzhalter für jedes Element in der Iteration
    - iterable → Sammlung, über die iteriert wird
    - condition (optional) → Filterbedingung

"""
# quadrate
quadrate = { n :n*n for n in range(0,100)}
print(quadrate)

# eine liste der Wörter mit der Menge
words = ["Python", "ist", "cool", "ist", "cool"]
wordLength = { word : len(word) for word in words}
print(wordLength)

# nur gerade quadrate zahlen
quadrateGerade = { x:x*x for x in range(0,10) if x % 2 == 0 }
print(quadrateGerade)

# umkehrung eines dict
# Achtung! geht nur wenn die werte nicht doppelt sind
original = {"a" : 2, "b" : 5, "c": 10}
key_value_flip = { v: k for k, v in original.items()}
print(original)
print(key_value_flip)





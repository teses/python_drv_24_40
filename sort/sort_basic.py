"""

    Grundidee:
    Listen kann man sortieren mit list.sort() und mit der Funktion sorted()

    - list.sort() -> sortiert die bestehende Liste
    - sorted() -> gibt eine sortierte Kopie zurück

    Syntax

        list.sort(reverse=True, key=function)
        sorted(iterable, reverse=True, key=function)

        - reverse: auf oder absteigend True/False
        - key -> eine Funktion die auf jedes Element angewendet wird
"""

# list.sort() sortiert die bestehende Liste
zahlen = [5, 3, 4, 1 , 2]
ret = zahlen.sort() # Achtung sort() liefert None zurück und keine liste
print(zahlen, ret)

# sorted() eine sortierte Kopie zurück
zahlen2 = [5, 3, 4, 1 , 2]
zahlen2sortiert = sorted(zahlen2)
print(zahlen2)
print(zahlen2sortiert)

# reverse
zahlen3 = [5, 3, 4, 1 , 2]
zahlen3.sort(reverse=True)
print(zahlen3)

# wichtig, es wird case sensitiv sortiert - aphanumerisch
words = ["Hallo", "schöne", "Welt", "abend", "10", "1", "2"]
words.sort()
print(words)
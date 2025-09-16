

# Summe von 1 bis 100
summe = sum([x for x in range(1,101)])
print(summe)

# Summe von 1 bis 100 - geht auch
summe = sum(x for x in range(1,101))
print(summe)

# Eine verschachtelte Liste in lineare Liste wandeln (flatten)
matrix = [[1,2,3], [10,5,6], [7,8,9]]
matrix_flat = [number for row in matrix for number in row]
print(matrix_flat)

# Wörter nach Länge filtern
# Erzeuge eine Liste aller Wörter, die länger als 3 Buchstaben haben, und wandle sie in Großbuchstaben um.
words = ["house", "dog", "international", "cups", "AI"]
filtert = [w.upper() for w in words if len(w) > 3]
print(filtert)


# Erstellt eine Liste mit n Zufallszahlen
import random
zufallszahlen = [random.randint(1, 100) for i in range(0,10)]
print(zufallszahlen)

#######################################################################
sitzplan = [
    ["Jason", "Barry", "Mark", "Peter", "Andreas", "Maik"],
    ["John", "Jane", "Susi", "Sara", "Sven"],
    ["Max", "Moritz", "Mia", "Anna", "Markus"],
    ["Lukas", "Lena", "Joshua", "Luke", "Oliver"],
]

# summe aller plätze
sum_of_seats_total = sum(len(row) for row in sitzplan)
print(sum_of_seats_total)
# 21

# Die Summe der Plätze in einer Reihe
# jetzt alle durchläufe in eine liste
# [6,5,5,5]
sum_of_seats_per_row = [len(row) for row in sitzplan]
print(sum_of_seats_per_row)



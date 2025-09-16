
# Einfache Zahlenliste
# Aufgabe: Sortiere die Liste nach der Restklasse bei Division durch 3.
# wenn möglich mit lambda funktion
zahlen = [5, 12, 3, 21, 8]
zahlen_sorted = sorted(zahlen, key=lambda num: num % 3)
print(zahlen_sorted)

# Sortiere die Liste nach dem Alter (zweites Element des Tupels).
personen = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
personen_sorted = sorted(personen, key=lambda person: person[1])
for person in personen_sorted:
    print(person)

# Aufgabe: Sortiere die Liste nach den Noten (aufsteigend).
students = [
    {"name": "Alice", "note": 2.5},
    {"name": "Bob", "note": 1.7},
    {"name": "Charlie", "note": 3.0}
]
students_sorted = sorted(students, key=lambda student: student["note"])
for student in students_sorted:
    print(student)

# Aufgabe: Sortiere zuerst nach Alter, dann nach Note (aufsteigend).
students2 = [
    {"name": "Alice", "note": 2.5, "alter": 25},
    {"name": "Bob", "note": 1.7, "alter": 25},
    {"name": "Charlie", "note": 3.0, "alter": 20}
]
students2_sorted = sorted(students2, key=lambda student: (student["alter"], student["note"]))
for student in students2_sorted:
    print(student)


# Aufgabe: Sortiere die Namen alphabetisch, unabhängig von Groß-/Kleinschreibung.
namen = ["alice", "Bob", "charlie", "David"]
namen_sorted = sorted(namen, key=lambda name: name.lower())
namen.sort(key = str.lower) # Lösung 2
print(namen_sorted)
print(namen)



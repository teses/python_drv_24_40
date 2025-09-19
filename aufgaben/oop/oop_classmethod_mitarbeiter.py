"""
Aufgabe: Mitarbeiter-Management

Du sollst eine Klasse Mitarbeiter schreiben:

- Jeder Mitarbeiter hat Name und Abteilung.
- Es gibt ein Klassenattribut alle_mitarbeiter, in dem alle Instanzen gespeichert werden.
- Erstelle eine Klassenmethode from_string("Name,Abteilung"), die einen neuen Mitarbeiter erzeugt.
- Erstelle eine Klassenmethode get_by_department(department), die alle Mitarbeiter einer bestimmten Abteilung zurückgibt.
- Füge eine Klassenmethode count() hinzu, die die Gesamtanzahl der Mitarbeiter liefert.
"""


# --- Test ---
m1 = Mitarbeiter("Anna", "IT")
m2 = Mitarbeiter.from_string("Ben, HR")
m3 = Mitarbeiter.from_string("Clara, IT")


print("Gesamtanzahl:", Mitarbeiter.count())

###
itAbteilung = Mitarbeiter.get_by_department("IT")
for m in itAbteilung:
    print(m.name, m.abteilung)

##
print("HR Abteilung", [m.name + ", " + m.abteilung for m in Mitarbeiter.get_by_department("HR")])

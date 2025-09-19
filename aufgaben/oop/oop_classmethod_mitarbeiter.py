"""
Aufgabe: Mitarbeiter-Management

Du sollst eine Klasse Mitarbeiter schreiben:

- Jeder Mitarbeiter hat Name und Abteilung.
- Es gibt ein Klassenattribut alle_mitarbeiter, in dem alle Instanzen gespeichert werden.
- Erstelle eine Klassenmethode from_string("Name,Abteilung"), die einen neuen Mitarbeiter erzeugt.
- Erstelle eine Klassenmethode get_by_department(department), die alle Mitarbeiter einer bestimmten Abteilung zurückgibt.
- Füge eine Klassenmethode count() hinzu, die die Gesamtanzahl der Mitarbeiter liefert.
"""
class Mitarbeiter:

    all_mitarbeiter = []

    def __init__(self, name, department):
        self.name = name
        self.department = department
        Mitarbeiter.all_mitarbeiter.append(self)

    # constructor
    @classmethod
    def from_string(cls, string):
        name, department = string.replace(" ", "").split(",")
        return cls(name, department)

    @classmethod
    def get_all_mitarbeiter(cls):
        return cls.all_mitarbeiter

    @classmethod
    def get_by_department(cls, department):
        return [mitarbeiter for mitarbeiter in cls.all_mitarbeiter if mitarbeiter.department == department]

    @classmethod
    def get_by_name(cls, name):
        return [mitarbeiter for mitarbeiter in cls.all_mitarbeiter if mitarbeiter.name == name]

    @classmethod
    def count(cls):
        return len(cls.all_mitarbeiter)

    def __str__(self):
        return f"{self.name}, {self.department}"



# --- Test ---
m1 = Mitarbeiter("Max", "HR")
m2 = Mitarbeiter("Monika", "HR")
m3 = Mitarbeiter.from_string("Moritz, IT")
m4 = Mitarbeiter("Anna", "IT")
m5 = Mitarbeiter("Janik", "HR")
m6 = Mitarbeiter("Ben", "IT")
m7 = Mitarbeiter("Clara", "Sales")
m8 = Mitarbeiter("Jonathan", "Sales")
m9 = Mitarbeiter("Lukas", "IT")
m10 = Mitarbeiter("Lena", "HR")
m11 = Mitarbeiter("Lily", "IT")
m12 = Mitarbeiter("Gregory", "HR")


print("Gesamtanzahl:", Mitarbeiter.count())

###
itAbteilung = Mitarbeiter.get_by_department("IT")
for m in itAbteilung:
    print(m.name, m.department)

##
print("IT Abteilung", [m.__str__() for m in Mitarbeiter.get_by_department("IT")])
print("HR Abteilung", [m.name + ", " + m.department for m in Mitarbeiter.get_by_department("HR")])

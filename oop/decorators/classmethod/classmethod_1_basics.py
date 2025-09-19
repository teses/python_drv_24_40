"""
In Python ist @classmethod ein Dekorator, mit dem man Methoden einer Klasse definiert,
die auf die Klasse selbst statt auf eine Instanz zugreifen.

- Normale-Methoden erhalten als erstes Argument self (Die Instanz)
- Klassen-Methoden erhalten als erstes Argument cls (Die Klasse)

Einsatzgebiete Beispiele:
- eine art counter (Wieviel Objekte sind erstellt worden?)
- caching in der Klasse (Datenobjekten)
- zusätzliche Konstruktoren
"""

class Mitarbeiter:

    anzahl = 0 # Klassenattribut

    def __init__(self, name):
        self.name = name
        Mitarbeiter.anzahl += 1  # Achtung ! Hier wird das Klassenattribut hochgezählt

    @classmethod
    def get_anzahl(cls):
        return cls.anzahl



# Nutzung
m1 = Mitarbeiter("Anna")
m2 = Mitarbeiter("Ben")

print("m1.anzahl", m1.anzahl)  # zugriff auf Klassenattribut
print(m1.__dict__) # hier kann man sehen ob es wirklich ein klassenattribut ist, wenn es nicht auftaucht im __dict__

print("m1.anzahl", m1.anzahl) # 2
print("m1.get_anzahl()", m1.get_anzahl())  # 2
print("m3.get_anzahl()", m2.get_anzahl())  # 2
print("Mitarbeiter.get_anzahl()", Mitarbeiter.get_anzahl())  # 2 # Hier kann jetzt die Klassenmethode aufgerufen werden



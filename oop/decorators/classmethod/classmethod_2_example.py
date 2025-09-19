"""



"""

class Mitarbeiter:

    def __init__(self, firstname="", lastname=""):
        self.firstname = firstname
        self.lastname = lastname


    # Alternative Konstruktor
    @classmethod
    def from_string(cls, name):
         parts = name.replace(" ","").split(",")
         return cls(parts[1], parts[0])


    def __str__(self):
        return f"{self.firstname} {self.lastname}"


# Lösung durch vererbung und überschreiben des originalkonstruktors
class Mitarbeiter2(Mitarbeiter):

    def __init__(self,  name="" ):
        parts = name.replace(" ", "").split(",")
        super().__init__(parts[1], parts[0])



vorname = "Susi"
nachname = "Sauer"
m1 = Mitarbeiter(vorname, nachname)  # Standartkonstruktor
print(m1)

dername = "Sauer, Susi"
m2 = Mitarbeiter.from_string(dername)
print(m2)
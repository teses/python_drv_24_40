"""

Eine Klasse Geld

Attribute
- betrag
- währung

__str__
__repr__
__add__ nur gleiche Währungen können addiert werden. sonst Fehlermeldung raisen (ValueError)
__sub__  ""
__eq__
__lt__
__bool__  wenn kein Geld vorhanden
"""
class Geld:
    def __init__(self, betrag, waehrung):
        self.betrag = betrag
        self.waehrung = waehrung

    def __str__(self):
        return f"{self.betrag} {self.waehrung}"

    def __repr__(self):
        return f"Geld({self.betrag}, {self.waehrung})"

    # Addition
    def __add__(self, other):
        if isinstance(other, Geld):
            if self.waehrung != other.waehrung:
                raise ValueError("Die Währungen müssen übereinstimmen")
            return Geld(self.betrag + other.betrag, self.waehrung)
        elif isinstance(other, (int, float)):
            return Geld(self.betrag + other, self.waehrung)
        return NotImplemented

    # Subtraktion
    def __sub__(self, other):
        if isinstance(other, Geld):
            if self.waehrung != other.waehrung:
                raise ValueError("Die Währungen müssen übereinstimmen")
            return Geld(self.betrag - other.betrag, self.waehrung)
        elif isinstance(other, (int, float)):
            return Geld(self.betrag - other, self.waehrung)
        else:
            NotImplemented

    # Gleichheit, funktioniert gleichzeitig als ungleichheit
    def __eq__(self, other):
        if isinstance(other, Geld):
            return self.betrag == other.betrag and self.waehrung == other.waehrung
        return False

    # Kleiner als, funktioniert gleichzeitig als größer als
    def __lt__(self, other):
        if isinstance(other, Geld):
            if self.waehrung != other.waehrung:
                raise ValueError("Verschiedene Währungen können nicht verglichen werden!")
            return self.betrag < other.betrag
        return self.betrag < other

    def __bool__(self):
        return self.betrag > 0




## Tests:
## Tests
euro1 = Geld(10, "€")
euro2 = Geld(20, "€")

dollar1 = Geld(10, "$")

print("-"*50)

if euro1:
    print("geld ist nicht leer")

if not euro1:
    print("geld ist leer")

print("-"*50)

print("gleichheit")
print(euro1 == euro2)

print("-"*50)

print("ungleichheit")
print(euro1 != euro2)

print("-"*50)

print("kleiner als")
print(euro1 < euro2)

print("-"*50)

print("kleiner als verschiedene Währung")
#print(euro1 < dollar1) # Fehler

print("-"*50)

print("größer als")
print(euro1 > euro2)

print("-"*50)

print("Addition von 2 gleichen Währungen")
print(euro1 + euro2)

print("-"*50)

print("Subtraktion von 2 gleichen Währungen")
print(euro1 - euro2)

print("-"*50)

print("Addition von Geld mit Integer")
print(euro1 + 10)

print("-"*50)

print("Subtraktion von Geld mit Integer")
print(euro1 - 10)

print("-"*50)

print("gleichheit von 2 währungen(ist nie wahr)")
print(euro1 == dollar1)

print("-"*50)

print("Addition von 2 währungen(raises ValueError)")
#print(euro1 + dollar1) # Fehler

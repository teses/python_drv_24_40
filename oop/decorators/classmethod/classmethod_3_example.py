

class Datum:
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    @classmethod
    def from_de_string(cls, datum_str):
        parts = datum_str.split(".")
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))

    @classmethod
    def from_usa_string(cls, datum_str):
        parts = datum_str.split("/")
        return cls(int(parts[1]), int(parts[0]), int(parts[2]))


# Nutzung
d1 = Datum(31, 1, 2025)
d2 = Datum.from_de_string("31.01.2024")
d3 = Datum.from_usa_string("01/31/2024")

print(d1.__dict__)
print(d2.__dict__)
print(d3.__dict__)
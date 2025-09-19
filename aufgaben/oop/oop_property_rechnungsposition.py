"""

Erstelle eine Klasse RechnungsPosition, die folgende Attribute hat:

    beschreibung (str) – was verkauft wird
    menge (int) – Anzahl der Artikel
    preis_netto (float) – Preis pro Stück ohne Steuer
    mwst_satz (float) – Mehrwertsteuersatz in Prozent

Implementiere berechnete Properties:
    gesamt_netto
    steuerbetrag
    gesamt_brutto

Baue eine Validierung ein:
    menge muss > 0 sein
    preis_netto darf nicht negativ sein
    MwSt-Satz darf nicht negativ sein!

"""

class RechnungsPosition:
    def __init__(self, beschreibung: str, menge: int, preis_netto: float, mwst_satz: float = 19):
        self.beschreibung = beschreibung
        self.menge = menge
        self.preis_netto = preis_netto
        self.mwst_satz = mwst_satz



    # berechnete Properties
    @property
    def steuerbetrag(self):
        return round(self.gesamt_netto * (self.mwst_satz / 100), 3)

    @property
    def gesamt_brutto(self):
        #return self.gesamt_netto * (1 + (self.mwst_satz / 100))
        return self.gesamt_netto + self.steuerbetrag

    @property
    def gesamt_netto(self):
        return self.preis_netto * self.menge


    # getter and setter
    @property
    def menge(self):
        return self.__menge

    @menge.setter
    def menge(self, menge):
        if menge < 0:
            raise ValueError("Menge muss größer 0 sein")

        self.__menge = menge


    @property
    def preis_netto(self):
        return self.__preis_netto

    @preis_netto.setter
    def preis_netto(self, preis_netto):
        if preis_netto < 0:
            raise ValueError("Preis Netto muss größer 0 sein")

        self.__preis_netto = preis_netto


    @property
    def mwst_satz(self):
        return self.__mwst_satz

    @mwst_satz.setter
    def mwst_satz(self, mwst_satz):
        if mwst_satz < 0:
            raise ValueError("MWST Satz muss größer 0 sein")

        self.__mwst_satz = mwst_satz


# Erwartete Nutzung
# Beispiel: 3 Bücher à 12.50 €, 7 % MwSt.
pos = RechnungsPosition("Buch", 3, 12.50, 7)

# public properties
print(pos.beschreibung)   # "Buch"
print(pos.menge)
print(pos.preis_netto)
print(pos.mwst_satz)

#  berechnete Properties
print(pos.gesamt_netto)   # 37.5
print(pos.steuerbetrag)   # 2.625
print(pos.gesamt_brutto)  # 40.125

# Fehler
#pos.menge = -1
#pos.preis_netto = -1
#pos.mwst_satz = -1
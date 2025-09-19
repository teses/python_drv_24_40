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

## Tests:
geld1 = Geld(50, "EUR")
geld2 = Geld(30, "EUR")
geldDollar = Geld(30, "$")
geld3 = Geld(0, "EUR")


if geld1:
    print("geld ist nicht leer")

if not geld2:
    print("geld ist leer")

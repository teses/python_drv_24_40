"""
Aufgabe : Alter prüfen
Schreibe einen bedingten Ausdruck, der "Volljährig" ausgibt, wenn alter >= 18 ist, sonst "Minderjährig".
"""
alter = 17
status = "Volljährig" if alter >= 18 else "Minderjährig"
print(status)

"""
Aufgabe: Minimum zweier Zahlen
Gebe das kleinere von zwei Zahlen a und b mit einem bedingten Ausdruck aus.
"""
a = 12
b = 7
minWert = a if a < b else b
print(f"A: {a}, B: {b}")
print(minWert)


"""
Aufgabe : Note anhand von Punktzahl
Verwende einen bedingten Ausdruck, um Noten zu vergeben:
>= 90: "A"
>= 80: "B"
>= 70: "C"
Sonst: "D"
"""
punktzahl = 75
note = "A" if punktzahl >= 90 else "B" if punktzahl >= 80 else "C" if punktzahl >= 70 else "D"
print(note)  # Ausgabe: C

"""
Aufgabe: Gerade oder ungerade
Gebe "Gerade" aus, wenn eine Zahl gerade ist, sonst "Ungerade".
"""
zahl = 9
typ = "Gerade" if zahl % 2 == 0 else "Ungerade"
print(typ)  # Ausgabe: Ungerade


"""
Aufgabe: Absoluter Wert (Betrag)   
Gebe den absoluten Wert einer Zahl x mit einem bedingten Ausdruck aus.
"""
x = 15 # 15
#x = -15 # 15
absWert = x if x >= 0 else -x
print(absWert)

"""
Aufgabe: Alterskategorie

Gebe die Alterskategorie basierend auf alter aus:
< 13: "Kind"
13-19: "Teenager"
20-59: "Erwachsener"
>= 60: "Senior"
"""
alter = 45
kategorie = "Kind" if alter < 13 else "Teenager" if alter <= 19 else "Erwachsener" if alter <= 59 else "Senior"
print(kategorie)


"""
    Aufgabe: Wetterempfehlung

    Gebe eine Empfehlung basierend auf Temperatur (temp) und Regen (regnet) aus:
    temp >= 25 und not regnet: "Gehe schwimmen"
    temp >= 20 und not regnet: "Gehe spazieren"
    regnet: "Bleib drinnen"
    Sonst: "Zieh dich warm an"
"""
temp = 19
regnet = False
erg = "Gehe schwimmen" if temp >= 25 and not regnet else "Gehe spazieren" if temp >= 20 and not regnet else "Bleib drinnen" if regnet else "Zieh dich warm an."
print(erg)


"""
    IF Einzeiler

    In Python ist ein bedingter Ausdruck (auch ternärer Operator genannt) eine kompakte Möglichkeit,
    eine if-else-Anweisung in einer einzigen Zeile zu schreiben.

    Die allgemeine Syntax lautet:

    <wert_wenn_wahr> if bedingung else <wert_wenn_falsch>

    Verschachtelt
    <Expr1> if bedingung else <Expr2> if condition else <Expr3>

"""

alter = 20

# normaler IF/Else
# Wenn ich über 18 bin, dann bin ich erwachsen sonst minderjährig
if alter >= 18:
    status = "Erwachsen"
else:
    status = "Minderjährig"


# Conditional Expression
# Ich bin Erwachsen, wenn ich über 18 bin, sonst bin ich Minderjährig
status = "Erwachsen" if alter >= 18 else "Minderjährig"
print(status)

#############################################################################################
# Beispiel: Verschachtelte bedingte Ausdrücke
# Note A >= 90
# Note B >= 80
# sonst Note C
# Note A wenn punktzahl >= 90, sonst Note B wenn punktzahl >= 80, sonst Note C
punktzahl = 20
note = "Note A" if punktzahl >= 90 else "Note B" if punktzahl >= 80 else "Note C"
print(note)





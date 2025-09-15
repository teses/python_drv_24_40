

# Letzte Ziffer einer Zahl
# 1234 -> 4
# 9876 -> 6
num = 9876
last_digit = lambda number: number % 10
print(last_digit(num))

# Maximum von zwei zahlen mit Lambda
max_of_2 = lambda a, b: a if a > b else b
print(max_of_2(5, 10))

# Palindrom-Prüfung (Bonus)
# Ein Palindrom ist ein Wort welches vorwärts und rückwärts das selbe ergibt
# Zusatz: groß- und kleinschreibung ignorieren
# otto -> True
# anna -> True
# maoam -> True
# reliefpfeiler -> True
# lagerregal -> True
# Thomas -> False

#palindrom = lambda text: text == text[::-1]
palindrom = lambda text: text.lower() == text[::-1].lower()

print(palindrom("otto"))   # Ausgabe: True
print(palindrom("anna"))   # Ausgabe: True
print(palindrom("maoam"))   # Ausgabe: True
print(palindrom("reliefpfeiler"))   # Ausgabe: True
print(palindrom("Reliefpfeiler"))   # Ausgabe: True
print(palindrom("lagerregal"))   # Ausgabe: True
print(palindrom("Thomas"))   # Ausgabe: False

#
palindrom2 = lambda text: text.replace(" ", "").lower() == text[::-1].replace(" ", "").lower()
print(palindrom2("Eine Horde bedrohe nie"))

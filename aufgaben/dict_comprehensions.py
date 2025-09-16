

# Wörterbuch mit List Comprehension
# Erstelle ein Dictionary mit einer Dict Comprehension, in dem der Schlüssel der Name ist und der Wert die Länge des Namens.
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

# Zeichenhäufigkeit
text = "Mississippi"
char_count_dict = {char: text.count(char) for char in text}
print(char_count_dict)

# Häufigkeit zählen mit Dict Comprehension
lst = ["Apfel", "Banane", "Apfel", "Kirsche", "Banane", "Apfel"]
fruit_count_dict = {fruit: lst.count(fruit) for fruit in lst}
print(fruit_count_dict)

# ASCII-Tabelle
# chr() wandelt Zahl in Buchstabe, ord() gibt ASCII-Code.
# eine Tabelle nur mit den Großbuchstaben
ascii_dict = {chr(i): i for i in range(65, 91)}
print(ascii_dict)
# lösung 2
ascii_dict = {chr(i): i for i in range(128) if chr(i).isalpha() and chr(i) == chr(i).upper()}
print(ascii_dict)

# Preise inkl. Mehrwertsteuer
prices = {"Apfel": 1.00, "Banane": 0.50, "Kirsche": 0.10}
mwst = 19
prices_with_mwst = {fruit: price * (1 + mwst / 100) for fruit, price in prices.items()}
print(prices_with_mwst)


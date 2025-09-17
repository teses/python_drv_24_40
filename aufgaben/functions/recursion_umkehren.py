"""
Aufgabe:
Schreibe eine rekursive Funktion umkehren(text), die einen String umkehrt.



"""

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


def umkehren(text):
    # Abbruchbedingung: leerer String oder ein Zeichen
    if len(text) <= 1:
        return text
    else: # Rekursiver Schritt: letztes Zeichen + umgekehrter Rest
        return text[-1] + umkehren(text[:-1])

# ohne else
def umkehren2(text):
    if len(text) <= 1:
        return text
    return text[-1] + umkehren(text[:-1])



# Test
print(umkehren("Ha"))
print(umkehren("Hallo"))   # Ausgabe: "ollaH"
print(umkehren("Python"))  # Ausgabe: "nohtyP"


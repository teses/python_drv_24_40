"""

    Vorteile von with open(...):

    - Datei wird automatisch geschlossen (auch bei Fehlern).
    - Kein manuelles f.close() nötig.

"""

with open("..\\data\\testdatei.txt", "r") as file:
    inhalt = file.read()
    # verarbeitung
    print(inhalt)

# verarbeiten
print(inhalt)

##########################################################
with open("..\\data\\testdatei.txt", "a") as file:
    file.write("Hallo\n")
    file.write("Welt")


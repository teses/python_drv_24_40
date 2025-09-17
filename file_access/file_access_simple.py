
# quick and dirty
try:
    file = open("data\\testdatei.txtt", "r")
    text = file.read()
    file.close()

    print(text)
except FileNotFoundError as error:
    print("Datei nicht gefunden")

##############################################################
try:
    file = open("data\\testdatei.txt", "r")

    # Datei zeilenweise einlesen
    for line in file:
        # verarbeiten
        print(line, end="")

    file.close()
except FileNotFoundError as error:
    print("Datei nicht gefunden")


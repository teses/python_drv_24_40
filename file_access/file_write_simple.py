



filename = "..\\data\\exist.txt"

text = "Hallo Welt hallo hallo\n"

try:

    file = open(filename, "a")
    try:
        file.write(text)
    except Exception as error:
        print("Beim schreiben ist ein Fehler aufgetreten")
    finally:
        file.close()

except FileNotFoundError as error:
    print("Datei nicht gefunden")
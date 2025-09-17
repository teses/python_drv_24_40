"""
beim Datei-Zugriff können leicht Fehler auftreten (z. B. Datei nicht vorhanden, keine Schreibrechte).
Diese müssen abgefangen werden

Dies ist die beste Art und weise
"""

filename = "..\\data\\testdatei.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        inhalt = f.read()
        print("Datei erfolgreich gelesen:")
        print(inhalt)

except IsADirectoryError as e:
    print(f"Fehler: Die Datei {filename} ist ein Verzeichnis.")

except UnicodeDecodeError:
    print(f"Falsches Encoding in Datei {filename}. Bitte Zeichensatz prüfen.")

except FileNotFoundError:
    print(f"Fehler: Die Datei {filename} wurde nicht gefunden.")

except PermissionError:
    print(f"Fehler: Keine Berechtigung zum Lesen der Datei: {filename}")

except OSError as e:  # Oberklasse für viele Datei-Fehler
    print(f"Betriebssystem-Fehler: {e}")

except Exception as e:
    print(f"Unerwarteter Fehler: {e}")
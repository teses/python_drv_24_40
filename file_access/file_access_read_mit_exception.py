"""
Normale Art um eine Datei zu lesen
"""

try:
    filehandler = open("..\\data\\testdatei.txtt", mode="r")
    # Datenverarbeitung
    text = filehandler.read()
    print(text)
    filehandler.close() # schliessen wird hier nicht ausgeführt bei einem Fehler

except FileNotFoundError as e:
    print(f"Datei wurde nicht gefunden: {e}")

finally:
    try:
        filehandler.close()
    except:
        pass

"""
ValueError → ungültiger Wert (z. B. int("abc"))
TypeError → falscher Typ (z. B. "3" + 5)
IndexError → Listenindex außerhalb des Bereichs
KeyError → Zugriff auf nicht vorhandenen Dictionary-Key
ZeroDivisionError → Division durch null
FileNotFoundError → Datei nicht gefunden
ImportError / ModuleNotFoundError → Modul nicht importierbar
AttributeError → Zugriff auf nicht vorhandenes Attribut
RuntimeError → allgemeiner Laufzeitfehler
StopIteration → vom Iterator ausgelöst, wenn keine Werte mehr da sind
IsADirectoryError
UnicodeDecodeError
PermissionError
Exception
"""
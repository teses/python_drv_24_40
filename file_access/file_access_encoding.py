"""

Encoding der Datei beachten!!

Am besten heutzutage UTF-8 nutzen


"""


filename = "..\\data\\testdatei.txt"


with open(filename, "r", encoding="utf-8") as f:
    inhalt = f.read()
    print("Datei erfolgreich gelesen:")
    print(inhalt)



"""

    Nur lesen                   r
    Lesen und schreiben         r+

    nur anhängen                a   hier wird die datei angelegt
    anhängen und lesen          a+  hier wird die datei angelegt

    nur schreiben               w   hier wird die datei angelegt
    schreiben und lesen         w+  hier wird die datei angelegt

    zusätzlich noch den Modus ob Text oder binär
     t = Textmodus (standard)
     b = binärmodus
"""

filehandler = open("..\\data\\testdatei.txt", mode="r")

# komplette Datei einlesen - Nicht ideal bei großen Dateien
print(filehandler.read())

# Teile einlesen Datei einlesen
filehandler.seek(0) # Zeiger wieder zum Anfang setzen
print(filehandler.read(20))
print(filehandler.read(5))

# Zeilenweise einlesen
print("-" * 50)
filehandler.seek(0)
print(filehandler.readline())
print(filehandler.readline())
print(filehandler.readline())

# zeilenweise mit einer for schleife
print("-" * 50)
filehandler.seek(0)
for line in filehandler:
    print(line)

# Alle Zeilen in ein Array einlesen
print("-" * 50)
filehandler.seek(0)
lines = filehandler.readlines() # die ganze datei im speicher lesen
for line in lines:
    print(line)


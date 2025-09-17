"""

3 Funktionen

- writeHighscore(data) - Eine Funktion zum speichern einer Highscore Datenliste in einer Textdatei
  Eine Liste mit einem Dictionary als Input

- readHighscore() - Eine Funktion, die die Highscore Datei ausliest und die Daten als Dictionary zurückgibt

- updateHighscore(username, score) - EIne Funktion zum updaten einer Punktzahl eines users
  updateHighscore(username, score)

name,score,games
---------------------
Susi,1000,3
Moritz,40,2
Hans,200,10


"""

FILENAME = "..\\data\\highscore_test.txt"


def writeHighscore(data):
    pass


def readHighscore():
    pass


def updateHighscore(username, score):
    pass


#############################
#  schreiben Test
"""
data = [
    {'name': 'Susi', 'score': 1000, 'games': 3},
    {'name': 'Moritz', 'score': 40, 'games': 2},
    {'name': 'Hans', 'score': 200, 'games': 10}
]
writeHighscore(data)"""

##########################################################
# updaten Test
"""
#username = input("Bitte Name eingeben: ")
username = "Susi"
updateHighscore(username, 80)
"""

############################
# lesen Test
"""
ergebnis = readHighscore()
for erg in ergebnis:
    print(erg)
"""
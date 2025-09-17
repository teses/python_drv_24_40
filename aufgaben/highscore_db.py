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
    ## verarbeiten und content erstellen
    content = ""
    for row in data:
        line = ",".join([
            row["name"],
            str(row["score"]),
            str(row["games"])
        ])
        content += line + "\n"

    # in Datei schreiben
    with open(FILENAME, "w", encoding="utf-8") as fh:
        fh.write(content)



def readHighscore():
    data = []
    with open(FILENAME, "r", encoding="utf-8") as fh:
        for line in fh:
            # zeile in liste umwandeln. am komma
            tmp = line.rstrip("\n").split(",")
            # dictionary erstellen
            d = {
                "name" : str(tmp[0]),
                "score": int(tmp[1]),
                "games": int(tmp[2])
            }
            # dictionary in liste packen
            data.append(d)
    return data


def updateHighscore(username, score: int):
    data = readHighscore()

    # Daten manipulieren wenn eintrag vorhanden
    found = False
    for i, entry in enumerate(data):
        if entry["name"] == username:
            entry["score"] += score
            entry["games"] += 1
            found = True
            break

    # Falls noch nicht vorhanden -> neu anhängen
    if not found:
        row = {
            "name": username,
            "score": score,
            "games": 1
        }
        data.append(row)

    writeHighscore(data)

#############################
#  schreiben Test
"""
data = [
    {'name': 'Susi', 'score': 1000, 'games': 3},
    {'name': 'Moritz', 'score': 40, 'games': 2},
    {'name': 'Hans', 'score': 200, 'games': 10}
]
writeHighscore(data)
"""
##########################################################
# updaten Test

#username = input("Bitte Name eingeben: ")
username = "Helmut"
updateHighscore(username, 100)


############################
# lesen Test
"""
ergebnis = readHighscore()
print(ergebnis)
for erg in ergebnis:
    print(erg)
"""

FILENAME = "..\\data\\highscore_test.txt"

def writeHighscore(data: list[dict]):
    try:
        with open(FILENAME, "w") as file:
            for entry in data:
                file.write(f"{entry['name']},{entry['score']},{entry['games']}\n")
    except Exception as e:
        print(f"Fehler beim Schreiben der Highscoredatei: {e}")


def readHighscore():
    try:
        with open(FILENAME, "r") as file:
            data = file.readlines()
            # List comprehension
            return [
                {
                    "name": entry.split(",")[0].strip(),
                    "score": entry.split(",")[1].strip(),
                    "games": entry.split(",")[2].strip()
                }
                for entry in data
            ]

    except Exception as e:
        print(f"Fehler beim Lesen der Highscoredatei: {e}")

def updateHighscore(username, score: int):
    try:
        data = readHighscore()
        found = False
        for entry in data:
            if entry["name"] == username:
                entry["score"] = str(int(entry["score"]) + score)
                entry["games"] = str(int(entry["games"]) + 1)
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

    except Exception as e:
        print(f"Fehler beim Updaten der Highscoredatei: {e}")

################################################################################################
"""
data = [
    {'name': 'Susi', 'score': 1000, 'games': 3},
    {'name': 'Moritz', 'score': 40, 'games': 2},
    {'name': 'Hans', 'score': 200, 'games': 10}
]
writeHighscore(data)
"""

# updaten Test

#username = input("Bitte Name eingeben: ")
username = "Henry der 2"
updateHighscore(username, 80)




# lesen Test
"""
ergebnis = readHighscore()
print(ergebnis)
for erg in ergebnis:
    print(erg)

"""

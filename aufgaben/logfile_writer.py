""""

Eine Funktion die eine logeintrag in einer Logdatei speichert

Das Logformat soll so aussehen:

[2025-09-17 09:21:22] Datei konnte nicht gefunden werden. /data/nichtda.txt
[2025-09-17 09:21:22] Fehler ....


"""

# Konfiguration
myLogFile = "..\\data\\erster_log.txt"


def writeLog(logfile, message):
    pass




writeLog(myLogFile, "Datei konnte nicht gefunden werden. /data/nichtda.txt")
writeLog(myLogFile, "Neuer Eintrag")
writeLog(myLogFile, "Fehler: Die Welt explodiert gleich..")





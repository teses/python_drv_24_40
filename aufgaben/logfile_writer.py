""""

Eine Funktion die eine logeintrag in einer Logdatei speichert

Das Logformat soll so aussehen:

[2025-09-17 09:21:22] Datei konnte nicht gefunden werden. /data/nichtda.txt
[2025-09-17 09:21:22] Fehler ....


"""
import time


# Konfiguration
myLogFile = "..\\data\\erster_log.txt"


def writeLog(logfile, message):
    pass




writeLog(myLogFile, "Datei konnte nicht gefunden werden. /data/nichtda.txt")
time.sleep(2)
writeLog(myLogFile, "Neuer Eintrag")
time.sleep(2)
writeLog(myLogFile, "Fehler: Die Welt explodiert gleich..")





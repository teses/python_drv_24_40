"""

    analyse einer logdatei

    # Datum und Uhrzeit extrahieren -> ausgebe der ersten logzeit und der letzten
    # Log-Level extrahieren
    # E-Mail-Adressen aus Logs
    # Dateipfade finden
"""


import re

logTextInput = """
2024-01-15 09:30:15 INFO: Benutzer /max.mustermann@firma.de angemeldet
2024-01-15 09:31:22 ERROR: Datei nicht gefunden /pfad/zur/datei.txt
2024-01-15 09:32:18 INFO: Downl@oad gestartet (Size: 1024 KB)
2024-01-15 09:33:45 WARNING: Lang / same Antwortzeit (2.5s)
2024-01-15 09:34:12 INFO: Benutzer anna.schmidt@firma.de angemeldet
2024-01-15 09:44:24 ERROR: Datei nicht gefunden /pfad/zur/datei2.txt
"""

def logfile_analyse(log_text):
    # Datum und Uhrzeit extrahieren
    #match1 = r"[0-9]{2}:[0-9]{2}:[0-9]{2}" # leider nur uhr
    match1 = r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
    zeitstempel = re.findall(match1, log_text)
    print(f"log start: {zeitstempel[0]}:")
    print(f"log ende: {zeitstempel[-1]}")

    # E-Mail-Adressen extrahieren
    #match_email = r"[^\s]+@[^\s]+[^\s]"
    match_email = r'([a-zA-Z0-9._%+-~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    search_email = re.findall(match_email, logTextInput, re.MULTILINE)
    print(search_email)

    #Dateipfade finden
    #match_path = r"/[^\s]+"
    match_path = r'(/[a-zA-Z0-9._/-]+)'
    search_path = re.findall(match_path, logTextInput, re.MULTILINE)
    print(search_path)

    level_pattern = r'(INFO|ERROR|WARNING)'
    levels = re.findall(level_pattern, log_text)
    print(f"\nLog-Level:", levels)

    for level in set(levels):
        anzahl = levels.count(level)
        print(f"{level} {anzahl}")





logfile_analyse(logTextInput)





"""

    analyse einer logdatei

    # Datum und Uhrzeit extrahieren -> ausgebe der ersten logzeit und der letzten
    # Log-Level extrahieren
    # E-Mail-Adressen aus Logs
    # Dateipfade finden
"""


import re

logTextInput = """
2024-01-15 09:30:15 INFO: Benutzer max.mustermann@firma.de␣angemeldet
2024-01-15 09:31:22 ERROR: Datei nicht gefunden /pfad/zur/datei.txt
2024-01-15 09:32:18 INFO: Download gestartet (Size: 1024 KB)
2024-01-15 09:33:45 WARNING: Langsame Antwortzeit (2.5s)
2024-01-15 09:34:12 INFO: Benutzer anna.schmidt@firma.de angemeldet
2024-01-15 09:44:24 ERROR: Datei nicht gefunden /pfad/zur/datei2.txt
"""
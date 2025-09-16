"""

Regex Mustererkennung

Die wichtigsten Funktionen:

Funktion	                    Zweck
re.match(pattern, string)	    Prüft, ob das Muster am Anfang des Strings passt
re.search(pattern, string)	    Prüft, ob das Muster irgendwo im String vorkommt
re.findall(pattern, string)	    Gibt eine Liste aller Treffer zurück
re.sub(pattern, repl, string)	Ersetzt alle Treffer durch repl
re.split(pattern, string)	    Teilt den String nach dem Muster


Hallo thomas@hallo.de Welt
hallo-|12|-sdfasdfgad-|13|-ysfasfv

"""

import re

text = """Kontakt-Informationen:
E-Mail: max.mustermann@beispiel.de
Handy: +49 179 1234567
Telefon: +49 123 456789
Website: https://www.beispiel.de
Weitere E-Mail: anna.schmidt@firma.com
"""

# findet alle Labels
muster = r"^[a-zA-Z-\s]+:"
gefunden = re.findall(muster, text, re.MULTILINE)
print(gefunden)

##############################################################################################
# findet alle Labels und die Werte
muster2 = r"^([a-zA-Z-\s]+:) ([+a-zA-Z0-9.:/@\w ]+)"
gefunden = re.findall(muster2, text, re.MULTILINE)
print(gefunden)




"""

In Python bezeichnet man als Callback-Funktion eine Funktion, die als Argument an eine andere Funktion übergeben wird
und dort zu einem späteren Zeitpunkt aufgerufen wird.

Verwendung:
- Sortierung
- GUI Event-Handling
- Event-handling
"""

def begruessung(name):
    print(f"Hallo {name}")


def abschied(name):
    print(f"Auf wiedersehen {name}")


# Hauptfunktion, die die Callback entgegen nimmt
def nutze_callback(callback, name):
    # Hier wird die übergebene Funktion aufgerufen
    callback(name)



nutze_callback( begruessung, name="Max" )
nutze_callback( abschied, "Max" )
nutze_callback( begruessung, "Susi" )

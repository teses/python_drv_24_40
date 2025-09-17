"""

Auf Ereignisse reagieren
Event-Handling
"""

class EventSystem:

    def __init__(self):
        self.__callbacks = {}


    def registriere_event(self, event_name, callback):
        if event_name not in self.__callbacks:
            self.__callbacks[event_name] = []
        self.__callbacks[event_name].append(callback)

    def feuere_event(self, event_name, name):
        if event_name in self.__callbacks:
            # läuft das array durch mit den registrierten callbacks für das event
            for callback in self.__callbacks[event_name]:
                callback(name)


# Beispiel-Callbacks
def begruessung(name):
    print(f"Hallo {name}!")

def alarm(name):
    print(f"Achtung, {name} hat etwas Wichtiges gemacht!")

def abschied(name):
    print(f"Auf wiedersehen {name}")

# Event-System erstellen
events = EventSystem()

# Callbacks registrieren
events.registriere_event("login", begruessung)
events.registriere_event("login", alarm)
events.registriere_event("logout", abschied)

# Event auslösen
events.feuere_event("login", "Anna")
#
events.feuere_event("logout", "Anna")

print(events.__dict__)
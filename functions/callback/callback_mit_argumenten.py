"""

mit *args und **kwargs müssen die argumente durchgeleitet werden, damit alle Funktionssignaturen funktionieren.

*args erlaubt beliebig viele Positionsargumente
**kwargs erlaubt beliebig viele benannte Argumente

"""


def begruessung(*args, **kwargs):
    print(f"Hallo {kwargs['name']}")

def abschied(*args, **kwargs):
    print(f"Auf wiedersehen {kwargs['name']}")

def birthdayGrussAlter(*args, **kwargs):
    print(f"Herzlichen Glückwunsch zum {kwargs['age']}. Geburtstag {kwargs['name']}")

# Hauptfunktion, die die Callback entgegen nimmt
def nutze_callback(callback, *args, **kwargs):
    #print(args)
    #print(kwargs)

    # Hier wird die übergebene Funktion aufgerufen
    callback(*args, **kwargs)



nutze_callback( begruessung, name="Max" )
nutze_callback( abschied, name="Max" )
nutze_callback( birthdayGrussAlter, name="Max", age=40 )



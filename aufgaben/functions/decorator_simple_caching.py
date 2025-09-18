"""

Ein simpler Cache, der das ergebnis einer Funktion zwischenspeichert

Tipp;
- im cache muss man die daten wiederfinden
- mit funktionsnamen und den parametern einen eindeutigen schlüssel bilden

"""


#
import time


def simple_cache(func):
    #variablen definieren, die in allen dekorierten funktionen gleich ist
    cache = {}

    def wrapper(*args, **kwargs):
        #print(f"Vor der Funktion: {func.__name__}")
        ret = func(*args, **kwargs)
        #print(f"Nach der Funktion: {func.__name__}")
        return ret

    return wrapper


@simple_cache
def addiere(x, y):
    print("addiere aufgerufen")
    time.sleep(2)
    return x + y

@simple_cache
def quadriere(x):
    print("quadriere aufgerufen")
    time.sleep(2)
    return x * x




print(addiere(5, 3))  # dauert 2 sekunden
print("-"*10)
print(addiere(5, 3))  # kommt sofort
print("-"*10)
print(addiere(5, 3))  # kommt sofort
print("-"*10)
print(addiere(10, 5))  # dauert 2 sekunden
print("-"*10)
print(addiere(10, 5)) # kommt sofort

#print(quadriere(3))

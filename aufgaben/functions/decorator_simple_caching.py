"""

Ein simpler Cache, der das ergebnis einer Funktion zwischenspeichert

Tipp;
- im cache muss man die daten wiederfinden
- mit funktionsnamen und den parametern einen eindeutigen schlüssel bilden


Diese Technik nennt man Memoisation
"""


#
import time


def simple_cache(func):
    #variablen definieren, die in allen dekorierten funktionen gleich ist
    cache = {}

    def wrapper(*args, **kwargs):

        # Schritt 1: Schlüssel erstellen
        key = str(hash(str(func.__name__)+str((args, tuple(sorted(kwargs.items()))))))

        # Schritt 2: Prüfen, ob Ergebnis im Cache ist
        if key in cache:
            return cache[key]

        # Schritt 3: Ergebnis neu berechnen
        else :
            # ursprüngliche Funktion ausführen
            ret = func(*args, **kwargs)
            # Ergebnis im Cache speichern
            cache[key] = ret
            return ret


    return wrapper

@simple_cache
def get_userdata(id):
    time.sleep(2) # simulierung einer langsammen abfrage
    return {"id":id, "name":"user_"+str(id), "age": 20}



@simple_cache
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

@simple_cache
def addiere(x, y):
    print("addiere aufgerufen")
    time.sleep(2)
    return x + y

@simple_cache
def subtrahiere(x, y):
    print("subtrahiere aufgerufen")
    time.sleep(2)
    return x + y

@simple_cache
def quadriere(x):
    print("quadriere aufgerufen")
    time.sleep(2)
    return x * x



"""
print("dauert 2 sekunden", addiere(x=5, y=3))  # dauert 2 sekunden
print("-"*10)
print("dauert 2 sekunden", subtrahiere(x=5, y=3))  # dauert 2 sekunden
print("-"*10)
print("kommt sofort", addiere(y=3, x=5))  # kommt sofort
print("-"*10)
print("dauert 2 sekunden", addiere(5, y=3))  # dauert 2 sekunden
print("-"*10)
print("dauert 2 sekunden", addiere(5, 3))  # kommt sofort
print("-"*10)
print("kommt sofort", addiere(5, 3))  # kommt sofort
print("-"*10)
print("dauert 2 sekunden", addiere(10, 5))  # dauert 2 sekunden
print("-"*10)
print("kommt sofort", addiere(10, 5)) # kommt sofort
"""
#print(quadriere(3))

#print(fibonacci(36))
#print(fibonacci(36))
#print(fibonacci(37))
#print(fibonacci(400))


print(get_userdata(1))
print(get_userdata(1))
print(get_userdata(1))

print(get_userdata(2))
print(get_userdata(2))


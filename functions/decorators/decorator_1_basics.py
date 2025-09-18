"""
Ein Dekorator ist eine Funktion, die eine Funktion als Argument entgegennimmt.
Diese Dekorator-Funktion erweitert oder verändert das Ergebnis der entgegengenommenen Funktion.

Anwendung:
- Timing-Verhalten einer Funktion messen
- Logging
- Caching
- Zugriffskontrollen

Grundprinzip: Ein Dekorator ist eine Funktion die eine andere Funktion "umwickelt"
"""

# eine einfache Dekorator Funktion
def simple_decorator(func):

    def wrapper():
        print("Vor der Funktion")
        func()
        print("Nach der Funktion")

    return wrapper


@simple_decorator
def say_hello():
    print("Hallo")

@simple_decorator
def say_gaga():
    print("Gaga")

say_hello()
print("-")
say_gaga()


#simple_decorator(say_hello)

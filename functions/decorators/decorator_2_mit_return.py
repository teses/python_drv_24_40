



# eine einfache Dekorator Funktion
def simple_decorator_return(func):

    def wrapper():
        print("Vor der Funktion")
        ret = func()
        print("Nach der Funktion")
        return ret

    return wrapper

@simple_decorator_return
def say_hello():
    print("say_hello aufgerufen")
    return "Hallo"


# Achtung wenn man dekoriert wird eigentlich die wrapper funktion zurückgegeben
print(say_hello(), type(str(say_hello)))

# zum weiterverarbeiten am besten in den passenden Datentypen umwandeln
test = say_hello()
print("test", str(test))



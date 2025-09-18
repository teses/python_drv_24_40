"""

Decorator mit Argumenten

"""


#
def simple_decorator_args(func):

    def wrapper(*args, **kwargs):
        print(f"Vor der Funktion: {func.__name__}")
        ret = func(*args, **kwargs)
        print(f"Nach der Funktion: {func.__name__}")
        return ret

    return wrapper


@simple_decorator_args
def addiere(x, y):
    print("addiere aufgerufen")
    return x + y

@simple_decorator_args
def quadriere(x):
    print("quadriere aufgerufen")
    return x * x




print(addiere(5, 3))
print(quadriere(3))

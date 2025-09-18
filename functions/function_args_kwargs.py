"""

*args erlaubt beliebig viele Positionsargumente
**kwargs erlaubt beliebig viele benannte Argumente

"""


def testFunktion(*args, **kwargs):
    print(f"Argumente {args}, {kwargs}")


def testFunktionArgs(*args):
    print(f"Argumente {args}")

# die optimale art und weise: aber hier kann man nicht die parameter sehen
def testFunktionKwargs(**kwargs):
    """

    :param kwargs: {"name":"Max", "age":10}
    :return:
    """
    print(f"Argumente {kwargs}")

def testFunktionDict(theDict: dict):
    print(f"Argumente: ", theDict)


# args
testFunktion("a", "b", 10, 20)
testFunktion("a", "b", 10, 20, "hallo")

# kwargs
testFunktion(name="max", age=10)

# mischen geht auch
# positionierte MÜSSEN vor den benannten stehen
testFunktion("a", "b", 10, 20, "hallo", name="max", age=10)

# nur positionierte erlaubt
testFunktionArgs("max", 10)

# nur benannte erlaubt
testFunktionKwargs(name="max", age=10)

# man kann es auch direkt mit einer Dictionary machen.
# Der Aufruf ist nur anders
testFunktionDict({"name":"Max", "age":10})

#
print("--")
myDict = {"name":"Max", "age":10}
# normales füttern über die benannten parameter
# Das ist viel schreibarbeit
testFunktionKwargs(name=myDict["name"], age=myDict["age"])

# mit ** operator
testFunktionKwargs(**myDict)




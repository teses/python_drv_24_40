
import math

zahlen = [1 ,4, 9, 16, 100]


def quadrat(x):
    return x*x

def wurzel(x):
    #return x ** 0.5
    return math.sqrt(x)

def mwst_add(x):
    return x * 1.19


def verarbeite_liste(liste: list[int], callback):
    ret = []
    for x in liste:
        erg = callback(x)
        ret.append(erg)
    return ret


print(verarbeite_liste(zahlen, quadrat))
print(verarbeite_liste(zahlen, wurzel))
print(verarbeite_liste(zahlen, mwst_add))

"""
    In Python stammt @abstractmethod aus dem Modul abc (Abstract Base Classes) und dient dazu,
    abstrakte Methoden in einer Basisklasse zu definieren. Eine abstrakte Methode ist eine Methode,
    die in der Basisklasse nur deklariert, aber nicht implementiert wird.

    Jede konkrete Subklasse muss diese Methode implementieren, sonst kann man die Subklasse nicht instanziieren.


"""
from abc import ABC , abstractmethod


class Tier(ABC):

    @abstractmethod
    def laut_machen(self):
        pass



class Hund(Tier):

    def laut_machen(self):
        print("Wau Wau")


class Katze(Tier):

    def laut_machen(self):
        print("Miau")


class Maus(Tier):

    def laut_machen(self):
        print("Piep")




# Fehler - kann nicht mehr instanziert werden
#t = Tier()

meine_katze = Katze()
meine_katze.laut_machen()

mein_hund = Hund()
mein_hund.laut_machen()

meine_maus = Maus()
meine_maus.laut_machen()



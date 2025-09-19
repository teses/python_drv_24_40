"""

In Python ist @staticmethod ein Dekorator, mit dem man eine Methode in einer Klasse definiert,
die keinen Zugriff auf die Instanz (self) oder die Klasse (cls) benötigt.

Sie verhält sich wie eine ganz normale Funktion, gehört aber zum Namensraum der Klasse.

def name(self) -> normale Methode
def name(cls) -> klassenmethoden
def name() -> static methoden


"""


def normale_methode(arg1, arg2):
    return arg1 + arg2



class MeineKlasse:

    @staticmethod
    def meine_methode(arg1, arg2):
        return arg1 + arg2


# aufruf einer normalen Methode
print(normale_methode(5, 3))

# aufruf der methode in der Klasse
print(MeineKlasse.meine_methode(5, 3))



"""

Public
    Standard in Python: alles ist öffentlich, solange es nicht mit _ oder __ beginnt.
    Es kann von überall zugegriffen werden (innerhalb und außerhalb der Klasse).

Protected (Konvention: ein Unterstrich _)
    Bedeutet "bitte nur innerhalb der Klasse oder von Subklassen benutzen".
    Es ist nicht wirklich geschützt, man kann trotzdem von außen darauf zugreifen.
    Wird nur als Hinweis für Entwickler verwendet.

Private (Names-Mangling mit __)
    Zwei Unterstriche am Anfang: __attribut → Python macht Namensumwandlung (name mangling).
    Der Name wird intern umgeschrieben auf _Klassenname__attribut.
    So wird verhindert, dass Subklassen versehentlich Attribute überschreiben.
    Zugriff von außen ist möglich, aber umständlicher.
"""


class TestKlasse:

    def __init__(self):
        self.publicAttribut = "public"
        self._protectedAttribut = "protected"
        self.__privateAttribut = "private"

    def testMethode(self):
        print(f"{self.publicAttribut}")

    def publicMethod(self):
        print("Ich bin public in der Klasse " + type(self).__name__)

    def _protectedMethod(self):
        print("Ich bin protected in der Klasse " + type(self).__name__)

    def __privateMethod(self):
        print("Ich bin private in der Klasse " + type(self).__name__)


test = TestKlasse()


print(test._protectedAttribut)  # geht, sollte aber nicht gehen. Dies sollte vermieden werden
#print(test.__privateAttribut) # GEHT NICHT !!
print(test._TestKlasse__privateAttribut) # fiese sache um auf private attribute zuzugreifen

#test.publicMethod()
test._protectedMethod() # geht, sollte aber nicht gehen. Dies sollte vermieden werden
#test.__privateMethod() # GEHT NICHT !!
test._TestKlasse__privateMethod() # fiese sache um auf private attribute zuzugreifen



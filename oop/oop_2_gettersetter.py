"""

Getter Setter normal implementiert

"""



class BeispielKlasse:

    def __init__(self, name):
        #self.__name = name  # Attribut mit doppeltem Unterstrich (privat)
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, neuer_name):
        if neuer_name == "":
            raise ValueError

        self.__name = neuer_name.strip()





person = BeispielKlasse(" Thomas ")
#person.set_name("")
print(person.get_name())

print(person.__dict__)
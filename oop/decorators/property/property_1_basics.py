"""

    Thema Getter/Setter

    @property-Decorator

    Damit kann man getter, setter definieren ohne explizite methoden get_.. oder set_... zu schreiben


"""
############################################################
# Unsicher - public
class PersonUnsicher:

    def __init__(self, name):
        self.name = name

#p = PersonUnsicher("Max")
#print(p.name)

#p.name = "Hans"
#print(p.name)

############################################################
class PersonSicher:

    def __init__(self, name):
        #self.__name = name # attribut direkt belegen (8)nicht ideal)
        self.name = name # verwendet den setter

    @property
    def name(self):
        print("getter")
        return self.__name

    @name.setter
    def name(self, name):
        print("setter")
        self.__name = name.strip()



p = PersonSicher(" Max ")
p.name = " Tim "
print(p.name)
print(p._PersonSicher__name) # bitte NICHT!


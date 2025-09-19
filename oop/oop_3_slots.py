"""

In Python sind __slots__ eine spezielle Klassen-Definition, mit der man festlegen kann,
welche Attribute die Objekte einer Klasse haben dürfen.

Standardmäßig speichert Python Objektattribute in einem Dictionary (__dict__).
Das macht Instanzen flexibel, aber auch speicherintensiver.

Mit __slots__ kann man dieses Verhalten ändern:

Vorteile von __slots__
- Weniger Speicherverbrauch
- Instanzen haben kein __dict__ → weniger Overhead.
- Schnellerer Zugriff auf Attribute.
- Einschränkung: verhindert, dass Objekte beliebige Attribute bekommen.

Einschränkung
- Keine Mehrfachvererbung. Wenn die Bassisklasse __slots__ verwendet.

"""

class Person:

    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Susi", 30)
print(p.name)
print(p.age)

#print(p.__dict__) # dies gibt es nicht mehr wenn __slots__ benutzt werden
print(p.__slots__)

#p.city = "Berlin"




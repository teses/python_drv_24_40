




class Person:

    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age



# Typehint angabe wo der Datentyp eine Klasse ist
myPerson: Person = Person("John", 18)
print(myPerson.name)
print(myPerson.age)


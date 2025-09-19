

class Person:

    def __init__(self, name, alter):
        self.name = name # verwendet den setter
        self.alter = alter

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Der Name darf nicht leer sein")
        self.__name = name

    @property
    def alter(self):  # Getter
        return self.__alter

    @alter.setter
    def alter(self, value):
        if not isinstance(value, int):
            raise ValueError("Alter muss eine ganze Zahl sein!")
        if value < 0:
            raise ValueError("Alter kann nicht negativ sein!")
        if value > 150:
            raise ValueError("Alter über 150 ist unrealistisch!")
        self.__alter = value

    def __str__(self):
        return f"{self.name}, {self.alter} Jahre alt"




## Tests:
person = Person("Max", 30)
print(person) # Max, 25 Jahre alt

## Normales Setzen funktioniert:
person.alter = 40
print(person)

## Fehlerhafte Werte kann man abfangen:

try:
    person.alter = -5
except ValueError as e:
    print(f"Fehler: {e}")

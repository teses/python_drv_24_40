""""

Ein Kreis

public
    radius mit @property
    area mit @property
    circumference mit @property

"""

import math

class Kreis:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def diameter(self): # Durchmesser
        return self.radius * 2

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value <= 0:
            raise ValueError("Der Radius muss größer als 0 sein.")
        self._radius = value

    @property
    def area(self) -> float:
        return math.pi * self._radius ** 2

    @property
    def circumference(self) -> float:
        return 2 * math.pi * self._radius

    def __str__(self):
        return (f"Circle(radius={self.radius},"
                f"diameter={self.diameter},"
                f"area={self.area},"
                f"circumference={self.circumference})")


k = Kreis(5)
print(k.radius)    # 5
print(k.area)   # 78.5398...
print(k.circumference)    # 31.4159...
print(k.diameter)    #10
print(k)
"""

Arithmetische Operatoren
__add__(self, other) – Überladung von +.
__sub__(self, other) – Überladung von -.
__mul__(self, other) – Überladung von *.
__truediv__(self, other) – Überladung von /.
__floordiv__(self, other) – //

Vergleichsoperatoren
__eq__(self, other) – ==
__ne__(self, other) – !=
__lt__(self, other) – <
__le__(self, other) – <=
__gt__(self, other) – >
__ge__(self, other) – >=

"""
class Vektor:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vektor(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vektor(self.x * other, self.y * other)

        return Vektor(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"


v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

v3 = v1 + v2
print("__add__", v3, type(v3))

print("__sub__", v1 - v2, type(v1 - v2))

print("__mul__", v1 * v2 )
print("__mul__ mit int",  v1 * 3 )



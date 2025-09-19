"""

    2 public attribute
        width
        height

    2 public attribute über getter
        area
        circumference
        is_square
"""


class Rechteck:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # aus der Methode wird mit @property ein Attribut
    @property
    def is_square(self):
        return self.width == self.height

    @property
    def area(self):
        return self.width * self.height

    @property
    def circumference(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        form = "Quadrat" if self.is_square else "Rechteck"
        return f"{form}: {self.width}x{self.height}, Fläche: {self.area},Umfang: {self.circumference}"


# Test
rechteck = Rechteck(5, 5)
rechteck.width = 10
print(rechteck.is_square)
print(rechteck.area)
print(rechteck.circumference)
rechteck.area = 40
print(rechteck)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height *2)

    def to_string(self):
        return f'Reactangle: width={0}, height={1}'.format(self.width, self.height)

    def set_color(self, color):
        if color != str:
            raise ValueError("Color invalid")
        else:
            self._color = color

    def get_color(self):
        return self._color

    def __repr__(self):
        return f"Rectangle({0}, {1})".format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)

print(f'width={r1.width}')

print(f'area={r1.area()}')

print(r1.to_string())

print(r1 is not r2)

print(r1 == r2) # overridden by the __eq__ method which allows
                # you to deterimine if instances of a class are equal

print(r1 == 0)

print('Less than:', r1 < r2)

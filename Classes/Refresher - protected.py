class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height


    def area(self):
        return self._width * self._height

    def perimeter(self):
        return (self._width * 2) + (self._height *2)

    def to_string(self):
        return f'Reactangle: width={0}, height={1}'.format(self._width, self._height)

    def set_color(self, color):
        if color != str:
            raise ValueError("Color invalid")
        else:
            self._color = color

    def get_color(self):
        return self._color

    def __repr__(self):
        return f"Rectangle({0}, {1})".format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
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

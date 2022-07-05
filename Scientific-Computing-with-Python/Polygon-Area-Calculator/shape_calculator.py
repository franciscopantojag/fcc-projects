class Rectangle:
    def __init__(self, width: 'int', height: 'int'):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width: 'int'):
        self.width = width

    def set_height(self, height: 'int'):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self) -> 'int|float':
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        return (('*' * self.width) + '\n') * self.height

    def get_amount_inside(self, shape: 'Rectangle|Square'):
        current_area = self.get_area()
        shape_area = shape.get_area()
        return int(current_area / shape_area)


class Square(Rectangle):
    def __init__(self, side: int):
        self.height = side
        self.width = side

    def __str__(self) -> str:
        return f'Square(side={self.width})'

    def set_side(self, side: 'int'):
        self.width = side
        self.height = side

    def set_width(self, width: 'int'):
        self.set_side(width)

    def set_height(self, height: 'int'):
        self.set_side(height)


test = Rectangle(10, 2)
print(test.set_height(3))
print(test.width)
print(test.get_area())
print(test.get_perimeter())
print(test.get_diagonal())
print(test.get_picture())

test_2 = Square(2)
print(test_2)
print(test_2.set_height(3))
print(test_2)

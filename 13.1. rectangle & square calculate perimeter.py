class Rectangle():
    def __init__(self, a, b):
        self.a_side = a
        self.b_side = b

    def calculate_perimeter(self):
        return self.a_side * 2 + self.b_side * 2

rectangle = Rectangle(2, 4)
print(rectangle.calculate_perimeter())

class Square():
    def __init__(self, c):
        self.c_side = c

    def calculate_perimeter(self):
        return self.c_side * 4

square = Square(5)
print(square.calculate_perimeter())

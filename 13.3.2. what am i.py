# ? ? ? ? ? ? ? ?  ? ? ? ? ?? ? ? ? ? ?? ?/////////...............

class Shape():
    def __init__(self, a, b, c):
        self.a_side_rectangle = a
        self.b_side_rectangle = b
        self.c_side_square = c

    def what_am_i(self):
        print("Я - фигура")

    

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

shape = Shape(2, 4, 10)

shape.what_am_i()

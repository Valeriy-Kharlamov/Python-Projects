# Варинат решения № 1
"""
class Square():
    square_list = []

    def __init__(self, a):
        self.square_side = a
        self.square_list.append(f" {self.square_side} на {self.square_side} на {self.square_side} на {self.square_side}")

square = Square(29)
print(Square.square_list)
"""
# Варинат решения № 2

class Square():
    def __init__(self, square_side):
        self.a = square_side

    def print_size(self):
        print(f"{self.a} на {self.a} на {self.a} на {self.a}")

square = Square(29)
print(square.print_size())
        

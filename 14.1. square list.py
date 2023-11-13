class Square():
    square_list = []

    def __init__(self, a):
        self.square_side = a
        self.square_list.append(self.square_side)

square = Square(9)

print(Square.square_list)

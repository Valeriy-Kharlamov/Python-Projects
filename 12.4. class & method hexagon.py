class Hexagon():
    def __init__(self, a, b, c, d, e, f):
        self.a_side = a
        self.b_side = b
        self.c_side = c
        self.d_side = d
        self.e_side = e
        self.f_side = f
        

    def calculate_perimeter(self):
        return self.a_side + self.b_side + self.c_side + self.d_side + self.e_side + self.f_side

hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())

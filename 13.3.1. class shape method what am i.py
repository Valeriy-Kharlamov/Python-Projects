class Shape():
    def __init__(self, t, s, a, b, c, k):
        self.triangle = t
        self.square = s
        self.a_side = a
        self.b_side = b
        self.c_side = c
        self.k_side = k
        print("Create!")

    def what_am_i(self):
        print(f"Я {self.triangle} со сторонами A={self.a_side}, B={self.b_side} и C={self.c_side}")
        print(f"Я {self.square} со стороной K={self.k_side}")

name = Shape("Треугольник", "Квадрат", 3, 3, 3, 10)

name.what_am_i()

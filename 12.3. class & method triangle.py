class Triangle():
    def __init__(self, h, a):
        self.height = h
        self.a_side = a
        print("Create!")

    def area(self):
        return 0.5 * self.height * self.a_side

triangle = Triangle(10, 5)
print(triangle.area())

print("ASKHSH 3")
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def emvadon(self):
        self.emv = self.radius * 3.14
    def perimetros(self):
        self.per = 2 * 3.14 * self.radius
circle1 = Circle(5)
circle1.emvadon()
print(circle1.emv)
circle1.perimetros()
print(circle1.per)
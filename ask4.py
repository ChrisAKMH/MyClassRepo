# print("ASKHSH 4")
import math

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def ReadData(self):
        self.x = float(input("Write x: "))
        self.y = float(input("Write y: "))
    def SetData(self, xi, yi):
        self.x = xi
        self.y = yi
    def PrintData(self):
        print("X: ", self.x)
        print("Y: ", self.y)
    def Metro(self):
        return math.sqrt(self.x**2 + self.y**2)


v1 = Vector(1,2)
v1.PrintData()

v2 = Vector()
v2.ReadData()
v2.PrintData()
a = print(v2.Metro())


class Akeraios:
    count = 0

    def __init__(self, x = 0):
        self.x = x
        Akeraios.__count += 1
        print(">>> Ένα αντικείμενο akeraios καταστράφηκε.")
    def SetData(self, x):
        self.x = x
    def getData(self):
        return self.x
    
    def Ekthetis(self, e):
        ekthetis = self.x**e
        print(f"O ekthetis tou {self.x} einai {ekthetis}")
    
    def printCount(self):
        print("To plithos twn antikeimenwn einai ", self.count)
    def getCount():
        return count

    def AddObject():
        count += 1
    def DeleteObject(self):
        count -= 1

v1 = Akeraios(5)
v1.Ekthetis(2)

v1.AddObject()
v1.printCount()

         
    
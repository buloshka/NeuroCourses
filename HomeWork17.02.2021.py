import math

class Triangle:
    def __init__(self,x1,y1,z1,x2,y2,z2,x3,y3,z3):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.z1 = int(z1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.z2 = int(z2)
        self.x3 = int(x3)
        self.y3 = int(y3)
        self.z3 = int(z3)

    def Perimetr(self):
        self.a = math.sqrt((math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2))**2 + (self.z1 - self.z2)**2)
        self.b = math.sqrt((math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2))**2 + (self.z2 - self.z3)**2)
        self.c = math.sqrt((math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2))**2 + (self.z3 - self.z1)**2)
        
        self.perimetr = self.a + self.b + self.c
        return self.perimetr
        
    def Ploshad(self):
    	self.ploshad =  math.sqrt((self.perimetr/2)*((self.perimetr/2) - self.a)*((self.perimetr/2) - self.b)*((self.perimetr/2) - self.c))
    	
    	return self.ploshad

tri = Triangle(input("Введите x1: "),input("Введите y1: "),input("Введите z1: "),input("Введите x2: "),input("Введите y2: "),input("Введите z2: "),input("Введите x3: "),input("Введите y3: "),input("Введите z3: "))
print("Периметр треугольника: ",tri.Perimetr())
print("Площадь треугольника: ",tri.Ploshad())

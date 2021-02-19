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
        self.a = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        self.b = math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        self.c = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)

        self.aa = math.sqrt((self.a)**2 + (self.z1 - self.z2)**2)
        self.bb = math.sqrt((self.b)**2 + (self.z2 - self.z3)**2)
        self.cc = math.sqrt((self.c)**2 + (self.z3 - self.z1)**2)
        
        self.answer = self.aa + self.bb + self.cc
        return self.answer
        
    def Ploshad(self):
    	self.ans = self.answer/2
    	self.ploshad =  math.sqrt(self.ans*(self.ans - self.aa)*(self.ans - self.bb)*(self.ans - self.cc))
    	
    	return self.ploshad

tri = Triangle(input("Введите x1: "),input("Введите y1: "),input("Введите z1: "),input("Введите x2: "),input("Введите y2: "),input("Введите z2: "),input("Введите x3: "),input("Введите y3: "),input("Введите z3: "))
print(tri.Perimetr())
print(tri.Ploshad())
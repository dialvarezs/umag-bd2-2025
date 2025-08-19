import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distancia_origen(self):
        return math.sqrt(self.x**2 + self.y**2)

p1 = Punto(3, 4)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(p1)                   # (3, 4)
suma = p1 + p2
print(suma)                 # (4, 6)
print(p1 == p3)             # True
print(p1 == p2)             # False
print(p1.distancia_origen())# 5.0

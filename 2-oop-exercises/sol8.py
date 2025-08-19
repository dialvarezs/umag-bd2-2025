""" Crea una clase Punto que represente un punto en el plano cartesiano:

Atributos x e y
Debe poder imprimirse como "(x, y)"
Debe poder sumarse con otro punto usando + (suma las coordenadas)
Debe poder compararse con otro punto usando == (igualdad de coordenadas)
Método distancia_origen() que calcule la distancia al punto (0,0)
# Ejemplo:
p1 = Punto(3, 4)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(p1)                    # (3, 4)
suma = p1 + p2               # Suma de puntos
print(suma)                  # (4, 6)
print(p1 == p3)              # True
print(p1 == p2)              # False
print(p1.distancia_origen()) # 5.0 """

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def distancia_origen(self):
        a = self.x**2 + self.y**2
        return math.sqrt(a)
    
    def igual_coordenadas(self, coordenada_2):
        if self.x == coordenada_2.x and self.y == coordenada_2.y:
            return True
        else:
            return False
    
    def __add__(self, coordenada2):
        return Punto(self.x + coordenada2.x, self.y + coordenada2.y)
    
p1 = Punto(3, 4)  
p2 = Punto(1, 2)   
p3 = Punto(3, 4)

print(p1)
suma = p1 + p2
print(suma) 
print(p1.distancia_origen())
print(p1.igual_coordenadas(p3))   
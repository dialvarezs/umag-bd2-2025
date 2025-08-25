"""Crea una clase Calculadora con:

Métodos sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)
El método dividir debe mostrar un mensaje de error si se divide por cero
Método __str__() que retorne "Calculadora lista para usar"
# Ejemplo:
calc = Calculadora()
print(calc.sumar(5, 3))     # 8
print(calc.dividir(10, 0))  # Error: No se puede dividir por cero
print(calc)"""


class Calculadora:
    def __init__(self):
        pass

    def __str__(self):
        return "Calculadora lista para usar"

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        return a / b


calc = Calculadora()
print(calc.sumar(5, 3))
print(calc.dividir(10, 2))
print(calc)

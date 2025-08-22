class Rectangle:
    def __init__(self, width, high):
        self.width = width
        self.high = high

    @property
    def width(self):
        return self._width
    
    @property
    def high(self):
        return self._high

    @width.setter
    def width(self, set_width):
        if set_width > 0:
            self._width = set_width
        else:
            print("El ancho debe ser un valor positivo")
        
    @high.setter
    def high(self, set_high):
        if set_high > 0:
            self._high = set_high
        else:
            print("El alto debe ser un valor positivo")

    @property
    def area(self):
        return self._width * self._high
    
    @property
    def perimeter(self):
        return (self._width + self._high) * 2

    def __str__(self):
        return (f"Rectangulo : {self._width} , {self._high} ; Area : {self.area}, Perimetro : {self.perimeter}")
    
rect = Rectangle(5, 3)
print(rect.area)
rect.width = 10
print(rect.area)
rect.width = -5
print(rect)
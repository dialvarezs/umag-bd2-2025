class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.nombre}, {self.precio}, {self.stock}")
    
    def aplicar_descuento(self, porcentaje):
        self.precio = (self.precio*(100 - porcentaje)/100)
    
    def vender(self, cantidad):
        if (cantidad <= self.stock):
            self.stock = self.stock - cantidad
        else:
            print(f"No hay cantidad suficiente para vender.")

# Ejemplo de uso:
producto = Producto("Laptop", 800000, 5)
producto.mostrar_info()
producto.aplicar_descuento(10)
producto.vender(2)
producto.mostrar_info()

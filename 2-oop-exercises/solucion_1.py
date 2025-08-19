class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")
    
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Nuevo precio de {self.nombre} después del descuento: {self.precio:.0f}")

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Vendidos {cantidad} de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad} de {self.nombre}. Stock actual: {self.stock}")

producto = Producto("Laptop", 800000, 5)
producto.mostrar_info()
producto.aplicar_descuento(10)
producto.vender(2)
# Crea una clase Vehiculo con:

# marca, modelo, año
# Método arrancar() que imprime "El vehículo está arrancando"
# Método __str__() con información del vehículo
# Crea las clases Auto y Motocicleta que funcionen como Vehiculo pero:

# Auto:

# Atributo adicional: num_puertas
# Su arrancar() debe decir "El auto está arrancando"
# Motocicleta:

# Atributo adicional: cilindrada
# Su arrancar() debe decir "La motocicleta está arrancando"
# Crea una función probar_vehiculo(vehiculo) que funcione con cualquier tipo de vehículo.

# # Ejemplo:
# auto = Auto("Toyota", "Corolla", 2020, 4)
# moto = Motocicleta("Honda", "CBR", 2021, 600)

# vehiculos = [auto, moto]
# for vehiculo in vehiculos:
#     probar_vehiculo(vehiculo)


class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        print(f"El vehículo esta arrancando")

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas

    def arrancar(self):
        print("El auto esta arrancando")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def arrancar(self):
        print("La motocicleta esta arrancadando")


def probar_vehiculo(vehiculo):
    vehiculo.arrancar()
    print(vehiculo)


auto = Auto("Toyota", "Corolla", 2020, 4)
moto = Motocicleta("Honda", "CBR", 2021, 600)

vehiculos = [auto, moto]
for vehiculo in vehiculos:
    probar_vehiculo(vehiculo)

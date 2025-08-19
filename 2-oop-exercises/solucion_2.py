class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo_inicial=0):
        self.titular = titular
        self.__numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito realizado: {monto}. Saldo actual: {self.saldo}.")
        else:
            print("La cantidad a depositar debe ser positiva.")
        
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro realizado: {monto}. Saldo actual: {self.saldo}.")
        else:
            print("Fondos insuficientes o cantidad inválida para retirar.")
        
    def obtener_saldo(self):
        return self.saldo
        
    def transferir(self, cuenta_destino, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            cuenta_destino.saldo += monto
            print(f"Transferencia de {monto} a {cuenta_destino.titular} realizada. Saldo actual: {self.saldo}.")
        else:
            print("Fondos insuficientes o cantidad inválida para transferir.")

    def obtener_numero_cuenta(self):
        """Método para acceder al número de cuenta de forma controlada"""
        return self.__numero_cuenta

    def __str__(self):
        return f"Cuenta de {self.titular} (Número: {self.__numero_cuenta}) - Saldo: {self.saldo}"

cuenta1 = CuentaBancaria("Ana García", "123456789", 100000)
cuenta2 = CuentaBancaria("Carlos López", "987654321", 50000)
cuenta1.transferir(cuenta2, 25000)
print(cuenta1)

# Demostración de que el atributo es privado
print("\n--- Demostrando privacidad del número de cuenta ---")
print(f"Acceso mediante método: {cuenta1.obtener_numero_cuenta()}")

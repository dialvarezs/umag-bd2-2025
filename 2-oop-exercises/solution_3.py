# Crea una clase base `Empleado` con:
# - `nombre`, `apellido`, `rut`, `sueldo_base`
# - Método `calcular_sueldo()` que retorna el sueldo base
# - Método `__str__()` que muestra información del empleado

# Crea las siguientes clases que deben funcionar como `Empleado` pero con características adicionales:

# **`Vendedor`**:
# - Atributo adicional: `comisiones` (lista de montos)
# - Su `calcular_sueldo()` debe incluir: sueldo base + suma de comisiones
# - Método `agregar_comision(self, monto)` para añadir comisiones

# **`Gerente`**:
# - Atributo adicional: `bono_gerencial` (porcentaje)
# - Su `calcular_sueldo()` debe incluir: sueldo base + (sueldo base * bono/100)

class Employee:
    """Representa un empleado con información básica.
    
    Attributes:
        name: Nombre del empleado.
        last_name: Apellido del empleado.
        social_number: Número de identificación social.
        salary: Salario del empleado.
    """
    def __init__(self, name, last_name, social_number, initial_salary=0):
        """Inicializa una nueva instancia de Employee.
        
        Args:
            name: Nombre del empleado.
            last_name: Apellido del empleado.
            social_number: Número de identificación social.
            initial_salary: Salario inicial (por defecto 0).
        """
        self.name = name
        self.last_name = last_name
        self.social_number = social_number
        self.salary = initial_salary

    def calculate_salary(self):
        """Calcula el salario del empleado.
        
        Returns:
            El salario calculado.
        """
        return self.salary

    def __str__(self):
        """Representación en cadena del empleado.
        
        Returns:
            Cadena con detalles del empleado.
        """
        return f"Employe details - Name : {self.name} ; Last Name : {self.last_name} ; Social Number : {self.social_number} ; Salary : {self.salary}"


class Seller(Employee):
    """Representa un vendedor con comisiones.
    
    Attributes:
        commissions: Lista de comisiones ganadas.
    """
    def __init__(self, name, last_name, social_number, initial_salary, commissions=None):
        """Inicializa una nueva instancia de Seller.
        
        Args:
            name: Nombre del vendedor.
            last_name: Apellido del vendedor.
            social_number: Número de identificación social.
            initial_salary: Salario inicial.
            commissions: Lista inicial de comisiones (por defecto None).
        """
        super().__init__(name, last_name, social_number, initial_salary)

        if commissions is None:
            self.commissions = []
        else:
            self.commissions = commissions

    def add_commission(self, amount):
        """Añade una comisión a la lista.
        
        Args:
            amount: Monto de la comisión.
        """
        self.commissions.append(amount)

    def calculate_salary(self):
        """Calcula el salario incluyendo comisiones.
        
        Returns:
            El salario total con comisiones.
        """
        total_commissions = sum(self.commissions)
        self.salary += total_commissions
        return self.salary


class Manager(Employee):
    """Representa un gerente con bonificación.
    
    Attributes:
        manager_bonus: Porcentaje de bonificación gerencial.
    """
    def __init__(self, name, last_name, social_number, initial_salary, manager_bonus):
        """Inicializa una nueva instancia de Manager.
        
        Args:
            name: Nombre del gerente.
            last_name: Apellido del gerente.
            social_number: Número de identificación social.
            initial_salary: Salario inicial.
            manager_bonus: Porcentaje de bonificación gerencial.
        """
        super().__init__(name, last_name, social_number, initial_salary)
        self.manager_bonus = manager_bonus

    def calculate_salary(self):
        """Calcula el salario con bonificación gerencial.
        
        Returns:
            El salario con bonificación aplicada.
        """
        self.salary = self.salary + (self.salary * (self.manager_bonus / 100))
        return self.salary


seller = Seller("Juan", "Pérez", "12345678-9", 500000)
seller.add_commission(50000)
seller.add_commission(75000)
print(f"Seller salary : {seller.calculate_salary()}")

manager = Manager("María", "González", "98765432-1", 800000, 25)
print(f"Manager salary: {manager.calculate_salary()}")

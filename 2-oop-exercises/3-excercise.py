
class Employes:
    def __init__(self,name,last_name,social_number,initial_salary=0):
        self.name = name
        self.last_name = last_name
        self.social_number = social_number
        self.salary = initial_salary

    def calculate_salary(self):
        return self.salary
    
    def __str__(self):
        return f"Employe details - Name : {self.name} ; Last Name : {self.last_name} ; Social Number : {self.social_number} ; Salary : {self.salary}"

class Seller(Employes):
    def __init__(self,name,last_name,social_number,initial_salary,commissions=None):
        super().__init__(name,last_name,social_number,initial_salary)

        if commissions is None:
            self.commissions = []
        else:
            self.commissions = commissions

    def add_commission(self,amount):
        self.commissions.append(amount)

    def calculate_salary(self):
        total_commissions = sum(self.commissions)
        self.salary += total_commissions
        return f"{self.salary}"


class Manager(Employes):
    def __init__(self,name,last_name,social_number,initial_salary,manager_bonus):
        super().__init__(name,last_name,social_number,initial_salary)
        self.manager_bonus = manager_bonus

    def calculate_salary(self):
        self.salary = self.salary + (self.salary * (self.manager_bonus/100) )
        return f"{self.salary:.0f}"

seller = Seller("Juan", "Pérez", "12345678-9", 500000)
seller.add_commission(50000)
seller.add_commission(75000)
print(f"Seller salary : {seller.calculate_salary()}")

manager = Manager("María", "González", "98765432-1", 800000, 25)
print(f"Manager salary: {manager.calculate_salary()}")
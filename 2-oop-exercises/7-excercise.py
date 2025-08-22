class Inventory:
    def __init__(self):
        self.items = {}

    def __setitem__(self, item_name, price):
        self.items[item_name] = price
    
    def __getitem__(self,item_name):
        return self.items[item_name]
    
    def __len__(self):
        return len(self.items)
    
    def total(self):
        return sum(item['precio'] * item['cantidad'] for item in self.items.values())

    

inventory = Inventory()
inventory["laptop"] = {"precio": 800000, "cantidad": 5}
inventory["mouse"] = {"precio": 15000, "cantidad": 20}
print(len(inventory))  # 2
print(inventory["laptop"])  # {'precio': 800000, 'cantidad': 5}
print(f"Valor total: ${inventory.total()}")
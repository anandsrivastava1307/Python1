class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_details(self):
        
        print(f"Product: {self.name}, Price: {self.price}")

class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def show_details(self):
        print(f"Electronics: {self.name}, Price: {self.price}, Warranty: {self.warranty} month")

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def show_details(self):
        print(f"Clothing: {self.name}, Price: ${self.price}, Size: {self.size}")

p1 = Electronics("Refrigerator", 15000, 12)
p2 = Clothing("T-shirt", 550, "L")

p1.show_details()
p2.show_details()

class Product:
    def __init__(self, name: str, price:float, quantity: int):
        if not name or not isinstance(name, str):
            raise ValueError("Name of the product must be a non-empty string.")
        if price < 0:
            raise ValueError("There cannot be a negative price.")
        if quantity < 0:
            raise ValueError("Quantity can not be negative")
        
        self.name = name.strip()
        self.price = price
        self.quantity = quantity
    def add_inventory(self, amount: int):
        if amount < 0:
            raise ValueError("We can not add negative quantity.")
        self.quantity += amount
    def remove_inventory(self, amount: int):
        if amount < 0:
            raise ValueError("We can not remove negative quantity.")
        if amount > self.quantity:
            raise ValueError("There is no enough inventory to remove.")
        self.quantity -= amount
    def total_value(self) -> float:
        return self.price*self.quantity
    def __str__(self):
        return f"{self.name}- ${self.price:.2f}, Quantity: {self.quantity}"
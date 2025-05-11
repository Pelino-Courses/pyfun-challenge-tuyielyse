from product import Product
class Inventory:
    def __init__(self):
        self.products = {} 

    def add_product(self, product: Product):
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists.")
        self.products[product.name] = product

    def remove_product(self, product_name: str):
        if product_name not in self.products:
            raise KeyError(f"product '{product_name}' not found.")
        del self.products[product_name]

    def get_total_value(self) -> float:
        return sum(p.total_value() for p in self.products.values())
    
    def list_products(self):
        for product in self.products.values():
            print(product)


h = Inventory()
p1 = Product("Salt", 3.5, 10) 
p2 = Product("Rice", 68.0, 60)

h.add_product(p1)
h.add_product(p2)

h.list_products()
print("Total Inventory:", h.get_total_value())

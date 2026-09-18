class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    
    def __init__(self):
        self.product_list = []

    def add_product(self, product:Product):
        self.product_list.append(product)

    def show_product_list(self):
        for product in self.product_list:
            print(f"""{product.name} - {product.price} - {product.quantity}""")

    def calc_total_inventary(self):
        total = 0
        for product in self.product_list:
            print(f"Total: {total} \n Product name: {product.name} \n Product price: {product.price} \n Product Quantity: {product.quantity}")
            total += (product.price * product.quantity)
        return total;

def start():
    product1 = Product("Mouse", 5000, 3)
    product2 = Product("Teclado", 8000, 2)
    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)

    print(f"El Valor total del inventario es de: {inventory.calc_total_inventary()}")

start()
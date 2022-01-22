class Product:

    product_id = 1

    def __init__(self, name = "Unknown Product", price = 999, category = "Unknown"):
        self.name = name
        self.price = price
        self.category = category
        self.id = Product.product_id
        Product.product_id += 1

    def update_price(self, percent_change, is_increased):
        if(is_increased == True):
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self

    def print_info(self):
        print(f"Product: {self.name}\nCategory: {self.category}\nPrice: ${self.price}\n")


apple = Product("Apple", 2, "Fruit")
banana = Product("Banana", 3, "Fruit")
soap = Product("Soap", 5, "Hygiene")
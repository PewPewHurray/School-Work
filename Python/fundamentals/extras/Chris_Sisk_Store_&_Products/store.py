import product

class Store:
    def __init__(self, name = "Buy More", product_list = []):
        self.name = name
        self.product_list = product_list

    def add_products(self, new_product):
        self.product_list.append(new_product)
        return self

#    def sell_product(self, id):
#        self.product_list.remove(id)
#        return self

    def sell_product(self, id):
        for item in self.product_list:
            if (item.id == id):
                self.product_list.remove(item)
                return self
        return self

    def inflation(self, percent_increase):
        for item in self.product_list:
            item.update_price(percent_increase, True)
        return self
    
    def set_clearance(self, category, percent_discount):
        for item in self.product_list:
            if (item.category == "Fruit"):
                item.update_price(percent_discount, False)
        return self
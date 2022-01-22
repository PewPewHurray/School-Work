import store
import product

first = store.Store()

first.add_products(product.apple).add_products(product.banana).add_products(product.soap)

print("Product List")
first.product_list[0].print_info()
first.product_list[1].print_info()
first.product_list[2].print_info()

first.inflation(.05)

print("Product List with Inflation")
first.product_list[0].print_info()
first.product_list[1].print_info()
first.product_list[2].print_info()

first.set_clearance("Fruit", .5)

print("Product List with Fruit Clearanced")
first.product_list[0].print_info()
first.product_list[1].print_info()
first.product_list[2].print_info()

#first.sell_product(first.product_list[0])
first.sell_product(1)

print("Product List after selling the Apple")
first.product_list[0].print_info()
first.product_list[1].print_info()
first.product_list[2].print_info()


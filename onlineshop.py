class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.addresses = []
        self.shopping_cart = ShoppingCart()
        self.orders_history = []

    def add_address(self, street, city, zip_code):
        address = Address(street, city, zip_code)
        self.addresses.append(address)
        print("New address added successfully.")

    def search_product(self, product_name, products_list):
        results = []
        for product in products_list:
            if product_name.lower() in product.name.lower():
                results.append(product)
        return results

    def products_by_price(self, products_list):
        return sorted(products_list, key=lambda product: product.price)

    def add_to_shoppingcart(self, product, quantity):
        self.shopping_cart.add_product(product, quantity)
    
    def show_shopping_cart(self):
        self.shopping_cart.show_cart()

    def finalize_purchase(self):
        total = self.shopping_cart.calculate_total()
        confirmation = input(f"Total price: {total} - Confirm purchase? (yes/no): ")
        if confirmation.lower() == "yes":
            self.orders_history.append(self.shopping_cart.items)
            self.shopping_cart = ShoppingCart()
            print("Purchase completed successfully.")
        else:
            print("Purchase canceled.")


class Admin:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, description):
        product = Product(name, price, description)
        self.products.append(product)
        print(f"Product '{name}' added successfully.")

    def delete_product(self, product_name):
        updated_products = []
        for product in self.products:
            if product.name != product_name:
                updated_products.append(product)
        self.products = updated_products
        print(f"Product '{product_name}' deleted successfully.")

    def edit_product(self, product_name, new_name=None, new_price=None, new_description=None):
        for product in self.products:
            if product.name == product_name:
                if new_name: product.name = new_name
                if new_price: product.price = new_price
                if new_description: product.description = new_description
                print(f"Product '{product_name}' updated successfully.")
                return
        print(f"Product '{product_name}' not found.")


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))
        print(f"{quantity} x '{product.name}' added to cart.")

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def show_cart(self):
        print("Your shopping cart:")
        for product, quantity in self.items:
            print(f"{product.name} - Quantity: {quantity} - Unit Price: {product.price}")
        print(f"Total: {self.calculate_total()}")


if __name__ == "__main__":
    admin = Admin()
    admin.add_product("Laptop", 1500, "A powerful laptop for work and gaming.")
    admin.add_product("Phone", 800, "A flagship smartphone.")
    admin.add_product("Headphones", 50, "High-quality headphones.")
    admin.add_product("Laptop Stand", 20, "A portable laptop stand.")

    print("\nAvailable products:")
    for product in admin.products:
        print(f"{product.name} - Price: {product.price}")

    user1 = User("ali", "1234")
    user1.add_address("Freedom Street", "Tehran", "1234567890")

    search_results = user1.search_product("laptop", admin.products)
    print("\nSearch results for 'laptop':")
    for product in search_results:
        print(f"{product.name} - Price: {product.price} - Description: {product.description}")

    user1.add_to_shoppingcart(admin.products[0], 1)
    user1.add_to_shoppingcart(admin.products[2], 2)

    user1.show_shopping_cart()

    user1.finalize_purchase()

    print("\nOrder history:")
    for order in user1.orders_history:
        for product, quantity in order:
            print(f"{product.name} - Quantity: {quantity}")
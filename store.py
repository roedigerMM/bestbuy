from products import Product

class Store:

    def __init__(self, products):
        self.products = []
        for product in products:
            if not isinstance(product, Product):
                raise TypeError("Product must be of type Product")
            else:
                self.products.append(product)


    def add_product(self, product):
        """Adds a product to the store"""
        if not isinstance(product, Product):
            raise TypeError("Product must be of type Product")
        else:
            self.products.append(product)
        #self.products.append(product)


    def remove_product(self, product):
        """Removes a product from the store"""
        if type(product) is not Product:
            raise TypeError("Product must be of type Product")
        elif product not in self.products:
            raise ValueError("Product not in the store")
        else:
            self.products.remove(product)


    def get_total_quantity(self) -> int:
        """Returns the total quantity of products in the store"""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self) -> list[Product]:
        """Returns all products in the store that are active"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0

        # Validation Loop
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("Product must be of type Product")

            elif not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be positive")

            elif product not in self.products:
                raise ValueError("Product not in the store")

            elif not product.is_active():
                raise ValueError("Product is not available")

            elif quantity > product.get_quantity():
                raise ValueError("Not enough items in stock")

        # Execution Loop
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
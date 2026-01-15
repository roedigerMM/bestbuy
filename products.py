class Product:

    total_quantity = 0

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        Product.total_quantity += quantity


    def get_quantity(self) -> int:
        """Returns the quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity."""
        Product.total_quantity = Product.total_quantity - self.quantity + quantity
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        """Returns True if the product is active."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self):
        """Prints a string that represents the product"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.
        """
        if quantity > self.quantity:
            raise ValueError("Quantity cannot be greater than available product quantity")

        self.set_quantity(self.quantity - quantity)
        return float(self.price * quantity)
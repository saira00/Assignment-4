class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Getter

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value  # Setter

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price  # Deleter

# Example usage
p = Product(100)

print("Initial Price:", p.price)  # Accessing price via getter

p.price = 150  # Setting price via setter
print("Updated Price:", p.price)

p.price = -50  # Invalid price (negative)

del p.price  # Deleting price

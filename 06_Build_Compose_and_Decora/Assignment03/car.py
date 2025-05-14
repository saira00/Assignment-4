class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand

    # Public method
    def start(self):
        print(f"{self.brand} car is starting...")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Brand:", my_car.brand)

# Call public method
my_car.start()

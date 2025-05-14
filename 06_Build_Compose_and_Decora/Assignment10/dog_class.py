class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Example usage
dog1 = Dog("Buddy", "Labrador")
dog1.bark()

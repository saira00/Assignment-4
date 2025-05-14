class Student:
    def __init__(self, name, marks):
        self.name = name      # Initializing name using self
        self.marks = marks    # Initializing marks using self

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage:
student1 = Student("Saira", 92)
student1.display()

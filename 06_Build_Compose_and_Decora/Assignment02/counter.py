class Counter:
    # Class variable to track number of objects created
    count = 0

    def __init__(self):
        # Increment the class variable each time an object is created
        Counter.count += 1

    @classmethod
    def show_count(cls):
        # Display the count using cls
        print(f"Total objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the total count of objects
Counter.show_count()  # Output: Total objects created: 3

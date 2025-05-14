class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an object of Multiplier
times_three = Multiplier(3)

# Test if the object is callable
print("Is 'times_three' callable?", callable(times_three))

# Call the object like a function
result = times_three(10)
print("Result of times_three(10):", result)

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # Return the iterator object itself
        return self

    def __next__(self):
        # Stop iteration when current is less than 0
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Example usage:
for number in Countdown(5):
    print(number)

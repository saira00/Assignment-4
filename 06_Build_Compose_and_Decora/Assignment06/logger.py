class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object is being destroyed.")


# Example usage
logger = Logger()

# Deleting the object manually to see the destructor message
del logger

# Or let the program end and the destructor will be called automatically

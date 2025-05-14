class Book:
    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
# Example usage
book1 = Book("Harry Potter")
book2 = Book("The Hobbit")

print(f"Total books added: {Book.get_total_books()}")

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True   # default availability

    def __str__(self):
        return f"{self.title} by {self.author}"


class LibraryService:
    def __init__(self):
        # dictionary to store books: key = book_id
        self._books = {}

    def add_book(self):
        # Step 1: Input details
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")

        # Step 2: Create Book object
        new_book = Book(book_id, title, author)

        # Step 3: Store in dictionary
        self._books[new_book.book_id] = new_book

        # Step 4: Output confirmation
        print(f"Book added: {new_book.title}")


# Demo run
if __name__ == "__main__":
    library = LibraryService()
    library.add_book()

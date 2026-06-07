class LibraryService:
    def __init__(self):
        self._books = {}

    def view_books(self):
        # Step 1: Get list of books
        books = list(self._books.values())

        # Step 2: Decision - empty?
        if not books:
            print("No books found.")
            return

        # Step 3: Output header
        print("Books:")

        # Step 4: Iterate through books
        for book in books:
            # Step 5: Decision - available?
            status = "Available" if book.available else "Borrowed"

            # Step 6: Output book details
            print(f"{book.book_id} - {book.title} by {book.author} [{status}]")


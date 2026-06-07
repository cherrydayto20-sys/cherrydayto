class BookNotFoundError(Exception):
    pass

class MemberNotFoundError(Exception):
    pass

class BookUnavailableError(Exception):
    pass


class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        self.available = False


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email


class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = []
        self._loan_counter = 0

    def borrow_book(self):
        try:
            # Step 1: Input details
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")

            # Step 2: Lookup book
            book = self._books.get(book_id)
            if book is None:
                raise BookNotFoundError("Book not found.")

            # Step 3: Lookup member
            member = self._members.get(member_id)
            if member is None:
                raise MemberNotFoundError("Member not found.")

            # Step 4: Check availability
            if not book.available:
                raise BookUnavailableError("Book is already borrowed.")

            # Step 5: Borrow book + create loan
            book.borrow()
            self._loan_counter += 1
            loan_id = f"L{self._loan_counter:03}"
            loan = Loan(loan_id, book, member)
            self._loans.append(loan)

            # Step 6: Output success
            print(f"{member.name} borrowed {book.title}")

        except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
            # Step 7: Output error
            print(f"Error: {e}")

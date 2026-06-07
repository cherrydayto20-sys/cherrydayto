class LoanNotFoundError(Exception):
    pass


class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = []
        self._loan_counter = 0

    def return_book(self):
        try:
            # Step 1: Input details
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")

            # Step 2: Find loan
            loan = None
            for l in self._loans:
                if l.book.book_id == book_id and l.member.member_id == member_id:
                    loan = l
                    break

            # Step 3: Decision - loan not found
            if loan is None:
                raise LoanNotFoundError("Loan record not found.")

            # Step 4: Process return
            loan.book.available = True
            self._loans.remove(loan)

            # Step 5: Output success
            print(f"{loan.member.name} returned {loan.book.title}")

        except LoanNotFoundError as e:
            # Step 6: Output error
            print(f"Error: {e}")

class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.is_active = True   # default when created

    def close(self):
        self.is_active = False


class LibraryService:
    def __init__(self):
        self._loans = []

    def view_loans(self):
        # Step 1: Get list of loans
        loans = list(self._loans)

        # Step 2: Decision - empty?
        if not loans:
            print("No loans found.")
            return

        # Step 3: Output header
        print("Loans:")

        # Step 4: Iterate through loans
        for loan in loans:
            # Step 5: Decision - active?
            status = "Active" if loan.is_active else "Closed"

            # Step 6: Output loan details
            print(f"{loan.loan_id} - {loan.member.name} borrowed {loan.book.title} [{status}]")

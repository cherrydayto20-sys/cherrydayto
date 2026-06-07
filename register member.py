class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class LibraryService:
    def __init__(self):
        # dictionary to store members: key = member_id
        self._members = {}

    def register_member(self):
        # Step 1: Input details
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        email = input("Enter Member Email: ")

        # Step 2: Create Member object
        new_member = Member(member_id, name, email)

        # Step 3: Store in dictionary
        self._members[new_member.member_id] = new_member

        # Step 4: Output confirmation
        print(f"Member registered: {new_member.name}")


# Demo run
if __name__ == "__main__":
    library = LibraryService()
    library.register_member()

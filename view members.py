class LibraryService:
    def __init__(self):
        self._members = {}

    def view_members(self):
        # Step 1: Get list of members
        members = list(self._members.values())

        # Step 2: Decision - empty?
        if not members:
            print("No members found.")
            return

        # Step 3: Output header
        print("Members:")

        # Step 4: Iterate through members
        for member in members:
            # Step 5: Output member details
            print(f"{member.member_id} - {member.name} ({member.email})")

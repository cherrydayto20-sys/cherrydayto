def main():
    library = LibraryService()

    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.register_member()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.view_books()
        elif choice == "6":
            library.view_members()
        elif choice == "7":
            library.view_loans()
        elif choice == "8":
            # Step 1: Output closing message
            print("Program closed.")
            # Step 2: Break loop
            break
        else:
            print("Invalid choice. Please try again.")

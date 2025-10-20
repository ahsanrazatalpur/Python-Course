# Import necessary modules for handling dates and time
from datetime import date, timedelta

# Define the main class for the Library Management System
class Library:
    # Constructor method to initialize the library data
    def __init__(self):
        # Initialize a list of books with sample data, now including 'category'
        self.books = [
            {'id': 101, 'title': 'Python Programming', 'author': 'Guido van Rossum', 'category': 'Technology', 'total_copies': 5, 'available_copies': 5},
            {'id': 102, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'category': 'Fiction', 'total_copies': 3, 'available_copies': 2}, # 1 copy borrowed
            {'id': 103, 'title': 'Data Structures in C++', 'author': 'Various', 'category': 'Computer Science', 'total_copies': 2, 'available_copies': 0}, # All copies borrowed
        ]
        # Initialize a list of members with sample data
        self.members = [
            {'id': 1, 'name': 'Alice Johnson'},
            {'id': 2, 'name': 'Bob Smith'},
        ]
        # Initialize a list of transactions (records of borrowed books)
        self.transactions = [
            # Sample transaction: Overdue book for testing
            {'member_id': 2, 'book_id': 102, 'borrow_date': date.today() - timedelta(days=10), 'due_date': date.today() - timedelta(days=3)},
            # Sample transaction: On-time book
            {'member_id': 1, 'book_id': 103, 'borrow_date': date.today() - timedelta(days=2), 'due_date': date.today() + timedelta(days=5)},
            # Another transaction: On-time book
            {'member_id': 1, 'book_id': 103, 'borrow_date': date.today() - timedelta(days=1), 'due_date': date.today() + timedelta(days=6)},
        ]
        # Set initial IDs for new books and members
        self.next_book_id = 104
        self.next_member_id = 3
        # Define the due period in days
        self.due_period_days = 7

    # Helper function to print book table header with category
    def _print_book_header(self, include_total=False):
        # Define the header format
        header = f"{'ID':<5}{'Title':<30}{'Author':<20}{'Category':<15}"
        # Add 'Total Copies' column if requested
        if include_total:
            header += f"{'Total Copies':<15}"
        # Always include 'Available' column
        header += f"{'Available':<10}"
        
        # Print the header and separator line
        print(header)
        print("="*(len(header) + 25))

    # Helper function to print a single book row
    def _print_book_row(self, book, include_total=False):
        # Define the row format
        row = f"{book['id']:<5}{book['title']:<30}{book['author']:<20}{book['category']:<15}"
        # Add 'Total Copies' value if requested
        if include_total:
            row += f"{book['total_copies']:<15}"
        # Always include 'Available' value
        row += f"{book['available_copies']:<10}"
        
        # Print the row
        print(row)

    # 1. Display All Books
    def display_all_books(self):
        # Print a header for the book list
        print("\n--- All Library Books (Full Inventory) ---")
        # Check if the book list is empty
        if not self.books:
            print("The library currently has no books in its catalog.")
            return

        # Print the book table header, including total copies
        self._print_book_header(include_total=True)
        # Loop through each book in the list
        for book in self.books:
            # Print the book details
            self._print_book_row(book, include_total=True)

    # 2. Display Available Books
    def display_available_books(self):
        # Print a header for the available book list
        print("\n--- Books Available for Borrowing ---")
        # Initialize a flag to check if any books are available
        available_found = False

        # Print the book table header (only showing available count)
        self._print_book_header(include_total=False)
        # Loop through each book in the list
        for book in self.books:
            # Check if there is at least one available copy
            if book['available_copies'] > 0:
                # Set flag to True
                available_found = True
                # Print the available book details
                self._print_book_row(book, include_total=False)
        
        # If no available books were found, print a message
        if not available_found:
            print("\nNo books are currently available for borrowing.")

    # 3. Display All Members
    def display_all_members(self):
        # Print a header for the member list
        print("\n--- Registered Library Members ---")
        # Check if the member list is empty
        if not self.members:
            print("The library currently has no registered members.")
            return

        # Print table header
        print(f"{'ID':<5}{'Name':<30}")
        print("="*35)
        # Loop through each member in the list
        for member in self.members:
            # Print the member details
            print(f"{member['id']:<5}{member['name']:<30}")

    # 4. Search Books
    def search_books(self):
        # Get the search term from the user
        query = input("Enter book title, author, or category to search: ").strip().lower()
        # Initialize a list to hold matching books
        matches = []
        # Loop through each book
        for book in self.books:
            # Check if the query is in the title, author, or category (case-insensitive)
            if query in book['title'].lower() or query in book['author'].lower() or query in book['category'].lower():
                matches.append(book)

        # Print search results header
        print(f"\n--- Search Results for '{query}' ---")
        # Check if any matches were found
        if not matches:
            print("No books found matching your search criteria.")
            return

        # Print table header for results
        self._print_book_header(include_total=False)
        # Loop through and print the matching books
        for book in matches:
            self._print_book_row(book, include_total=False)

    # 5. Borrow a Book (Updated with search and confirmation)
    def borrow_a_book(self):
        # Print a header
        print("\n--- Borrow a Book ---")
        
        # Get search inputs (Title/Author is mandatory)
        title_query = input("Enter book title (optional): ").strip()
        author_query = input("Enter book author (optional): ").strip()

        # Check if at least one search field was provided
        if not title_query and not author_query:
            print("Error: You must enter at least a Book Title or an Author Name to proceed.")
            return

        # Perform search based on inputs
        matches = []
        for book in self.books:
            title_match = title_query.lower() in book['title'].lower() if title_query else False
            author_match = author_query.lower() in book['author'].lower() if author_query else False
            
            # If both are provided, both must match. If only one is provided, it must match.
            if (title_query and author_query and title_match and author_match) or \
               (title_query and not author_query and title_match) or \
               (author_query and not title_query and author_match):
                
                # Also ensure the book is available before showing it as a borrowable match
                if book['available_copies'] > 0:
                    matches.append(book)

        # Handle search results
        if not matches:
            print("\nSORRY: No available books found matching your search criteria.")
            return
        
        # Display matches and ask for ID confirmation
        print("\nFound the following AVAILABLE matches:")
        self._print_book_header(include_total=False)
        for book in matches:
            self._print_book_row(book, include_total=False)

        try:
            # Ask the user to confirm the book ID from the matches
            book_id = int(input("\nEnter the ID of the specific book you want to borrow from the list above: "))
            member_id = int(input("Enter your Member ID: "))
        except ValueError:
            print("Error: Invalid ID format. Please enter a number.")
            return
        
        # Find the confirmed book (should be in the matches list and thus available) and member
        book = next((b for b in matches if b['id'] == book_id), None)
        member = next((m for m in self.members if m['id'] == member_id), None)

        # Check if the confirmed book ID is valid
        if not book:
            print(f"Error: Book ID {book_id} not found or not available.")
            return
        
        # Check if the member ID is valid
        if not member:
            print(f"Error: Member with ID {member_id} not found. Please register first.")
            return

        # Final check for availability (should be covered by the search, but good practice)
        if book['available_copies'] > 0:
            # Check if the member has already borrowed this specific book (limit one copy per book title per member)
            already_borrowed = any(t['member_id'] == member_id and t['book_id'] == book_id for t in self.transactions)
            if already_borrowed:
                print(f"Error: Member {member_id} has already borrowed a copy of '{book['title']}'.")
                return

            # Decrease the available copy count
            book['available_copies'] -= 1
            
            # Calculate the due date (7 days from today)
            borrow_date = date.today()
            due_date = borrow_date + timedelta(days=self.due_period_days)

            # Record the new transaction
            self.transactions.append({
                'member_id': member_id,
                'book_id': book_id,
                'borrow_date': borrow_date,
                'due_date': due_date
            })

            # Success message
            print(f"\nSUCCESS: '{book['title']}' borrowed by {member['name']}.")
            print(f"Due Date: {due_date.strftime('%Y-%m-%d')} (7-day loan period).")
        else:
            # Safety net message if somehow we missed the availability check
            print(f"SORRY: '{book['title']}' has no available copies right now.")

    # 6. Return a Book
    def return_a_book(self):
        # Print a header
        print("\n--- Return a Book ---")
        try:
            # Get the book ID being returned
            book_id = int(input("Enter the ID of the book being returned: "))
            # Get the member ID returning the book
            member_id = int(input("Enter your Member ID: "))
        except ValueError:
            # Handle non-integer input
            print("Error: Invalid ID format. Please enter a number.")
            return

        # Find the book object
        book = next((b for b in self.books if b['id'] == book_id), None)
        # Find the member object (for confirmation message)
        member = next((m for m in self.members if m['id'] == member_id), None)

        # Check for matching transaction
        transaction_to_remove = next((
            t for t in self.transactions 
            if t['book_id'] == book_id and t['member_id'] == member_id
        ), None)

        # Check if a matching transaction was found
        if transaction_to_remove:
            # Remove the transaction from the list
            self.transactions.remove(transaction_to_remove)
            
            # Increase the available copy count
            book['available_copies'] += 1
            
            # Success message
            print(f"\nSUCCESS: '{book['title']}' returned successfully by {member.get('name', 'Unknown Member')}.")
        else:
            # Error message if the record doesn't exist
            print("Error: No outstanding loan record found for this Book ID and Member ID combination.")

    # 7. View Member's Borrowed Books
    def view_member_borrowed_books(self):
        # Print a header
        print("\n--- View Member's Borrowed Books ---")
        try:
            # Get the member ID
            member_id = int(input("Enter the Member ID: "))
        except ValueError:
            # Handle non-integer input
            print("Error: Invalid ID format. Please enter a number.")
            return
        
        # Find the member object
        member = next((m for m in self.members if m['id'] == member_id), None)

        # Check if the member was found
        if not member:
            print(f"Error: Member with ID {member_id} not found.")
            return

        # Filter transactions for the specified member
        member_transactions = [t for t in self.transactions if t['member_id'] == member_id]

        # Print member name
        print(f"\nBooks currently borrowed by {member['name']} (ID: {member_id}):")

        # Check if the member has any borrowed books
        if not member_transactions:
            print("This member currently has no books borrowed.")
            return

        # Print table header, including Category
        print(f"{'Book ID':<10}{'Title':<30}{'Category':<15}{'Due Date':<15}{'Status':<10}")
        print("="*80)
        # Loop through the member's transactions
        for t in member_transactions:
            # Find the full book details using the book ID
            book = next(b for b in self.books if b['id'] == t['book_id'])
            
            # Check if the book is overdue
            status = "OVERDUE" if t['due_date'] < date.today() else "ON TIME"
            
            # Print the book and transaction details
            print(f"{t['book_id']:<10}{book['title']:<30}{book['category']:<15}{t['due_date'].strftime('%Y-%m-%d'):<15}{status:<10}")

    # 8. View Overdue Books
    def view_overdue_books(self):
        # Print a header
        print("\n--- Overdue Books Report ---")
        # Initialize a list to hold overdue transactions
        overdue_transactions = []
        
        # Get today's date
        today = date.today()

        # Loop through all transactions
        for t in self.transactions:
            # Check if the due date is before today's date
            if t['due_date'] < today:
                overdue_transactions.append(t)

        # Check if any books are overdue
        if not overdue_transactions:
            print("No books are currently overdue. All loans are up to date!")
            return

        # Print table header, including Category
        print(f"{'Book ID':<10}{'Title':<30}{'Category':<15}{'Member Name':<20}{'Due Date':<15}{'Days Overdue':<15}")
        print("="*105)
        
        # Loop through and print overdue transactions
        for t in overdue_transactions:
            # Find book and member details
            book = next(b for b in self.books if b['id'] == t['book_id'])
            member = next(m for m in self.members if m['id'] == t['member_id'])
            
            # Calculate days overdue
            days_overdue = (today - t['due_date']).days
            
            # Print the overdue information
            print(f"{t['book_id']:<10}{book['title']:<30}{book['category']:<15}{member['name']:<20}{t['due_date'].strftime('%Y-%m-%d'):<15}{days_overdue:<15}")

    # 9. Library Report
    def library_report(self):
        # Print a header
        print("\n--- Comprehensive Library Report ---")
        print("="*50)
        
        # Total counts
        total_books = len(self.books) # Number of unique titles
        total_members = len(self.members)
        total_transactions = len(self.transactions) # Number of copies currently borrowed

        # Book copies calculation
        total_copies = sum(b['total_copies'] for b in self.books)
        available_copies = sum(b['available_copies'] for b in self.books)
        borrowed_copies = total_copies - available_copies

        # Print summary statistics
        print(f"Total Unique Titles (Categories): {total_books}")
        print(f"Total Book Copies in Collection:  {total_copies}")
        print("-" * 30)
        print(f"Total Available Copies: {available_copies}")
        print(f"Total Copies Currently Borrowed: {borrowed_copies}")
        print("-" * 30)
        print(f"Total Registered Members: {total_members}")
        print(f"Active Borrowing Records: {total_transactions}")
        print("-" * 50)
        
        # Display the overdue status summary
        overdue_count = sum(1 for t in self.transactions if t['due_date'] < date.today())
        print(f"Overdue Books Count: {overdue_count}")
        print("="*50)

    # 10. Add New Book (Updated to include Category)
    def add_new_book(self):
        # Print a header
        print("\n--- Add New Book to Catalogue ---")
        # Get book details from the user
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        category = input("Enter book category (e.g., Fiction, Science, etc.): ").strip()
        try:
            # Get the number of copies
            copies = int(input("Enter number of copies to add: "))
            # Validate that copies is a positive number
            if copies <= 0:
                print("Error: Number of copies must be positive.")
                return
        except ValueError:
            # Handle non-integer input
            print("Error: Invalid number of copies. Please enter an integer.")
            return

        # Create a dictionary for the new book, including the new 'category' field
        new_book = {
            'id': self.next_book_id,
            'title': title,
            'author': author,
            'category': category,
            'total_copies': copies,
            'available_copies': copies  # Initially all copies are available
        }
        
        # Add the new book to the library's book list
        self.books.append(new_book)
        # Increment the next book ID for the next addition
        self.next_book_id += 1
        
        # Success message
        print(f"\nSUCCESS: Book '{title}' ({category}) added with ID {new_book['id']} ({copies} copies).")

    # 11. Register New Member
    def register_new_member(self):
        # Print a header
        print("\n--- Register New Member ---")
        # Get the member's name from the user
        name = input("Enter member's full name: ").strip()

        # Create a dictionary for the new member
        new_member = {
            'id': self.next_member_id,
            'name': name,
        }
        
        # Add the new member to the library's member list
        self.members.append(new_member)
        # Increment the next member ID for the next registration
        self.next_member_id += 1
        
        # Success message
        print(f"\nSUCCESS: Member '{name}' registered with ID {new_member['id']}.")

# Function to display the main menu (updated with new title)
def display_menu():
    # Print the system title header with the requested name
    print("\n" + "="*50)
    print("    ** LIBRARY MANAGEMENT BY AHSNA RAZA **")
    print("="*50)
    # Print all menu options
    print("1. Display All Books")
    print("2. Display Available Books")
    print("3. Display All Members")
    print("4. Search Books (Title, Author, or Category)")
    print("5. Borrow a Book (Search & Confirm)")
    print("6. Return a Book")
    print("7. View Member's Borrowed Books")
    print("8. View Overdue Books")
    print("9. Library Report")
    print("10. Add New Book (Includes Category)")
    print("11. Register New Member")
    print("0. Exit")
    print("="*50)

# Main function to run the application
def main():
    # Create an instance of the Library class
    library = Library()
    
    # Start the main loop
    while True:
        # Display the menu options
        display_menu()
        
        # Get user input for their choice
        choice = input("Enter your choice (0-11): ")
        
        # Use if/elif/else structure to handle choices
        if choice == '1':
            # Call the function to display all books
            library.display_all_books()
        elif choice == '2':
            # Call the function to display only available books
            library.display_available_books()
        elif choice == '3':
            # Call the function to display all registered members
            library.display_all_members()
        elif choice == '4':
            # Call the function to search for books by title, author, or category
            library.search_books()
        elif choice == '5':
            # Call the updated function to handle borrowing with search and confirmation
            library.borrow_a_book()
        elif choice == '6':
            # Call the function to handle returning a book
            library.return_a_book()
        elif choice == '7':
            # Call the function to view books currently borrowed by a specific member
            library.view_member_borrowed_books()
        elif choice == '8':
            # Call the function to show books that are past their due date
            library.view_overdue_books()
        elif choice == '9':
            # Call the function to generate a summary report of the library's status
            library.library_report()
        elif choice == '10':
            # Call the function to add a new title, including category
            library.add_new_book()
        elif choice == '11':
            # Call the function to register a new user/member
            library.register_new_member()
        elif choice == '0':
            # Exit the loop and the program
            print("\nThank you for using the Library Management System. Goodbye!")
            break
        else:
            # Handle invalid input
            print("\nInvalid choice. Please enter a number between 0 and 11.")
        
        # Pause before showing the menu again (except for exit)
        if choice != '0':
            input("\nPress Enter to return to the main menu...")

# Check if the script is being run directly (best practice)
if __name__ == "__main__":
    # Start the main execution flow
    main()

library_books = ["Python", "Java", "C++", "HTML", "Data Science"]

borrowed_books = []

def display_books():
    print("\nAvailable Books:")
    if len(library_books) == 0:
        print("No books available.")
    else:
        for book in library_books:
            print(book)

def borrow_book():
    book_name = input("Enter book name to borrow: ")
    
    if book_name in library_books:
        library_books.remove(book_name)
        borrowed_books.append(book_name)
        print("Book borrowed successfully.")
    else:
        print("Book not available.")

def return_book():
    book_name = input("Enter book name to return: ")
    
    if book_name in borrowed_books:
        borrowed_books.remove(book_name)
        library_books.append(book_name)
        print("Book returned successfully.")
    else:
        print("This book was not borrowed.")

while True:
    print("\nLibrary Menu")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")

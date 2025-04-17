import os
import json

FILE_NAME = "library.txt"   # <-- yahan ab .txt file use hogi

# File se books load karna
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        return []

# Books ko file mein save karna
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# Book add karna
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    book = {
        "title": title,
        "author": author,
        "read": False
    }
    books.append(book)
    save_books(books)
    print(f"Book '{title}' added successfully!")

# Book remove karna
def remove_book(books):
    title = input("Enter book title to remove: ").strip()
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f"Book '{title}' removed successfully!")
            return
    print(f"Book '{title}' not found!")

# Book search karna
def search_book(books):
    title = input("Enter book title to search: ").strip()
    for book in books:
        if book["title"].lower() == title.lower():
            print("\nBook Found:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Status: {'Read' if book['read'] else 'Not Read'}\n")
            return
    print(f"Book '{title}' not found!")

# Saari books display karna
def display_books(books):
    if not books:
        print("No books in the library.")
        return
    print("\n--- All Books ---")
    for idx, book in enumerate(books, start=1):
        status = "Read" if book["read"] else "Not Read"
        print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Status: {status}")
    print("-----------------\n")

# Total books aur percentage read dikhana
def static_info(books):
    total = len(books)
    read_books = sum(1 for book in books if book["read"])
    read_percentage = (read_books / total * 100) if total > 0 else 0
    print(f"Total Books: {total}")
    print(f"Books Read: {read_books} ({read_percentage:.2f}%)")

# Kisi book ko read mark karna
def mark_as_read(books):
    title = input("Enter book title to mark as read: ").strip()
    for book in books:
        if book["title"].lower() == title.lower():
            book["read"] = True
            save_books(books)
            print(f"Book '{title}' marked as Read!")
            return
    print(f"Book '{title}' not found!")

# Main menu
def menu():
    print("\nWelcome to Personal Library Management System!\n")
    books = load_books()

    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Static Info (Total & Percentage Read)")
        print("6. Mark Book as Read")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            display_books(books)
        elif choice == '5':
            static_info(books)
        elif choice == '6':
            mark_as_read(books)
        elif choice == '7':
            print("Thank you for using Personal Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    menu()

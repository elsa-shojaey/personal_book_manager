from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os
load_dotenv()
name = input("enter your name: ")

print("welcome back", name)

admin_mode = input("Would you like to enter Admin Mode? (yes/no)? ")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("Amin Mode activated successfully!")
    else:
        print("Incorrect password. Please try again.")
books = load_books()
count = int(input("how many do you want to add book? : "))
for i in range(count):
    book_name = input("enter a book: ")
    priority = input("enter priority(low/medium/high): ").lower()
    book = {
        "book_name": book_name,
        "priority": priority,
        "count": count
    }

    books.append(book)
show_books(books)
print("total book:", len(books))
save_books(books)
print(book, "Python Basics added successfully")
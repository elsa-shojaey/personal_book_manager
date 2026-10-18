from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os
load_dotenv()
name = input("enter your name: ")
print("welcome", name)
admin_mode = input("do you want to enter admin mode (yes/no)? ")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("amin mode activated")
    else:
        print("wrong password")
books = load_books()
count = int(input("how many do you want to add book? : "))
for i in range(count):
    book = input("enter a book: ")
    books.append(book)
show_books(books)
save_books(books)
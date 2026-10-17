from books import show_books
name = input("enter your name: ")
print("welcome", name)
books = []
count = int(input("how many do you want to add book? : "))
for i in range(count):
    book = input("enter a book: ")
    books.append(book)
show_books(books)
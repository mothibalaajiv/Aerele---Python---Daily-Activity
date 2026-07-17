from model.Book import Book 

def add(books,book):
    if(book in books):
        print(f"{book.get_book_name()} already exists")
    else:
        books.append(book)
        print(f"{book.get_book_name()} added successfully")


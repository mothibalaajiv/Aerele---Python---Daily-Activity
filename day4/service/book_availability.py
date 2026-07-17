from model.Book import Book 

def availability(book):
    if(book.available==True):
        print(f"{book.get_book_name() } is available")
    else:
        print(f"{book.get_book_name()} is not available")


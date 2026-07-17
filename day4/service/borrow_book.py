from model.Book import Book 

def borrow(book):
    if(book.available==True):
        print("book is available and now you are borrowing it")

    else:
        print("book is already borrowed")

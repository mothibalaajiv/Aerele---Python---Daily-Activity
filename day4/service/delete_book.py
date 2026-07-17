from model.Book import Book 

def delete(book,books):
    if(book in books):
        books.remove(book)
        print("book removed successfully")
    else:
        print("book doesnt exist")
        print("book deletion failed")

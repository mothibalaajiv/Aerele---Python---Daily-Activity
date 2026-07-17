from model.Book import Book 
from service import add_book
from service import borrow_book
from service import delete_book
from service import book_availability

book1 = Book(name= "wings of fire", available= True, author= "Mothi", id= 100)
book2 = Book(name= "siragugal", available= False, author= "Kishore", id= 200)

books = []

add_book.add(books,book1)
add_book.add(books,book2)

book_availability.availability(book2)

borrow_book.borrow(book1)

delete_book.delete(book1,books)


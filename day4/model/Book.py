from dataclasses import dataclass

@dataclass
class Book:
    name : str
    id : int
    author : str
    available : bool

    def __init__(self,name,id,author,available):
        self.name = name
        self.id = id
        self.author = author
        self.available = available

    def get_book_id(self):
        return self.id
    
    def get_book_name(self):
        return self.name

    def get_book_author(self):
        return self.author


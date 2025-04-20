class Book():

    def __init__(self, title, author, isbn, checked_out = False):
        """ base class for all books"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = checked_out
    
    def check_out(self):
        """ marks book as checked out"""
        self.check_out = True
    
    def check_in(self):
        """ marks book as checked in"""
        self.check_out = False

    def display_info(self):
        print(f"\tThe book {self.title} by {self.author} with the isbn {self.isbn} is currently checked out {self.checked_out}")




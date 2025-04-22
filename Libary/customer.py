from book import Book

class Customer():

    def __init__(self, name, customer_id:str, checked_out_books:bool = None):
        self.name = name
        self.customer_id = customer_id
        # You can also use type hints when assigning variables.
        self.checked_out_books:list = checked_out_books if checked_out_books is not None else []

    def check_out_book(self, book:Book):
        self.checked_out_books.append(book)
        print(f"The Book: {book} is checked out")

    def check_in_book(self,book:Book):
        self.checked_out_books.remove(book)

    def display_info(self):
        print(f"\t{self.name} with the ID: {self.customer_id} has the following books: {self.checked_out_books}")

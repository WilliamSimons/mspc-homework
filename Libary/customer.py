class Customer():

    def __init__(self, name, customer_id, checked_out_books = None):
        self.name = name
        self.customer_id = customer_id
        self.checked_out_books = checked_out_books if checked_out_books is not None else []
    
    def check_out_book(self, book):
        self.checked_out_books.append(book)
        print(f"The Booke: {book} is chacked out")
    
    def check_in_book(self,book):
        self.checked_out_books.remove(book)
    
    def display_info(self):
        print(f"\t{self.name} with the ID: {self.customer_id} has the following books: {self.checked_out_books}")

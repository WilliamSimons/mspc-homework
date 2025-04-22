
# We import the `Book` and `Costumer` classes to aggregate type hints.
# This will not change the code functioning, but it will help us to during development
# and it also facilitates the static type checkers of IDE (e.g., cursor). In other
# words, better highlighting and errors checking.

from book import Book
from customer import Customer

class Libary():

    def __init__(self):
        """Creats a Libary"""
        self.books = []
        self.customers = []

    def add_book(self, book:Book):
        """Adds a Book to the Libary"""
        self.books.append(book)
        print(f"{book.title} is now in the libary")

    def add_customer(self, customer:Customer):
        """Adds a customer to the Libary"""
        self.customers.append(customer)
        print(f"{customer.name} is now registered")

    def find_book(self, ISBN:int):
        """Finds a book in the libary with the ISBN"""
        for book in self.books:
            if book.isbn == ISBN:
                return book
        return False

    def find_customer(self, customer_ID:str):
        """Finds name of a customer with the customer ID"""
        for customer in self.customers:
            if customer.customer_id == customer_ID:
                return customer
        return False

    def check_out_book(self, customer_ID:str, ISBN:int):
        """Checks out the book to a customer"""
        if self.find_customer(customer_ID) and self.find_book(ISBN):
            if self.find_book(ISBN).checked_out == False:
                self.find_customer(customer_ID).checked_out_books.append(self.find_book(ISBN))
                self.find_book(ISBN).checked_out = True
                print(f"{customer_ID} checked out {ISBN}")
        else:
            print("Book or customer not found")

    def check_in_book(self, customer_ID:str, ISBN:int):
        """Checks in the book"""
        if self.find_customer(customer_ID) and self.find_book(ISBN):
            if self.find_book(ISBN) in self.find_customer(customer_ID).checked_out_books:
                self.find_customer(customer_ID).checked_out_books.remove(self.find_book(ISBN))
                self.find_book(ISBN).checked_out = False
                print(f"{customer_ID} checked in {ISBN}")
        else:
            print("Book or customer not found")

    def display_books(self):
        """Displays all books in the library"""
        print(f"\nLIST OF BOOKS")
        for book in self.books:
            book.display_info()

    def display_customers(self):
        """Displays all customers of the library"""
        print(f"\nLIST OF CUSTOMERS")
        for customer in self.customers:
            customer.display_info()







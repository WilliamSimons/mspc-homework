"""Example use of the Libary system"""

from libary import Libary
from book import Book
from customer import Customer

def test_libary():

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("1984", "George Orwell", "9780451524935")

# Create customers
    customer1 = Customer("Alice Smith", "C001")
    customer2 = Customer("Bob Johnson", "C002")

# Create library
    library = Libary()
    library.add_book(book1)
    library.add_book(book2)
    library.add_customer(customer1)
    library.add_customer(customer2)


# Perform check-outs
    library.check_out_book("C001", "9780743273565")  # Alice checks out The Great Gatsby
    library.check_out_book("C001", "9780451524935")  # Alice checks out 1984
    library.check_out_book("C002", "9780743273565")  # Bob tries to check out an already checked-out book


# Display info
    library.display_books()
    library.display_customers()

# Perform check-ins
    library.check_in_book("C001", "9780743273565")  # Alice returns The Great Gatsby
    library.check_in_book("C002", "9780743273565")  # Bob tries to return a book he didn't check out

# Display updated info
    library.display_books()


if __name__ == '__main__':
    test_libary()
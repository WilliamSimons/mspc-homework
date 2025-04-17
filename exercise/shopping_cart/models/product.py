"""
Product models for the shopping cart system.
"""
from ..constants import PRODUCT_TYPES

class Product():
    """Base class for all products."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - ${self.price:}")

class Food(Product):
    """Food products with additional attributes."""
    def __init__(self, name, price, expiration_days, organic, calories):
        super().__init__(name, price)
        self.get_expiration_date = expiration_days
        self.is_organic = organic
        self.get_calories = calories

    def get_expiration_date(self):
        print(f" the expiration date is {self.get_expiration_date}")

    def is_organic(self) -> bool:
        if self.is_organic == True:
            print("food is organic")
        else:
            print("food is not organic")
    
    def get_calories(self):
        print(f"the food has {self.get_calories} calories")

class Cleaning(Product):
    """Cleaning products with safety information."""
    def __init__(self, name, price, safe_for_children = False):
        super().__init__(name, price)
        self.is_safe_for_children = safe_for_children

    def is_safe_for_children(self):
        if self.is_safe_for_children == True:
            print("The product is safe for children")
        else:
            print("The product is NOT safe for children")

class Drink(Product):
    """Drink products with container and sugar information."""
    def __init__(self, name, price, expiration_days, sugar_content, container):
        super().__init__(name, price)
        self.get_expiration_date = expiration_days
        self.get_sugar_content = sugar_content
        self.container = container

    def get_expiration_date(self):
        print(f" the expiration date is {self.get_expiration_date}")

    def get_sugar_content(self):
        print(f"the expiration date is {self.get_expiration_date}")

    def get_container_type(self):
        print(f"This product comes in a {self.container}")


# CREATE A PRODUCT
def create_product(product_type, name):
    """Factory function to create products based on type and name. This function MUST return a Product object. """

    product_data = PRODUCT_TYPES[product_type][name]
    
    if product_type == 'food':
        return Food(
            name=name,
            price=product_data['price'],
            expiration_days=product_data['expiration_days'],
            organic=product_data['organic'],
            calories=product_data['calories']
        )
    elif product_type == 'cleaning':
        return Cleaning(
            name=name,
            price=product_data['price'],
            safe_for_children=product_data['safe_for_children']
        )
    elif product_type == 'drinks':
        return Drink(
            name=name,
            price=product_data['price'],
            expiration_days=product_data['expiration_days'],
            sugar_content=product_data['sugar_content'],
            container=product_data['container']
            )
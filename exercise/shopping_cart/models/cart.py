"""
Shopping cart model with user support and error handling.
"""
from ..decorators import membership_welcome
from typing import List, Dict, Union, Optional
from .product import create_product

class ShoppingCart:
    """Shopping cart with user support and error handling."""
    @membership_welcome # This is a decorator, I chose to record data here, you can change it if needed.
    def __init__(self, user: dict=None): #dict=None means that the user should be a dictionary
        self._items = {}  # Format: {product.name: {"product": product, "quantity": quantity}}
        self.user = user # This is new


# ADD PRODUCT
    def add_product(self, 
                    product_type: str, 
                    product_name: str, 
                    quantity=1 
                    #OR:  quantity: Optional[Union[int, float]]=1 --> Union take multiple data types
                    ) -> None: # This is a type hint, it means that the function returns None
        """Adds a product to the cart or increases its quantity."""

        try:
            product = create_product(product_type, product_name)

            if product.name in self._items:
                self._items[product.name]["quantity"]+=quantity
                print(f"you added {quantity} {product_name}")
            else:
                self._items[product.name]={"product":product.name, "quantity":quantity}
                print(f"you added {quantity} {product_name}")

        except:
            # If it fails, print this
            print("Error adding product")


# REMOVE PRODUCT
    def remove_product(self, product_name, quantity=1):
        """Removes a product from the cart or reduces its quantity."""
        try:
            if product_name in self._items:
                if quantity < self._items[product_name]["quantity"]:
                    self._items[product_name]["quantity"]-=quantity
                    print(f"you removed {quantity} {product_name}")
                else:
                    del self._items[product_name]    
                    print(f"you removed {product_name}")
            else:
                print(f"{product_name} was never in your cart")

        except:
            print("Error removing product")

# CALCULATE TOTAL
#    def calculate_total(self) -> float:
#        """Calculates the total cost of all items in the cart."""
#        total = 0.0
#        for item in self._items:
#            total = total + item["name"].price * item["quantity"]
#            print(f"your cart coststs {total} euro")

# CALCULATE TOTAL - solution from cours
    def calculate_total(self):
        """Calculates the total cost of all items in the cart."""
        total = 0.0
        for item in self._items.values():
            total += item["product"].price * item["quantity"]
        return total

# DISPLAY CART - solution from cours
    def display_cart(self) -> None:
        """Displays all items in the cart with their details."""

        print("Shopping Cart:")
        for name, item in self._items.items(): # Don't forget to iterate over the items
           print(f" your cart contains {name}{item}")
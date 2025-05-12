from .constants import CONSTANTS

class Burger:
    """Represents a single burger item with customizable toppings."""

    def __init__(self): # This is complete
        """Initializes a basic burger with no patty or cheese added yet."""
        self.patty = False
        self.cheese = False
        self.base_price = CONSTANTS['BURGUER_BASE_PRICE']
        print(f"Default burger is created")

    def add_patty(self): # THis is missing
        """Adds a patty to the burger."""
        self.patty = True # patty is now on the burger
        print("You added a patty")

    def add_cheese(self): # This is missing
        """Adds cheese to the burger."""
        self.cheese = True # cheese is now on the burger
        print("You added cheese on your burger")

    def get_price(self) -> float : # This is missing
        """Calculates the total price of the burger based on added toppings."""

        price = CONSTANTS['BURGUER_BASE_PRICE'] # access the CONSTANTS to get teh base price

        # If a patty is on the burger the price increases
        if self.patty == True:
            price += CONSTANTS['ADDITIONAL_PATTY_PRICE']

        # If a patty is on the burger the price increases
        if self.cheese == True:
            price += CONSTANTS['ADDITIONAL_CHEESE_PRICE']
    
        return round(price,2)


    def get_name(self)-> str:
        """Generates the display name for the burger based on added toppings."""

        if self.cheese == True and self.patty == True: # If chhese and patty are on teh burger its a cheese burger
            burger_name = "Cheese Burger"
        
        elif self.patty == False and self.cheese == True: # If no patty but cheese is on teh burger its a veggy cheese burger
            burger_name = "Veggy Cheese Burger"

        else: # in any other case its a burger
            burger_name = "Burger"
        return burger_name

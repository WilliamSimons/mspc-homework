""" This file imports dependencies"""
def run():
    
    class Product():
        def __init__(self, name, price):
            self.name = name
            self.price = price
            print(f"{self.name} is created")


    class ShoppingCart(Product):
        def __init__(self, name=0, price=0, quantity = 0):
            super().__init__(name, price)
            self.quantity = quantity
            self.name = name
            self.price = price
            self.cart = {}
            print (f"your shopping cart contains {self.cart}")
        
    # ADD
        def add_product(self, name=0, quantity=1):
            self.name = name
            self.quantity = quantity
            if name in self.cart:
                self.cart[self.name] += self.quantity   
            else:
                self.cart.update({self.name: self.quantity})
            print (f" your added {self.quantity} {self.name}")

    # DISPLAY
        def display_cart(self):
            return f" your cart contains {self.cart}"

    # REMOVE
        def remove_product(self, name, quantity=1):
            self.name = name
            self.quantity = quantity
            if name in self.cart:
                if self.cart[self.name] - quantity > 0:
                    self.cart[self.name] -= self.quantity
                else:
                    del self.cart[self.name]
                print(f" you removed {self.quantity} {self.name}")
            else:
                print (f"{self.name} is not in your cart")




    apple = Product("Apple", 0.99)
    banana = Product("Banana", 0.59)
    milk = Product("Milk", 3.49)

    cart = ShoppingCart()

    cart.add_product(apple, 3)
    cart.add_product(banana)
    cart.add_product(milk, 2)
    cart.display_cart()

    # Remove items
    cart.remove_product(apple, 1)
    cart.remove_product(banana)
    cart.display_cart()

    # Try to remove a product not in the cart
    cart.remove_product(milk, 5)  # Removes all milk
    cart.display_cart()


# file should be run as main
if __name__ == "__main__":
    print("starting")
    run()
    


from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod 
    def make_sound(self):
        pass

    # This is a concrete method, it is already implemented and it can be overriden.    
    def feed(self): 
        print("This animal is fed")

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(f"{self.name} is born")

    def make_sound(self):
        print("mooh")
    
    def milk(self):
        print("cow gives milk")
    
class Chicken(Animal):

    def make_sound(self):
        print("gikerigii")

    def egg(self):
        print("chicken gives egg")
    
class Sheep(Animal):
    def make_sound(self):
        print("mähhh")
    
    def whool(self):
        print("sheep gives whool")

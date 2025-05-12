class Farm():
    def __init__(self):
        self.population = {}
        print("hello, welcome to the your farm")
    
    """Adds an animal"""
    def add_animal(self, animal = str, amount = int):
        if animal in self.population:
            self.population[animal] += amount
        
        else:
            self.population.update({animal: amount})
    
    """removes an animal"""
    def remove_animal(self, animal = str, amount = int):
        try: 
            if animal in self.population:
                if amount < self.population[animal]:
                    self.population[animal] -= amount
                else:
                    del self.population[animal]
        except:
            print("there is no such animal")


    def show_population(self):
        print(self.population)
    
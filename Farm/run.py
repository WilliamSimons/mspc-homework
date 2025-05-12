from farm import Farm
from animal import Cow

def test_farm():

    #creating the farm
    my_farm = Farm()



    # adding animals to the farm
    my_farm.add_animal("cow",30)
    my_farm.add_animal("chicken",20)
    my_farm.remove_animal("chicken",10)
    my_farm.show_population()

    # creating some animals
    cow1 = Cow("peter",30)
    cow1.make_sound



if __name__ == '__main__':
    test_farm()
from animal import Animal
from instances import Bird, Fish, Dog
import random



class NatureReverce():
    '''Zoo class'''
    
    global zoo
    global dead_animals
    global new_zoo

    def __init__(self) -> None:
        pass

    zoo = [
        Bird(),
        Bird(),
        Fish(),
        Fish(),
        Dog(),
        Dog(),
        Animal(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 'Animal'),
        Animal(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 'Animal')        
    ]

    dead_animals = []
    new_zoo = []
    
    def is_dead(self):
        '''Animal health check function'''

        for item in zoo:
            item.is_too_old() # is_too_old check
            
            if item.energy <= 0 or item.weight <=0 or item.is_too_old == True:
                zoo.remove(item)
                dead_animals.append(item)

    def do_something(self):
        '''Calling the animals functions'''

        for item in zoo:
            item.sleep()
            item.eat()
            item.walk()
            item.try_increment_age()

    def new_amnimal(self):
        '''To produce offspring function'''
        global zoo
        zoo += [i for i in zoo if random.random() < 0.3]
        zoo += new_zoo



my_zoo = NatureReverce()
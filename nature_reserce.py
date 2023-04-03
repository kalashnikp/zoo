from animal import Animal
from instances import Bird, Fish, Dog
import random



class NatureReverce():
    '''Zoo class'''
    
<<<<<<< HEAD
=======
    global zoo
    global dead_animals
    global new_zoo

    def __init__(self) -> None:
        pass

>>>>>>> dcaa74bd788b1fda66557b5d53efd04a0601d536
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
<<<<<<< HEAD

    def __init__(self) -> None:
        pass

=======
    
>>>>>>> dcaa74bd788b1fda66557b5d53efd04a0601d536
    def is_dead(self):
        '''Animal health check function'''

        for item in self.zoo:
            item.is_too_old() # is_too_old check
            
            if item.energy <= 0 or item.weight <=0 or item.is_too_old == True:
                self.zoo.remove(item)
                self.dead_animals.append(item)

    def do_something(self):
        '''Calling the animals functions'''

        for item in self.zoo:
            item.sleep()
            item.eat()
            item.walk()
            item.try_increment_age()

    def new_amnimal(self):
        '''To produce offspring function'''
<<<<<<< HEAD

        for item in self.zoo:
            a = random.choices([1, 0], weights=[0.2, 0.8])
            b = int(''.join(map(str, a)))
            c = bool(b)
=======
        global zoo
        zoo += [i for i in zoo if random.random() < 0.3]
        zoo += new_zoo

>>>>>>> dcaa74bd788b1fda66557b5d53efd04a0601d536

            if c == True:
                self.new_zoo.append(item)

<<<<<<< HEAD
    def adding(self):
        self.zoo += self.new_zoo
    
=======
my_zoo = NatureReverce()
>>>>>>> dcaa74bd788b1fda66557b5d53efd04a0601d536

from animal import Animal
from instances import Bird, Fish, Dog
import random



class NatureReverce():
    '''Zoo class'''
    
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
    # Требуется добавить промежуточный список (накопитель) для вхождения new_zoo, впоследствии который надо будет схлопнуть с списком zoo 


    def __init__(self) -> None:
        pass

    def is_dead(self):
        '''Animal health check function'''

        for item in NatureReverce.zoo:
            item.is_too_old() # is_too_old check
            
            if item.energy <= 0 or item.weight <=0 or item.is_too_old == True:
                NatureReverce.zoo.remove(item)
                NatureReverce.dead_animals.append(item)

    def do_something(self):
        '''Calling the animals functions'''

        for item in NatureReverce.zoo:
            item.sleep()
            item.eat()
            item.walk()
            item.try_increment_age()

    def new_amnimal(self):
        '''To produce offspring function'''

        for item in self.zoo:
            a = random.choices([1, 0], weights=[0.2, 0.8])
            b = int(''.join(map(str, a)))
            c = bool(b)

            if c == True:
                NatureReverce.new_zoo.append(item)

    def adding(self):
        NatureReverce.zoo += NatureReverce.new_zoo
    

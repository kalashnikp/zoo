import random

class Animal():
    '''Parent class of the animal'''
    
    age = 1

    def __init__(self, energy, weight, max_age, name):
        self.energy = energy
        self.weight = weight
        self.max_age = max_age
        self.name = name

    def try_increment_age(self):
        '''Random increase in age'''

        b = random.choice([True, False])

        if b == True:
            Animal.age += 1
            return Animal.age
        
    def is_too_old(self):
        '''Checking the current age with the maximum / Boolean function'''

        if (Animal.age >= self.max_age):
            return True
        else:
            return False
    
    def sleep(self):
        '''Sleep function'''

        b = random.choice([True, False])

        if b == True:
            self.energy += 5
            return self.energy

    def eat(self):
        '''Eating function'''

        b = random.choice([True, False])

        if b == True:
            self.energy += 3
            self.weight += 1
            return self.energy, self.weight
        
    def walk(self):
        '''Walking function'''

        b = random.choice([True, False])

        if b == True:
            self.energy -= 5
            self.weight -= 1
            return self.energy, self.weight
        

    
        


        

        
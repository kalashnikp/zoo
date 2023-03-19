import random

class Animal():
    '''Родительский класс животного / Parent class of the animal'''
    age = 1
    
    def __init__(self, energy, weight, max_age, name):
        self.energy = energy
        self.weight = weight
        self.max_age = max_age
        self.name = name
        
    def is_too_old(self):
        '''Проверка текущего возраста с максимальным / Checking the current age with the maximum'''
        
        if (self.age >= self.max_age) :
            return True
        else:
            return False
        
    def try_increment_age(self):
        '''Рандомное увеличение возраста / Random increase in age'''
        
        b = random.choice([True, False])

        if b == True:
            if self.is_too_old() == False or self.weight > 0 or self.energy > 0:
                self.age += 1
                return self.age
        else:
           return self.age 
                
    def sleep(self):
        '''Функция сна экземпляра / Instance sleep function'''
        b = random.choice([True, False])

        if b == True:
            self.energy += 5
            self.try_increment_age()
            print(f'{self.name} is sleeping')
            return self.energy
 
              
    def eat(self):
        '''Функция приема пищи экземпляра / Instance eat function'''
        b = random.choice([True, False])

        if b == True:
            self.energy += 3
            self.weight += 1
            self.try_increment_age()
            print(f'{self.name} is eating')    
       
    def walk(self): 
        '''Функция приема пищи экземпляра / Instance eat function'''
        b = random.choice([True, False])

        if b == True:
            self.energy -= 5
            self.weight -= 1
            self.try_increment_age()
            print(f'{self.name} is walking')    

    
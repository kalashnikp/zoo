from animal import Animal
from instances import Bird, Fish, Dog
import random

class NatureReverse():
    '''Инициализация класса заповедника / Initialization of the reserve class'''
    
    global zoo
    global is_dead
    
    def __init__(self) -> None:
        pass
    
    zoo = [
        Bird(),
        Bird(),
        Bird(),
        Bird(),
        Bird(),
        Fish(),
        Fish(),
        Fish(),
        Dog(),
        Dog(),
        Animal(random.randint(1,5), random.randint(1,5), random.randint(3,5), 'Animal'),
        Animal(random.randint(1,5), random.randint(1,5), random.randint(3,5), 'Animal')
    ]
    
    is_dead = []
        
    def new_zoo(self):
        '''Функция производства потомства / to produce offspring function'''
    
        def prob():
            '''Функция генерации случайного булевого значения / Generate random Bool'''
            global b
            b = random.choice([True, False])
            return b
                
        i = 0    
        while i < 10: 
            prob()
            if b == True:
                q = random.choice([Animal(random.randint(1,5), random.randint(1,5), random.randint(1,5), 'Animal'), Bird(), Fish(), Dog()])
                zoo.append(q)
            i += 1    


    def do_something(self):
        '''Функция построения логики одной итерации / The function of building the logic of one iteration'''

        def prob():
            '''Функция генерации случайного булевого значения / Generate random Bool'''
            global b
            b = random.choice([True, False])
            return b

        for item in zoo:
            prob()
            if b == True:
                random.choice([item.walk(), item.sleep(), item.eat()])
    
        for item in zoo:
            if item.is_too_old == True or item.energy <= 0 or item.weight <= 0 or item.weight > 10:
                zoo.remove(item)
                is_dead.append(item)
               
        
    
    
    
        
                
       

        



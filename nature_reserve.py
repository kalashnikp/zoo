from animal import Animal
from instances import Bird, Fish, Dog
import random

class NatureReverse():
    '''Инициализация класса заповедника / Initialization of the reserve class'''
    
    global zoo
    
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
        Animal(random.randint(1,5), random.randint(1,5), random.randint(1,5), 'Animal'),
        Animal(random.randint(1,5), random.randint(1,5), random.randint(1,5), 'Animal')
    ]
    
        
    def new_zoo():
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


    def do_something():
        
        for item in zoo:
            print(item)
            
            
    

    






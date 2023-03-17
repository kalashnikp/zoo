from animal import Animal
from instances import Bird, Fish, Dog
import random

class NatureReverse():
    '''Инициализация класса заповедника / Initialization of the reserve class'''

    zoo = (
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
        Animal(),
        Animal()
    )
    
    def produce_offspring(self):
        '''Функция производства потомства / to produce offspring function'''
        
        probability = random.choice([True, False])
        
        


    






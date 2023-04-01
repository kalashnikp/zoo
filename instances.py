from animal import Animal

class Bird(Animal):
    '''The bird research class'''

    def __init__(self, energy=4, weight=4, max_age=3, name='Bird'):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is flying\n')

class Fish(Animal):
    '''The research class of fish'''

    def __init__(self, energy=3, weight=3, max_age=3, name='Fish'):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is swimming\n')

class Dog(Animal):
    '''The Dog research class'''

    def __init__(self, energy=5, weight=5, max_age=3, name='Dog'):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is running\n')



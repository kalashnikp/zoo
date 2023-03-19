from animal import Animal

class Bird(Animal):
    '''Наследовательский класс птицы / The bird's research class'''

    def __init__(self, energy=2, weight=3, max_age=3, name='Bird'):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is flying\n')

    

class Fish(Animal):
    '''Наследовательский класс рыбы / The research class of fish'''

    def __init__(self, energy=3, weight=2, max_age=3, name='Fish'):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is swimming\n')

class Dog(Animal):
    '''Наследовательский класс животного / The dog's research class '''

    def __init__(self, energy=4, weight=5, max_age=5, name='Dog'):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is running\n')


# elf = Fish(5, 2, 7, 'ed')

# elf.sleep()
# elf.walk()
# elf.eat()

# print(elf.energy)
# print(elf.age)
# print(elf.weight)
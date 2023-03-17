from animal import Animal

class Bird(Animal):
    '''Наследовательский класс птицы / The bird's research class'''

    def __init__(self, energy, weight, max_age, name):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is is flying')

    

class Fish(Animal):
    '''Наследовательский класс рыбы / The research class of fish'''

    def __init__(self, energy, weight, max_age, name):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is is swimming')

class Dog(Animal):
    '''Наследовательский класс животного / The dog's research class '''

    def __init__(self, energy, weight, max_age, name):
        super().__init__(energy, weight, max_age, name)

    def walk(self):
        super().walk()
        print(f'{self.name} is is swimming')


# elf = Fish(5, 2, 7, 'ed')

# elf.sleep()
# elf.walk()
# elf.eat()

# print(elf.energy)
# print(elf.age)
# print(elf.weight)
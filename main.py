from animal import Animal
from instances import Bird, Fish, Dog
from nature_reserce import NatureReverce


my_zoo = NatureReverce()
i = 0

def life_circle():
    my_zoo.do_something()
    my_zoo.is_dead()
    my_zoo.new_amnimal()
    my_zoo.adding()


while i <= 10:
    life_circle()
    i += 1

print(f'В зоопарке живет {len(my_zoo.zoo)} животное:')
for item in my_zoo.zoo:
    print(item.name)


print(f'Умерло {len(my_zoo.dead_animals)} животное:')
for item in my_zoo.dead_animals:
    print(item.name)

print(f'Родилось {len(my_zoo.new_zoo)} животное:')
for item in my_zoo.new_zoo                                                                                                                                                                                                                                                                                                                                                                                                            :
    print(item.name)


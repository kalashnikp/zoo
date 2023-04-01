from animal import Animal
from instances import Bird, Fish, Dog
from nature_reserce import NatureReverce, zoo, new_zoo, dead_animals, my_zoo

iterations = int(input(f'Введите количество итераций'))
i = 0

def life_circle():
    global i
    while i <= iterations:
        my_zoo.do_something()
        my_zoo.is_dead()
        my_zoo.new_amnimal()
        i += 1
    print(f'Пройдено {iterations} циклов')

    print(f'Животные зоопарка:')
    for item in zoo:
        print(f'{item.name}')
    print(f'В зоопарке находится {len(zoo)} животных')

    print(f'Умершие животные:')
    for item in dead_animals:
        print(f'{item.name} is dead')
    print(f'За {iterations} итераций умерло {len(dead_animals)} животных')

    print(f'Рожденные животные:')
    for item in new_zoo:
        print(f'{item.name} is new born')
    print(f'За {iterations} итераций родилось {len(new_zoo)} животных')

life_circle()



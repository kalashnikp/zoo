from animal import Animal
from instances import Bird, Fish, Dog
from nature_reserve import NatureReverse, zoo




def life_circle():
    global my_zoo
    my_zoo = NatureReverse() 
    my_zoo.new_zoo()       
    my_zoo.do_something()

def run():
    i = 0
    iterations = int(input(f'Введите количество циклов'))
    while i < iterations:
        life_circle()
        i += 1
    
def output():
    for item in my_zoo.zoo:
        print(f'we have a {item.name}\nhe has a {item.energy} energy\nhe has a {item.weight} weight \nhe a {item.age} years old\n')      



run()
output()





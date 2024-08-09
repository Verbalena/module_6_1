class Animal:            # БАЗОВЫЙ класс Животные
    alive = True         # атрибут класса (живой)
    fed = False          # атрибут класса (накормленный)

    def __init__(self, name):
        self.name = name
    def eat(self, food):
        Plant.name = food
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            if food.edible == False:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
class Mammal(Animal):    # дочерний класс
    pass
class Predator(Animal):  # дочерний класс
    pass

class Plant:           # БАЗОВЫЙ класс Растения
    edible = False     # атрибут класса (съедобнность)
    def __init__(self, name):
        self.name = name

class Flower(Plant):   # дочерний класс Цветы
    pass
class Fruit(Plant):    # дочерний класс Фрукты
    edible = True   # атрибут дочернего класса (переопределён)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


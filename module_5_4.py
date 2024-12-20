class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return self.name

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

house1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

house2 = House('ЖК Акация', 20)
print(House.houses_history)

house3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del house2
del house3

print(House.houses_history)
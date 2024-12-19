class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in (range(1,new_floor + 1)):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors

    def __radd__(self, value):
        return self.number_of_floors

    def __iadd__(self, value):
        return self.number_of_floors


house1 = House('ЖК Эльбрус', 30)
house2 = House('Университетская, 5', 5)


print(house1)
print(house2)
print(house1 == house2)
house2 = house2 + 25
print(house2)
print(house1 == house2)

house2 += 10
print(house2)

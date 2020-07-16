import inflect

p = inflect.engine()


class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number=1):
        if animal in self.animals.keys():
            self.animals[animal] += number
        else:
            self.animals[animal] = number

    def get_info(self):
        output = f"{self.name}'s Farm\n"
        for animal, amount in self.animals.items():
            if amount > 1:
                animal = p.plural(animal)
            space = " " * (10 - len(animal))
            output += f"{animal} {space} :{amount}\n"
        output += "    E-I-E-I-O    "
        return output

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        animals = ", ".join(self.get_animal_types())
        return f"{self.name}'s farm has {animals}."


farm = Farm("McDonald")
print(farm.animals)
farm.add_animal("cow", 5)
farm.add_animal("sheep")
farm.add_animal("goat", 4)
print(farm.animals)
print(farm.get_info())
print(farm.get_animal_types())
print(farm.get_short_info())

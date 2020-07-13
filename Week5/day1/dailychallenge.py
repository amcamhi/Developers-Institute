class Farm():
    animals_added = 0

    def __init__(self, farmName):
        self.FarmName = farmName
        self.animals = {}

    def add_animal(self, animal_name, quantity):
        animal_to_add = {animal_name: quantity}
        self.animals.update(animal_to_add)

    def get_info(self):
        print(f"{self.FarmName} farm")
        for animal in self.animals:
            print(f"{animal}\t : {self.animals[animal]}")

    def get_animal_types(self):
        animalTypes = []
        for animal in self.animals:
            animalTypes.append(animal)
            animalTypes.sort()
        return animalTypes

    def get_short_info(self):
        animals = self.get_animal_types()
        animals = " ".join(animals)
        print(str(self.FarmName)+" has " + animals)


mcdonalds = Farm("McDonalds")
mcdonalds.add_animal("Sheep", 4)
mcdonalds.add_animal("Cow", 2)
mcdonalds.add_animal("Goat", 3)

mcdonalds.get_info()
mcdonalds.get_animal_types()
mcdonalds.get_short_info()

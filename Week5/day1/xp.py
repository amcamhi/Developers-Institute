# Excercise 1
# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # Instantiate the Cat object with 3 cats
# # Create a function that finds the oldest cat
# # Print out: “The oldest cat is x years old.”. x will be the oldest cat age by using the function in  # 2

# cat1 = Cat("Tom", 4)
# cat2 = Cat("Garfield", 7)
# cat3 = Cat("Jimmy", 12)

# cats = [cat1, cat2, cat3]


# def oldest_cat(listofcats):
#     oldest_cat_age = 0
#     for cat in listofcats:
#         if cat.age > oldest_cat_age:
#             oldest_cat_age = cat.age
#     print(f"The oldest cat is {oldest_cat_age} years old")
#     return oldest_cat_age


# oldest_cat(cats)


# Excercise 2
#


# class Dog():
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def talkthat(self):
#         print(f"{self.name} barks! Wouaf")

#     def jump(self):
#         print(self.height*2)


# Davids_dog = Dog("Rex", 50)
# Sarahs_dog = Dog("Teacup", 20)

# Sarahs_dog.talkthat()
# Sarahs_dog.jump()

# dogs = [Davids_dog, Sarahs_dog]

# largest_dog = 0
# for dog in dogs:
#     if dog.height > largest_dog:
#         largest_dog = dog.height
#         if dog.height == largest_dog:
#             print(
#                 f"The largest dog is {dog.name}, his height is {dog.height}")
#             dog.winner = True
# print(Davids_dog.winner)

# Excercise 3
# Define a class called Songs, it will show the lyrics of a song.
# Its __init__() method should have two arguments:

# self
# lyrics: a list.
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line. Define a varible:

# happy_bday = Song(["Have a sunshine on you,",
#                    "Happy Birthday to you !"])
# Call the sing_me_song method on this variable.


# class Song():
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for sentence in self.lyrics:
#             print(sentence)

# happy_bday = Song(["Have a sunshine on you,", "Happy Birthday to you !"])

# happy_bday.sing_me_a_song()

# Exercise 4
# Create a class Zoo
# In this class create a method __init__, that takes one parameter: zoo_name
# It initializes two attributes: animals that is an empty list, name that is the name of the zoo.
# Create a method add_animal that takes one parameter new_animal. The point of the method is to add the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animals that prints all the of animals in the zoo.
# Create a method sell_animal that takes one parameter animal_sold. The point of the method is to say goodbye to the animal and then removing it from the list.
# Create a method sort_animal that sorts the animals. Each animal, depending on its first letter should be placed inside a pen. {1: "Ape", 2: ["Baboon", Bear"]}
# Create a method get_pen that prints the list of animals inside each pen.
# Create an object ramatGanSafari and call all the methods.


class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.sorted_list = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        print("goodbye " + animal_sold)
        self.animals.remove(animal_sold)

    def sort_animal(self):
        for animal in self.animals:
            number = ord(animal[0].upper())-64
            self.sorted_list
            return self.sorted_list


santiago_zoo = Zoo("SantiagoZoo")
santiago_zoo.add_animal("Lion")
santiago_zoo.add_animal("Dog")
santiago_zoo.add_animal("Cat")
santiago_zoo.add_animal("Crocodile")

print(santiago_zoo.animals)
santiago_zoo.sort_animal()

ramatGanSafari = Zoo("Ramat Gan Safari")
ramatGanSafari.add_animal("Lion")
ramatGanSafari.add_animal("Tiger")
ramatGanSafari.add_animal("Monkey")
ramatGanSafari.get_animals()
ramatGanSafari.sell_animal("Tiger")

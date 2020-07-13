# import math


# class Circle():
#     def __init__(self, radius=1.0):
#         self.radius = radius

#     def perimeter(self):

#         perimeter = 2*math.pi*self.radius
#         return perimeter

#     def area(self):
#         area = math.pi*(self.radius**2)
#         return area

#     def geometrical_definition(self):
#         print("A circle is a round, two-dimensional shape. All points on the edge of the circle are at the same distance from the center.")


# circle1 = Circle(5)
# print(circle1.perimeter())
# print(circle1.area())


# Exercise 2
# import random


# class MyList():
#     def __init__(self, list1=[]):
#         self.list = list1

#     def reversedList(self):
#         self.list.reverse()
#         reversed_list = self.list
#         return reversed_list

#     def sorted_list(self):
#         self.list.sort()
#         sorted_list = self.list
#         return sorted_list

#     def random_list(self):
#         length = len(self.list)
#         list_random = []
#         for i in range(length):
#             list_random.append(random.randint(0, 100))
#         return list_random


# list1 = MyList([3, 7, 5, 9])
# print(list1.list)
# print(list1.reversedList())
# print(list1.sorted_list())
# print(list1.random_list())

# Exercise 3
import random


class QuantumParticle():
    def __init__(self):
        self.initial_position = random.randint(1, 10000)
        self.momentum = random.random()
        list1 = [1/2, -1/2]
        self.spin = random.choice(list1)

    def disturbance(self):

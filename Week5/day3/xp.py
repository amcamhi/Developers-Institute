# class Currency():
#     def __init__(self, currency_type, float_value):
#         self.currency_type = currency_type
#         self.float_value = float_value

#     def __str__(self):
#         return f"{self.currency_type}, exchange rate: {self.float_value}"

#     def __repr__(self):
#         return f"Currency('{self.currency_type}', {self.float_value})"

#     def __float__(self):
#         return float(self.float_value)

#     def __add__(self, other):
#         if type(other) == int:
#             return self.float_value + other
#         elif self.currency_type == other.currency_type:
#             return self.float_value + other.float_value
#         else:
#             raise TypeError

#     def __sub__(self, other):
#         if type(other) == int:
#             return self.float_value - other
#         elif self.currency_type == other.currency_type:
#             return self.float_value - other.float_value
#         else:
#             raise TypeError

#     def __mul__(self, other):
#         if type(other) == int:
#             return self.float_value * other
#         elif self.currency_type == other.currency_type:
#             return self.float_value * other.float_value
#         else:
#             raise TypeError

#     def __div__(self, other):
#         if type(other) == int:
#             return self.float_value / other
#         elif self.currency_type == other.currency_type:
#             return self.float_value / other.float_value
#         else:
#             raise TypeError


# # NOT WORKING
#     # def __iadd__(self, other):
#     #     if type(other) == int:
#     #         return 2*self.float_value+other
#     #     elif self.currency_type == other.currency_type:
#     #         return 2*self.float_value+other.float_value

# shekel = Currency("Shekel", 3.5)
# clp = Currency("Peso Chileno", 800)

# print(str(shekel))
# print(repr(shekel))
# print(float(shekel))

# print(shekel+5)
# print(help(Currency))


# # # Exercise 2
# # The goal is to create a class that represents a simple circle.
# # A Circlecan be defined by either specifying the radius or the diameter. The user can query the circle for either its radius or diameter.

# # Other abilities of a Circle instance:

# # Compute the circle’s area
# # Print the circle and get something nice
# # Be able to add two circles together
# # Be able to compare two circles to see which is bigger
# # Be able to compare to see if there are equal
# # Be able to put them in a list and sort them

from random import randint
import math


def my_decorator(func):
    def wrap_function():
        print('**************')
        func()
        print('**************')
        return wrap_function


class Circle ():
    def __init__(self, radius=None, diameter=None):
        if radius == None:
            self.diameter = diameter
            self.radius = diameter/2
        elif diameter == None:
            self.radius = radius
            self.diameter = radius*2

    def area(self):
        return 2+math.pi*(self.radius**2)

    def __str__(self):
        return f"Such a nice circle! It´s radius is {self.radius}"

    def __add__(self, other):
        return self.radius + other.radius

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False


# list1 = []
# c1 = Circle(5)
# c2 = Circle(10)
# list1.append(c1)
# list1.append(c2)
# list1.sort()
# print(list1)


# EX3


def get_num():  # defining function get_num
    # number will be = to  a random number between 1 and 10
    number = randint(1, 10)
    return number


def pwr(func):  # definining a High Order funcion pwr, which takes a function as an argument
    number = func()  # number executes func function
    print(number, number*number)  # prints the random number and its square


pwr(get_num)  # call the function.

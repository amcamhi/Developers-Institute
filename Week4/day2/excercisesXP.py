# # Excercise 1 
# my_fav_numbers = {23,3,5,18}
# my_fav_numbers.add(7)
# my_fav_numbers.add(9)
# print(my_fav_numbers)
# my_fav_numbers.pop()
# print(my_fav_numbers)

# friend_fav_numbers = {6,1,8}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# # Excercise 2 

# my_fav_numbers = (23,5,18)
# x = list(my_fav_numbers)

# x.append(1)
# x.append(2)

# print(x)
# x.pop()
# my_fav_numbers = tuple(x)
# print(my_fav_numbers)

# friend_fav_numbers = (8,9,2)
# our_fav_numbers = friend_fav_numbers+my_fav_numbers
# print(our_fav_numbers)

# Excercise 3 UNFINISHED********

# A float is a number with decimals. integer is an integer..
# no




# Excercise 4

# numbers = range(1,21)

# for number in numbers:
#     print(number)

# Excercise 5

# topping = " "
# while topping != "quit":
#     topping = input("enter your toppings, enter quit once you´re done: ")
#     print("we will add "+topping+" to the pizza")

# Excercise 6
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Apply it to a family, ask every member of the family their age, and at the end of the loop, tell them the cost of the tickets for the whole family.
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which one can see the movie.
# # Tip: Try to add the allowed ones to a list.

# ages = []
# cost = []
# number_of_family_members = int(input("how many of you will watch the movie?: "))

# for members in range(0,number_of_family_members):
#     ele = int(input("what´s your age?: "))
#     ages.append(ele)

# print(ages)
# for age in ages:
#     price = 0
#     if age < 3:
#         cost.append(0)
#     elif 3 < age < 12:
#         cost.append(10)
#     else:
#         cost.append(15)
    
# print(cost)

# total = str(sum(cost))
# print("the total cost is $"+total)

# Excercise 7 UNFINISHED**************
# This time you have a list of users, and you want to remove every user that is below 16 years old.

# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# # At the end, print the final list.

# users = ["Tommy", "Ed", "Sandra", "Salah"]
# ages = []
# for user in range(0,len(users)):
#     ele = int(input("whats your age ?"))
#     ages.append(ele)

# print(ages)
# for age in ages:
#     index_of_age = ages.index(age)
#     if age < 16:
#         users.remove(users[index_of_age])
# print(users)

# Excercise 8
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.insert(len(basket)+1,"Kiwi")
# print(basket)
# basket.insert(0,"Apples")
# print(basket)
# apples = basket.count("Apples")
# print(apples)
# basket.clear()
# print(basket)

# Excercise 9
# list1 = ['Apples', 'Apples', 'Oranges', 'Kiwi']
# i = 0
# x = len(list1)
# while i < x:
#     print(list1[i])
#     i += 1

# Excercise 10
# list1 = ['Apples', 'Apples', 'Oranges', 'Kiwi','Strawberry','Pear']
# i = 0
# x = len(list1)
# while i < x :
#     if i%2 == 0:
#         print(list1[i])
#     else:
#         pass
#     i += 1
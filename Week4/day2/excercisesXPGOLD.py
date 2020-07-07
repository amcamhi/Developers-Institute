# # Excersise 1 
# test_data = input("write 3 numbers separated by a coma: ")

# list1 = test_data.split(",")
# print(list1)

# list1 = list(map(int,list1))
# print(max(list1))

# Exercise 2

# import re

# letter = input("enter a letter: ")

# if letter == "a" or letter =="e" or letter == "i" or letter =="o" or\
#     letter == "i" or letter =="u" or letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
#     print(letter+" is a vowel")
# else:
#     print(letter+" is a consonant")

# Excercise 3
# list1 = ['Apples', 'Apples', 'Oranges', 'Kiwi','Oranges']

# x = list1.index("Oranges")
# print(x)

# Excersise 4
# list1 = ['Apples', 'Apples', 'Oranges', 'Kiwi','Oranges']
# users = ["Tommy", "Ed", "Sandra", "Salah"]

# list1.extend(users)
# print(list1)

# Excercises 5 PENDING
# tuple1 = (Tom,19,80)
# tuple2 = (John,20,90)
# tuple3 = (Jony,17,91)
# tuple4 = (Jony,17,93)
# tuple5 = (Json,21,85)

#EXCERCISE 6

# customer_name = input("what is the customer´s name?: ")
# waiter_name = input("what is your name?: ")
# name_item = input("what did the customer order? (name the item): ")
# price_item = input("what is the price of the item?: ")
# amount_items = input("amount of ordered items?: ")
# discount = input("discount amount? (input 0 if no discount: ")

# total = str((int(price_item)* int(amount_items))*(1-int(discount)))
# total_vat = str(int(total)*1.19)

# bill =  "customer name: "+ customer_name + "\n" "waiter/waitress name: "+ waiter_name + "\n""items ordered: "+ name_item + " nº of items: "+ amount_items + " price: $" + price_item + "\n"" total: "+total + "\n"" total + taxes: " + total_vat + "\n""*************************"+"\n"+"Tip is not included <3"

# print(bill)

# Excercise7 
# import random

# secret_nuber = random.randint(1,10)
# guess = 0

# while secret_nuber != guess:
#     guess = int(input("guess the number between 1-9: "))
# print("Well done!")

# Excercise 8 

# list1 = list(range(0,1000001))
# for number in list1:
#     print(list1)

# Excercise 9 
# list1 = list(range(0,1000001))
# print(min(list1))
# print(max(list1))
# print(sum(list1))
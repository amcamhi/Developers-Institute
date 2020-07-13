# # Excercise 1
# list1 = [
#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7],
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2],
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76],
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# ]
# for i in list1:
#     print(f"The list of numbers is: {i}")
#     i.sort(reverse=True)
#     print(f"The list in reversed order(largest to smallest):{i}")
#     print(f"The sum of the numbers in the list: {sum(i)}")
#     print("\n")

# for lista in list1:
#     print("\n")
#     print(f"The first and last number: {i[0]},{i[-1]}")
#     greater_than50 = []
#     smaller_than10 = []
#     squared = []
#     no_duplicates = set()
#     for number in lista:
#         if number > 50:
#             greater_than50.append(number)
#     for number in lista:
#         if number < 10:
#             smaller_than10.append(number)
#     for number in lista:
#         squared.append(number**2)
#     for number in lista:
#         no_duplicates.add(number)

#     print(f"numbers greater than 50: {greater_than50}")
#     print(f"numbers smaller than 10: {smaller_than10}")
#     print(squared)
#     print(no_duplicates, f"total items: {len(no_duplicates)}")

#     for lista in list1:
#         average = sum(lista)/len(lista)
#         print(f"the average of each list is: {average}")
#         print(f"the largest number of each list is: {max(lista)}")
#         print(f"the smallest number of each list is: {min(lista)}")

# # Excercise 2
# paragraph = """ This sentence has five words. Here are five more words. Five-word sentences are fine. But several together become monotonous.
# Listen to what is happening. The writing is getting boring. The sound of it drones. It’s like a stuck record.
# The ear demands some variety. Now listen. I vary the sentence length, and I create music. Music. The writing sings.
# It has a pleasant rhythm, a lilt, a harmony. I use short sentences. And I use sentences of medium length.
# And sometimes, when I am certain the reader is rested,
#  I will engage him with a sentence of considerable length, a sentence that burns with energy and builds with all the impetus of a crescendo, the roll of the drums, the crash of the cymbals–sounds that say listen to this, it is important. """

# print(f"The amount of characters in the paragraph is: {len(paragraph)}")
# paragraph_list = paragraph.split()
# unique_words = len(set(paragraph_list))
# paragraph_sentences = len(paragraph.split("."))
# nonwhite_characters = "".join(paragraph_list)

# print(f"The number of words is: {len(paragraph_list)}")
# print(f"The number of sentences is: {paragraph_sentences}")
# print(f"The number of unique words is: {unique_words}")
# print(f"The number of nonwhite characters: {len(nonwhite_characters)}")
# print(len(paragraph_list)/paragraph_sentences)

# # Excercise 3
# input1 = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."


# def frequency_counter(string, count_this):
#     frecuency = string.count(count_this)
#     return frecuency, count_this


# print(frequency_counter(input1, "Python"))

# Excercise 6

# input1 = input("write a list of comma-sepparated numbers: ")

# list_input1 = input1.split(",")
# tuple_inpu1 = tuple(list_input1)

# print(list_input1)
# print(tuple_inpu1)

# Excercise 7
# Q = Square root of [(2 * C * D)/H]
# C is 50.
# H is 30.

inpu1 = input("write some numbers separated by a coma...: ")
def function(input1):

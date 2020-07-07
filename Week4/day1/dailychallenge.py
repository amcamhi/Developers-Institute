import random

string = input("enter a string that is 10 characters long")
print(string[0], string[-1])

for number in range(len(string)+1):
    print(string[:number]) 

    shuffled = list(string)
    random.shuffle(shuffled)
    shuffled = " ".join(shuffled)
    print(shuffled)
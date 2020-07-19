import random
import sys


def get_words_from_file():
    with open('wordlist.txt', 'r') as f:
        list1 = []
        for word in f:
            list1.append(word.replace('\n', ""))
    return list1


def get_random_sentence(number_of_words):
    list_sentence = []
    for i in range(number_of_words):
        word = random.choice(get_words_from_file())
        word = word.lower()
        list_sentence.append(word)
        sentence = " ".join(list_sentence)
    return sentence


def main():
    print("This program will allow you to create random sentences.\nYou can decide the length of the sentence by passing the desired length as an argument of the function")
    number_of_words = input(
        "Please enter the length of your desired sentence. Length must be between 2 an 20 words: ")
    if int(number_of_words) > 20 or int(number_of_words) < 2:
        print('invalid number, bye')
        sys.exit()
    else:
        print(get_random_sentence(int(number_of_words)))

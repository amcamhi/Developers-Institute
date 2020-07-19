import anagram_checker
import sys

print("Welcome to Anagram Checker: ")
input1 = input("Would you like to (C)heck a word or (E)xit?: ")
input1 = input1.upper()
while True:
    if input1 == "C":
        word = input("Please enter a word: ")
        word = word.upper()
        break
    elif input1 == "E":
        print("Ok, bye!")
        sys.exit()
        break
    else:
        print("Please enter a valid option 'C' or 'E")
        input1 = input("Would you like to (C)heck a word or (E)xit?")


while True:
    validation = len(word.split())
    if validation != 1:
        word = input("Please enter only one word: ")
    else:
        break

word = word.strip()
word = word.upper()

anagram1 = anagram_checker.AnagramChecker()
if anagram1.is_valid_word(word):
    print(
        f"Your word: {word}.\nThis is a valid English word\nAnagrams for your word: ")
    anagram1.get_anagrams(word)
else:
    print("not a valid english word")

import random

choices = ['r', 'p', 's']


def game():
    victories = 0
    defeats = 0
    ties = 0
    print('**Menu**')
    action = input("(g) Play a new game \n(x)Show score and exit: ")
    while True:
        if action == "g":
            user_choice = input("Select (r)ock, (p)aper, or (s)cissors: ")
            computer_choice = random.choice(choices)
            print("You chose: " + user_choice +
                  ", The computer chose: " + computer_choice)
            if user_choice == "r" and computer_choice == "s":
                print("You won!")
                victories += 1
            elif user_choice == "r" and computer_choice == "p":
                print("You lost!")
                defeats += 1
            elif user_choice == "p" and computer_choice == "s":
                print("You lost!")
                defeats += 1
            elif user_choice == "p" and computer_choice == "r":
                print("You won!")
                victories += 1
            elif user_choice == "s" and computer_choice == "r":
                print("You lost!")
                defeats += 1
            elif user_choice == "s" and computer_choice == "p":
                print("You won!")
                victories += 1
            elif user_choice == computer_choice:
                print("It's a draw!")
                ties += 1
        elif action == "x":
            print("Game results: ")
            print(f"You won {victories} times.")
            print(f"You lost {defeats} times.")
            print(f"You drew {ties} times.")
            print("\nThank you for playing!")
            break
        else:
            print("Invalid input, try again.")
        action = input("(g) Play a new game \n(x)Show score and exit: ")


game()

import random

choices = ['r', 'p', 's']


class Game():
    def __init__(self):
        self.user_item = None
        self.computer_item = None
        pass

    def get_user_item(self):
        self.user_item = input("Select (r)ock, (p)aper, or (s)cissors: ")
        while True:
            if self.user_item == "r" or self.user_item == "p" or self.user_item == "s":
                break
            else:
                print("Invalid input, try again.")
                self.user_item = input(
                    "Select (r)ock, (p)aper, or (s)cissors: ")
        return self.user_item

    def get_computer_item(self):
        self.computer_item = random.choice(choices)
        return self.computer_item

    def get_game_result(self, user_item, computer_item):
        if self.user_item == "r" and self.computer_item == "s":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You won!")
            return "win"
        elif self.user_item == "r" and self.computer_item == "p":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You lost!")
            return "loss"
        elif self.user_item == "p" and self.computer_item == "s":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You lost!")
            return "loss"
        elif self.user_item == "p" and self.computer_item == "r":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You won!")
            return "win"
        elif self.user_item == "s" and self.computer_item == "r":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You lost!")
            return "loss"
        elif self.user_item == "s" and self.computer_item == "p":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You won!")
            return "win"
        elif self.user_item == self.computer_item:
            print(
                f"You selected {user_item}, the computer selected {computer_item}. It's a draw!")
            return "tie"

    def play(self):
        self.get_user_item()
        self.get_computer_item()
        self.get_game_result(self.user_item, self.computer_item)

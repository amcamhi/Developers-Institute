import random

choices = ['r', 'p', 's']


class Game():
    def __init__(self):
        self.user_item = None
        self.computer_item = None

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
        self.won = 0
        self.lost = 0
        self.tied = 0
        self.results = {"won": self.won,
                        "lost": self.lost,
                        "tied": self.tied}
        if user_item == "r" and computer_item == "s":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You won!")
            self.won += 1
            return "win"
        elif user_item == "r" and computer_item == "p":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You lost!")
            self.lost += 1
            return "loss"
        elif user_item == "p" and computer_item == "s":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You lost!")
            self.lost += 1
            return "loss"
        elif user_item == "p" and computer_item == "r":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You won!")
            self.won += 1
            return "win"
        elif user_item == "s" and computer_item == "r":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You lost!")
            self.lost += 1
            return "loss"
        elif user_item == "s" and computer_item == "p":
            print(
                f"You selected {user_item}, the computer selected {computer_item}. You won!")
            self.won += 1
            return "win"
        elif user_item == computer_item:
            print(
                f"You selected {user_item}, the computer selected {computer_item}. It's a draw!")
            self.tied += 1
            return "draw"

    def play(self):
        self.get_user_item()
        self.get_computer_item()
        self.get_game_result(self.user_item, self.computer_item)

# # EX1
# class Pets():
#     animals = []

#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat(Pets):
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Bengal(Cat):
#     def sing(self, sounds="miau"):
#         return f'{sounds}'


# class Chartreux(Cat):
#     def sing(self, sounds="miau"):
#         return f'{sounds}'


# class Lion(Cat):
#     def sing(self, sounds="miau"):
#         return f"{sounds}"


# bengal = Bengal("Bengal", 5)
# chartreux = Chartreux("Chartreux", 2)
# lion = Lion("Mufasa", 10)

# my_cats = [bengal, chartreux, lion]
# my_pets = Pets(my_cats)
# print(my_pets.walk())

# EX2
class Bank():
    number_accounts = 0

    def __init__(self):
        pass


class BankAccount(Bank):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dp_amount):
        if dp_amount > 0:
            self.balance += dp_amount
        return f"you´ve added ${dp_amount} to your balance. Your new balance is ${self.balance}"

    def withdraw(self, wd_amount):
        if wd_amount < self.balance:
            self.balance += -wd_amount
            return f"you´ve withdrawed ${wd_amount} from your balance. Your remaining balance is ${self.balance}"
        else:
            return "Not enough funds"


class Owner(BankAccount):
    chances = 0

    def __init__(self, owner, balance, cc_num, password):
        super().__init__(owner, balance)
        self.cc_num = cc_num
        self.password = password

    def check_info(self, cc_input, password_input):
        if self.chances < 2 and cc_input == self.cc_num and password_input == self.password:
            action = input("Would you like to deposit, withdraw or exit?: ")
            if action == "deposit":
                return self.deposit(), self.check_info(cc_input, password_input)
            elif action == "withdraw":
                return self.withdraw()
            elif action == "exit":
                print("good bye!")
        elif self.chances < 2 and cc_input != self.cc_num and password_input != self.password:
            print("wrong credentials, please try again")
            self.chances += 1
        else:
            print("the card has been eaten by the machine!")
            del self.cc_num

    def deposit(self):
        print("We only accept bills of $20, $50 or $100 ")
        bill_20 = int(input("enter amount of bills of $20: "))
        bill_50 = int(input("enter amount of bills of $50: "))
        bill_100 = int(input("enter amount of bills of $100: "))
        total_deposit_amount = bill_20*20+bill_50*50+bill_100*100
        self.balance += total_deposit_amount
        return f"you´ve added ${total_deposit_amount} to your balance. Your new balance is ${self.balance}"

    def withdraw(self):
        print("You can only withdraw bills of $20 or $50")
        bill_20 = int(input("enter amount of bills of $20 to withdraw: "))
        bill_50 = int(input("enter amount of bills of $50 to withdraw: "))
        total_withdraw_amount = bill_20*20+bill_50*50
        self.balance += -total_withdraw_amount
        return f"you´ve withdrawed ${total_withdraw_amount} from your balance. Your new balance is ${self.balance}"


owner1 = Owner("Andres", 500, 230393, 123)

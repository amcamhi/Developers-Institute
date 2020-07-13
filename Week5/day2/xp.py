# Exercise 1
class Family():
    members = [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
               {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}]
    last_name = "Cohen"

    def __init__(self):
        pass

    def born(self, **baby):
        print("Congrats, a new baby has born")
        Family.members.append(baby)

class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **baby):
        print("Congrats, a new baby has born")
        self.members.append(baby)

    def over18(self, name):
        for member in self.members:
            if member['name'] == name:
                age = member["age"]
                print(age > 18)
                return age > 18

    def presentation(self):
        print(f"we are the {self.last_name} family")


cohens = Family([{
    'name': 'Michael',
    'age': 35,
    'gender': 'Male',
    'is_child': False
}, {
    'name': 'Sarah',
    'age': 32,
    'gender': 'Female',
    'is_child': False
}], "Cohen")

cohens.born(name='David', age=0, gender="Male", is_child=True)

print(cohens.members)

cohens.over18('David')


cohens = Family([{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False}, {
                'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}], "Cohen")

cohens.born(name="David", age="0", gender="male", is_child="True")


# Excercise 2
class TheIncredibles(Family):
    def __init__(self, members, last_name):
        super().__init__(members, last_name)
        for member in self.members:
            member["power"]

    def use_power(self):
        for member in self.members:
            if member["age"] >= 18:
                print(member["name"], member["power"])
            else:
                raise Exception("You have no power here!")

    def incredible_presentation(self):
        for member in self.members:
            print(
                f"My name is {member['incredible_name']} and my power is {member['power']}")


cohens = TheIncredibles([{
    'name': 'Michael',
    'age': 35,
    'gender': 'Male',
    'is_child': False,
    'power': 100,
    'incredible_name': 'Michael Jordan'
}, {
    'name': 'Sarah',
    'age': 32,
    'gender': 'Female',
    'is_child': False,
    'power': 80,
    'incredible_name': 'Sarahsana'
}], "Cohen")

cohens.use_power()

incredibles = TheIncredibles([{
    'name': 'Aragorn',
    'age': 35,
    'gender': 'Male',
    'is_child': False,
    'power': 100,
    'incredible_name': 'Super Aragorn'
}, {
    'name': 'Legolas',
    'age': 32,
    'gender': 'Male',
    'is_child': False,
    'power': 80,
    'incredible_name': 'Super Legolas'
},
    {
    'name': 'Gimli',
    'age': 90,
    'gender': 'Male',
    'is_child': False,
    'power': 120,
    'incredible_name': 'Super Gimli'
}], "Fellowship")

incredibles.incredible_presentation()
incredibles.presentation()

incredibles.born(name='Jack', age=0, gender="Male", is_child=True,
                 power="unknown", incredible_name="Jack Sparrow")
incredibles.incredible_presentation()
incredibles.presentation()

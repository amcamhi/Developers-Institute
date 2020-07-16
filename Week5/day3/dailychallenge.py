class Palindrome():
    def __init__(self, content):
        self.content = content

    def __call__(self):
        if self.content == self.content[-1::-1]:
            print("True")
            return True
        else:
            print("False")
            return False


pal1 = Palindrome("radar")
pal2 = Palindrome("casa")


pal1()
pal2()

class Dog:
    def __init__(self):
        print("Woof Woof")
    def pee(self):
        print("I Will Pee")

    
class Puppy(Dog):
    def pee(self):
        print("Go to the park")


p = Puppy()
p.pee()
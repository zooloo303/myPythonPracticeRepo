class Mammal:
    def walk(self):
        print("I'm walkin here")


class Dog(Mammal):
    def bark(self):
        print("Woof!")

class Cat(Mammal):
    def asshole(self):
        print("I'll eat yo face")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.asshole()
    
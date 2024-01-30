class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


neil = Person("Neil Ward")
neil.talk()

bob = Person("Billy Bob")
bob.talk()
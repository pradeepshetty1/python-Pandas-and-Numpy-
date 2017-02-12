class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Caty(Animal):
    def talk(self):
        return 'Meow!'

class Dogy(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Caty('Miss Cat'),
           Caty('Mr. Catee'),
           Dogy('Lussee')]

for animal in animals:
    print animal.name + ': ' + animal.talk()
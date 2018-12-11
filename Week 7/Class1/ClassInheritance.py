# Shape is the class
# Circle and Square are in this
# qualities of circle could be radius and circumfrence
# qualities of rectangle are length, height
# qualities of Shape are colour, thickness
# Circle has colour, thickness, radious and circumfrence
# rectangle has length, height, colour and thickness
# there is therefore some repetition that we should deal with.
# This is called inheritance.
# see classes 2 presentation
# see example of Animal classes
# Encapsulation means everything is done within the class.
# Polymorphism
class Animal:
    name = ""

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

d = Dog()
d.name = "spot"

c = Cat()
c.name = "Felix"

d.make_sound()

c.make_sound()


# There is no object yet.
# You can have no constructor (or initializer), or construtor in one or the other. If you want in all, put in class Animal.
# Make a constructor only if necessary at beginning of insubstantition. Need this to give name, for example.

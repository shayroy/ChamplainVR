from math import pi

class Shape:
    colour = ""

class Circle(Shape):
    radius = 0

     #constructor:
    def __init__(self, c, r):
        self.radius = r
        self.colour = c
    # the colour is inherited from Shape

    def get_area(self):
        # need to import pi so did so at top
        return (pi * (self.radius **2))

class Rect(Shape):
    len = 0
    height = 0

    # constructor:
    def __init__ (self, c, h, l):
        self.height = h
        self.len = l
        self.colour = c
    # the colour is inherited from Shape

    def get_area(self):
        return self.len * self.height

# get_area should be the same name throughout, but the implementation varies by class of shape
# how to set colour? We will never instantiate Shape on its own, so probably need to put colour in

my_shape = Rect("Red", 5, 10)

print (my_shape.get_area())

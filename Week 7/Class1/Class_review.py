class Shape:
    colour = ""
    #colour is an attribute of Shape
    # Constructor
    def __init__(self, input_colour):
        #variable colour that we input
#how do we set the colour to the input_colour. We have to use Self.colour  = input_colour
        self.colour = input_colour
    # if we want shape to do something
    # action here is to delcare yourself
    def declare_yourself(self):
        print("I am a shape and my colour is " + self.colour)
        #remember self is always required.
        #self refers to method variable. In this case, self.colour.

# pass colour in brackets to the object triangle1. Instantiation
triangle1 = Shape("Green")
# To have triangle1 declare itself:
triangle1.declare_yourself()

#delete an object with del
del triangle1
triangle1.declare_yourself()
#should give error as triangle1 has been deleted

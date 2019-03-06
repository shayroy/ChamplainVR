import math
import re

class Shape:
    """This is the parent class for shapes."""
    def __init__(self, colour):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour


class Rectangle(Shape):
    """This is the child class of Shape for Rectangles."""
    def __init__(self, colour, length, width):
        super().__init__(colour)
        self.__length = length
        self.__width = width
        self.__name = "Rectangle"

    def get_width(self):
        return self.__width

    def set_width(self):
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self):
        self.__length = length

    def get_area(self):
        return self.__width * self.__length

    def get_perimeter(self):
        return (self.__width + self.__length) * 2

class Square(Shape):
    """This is a child class of Shape for Squares."""
    def __init__(self, colour, side_length):
        super().__init__(colour)
        self.__side_length = side_length
        self.__name = "Square"

    def get_side_length(self):
        return self.__side_length

    def set_side_length(self, side_length):
        self.__side_length = side_length

class Circle(Shape):
    """This is a child class of Shapes for Circles."""
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.__radius = radius
        self.__name = "Circle"

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return self.math.pi.__self.radius * 2


class Shapes:
    """This is a collection class for shapes."""
    def __init__(self):
        self.__list_of_shape = []

    def add_shape(self, new_shape: Shape):
        self.__list_of_shape.append(new_shape)

    def delete_shape(self, shape: Shape):
        self.__list_of_shape.remove(shape)

    def clear_shape(self):
        self.__list_of_shape.clear()

    def get_shape_count(self):
        count = 0
        for x in self.__shapes:
            count += 1
        return (count)

    def get_total_area(self):
        total_area = 0
        for x in self.__list_of_shape:
            total_area =+ x.get_area()
        return total_area

r1 = Rectangle("Blue", length = 3, width = 4)
print(r1.get_colour() + str(r1.get_width()) + str(r1.get_length()))


#r2 = Rectangle("Red", 4, 5)
#print(r2.get_colour() + str(r2.get_width())

#sh = Shape()
#sh.add_shape(r1)
#sh.add_shape(r2)
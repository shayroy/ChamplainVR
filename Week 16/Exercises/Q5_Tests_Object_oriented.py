import unittest

from .Exercises.Q5_Object_oriented import Rectangle

class TestRectangle(unitest.TestCase):
    """Tests Rectangle class in Q5_Object_oriented_Paul_Shay.py"""

    def test_rectangle_colour(self):
        """Tests colour a rectangle."""

        r1 = Rectangle("Blue", length=3, width=4)

        result = r1.get_colour()

        self.assertEqual(expectedResult, "Blue")

if __name__ == '__main__':
    unittest.main()

        # expectedResult = The Rectangle r1 is Blue, its width is 4, its length is 3, its area is 12,
        # and its perimeter is 14.
        #
        # result = return("The Rectangle r1 is " + r1.get_colour() + ", its width is " + str(r1.get_width()) +
        # ", its length is " + str(r1.get_length()) + ", its area is " + str(r1.get_area()) + ", and its perimeter is "
        # + str(r1.get_perimeter()) + ".")





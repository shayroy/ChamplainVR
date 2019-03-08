import unittest

from Q5_Object_oriented import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests Rectangle class in Q5_Object_oriented_Paul_Shay.py"""

    def test_rectangle_colour(self):
        """Tests rectangle colour."""

        r1 = Rectangle("Blue", length=3, width=4)
        result = r1.get_colour()

        self.assertEqual(result, "Blue")

    def test_rectangle_length(self):
        """Tests rectangle length."""

        r1 = Rectangle("Blue", length=3, width=4)

        result = r1.get_length()

        self.assertEqual(result, 3)

    def test_rectangle_area(self):
        """Tests rectangle area."""

        r1 = Rectangle("Blue", length=3, width=4)

        result = r1.get_area()

        self.assertEqual(result, 12)

    def test_rectangle_perimeter(self):
        """Tests rectangle perimeter."""

        r1 = Rectangle("Blue", length=3, width=4)

        result = r1.get_perimeter()

        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()


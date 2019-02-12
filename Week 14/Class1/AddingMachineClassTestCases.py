import unittest

from .AddingMachineClass import *

class test_adding_machine(unittest.TestCase):

    def setUp(self):

        number1 = 2
        number2 = 3
        self.adding_machine_instance = AddingMachine(number1, number2)

    def class_instantiated(self):
        # tests that class exists
        self.assertIsNotNone(self.adding_machine_instance)

    def test_class_is_instance(self):

        self.assertIsInstance(self.adding_machine_instance, AddingMachine)

    def test_adding_integers(self):

        expected = 5

        result = self.adding_machine_instance.add()

        self.assertEqual(expected, result)





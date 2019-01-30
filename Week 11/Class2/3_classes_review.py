# make it work first before adding tweaks like tests for clear working.
import random

class PyCalc():
    """Calculates average, max and min from a list of random numbers."""

    def __init__(self, mylist):
        self.mylist = mylist

    def generate_random_data(self, numb, start, end):
        # Generates the random list.
        for x in range(numb):
            self.mylist.append(random.randint(start, end))

    def average(self, mylist):
        # Calculates the average of the list using sum and len.
        return sum(mylist) / len(mylist)

    def min(self, mylist):
        # Calculates the minimum of the list.
        mylist.sort()
        return str(mylist[0])

    def max(self, mylist):
        # Calculates the maximum of the list.
        mylist.sort()
        return str(mylist[-1])

    def clear_list(self, mylist):
        # Clears the list.
        mylist.clear()
# As written, this creates error with mylist line 33.
        # Brendan said better to put boolean and comment than for - else.

mylist = []

c = PyCalc(mylist)

str(c.generate_random_data(10, 1, 100))

print ("Here is a list of 10 random numbers:\n{0}:".format(str(c.mylist)))

print ("The average is " + (str(c.average(mylist))) + ".")

print ("The minimum number is " + c.min(mylist) + ".")

print ("The maximum number is " + c.max(mylist) + ".")

c.clear_list(mylist)






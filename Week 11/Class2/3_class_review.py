# make it work first before adding tweaks like tests for clear working.
import random

class PyCalc():
    """Calculates average, max and min from a list of random numbers."""

    def __init__(self, mylist):
        self.mylist = mylist

    def generate_random_data(self, x, y, z):
        mylist = random.sample(xrange(1, 101), 10)
        return "Here is a 10 random numbers between 1 and 100: " + str(mylist) + "."


    def average(self, mylist):
    # Calculates the average of the list using sum.

        return "The average of the numbers is " + str(sum(mylist) / len(mylist)) + "."

    def min_max(self, mylist):
    # Calculates the minimum and maximum of the list.
       mylist.sort()
       return "The minimum number is " + str(mylist[0]) + ".\n" + "The maximum number is " + str(mylist[-1]) + "."

# def clear(self, mylist):
#   self.mylist = []
#  if self.mylist != []:
#     return "The list should be cleared."
# else:
#   return "The list is now cleared."
# better to put boolean and comment cl

c = PyCalc(mylist)

#c.clear
print (c.generate_random_data (mylist))

print (str(c.average(mylist)))

print (c.min_max(mylist))


class PyCalc():
    """Calculates average, max and min from a list of numbers."""
    def __init__(self, mylist):
        self.mylist=mylist

    def average(self, mylist):
        # Calculates the average of the list manually.
        mysum = 0
        for x in mylist:
            mysum += x

        return "The average of the numbers is " + str(mysum / len(mylist)) + "."
        # Alternate more professional way would use sum and avoid the need for the for loop:
        # return "The average of the numbers is " + str(sum(mylist) / len(mylist)) + "."

    def min_max(self, mylist):
        # Calculates the minimum and maximum of the list.
        mylist.sort()
        return "The minimum number is " + str(mylist[0]) + ".\n" + "The maximum number is " + str(mylist[-1]) + "."

mylist = [5, 4, 2, 8, 10, 13, 14, 20, 17, 16]
print("Here is a list of 10 numbers: " + str(mylist))
c = PyCalc(mylist)
print (str(c.average(mylist)))
print (c.min_max(mylist))

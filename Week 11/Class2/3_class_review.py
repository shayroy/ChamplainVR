#make it work first before adding tweaks like tests for clear working.
# import random

class PyCalc():
    """Calculates average, max and min from a list of random numbers."""
    def __init__(self, mylist):
        self.mylist=mylist
        #
    #    print((x), end=" ")

    def gen_random(self,size,minrange,maxrange):
        for x in range(10):

    randomNumber = random.randint(1, 100)
    mylist.append(randomNumber)
    return "Here is a list of 10 random numbers: + str(mylist)."
     for x in mylist:

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


def clear(self, mylist):
    self.mylist = []
    if self.mylist != []:
        return "The list should be cleared."
    else:
        return "The list is now cleared."
    #better to put boolean and comment cl
#mylist = [5, 4, 2, 8, 10, 13, 14, 20, 17, 16]
#print("Here is a list of 10 numbers: " + str(mylist))

c = PyCalc(mylist)

c.clear
c.gen_random(10,1, 100)

print (str(c.average(mylist)))

print (c.min_max(mylist))



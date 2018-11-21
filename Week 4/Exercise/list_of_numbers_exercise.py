# Exercise
# Create a list of numbers, randomly assigned.
# Hint: To generate a reandom number use -> random.randomint(1,101)
# Scan the list and display several values:
# - The minimum, the maximum, the count and the average.
# - Brendan asks us not to use the built in functions.

import random
randomList = []
for x in range(10):
    randomNumber = random.randint(1, 100)
    randomList.append(randomNumber)
print("Here is a list of 10 random numbers:")
for x in randomList:
      print((x), end=" ")
print ()

randomList.sort()
print("The minimum number is " + str(randomList[0]) + ".")
print("The maximum number is " + str(randomList[-1]) + ".")
y=0

for x in randomList:
    y=(y+x)
print("The sum of the numbers is " + str(y) + ".")
print ("The average of the numbers is " + str(y/10) + ".")
















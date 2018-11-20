# if need to do something x times, need to use a for x in a range.
# need to use random.randint(1,11)
# need to import random (remember when something does not work to try to import it.)
# and append
# and something like list=list+[]


import random
randomList = []
# Add random numbers to the blank list.
for x in range(10):
    randomNumber = random.randint(1, 100)
    randomList.append(randomNumber)

# Method 1 to show in list format within square brackets and commas
print(randomList)

# Method 2 to display the list as just numbers with spaces
for x in randomList:
    print(x, end=" ")

print()

# to find greatest value, the build in way to do it is a follows.
print(max(randomList))
print()

# for homework, he would like us to finish the exercise by writing code or an algorithm to do it manually, for example, as follows:

maxVal = [0]
for y in randomList:
    if y > maxVal:
        maxVal = y
print(maxVal)

# Yuliya encouraged use, and Brendan agreed, to use randomList[0] (the first element in the list), rather than [0] so\
# that it will work for any range of numbers including negative numbers, and also min.

maxVal = randomList[0]
for y in randomList:
    if y > maxVal:
        maxVal = y
print(maxVal)






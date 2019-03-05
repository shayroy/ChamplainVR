import random
randomList = []
for x in range(10):
    randomNumber = random.randint(1, 101)
    randomList.append(randomNumber)
print("Here is a list of random numbers:")
for x in randomList:
      print((x), ' ', end="")

print('\nThe lowest number on the list is ' +  str(min(randomList)) + '.')
print('The highest number on the list is ' + str(max(randomList)) + '.')
print('There are ' + str(len(randomList)) + ' numbers in the list.')
print('The average of the numbers is ' + str(sum(randomList)/(len(randomList))) + '.')

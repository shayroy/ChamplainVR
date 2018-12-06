# Exercise
# Create a list of numbers, randomly assigned.
# Hint: To generate a reandom number use -> random.randomint(1,101)
# Scan the list and display several values:
# - The minimum, the maximum, the count and the average.
# - Brendan as ks us not to use the built in min, max, len  or sum functions.
#
# My solution:
# import random
# randomList = []
#for x in range(10):
#    randomNumber = random.randint(1, 100)
#    randomList.append(randomNumber)
#print("Here is a list of 10 random numbers:")
#for x in randomList:
#      print((x), end=" ")
#print ()
#
#randomList.sort()
#print("The minimum number is " + str(randomList[0]) + ".")
#print("The maximum number is " + str(randomList[-1]) + ".")
#y=0
#
#for x in randomList:
#    y=(y+x)
#print("The sum of the numbers is " + str(y) + ".")
#print ("The average of the numbers is " + str(y/10) + ".")

# Brendan wants us to find the min, max, length, sum, and average of a
# list of 10 random numbers.
# Need to import random. If you get an error such as "unresolved reference 'random', need to import.
# There is a list of what is and is not built in but comes with experience.

import random
my_list = []
# can't add something without a container, so we need to create an empty list as a container.
counter = 0
found = False
while counter <= 20:

    rand_val = random.randint(1,22)

    for x in my_list:
        if rand_val == x:
            found = True
            break

    if found == False:
        my_list.append(rand_val)
        counter += 1

    if counter == 20:
        break

for x in range(20):
    # ideally, should also code to ensure there is no duplicate. We will put in for loop to check for duplicates
    # we need to ask what we need to do. We need to perform an action 20 times, so add to a list 20 times.
    rand_val=random.randint(1,100)
    # my_list.append(random.randint(1, 100))
    # the previous line is the line from the original solution before we edited to ensure there are no duplicates.
    rand_val = random.randint(1, 22)
    for y in my_list:
        if rand_val == y:
            continue
    my_list.append(rand_val)
# do in chunks to check as beginner
print(my_list)

# it is good practice to define variables at top, but put within when necessary.

min_of_list = (my_list[0])
max_of_list = (my_list[0])
sum_of_list = 0
length_of_list = 0

for x in my_list:
# will be run 10 times
    length_of_list += 1
    sum_of_list += x
# a=a+1 is same as a+=1
    if x > max_of_list:
        max_of_list = x
    if x < min_of_list:
        min_of_list = x


print("Sum = " + str(sum_of_list))
print("Size = " + str(length_of_list))
print("Largest = " + str(max_of_list))
print("Smallest = " + str(min_of_list))

average_of_list = sum_of_list / length_of_list

print("Average = " + str(average_of_list))

#max_of_list = myslist[0]
#max_of_list therefore equals 60 (in his list)
#x = 60
#max_of_list= 60
#x = 80
#max_of_list is now 80
#x = 30
#max_of_list remains 80

# He will post practice questions with answers we can do over weekend.



# Assembly line of 4 cars with sequential numbers. 3 inspectors for each car, say 0, 1 and 2.
# They each give true or false for passing quality.
# Code as per example in list mylist2 = [mylist, 'abc,, mylist, [1, 2, 3]
# Then show results i.e:
# Inspection for car #0
#   Inspector 0: True
#   Inspector 1: False
# Can hard code it in more lines, or in shorter in 2 for loops.

car_inspections = [[True, False, True],
                   [True, True, True],
                   [False, False, False],
                   [True, True, True]]
count = 0

for car in car_inspections:
    count += 1
    print("Inspection for car number " + str(count))
    print("Inspector 1 : " + str(car[0]))
    print("Inspector 2 : " + str(car[1]))
    print("Inspector 3 : " + str(car[2]))
    print()

# can improve
# for insp in car to avoid having to do brackets at end of str(car[0])

# copying lists ages a=[22, 33] see slide Copying a List
# do not do b=a, as this is not a new list but only a pointer to the a list
# here is the problem:
a = [22, 33]
b = a
print(a)
print(b)
# prints OK at first
a[1] = 66
print(a)
print(b)
# b also changes to 66, which may not be what we want if we want b to be independent of a and not just pointing to it.
#print(a[:]) creates an independent copy and b would not change
# this is important in object orientated programming
# can also do b = a.copy()
a = [22, 33]
b = a.copy()
a[1] = 66
print(a)
print(b) # is this working?







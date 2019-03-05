# Practice Worksheet question 7.
# The exercise gives the numbers 0 to 7 in binary.
# it uses a recursive loop, our first real algorithm
# #first loop as to go from 0 to 1, with 4 runs on 0 and 4 on 1. Call x.
# the second loop could 00110011. Call y.
# the third is 01010101

counter = 0

for x in range(2):
    for y in range(2):
       for z in range(2):
          print(x,y,z)

print("The number of times this looped is " + str(counter))

# Yuliya suggested a version with letters to see how result was generated
counter = 0

for x in ["a", "b"]:
    for y in ["c", "d"]:
        for z in ["e", "f"]:
            print(x, y, z)


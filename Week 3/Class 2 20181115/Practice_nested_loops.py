#Brendan's beginning of a solution, not correct. This is to practice nested loops, indented for loops run within previous ones
u = 0
for x in range(2):
    print(x, end="")

    for y in range(2):
        print(y,end="")

        for z in range(2):
            print(z,end="")

            u = u + 1
print (u)
#ran 8 times
#when you run cursor over the little triangle/squares at the left tell you what is in which block.




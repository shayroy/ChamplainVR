# Brendan likes to call lists arrays, the proper name.

list1 = ["a", "b", "c"]
#this is the way to define lists. There are other ways. Can inlude numbers or strings as Python is dynamically typed,#
#meaning a variable can change type throughout a program.
print("The 2nd value in the list is " + list1[1])
#list indexes start at 0
#for loops
for listItem in list1:
#remember indents are within blocks
    print("The value is: ", end="")
    print(listItem)

list1.append("d")
for listItem in list1:
    print("The value is: ", end="")
    print(listItem)

list1.remove("c")
#if the list has two "c"s will remove the first

print("***")

for listItem in list1:
    print("The value is ", end="")
    print(listItem)

list2 = ["a", "b", "c"]
# I missed what he put as list2 so just made one up.
# Pop drops the last value in list
list2.pop(0)

# item count
print(len(list2))

#Length of string
print(len("Hello"))

#We reviewed how to get the portion of a list. See slide 6



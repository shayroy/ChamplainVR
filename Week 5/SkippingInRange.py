# PyCharm always suggests what can be typed in yellow
# Skipping in range is shortcut to make regular list to avoid doing modulus or other more complicated solution
for a in range(0, 101, 5):
    print(a)

# This gives a list counting by 5 i.e. 0 5 10 15 20 to 100

# Used to do this method, still OK.
# this hardcodes list

my_list = [11, 22, 33, 44]

for item in my_list:
    print(item)

# here is one from his slide

squares = [value**2 for value in range(1,11)]
print(squares)
# squares is a new list

#create my_list_2 with the answer [11, 22, 33, 44] using the method immediately above
# mine
my_list_2 = [11*x for x in range(1,5)]
print(my_list_2)
#Braden,s
my_list_2 = [value * 11 for value in range(1,5)]
print(my_list_2)
# this is more dynamic and is an example of modular programming that you can easily change and be understood by another /
# later.
# range(1,5) counts 1, 2, 3, 4. Python leaves off the ending number in a list.

# First 10 values of 2**n

my_list_3 = [2** n for n in range(11)]
print(my_list_3)
# This shows list of powers often seen in capacity of computer memory, which is binary.
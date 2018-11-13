# with else statement with if to give alternative action
mynumber = 42
if mynumber == 42:
    print("matched")
else:
    print("not match")

mynumber = 412
if mynumber ==42:
    print("matched")
else:
    print("not a match")

# also have greater than >, less than <, greater than or equal >=, lesser than or equal <=, not equal !=.

if mynumber > 42:
    print("The number " + str(mynumber) + " is greater than 42")
else:
    print("The nubmer " + str(mynumber) + " is less than or equal to 42")

# can combine these. see slide 36 Compount Equality and Logic
myvalue = 34
if myvalue > 20 and myvalue != 33:
    print ("The number is above 20 and it's not 33.")


my_list = {"A": "Brendan", "B":"Joe", "C": "Mary"}
# each key is unique, so can't give C to someone other than Mary. If by mistake you add another value for C, /
# such as Peter, it will replace Mary. Python will give message noting duplicate.
print(my_list["C"])
# this prints the value Mary for key C.
# see Dictionary Operations slide
# Under lists there can be arrays(also a list) and dictionaries, which are an indexed list, which behave differently.

# Try to find 2 ways to fix province list, one based on testing the existence of a key value, and another using something/
# we did before.

province_list = {"QC": "Quebec", "ON": "Ontario"}
prov = input("Please enter a province code > ")

if prov.upper() not in province_list:
    print("Sorry the province code is not recognized!")
else:
    result = province_list[prov.upper()]
    print("The province name is {0}".format(result))

# can also do try and exceptions else

province_list = {"QC": "Quebec", "ON": "Ontario"}
prov = input("Please enter a province code > ")

try:
    result = province_list[prov.upper()]
    print("The province name is {0)".format(result))
except KeyError:
    print("Sorry the province code is not recognized!")

# Brendan thinks the first is easier to understand, but both work fine. 

province_list.items()



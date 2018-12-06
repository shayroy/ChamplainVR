# Dictonaries
# key and value
# keys are unique will point to a value in list
# key could be province code, i.e. QC MB
# QC -> Quebec key QC points to the value Quebec
# PQ is also valid as a key, as unique, even if it points to the same value as QC
# keys can also point to an array, such as keeping track of scores.
# keys could be student ids and array could be result on four quizzes.
# json is a common way in java script to give a list.
# key colon vlaue is the

# try coding four or five provinces.

# Province Code > QC
# result Quebec
# case sensitive so need to allow them to enter both lower and upper by using upper or lower

province_list = {"QC": "Quebec", "ON": "Ontario"}
prov = input("Please enter a province code > ")
result = province_list[prov.upper()]
print("The province name is {0}".format(result))

# can improve with exceptions, for example, if someone enters ZZ gives KeyError: 'ZZ'
# see Dictonary1 for this.




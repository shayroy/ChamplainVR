#Uppercase, Titlecase, lowercase, length and replacement are important.
#for length "The Length of the string is x".
#for replacement, he would like us to change all "!" to ".".
myString = input(">")
print(myString.upper())
print(myString.title())
print(myString.lower())
print(">the length of the entered string is " + str(len(myString)))
print(myString.replace("!", "."))
#can concantonate more than one
print(myString.upper().replace("!", "."))




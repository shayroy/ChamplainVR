#these are examples of exceptions, followed by else. Excepts are for systems errors that give red text.
#if for a business rule, use if statements.
a = input("Enter the year you started work? >")
b = input ("Enter the current year >")

try:

    c = int(b) - int(a)

except ValueError:
    print("The value(s) entered are not numeric!")
except Exception:
    print("A general error has occurred.")
else:
    print ("You have been working for {0} years".format(c))
# FUNCTIONS
# If want to print 1+2 and then a series of spacers like --------------, and then 2+2 and a the same series of spacers,
# you can put the spacers in drawline() so you don't have to repeat it or copy/paste. You can also add numbers to each
# line, for example.
# Functions can encapsulate commands, such as add2 instead of needing to write add two.
# See slide Functio Definition. Defined with "def" prefix and then indented.
# Have to put function definition before it is called (unlike many languages).
# Have to leave two blank lines between the function and the code
def print_underscores():
    print("--------------")

def print_lots_of_equal_signs():
    print("==============")


print("This is line 1")

print_underscores()

print("This is line 2")

print_underscores()

print("This is line 3")

print_lots_of_equal_signs()


# Meaningful examples of functions often require input of information.



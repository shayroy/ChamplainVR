# (Java and C# prefer that you define functions with capitalized words and no spaces. Python prefers no capitals and
# underscore between words.)
# How to pass a value to a function.

def print_separator(width):

    for w in range(width):
        print("*", end="")
    print()

print("This is line 1")

print_separator(50)

# It will print the number of asterixes as you define in the variable w.
# Yuliya gave this other method:
def print_separator_2(width):
    print("*" * width)

print("This is line 1")

print_separator_2(50)



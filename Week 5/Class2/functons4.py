# Define a functon with 2 parameters.
# Separate the parameters with commas.

def add_numbers(number1, number2):
    print("Adding 2 numbers")
    print(int(number1) + int(number2))

def add_3_numbers(number1, number2, number3):
    print("Adding 3 numbers")
    print(int(number1) + int(number2) + int(number3))


print("Adding 1 + 2 gives")
add_numbers(1, 2)
# Python likes space after commas

print("Adding 1 + 2 + 3 gives")
add_3_numbers(1, 2, 3)

# this one requires 2 or 3 numbers.
add_numbers(1)
# gives error "TypeError: add_numbers() missing 1 required positional argument: 'number2'"




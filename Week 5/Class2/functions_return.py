
# functions don't always have a return statement, but they often do.
def add_numbers(num1, num2):
    result = int(num1) + int(num2)
    return result

my_result =  add_numbers(1, 2)

print(my_result)

# See Returning a Value slide

# can have two returns for a function.


def isnumbernegative(n):
    if n < 0:
        return True
    return False
mynumber = isnumbernegative(45)
print(mynumber)











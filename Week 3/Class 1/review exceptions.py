#exceptions see slide 24-26
try:
    print(10/3)
    print(10/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

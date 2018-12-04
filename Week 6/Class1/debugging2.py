def calculate_tax(amount):
    amount_with_tax = amount* 1.1556
    return amount_with_tax

value = 101

print ("The value is " + str(value))
# in debugging I can either go to the next line if I don't want to know what happens in next line.
# or I can step into and see how it shows what it is doing up in the function
value_with_tax = calculate_tax(value)

print ("The value with tax is " + str(value_with_tax))

# ----------------------
# Paul Shay
# FizzBuzz
# Print a list of numbers from 0 to 25.
# 1. If the number is divisible by 3, print "Fizz".
# 2. If the number id divisible by 5, print "Buzz".
# 3. If the number is divisible by both, print "FizzBuzz".
# Sample output
# 0:FizzBuzz
# 1:
# 2:
# 3:Fizz
# ...
# ------------------------

for number in range(26):
    if number % 3 == 0 and number % 5 == 0:
        print(str(number) + ": " + "FizzBuzz")
    elif number % 3 == 0 and number % 5 != 0:
        print(str(number) + ": " + "Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print(str(number) + ": " + "Buzz")
    else:
        print(str(number) + ": ")
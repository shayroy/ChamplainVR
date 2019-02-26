# Ask the user for a number, and then report whether the number is a multiple of 10 or not.
number = int(input('Please input a number and I will tell you if it is a multiple of 10: '))

if number % 10 == 0:
    print('Your number is a multiple of 10.')
else:
    print('Your number is not a multiple of 10.')

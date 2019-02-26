first_number = input("Enter a number: ")
second_number = input ("Enter a second number: ")

try:
    answer = int(first_number)/int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)

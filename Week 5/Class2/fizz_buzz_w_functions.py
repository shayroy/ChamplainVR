# what should be returned? The number and variable we are testing.
# so the parameters should be 1 - num and 2 - test value
# what should be returned?
# True or False
# if the remainder 0 return True else return False
# functions need to go on top
# in original the num % num == 0 is repeated four times so want to create function with it.
# for example, is four divisible by 3 is_divisible(4, 3)


def is_divisible(num, test_num):
    if num % test_num == 0:
        return True
    return False

for num in range(0, 21):
     print(str(num) + ": ", end="")
     if is_divisible(num, 3) and is_divisible(num, 5):
         print('FizzBuzz')
     elif is_divisible(num, 3):
         print('Fizz')
     elif is_divisible(num, 5):
         print('Buzz')
     else:
         print()


# Original we started with is actually shorter but it is less modular than the new one with functions.
# for num in range(0, 21):
#     print(str(num) + ": ", end="")
#     if num % 3 == 0 and num % 5==0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print()


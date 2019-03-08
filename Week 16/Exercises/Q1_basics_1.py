from Q1_func_test import *

Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!"]
char_list =[]
max_value =number_list_max
count = 0

for i in Input_list:
    count += 1
    is_a_number = test_num(str(i))
    is_a_char = test_char(str(i))

    print("Element #" + str(count) + ". Value is " + str(i), end='')

    if is_a_number:
        print(" This is a number. ", end='')
        if test_even:
            print(" This is an even number.", end='')
        if i == max_value:
            print(". This is the highest number in the list.")
        else:
            print(". This is not the highest number in the list.")


    elif is_a_char:
        char_list.append(i)
        char_list.sort()
        print(". This is a character.  ", end='')
        print( "So far, the characters found are ", end='')
        print("[" + ",".join(char_list) + "]")

    else:
        print(". This is a special character.")

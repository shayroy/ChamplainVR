import re
from func_test import *

Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!"]
num_list =[]
char_list =[]

count = 0
for i in Input_list:
    count = count + 1
    is_number = test_num(str(i))
    is_char = test_char(str(i))

    if is_number:
        num_list.append(i)
        mx = find_max(num_list)
        print("Element # " + str(count) + ": Value is " + str(i) + ". This is a number. ", end='')

        if int(i) % 2 == 0:
            is_evennum = True
            print(" This is an even number.", end='')

        if int(i) == int(max(num_list)):
            is_max = i
            print(" This is the highest number so far.")
        else:
            print(" This is not the highest number so far.")

    elif is_char:
        char_list.append(i)
        char_list.sort()
        print("Element # " + str(count) + ": Value is " + str(i) + ". This is a character.  ", end='')
        print( "So far, the characters found are ", end='')
        print("[" + ",".join(char_list) + "]")

    else:
        print("Element # " + str(count) + ": Value is " + str(i) + ". This is a special character.")

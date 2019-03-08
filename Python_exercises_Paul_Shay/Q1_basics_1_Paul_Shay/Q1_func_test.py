import re

def test_num(cand: str):
    return re.match("^[0-9]+$", cand)

def test_char(cand: str):
    return re.match("^[A-Za-z]*$", cand)

def test_even(i):
    if int(i) % 2 == 0:
        return True

def number_list_max(Input_list):
    numbers =[]
    for cand in Input_list:
        if is_a_number(str(i)):
            numbers.append(int(i))
    return max(numbers)

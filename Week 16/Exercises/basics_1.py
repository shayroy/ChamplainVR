import re

Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!"]
#variables for Boolean true or false)
is_number(True)
is_spec_char(True)


def regex_is_numeric(candidate):
    return re.match("^[0-9]+$", candidate)

def regex_is_spec_char(candidate):
    return re.match("[^A-Za-z0-9]")

if candidate.is_number:





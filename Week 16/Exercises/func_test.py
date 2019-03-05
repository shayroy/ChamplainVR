import re
def test_num(cand: str):
    return re.match("^[0-9]+$", cand)

def find_max(In_List):
    return max(In_List)

def test_char(cand: str):
    return re.match("^[A-Za-z]*$", cand)

#def regex_is_spec_char(candidate):
#    return re.match("^[^A-Za-z0-9]$", a)

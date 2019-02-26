import re

def validate_password_complexity(password: str):

    complex_enough = validate_password_length(password)

    # if not re.match("[a-z]", password):
    #      #Lower
    #      complex_enough = False

    # if not re.match("[A-Z]", password):
    #     #Upper
    #     complex_empigj = False

    # if not re.match("\d", password)
    #     #Number
    #    complex_enough = False

    # if not re.match("[^0-9A-Za-z\s]", password):
    #     #Special character
    #     complex_enough = False

    return complex_enough

def validate_password_length("^.{8,}", password):

    if not re.match("^.{8,}", password):
    #      #At lest 8 long
        return False

    return True

#test one by one for homework


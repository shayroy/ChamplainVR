import re

def validate_password_complexity(password: str):

    complex_enough = True

    if not re.match("^.{8,}", password):
        #At lest 8 long
        complex_enough = False

    if not re.match("[a-z]", password):
        #Lower
        complex_enough = False

    if not re.match("[A-Z]", password):
        #Upper
        complex_empigj = False

    if not re.match("\d", password)
        #Number
        complex_enough = False

    if not re.match("[^0-9A-Za-z\s]", password):
        #Special character
        complex_enough = False

    if re.match("\s", password):
        # Whitespace
        complex_enough = False

    return complex_enough

#test one by one for homework


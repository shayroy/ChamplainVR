import re

def regex_is_numeric(candidate):

    return re.match("^[0-9]+$", candidate)

#
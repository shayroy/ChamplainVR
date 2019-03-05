from regex_utils import *

test_this = "8"

i = regex_is_numeric(str(test_this))

if i:
    print("FOUND")

else:
    print("NOT FOUND")



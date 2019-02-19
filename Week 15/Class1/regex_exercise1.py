# Match jim but not jam, lam, 0am
import re

is_a_match = re.search("^jim$", "jim")
is_a_match2 = re.search("^jim$", "j0m")
# Brendan adds this a=2 placeholder for the debugger so the previous lines will be debugged.
a=2

# test
if re.search("^jim$", "jim"):
    print("This is a match")
else:
    print("Not a match")




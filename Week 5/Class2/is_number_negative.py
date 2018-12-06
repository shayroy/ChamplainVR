# See Returning a Value slide

# can have two returns for a function.

def is_num_negative(n):
    if n < 0:
        return True
    return False

# in Python, capitalize True and False.

the_number = input("Enter a number > ")

if is_num_negative(int(the_number)):
    print("negative")
else:
    print("positive")


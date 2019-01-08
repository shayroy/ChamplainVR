# less optimal way.
# f = open("example.txt")

# my_text = f.read()

# print(my_text)

# f.close()

# The "with open" command is the preferred method.
# Read is to read the entire file if no parameters. For example, if add 10, will show only the first 10 characters.
# Can add rstrip to remove blank lines.
# f.seek() skips the indicated number of characters.
# f.tell tells you where you are in a file.
#
with open("example.txt") as f:

   print(f.read(10).rstrip())




import os
f = open("seektest.txt", "w")
f.write("This is a test.")
f.close()

f2 = open("seektest.txt", "r")
print(f2.read())
# when you close an reopen a file, the pointer is reset to 0 so you do not need to use seek(0) to move it to the
# beginning so that it will print.
#f2.close()

try:
    os.remove("seektest.txt") #not case sensitive in Windows, Mac or SQL, but Linux is.

except IOError:
    print("Caught and IO error")

except Exception:
    print("caught a general exception")


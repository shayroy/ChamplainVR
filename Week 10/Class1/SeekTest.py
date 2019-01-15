f = open("seektest.txt", "w+")

f.write("This is a test.")

f.seek(0)
#pointer is at end of file and so prints nothing unless you include a seek(0).

print(f.read())




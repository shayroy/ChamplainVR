import os

#if os.path.exists("testfile5.txt"):
with open("testfile5.txt", 'w+') as f:
    try:
        f.write("This is testfile5")
        #f.seek(2)
        #f.write("$$")
        #f.seek(0)
        print(f.read())
    except IOError:
        print ("Could not read file:", testfile5.txt)
        sys.exit()


# Brendan recommends strongly we practice this at home
import os

os.path.curdir

while True:

    listing = os.listdir() # Listing is an array. To use array, need to use for loop.
    print("-"*50)
    counter = 1

    for file in listing: #Yuliya wonders if it would not be good to turn this into a function that can be called
        #again later when we change directory.
        print(counter, end="")

        if os.path.isdir(file):
            print("(Folder)", end="")

        else:
            print("( File )", end="")

        print(file)
        counter += 1

    print("-" * 50)

    a = input("Selection? >")

    if a ==".." or a == "back":
        os.chdir("..")
        print("Backed up one folder.")

    else:

        myfile = listing[int(a) - 1] #The first members of array are 1, 2, 3, 4, 5. To access name of file 1
        # When we run will create inside listing an array of 5 elements in his case. Need -1 as list starts at 0, not 1.

        if os.path.isfile(myfile):
            with open(myfile, "r") as f1: # f1 is a nickname or holder that allows us to refer to the file.
            #f1 is only alive in the current block.
                print(f1.read())
            print("File read!")
            print("Press any key to continue.")

        if os.path.isdir(myfile):
            os.chdir(myfile)
            print("Changed directory.")



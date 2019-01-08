my_list = []

my_list.append("This is line A\n")
my_list.append("This is line B\n")


with open("newfile.txt", "a") as f1: # f1 is the pointer to the file.
    f1.write("Hello this is a test.\n")
    f1.write("Hello this is line 2.\n")
    f1.writelines(my_list)
    # writelines will add

    # newfile shows in red, meaning it is not to be added to GIT. To add it, right click on the file and click on GIT.
    # It then turns green.

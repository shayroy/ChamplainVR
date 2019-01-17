import os
#if os.path.exists(test_file2.txt):
with open("testfile3.txt", 'r', encoding = 'utf-8') as file_object:
    for line in file_object:
        print(line.rstrip())

with open ("testfile4.txt", 'w+', encoding = 'utf-8') as file_object:
    file_object.write("Testing 234")
    print(file_object.read())
    file_object.seek(2)
    file_object.write("**")
    file_object.seek(0)
    print(file_object.read())

    







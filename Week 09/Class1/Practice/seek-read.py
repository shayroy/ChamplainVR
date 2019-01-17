with open("example2.txt") as file_object:
    contents = file_object.read()
    print(contents)

with open("example2.txt") as f:
   print(f.read().rstrip())

with open("example2.txt") as f:
    for line in f:
        print(line.rstrip())

with open("example2.txt") as f:
    f.seek(3)
    print (f.read()) #This prints without the first three characters "Thi"
    f.seek(1)
    print (f.read()) # This prints without the first character "T".
    f.seek(0)
    print (f.read()) # This prints everything.

with open("example2.txt") as f:
    lines = f.readlines()
for line in lines:
    print (line.rstrip())

with open("example2.txt") as f:
    lines = f.readlines()

for line in lines:
    print (line.rstrip())












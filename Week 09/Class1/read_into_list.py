with open ("example.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print(lines[1])

print(len(lines))

# you can get the number of characters or bytes by using len on each line.

text_file_size = 0

for line in lines:
    text_file_size += len(line)

print("Total file size is " + str(text_file_size))


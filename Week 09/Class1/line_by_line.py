with open("example.txt") as f:
    for line in f:
        print(line.rstrip())
        # print(line) alone without .rstrip prints a blank line between lines


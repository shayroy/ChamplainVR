import csv
with open("person1.csv", 'rt') as f:

    reader = csv.reader(f)
    line_counter = 1
    for row in reader:
        if line_counter == 1:
            pass # means do nothing
        else:
            print ("Student ID: " + row[0] + " Grade: " + row[1])

        line_counter +=1

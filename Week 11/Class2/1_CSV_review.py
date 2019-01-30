import csv

line_counter = 0
total_ages = 0
females = 0
average_age = 0
percent_female = 0
percent_male = 0
respondents = 0

with open("biostats.csv", "rt") as csv_file:
    reader = csv.reader(csv_file)
    next(reader) # this skips the title row in the csv file.
    for row in reader:
        total_ages += int(row[2])
        if row[1] == "F":
            females += 1

        line_counter += 1

    average_age = total_ages /(line_counter-1)
    percent_female = females /(line_counter-1)
    percent_male = 1 - percent_female

print('The average age is {0:.1f}'.format(average_age) + ".")
print('{:.1f} '.format(percent_female*100) + '% are female.')
print('{:.1f} '.format(percent_male*100) + '% are male.')



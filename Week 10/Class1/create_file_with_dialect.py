import csv

person = [["StudentId", "Grade"],[123456, "A"]]

csv.register_dialect ('myDialect',
quoting=csv.QUOTE_NONNUMERIC,
skipinitialspace=True, lineterminator="\n")
with open('person1.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)
        # is this done?
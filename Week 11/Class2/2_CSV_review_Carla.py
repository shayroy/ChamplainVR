import csv

row_counter = 1

csv.register_dialect('myDialect',
                     quoting=csv.QUOTE_NONNUMERIC,
                     skipinitialspace=True, lineterminator="\n")

line_counter = 1
cm_convert = 2.54
Kg_convert = 0.453592
reader = csv.reader(f)
"""The next line move the reader to the second register in the file"""
next(reader)
with open('biostats1.csv', 'w') as f:
   writer = csv.writer(f)
with open('biostats2.csv', 'w') as f:
   writer = csv.writer(f, dialect='myDialect')
for row in reader:
    line = []
    height = 0
    weight = 0
    if line_cpunter ==1:
        header = "Name,Sex,Age,Height(cm),Weight(Kg)"
        line.append("Name")
        line.append("Sex")
        line.append("Age")
        line.append("Height(cm)")
        line.append("Weight(Kg)")
    else:
        height = float(row[2]) * cm_convert
        weight = float(row[3]) *Kg_convert
        line.append(round(weight, 2))

    line_counter += 1
    writer.writerrow(line)


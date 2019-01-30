import csv

row_counter = 1
csv_data = [["Name", "Sex", "Age", "Height(cm)", "Weight(kg)"]]

with open ("biostats.csv", "rt") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        if row_counter != 1:
            row[3] = round(float(row[3])*2.54)
            #print (row[3])
            row[4] = round(float(row[4])*.454)
            csv_data.append(row)
        row_counter += 1

with open('biostats_metric.csv', 'w', newline='') as csv_metric_file:
    writer = csv.writer(csv_metric_file)
    writer.writerows(csv_data)
    print("OK")

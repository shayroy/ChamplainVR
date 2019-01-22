import csv

row_counter = 1
#unique_types = {} #This is a dictionary with curly brackets. A better way, that he had not shown us yet, is with a set.
unique_types = set() # This is the solution using set.
europe_orders = 0
total_units_sold = 0

with open("7_-_100_Sales_Records.csv") as cvs_file:

    reader = csv.reader(cvs_file)
    # next(reader) -Yuliya used the iterator "next" as in "next(reader)" to avoid needing to use row_counter.
    # Brendan did not show us iterators so did not use this approach.
    for row in reader: #This is loop that runs on each row.
        if row_counter != 1: # This avoids reading the header row.
           #unique_types[row[2]] = row[2] # This is the dictionary, which is accessed with square brackets.
           # See slides 14-18 in presentation 2 - Lists.
            unique_types.add(row[2]) # This is a more efficient approach than dictionary using a set.
           # Just add to a set. Won't add duplicates.
            total_units_sold += int(row[8]) # This adds the units sold in row 8, which is cells in column I in Excel.
            row_counter += 1

            if row[0] == "Europe":
                europe_orders += 1

        row_counter += 1

print("Total amount of units sold {0}".format(total_units_sold))
print("Total records from Europe {0}".format(europe_orders))
print ("")
print("Here is a list of unique item types:") # Item type is column C in Excel.

list_counter = 1
for x in unique_types: # Keys in dictionnaries are always unique. Printed with for loop.
    print(str(list_counter) + "" + x)
    list_counter += 1

#Brendan explained that Panda are libraries for Python that are useful for statistics, and had Yuliya demonstrate.
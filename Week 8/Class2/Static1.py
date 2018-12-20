class School:

    region = "Unknown"

    name = ""

# He wants all schools to be in the Montreal region, but each school needs a name.
# Montreal is a global variable, available everywhere.

school1 = School()
school1.name = "Champlain"

school2 = School ()
school2.name = "Dawson"

print("School name for school1 is " + school1.name)
print("Region for all schools is " + School.region)
print("Region for school2 is " + school2.region)
# Functions review using Python Crash Course 8-6 page 146
# functions usually give something back and do not have the print inside the function like the previous exercise,
# so this is more realistic use.

def city_country(city, country):
    return city + ", " + country

print (city_country("Montreal", "Canada"))
# If we input print (city_country("Montreal", 123))
# it fails as it is looking for string not number. Could put str before city and country in return line
# It could work with a number if we use the other print format.
def city_country(city, country):
    return"{0}, {1}".format(city,country)

print(city_country("Montreal", "Quebec"))
print(city_country("Montreal", 123))


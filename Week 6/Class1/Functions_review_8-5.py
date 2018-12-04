#Functions review Python Crash Course 8.5  p.141
# my solution:

def describe_city(city, country='canada'):
    print("\n" + city.title() + " is in " + country.title() + ".")

describe_city(city="toronto", )
describe_city(city="montreal", country="canada")
describe_city(city="paris", country="france")
describe_city(city="new york", country="united states")

#Brendan's solution, using both print formats
def city_names(city, country='unknown country'):
    print(city.title() + " is in " + country.title())
    print("{0} is in {1}".format(city.title(), country.title()))

city_names("montreal", "canada")
city_names("montreal")


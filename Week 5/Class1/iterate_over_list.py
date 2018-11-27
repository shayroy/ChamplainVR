# see printing all keys and values slide
#for x in countries:
#    print(x)
#
# to print keys, values and items (which prints both keys and values):

countries = {'us': 'USA',
             'fr': 'France',
             'uk': 'United Kingdom'}

for k, v in countries:
    print(k,v)

print ("------------")

for i in countries.items():
    print(i[1])

print("----------")

for a, b in countries.items():
    print(a, b)

print("-----------")

for a in countries.keys():
    print(a)

print("-----------")

for v in countries.values():
    print(v)


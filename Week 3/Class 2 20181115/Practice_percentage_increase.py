total = 34.00
increase_rate = .1556
print ("The total amount increased by the percentage rate is : " + str(float(total)+(total*increase_rate)))

#Brendan's solution, but maybe cheating a bit by converting percentage increase to floate increase
total = 34.00
increase_rate = 1.1556
result = total*increase_rate
print("The total amount increased by the percentage rate is " + str(result))

#another solution using percentate increase rate
total = 34.00
increase_rate = 15.56
result = total * (increase_rate * 0.01) + total
print("The total amount increased by the percentage rate is " + str(result))
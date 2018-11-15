#my start
# Sale1 = "1.40"
#Sale2 = "2.30"
#print("$"+ str(float(Sale1+Sale2))

#brendan's solution. Have to import things to avoid having too much info loaded at the same time. We will not use float in our
#course but decimal is useful
import decimal

Sale1 = "1.40"
Sale2 = "2,50"
sale_dec1 = decimal.Decimal(Sale1)
sale_dec2 = decimal.Decimal(Sale2)

print(sale_dec1 + sale_dec2)

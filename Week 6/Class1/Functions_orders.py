# See Unknown Amount of Arguments slide.
# He wants customer list with SKUs in their order.
# The name of the shoppers is a fixed list.
# The number of SKUs can vary in length.
# We do a for loop.

def create_order(customer, *skus):
    print("The customer name is: " + customer)

    for sku in skus:
        print(sku)

customer_name="Customer1"
create_order(customer_name, 1234567, 2345678, 3456789, 8888888)




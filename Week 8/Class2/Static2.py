class Item:
    # Since we want to pass it a sku automatically, no need to start with it.
    # We need to tell the class the last number used.

    last_serial_used = 0

    def __init__(self, name, price, taxable):


        self.name = name
        self.price = price
        self.taxable = taxable
        self.serial = Item.last_serial_used + 1
        Item.last_serial_used = self.serial

# "@" introduces a static method
    @staticmethod
    def print_last_serial_used():
        print (Item.last_serial_used)

a1 = Item ("first item", 2.00, True)
a2 = Item("Second item", 3.00, False)

print(a1.serial)
print(a2.serial)

Item.print_last_serial_used()


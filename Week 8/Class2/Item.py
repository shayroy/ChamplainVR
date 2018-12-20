class Item:

   # last_serial_used = 0

    def __init__(self, sku, name, price, taxable):
        """Instantiating the items"""

        self.__sku = sku
        self.__name = name
        self.__price = price
        self.__taxable = taxable
       # self.__item_number = Item.last_serial_used + 1
       # Item.last_serial_used = self.item_number

   # @staticmethod
   # def print_last_serial_used():
   #     print (Item.last_serial_used)

    def print_item(self):
        """Printing the description of the item"""
        self.item_description=("{0} {1} ${2} {3} {4}".format(self.__name,
                                            ("."*(20-len(self.__name))),
                                            self.__price,
                                            (" "*(7-len(str(self.__price)))),
                                            "T"*(self.__taxable)))
        return self.item_description

    def item_base_price(self):
        """Return gets the price and makes it available to user"""
        return self.__price


    def item_tax_amount(self):
        """Returns tax amount"""
        if self.__taxable:
            self.__tax_amount = self.__price * .1495
        else:
            self.__tax_amount = 0
        return self.__tax_amount

    def get_item_total(self):
        self.__item_total = self.__price + self.__tax_amount
        return self.__item_total



a1 = Item(12345678, "first item", 2.00, True)
# instantiating the first item
a2 = Item(23456789, "second item", 3.00, False)
# instantiating the second item

print(a1.print_item())
print(a2.print_item())
print(a1.item_base_price())
print(a1.item_tax_amount())
print(a2.item_base_price())
print(a2.item_tax_amount())
print(a1.get_item_total())
print(a2.get_item_total())



# still need to print sku, format price and determine Quebec tax formula.


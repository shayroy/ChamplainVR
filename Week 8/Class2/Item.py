class Item:

      def __init__(self, sku, name, price, taxable):
        """Instantiating the items"""

        self.__sku = sku
        self.__name = name
        self.__price = price
        self.__taxable = taxable


    def print_item(self):
        """Printing the description of the item"""
        self.item_description=("{} {} ${:0,.2f} {} {}".format(self.__name,
                                            ("."*(20-len(self.__name))),
                                            self.__price,
                                            (" "*(7-len(str(self.__price)))),
                                            "T"*(self.__taxable)))
        return self.item_description

    def item_base_price(self):
        """Return gets the price and makes it available to user"""
        return self.__price


    def item_gst_amount(self):
        """Returns tax amount"""
        if self.__taxable:
            self.__gst_amount = self.__price * .05
        else:
            self.__gst_amount = 0
        return self.__gst_amount

    def item_pst_amount(self):
        """Returns tax amount"""
        if self.__taxable:
            self.__pst_amount = self.__price * .09975
        else:
            self.__pst_amount = 0
        return self.__pst_amount

    def get_item_total(self):
        self.__item_total = self.__price + self.__gst_amount + self.__pst_amount
        return self.__item_total

"""Test area:

a1 = Item(12345678, "first item", 2.00, True)# instantiating the first item
a2 = Item(23456789, "second item", 3.00, False)# instantiating the second item

print(a1.print_item())
print(a2.print_item())
print(a1.item_base_price())
print(a1.item_gst_amount())
print(a1.item_pst_amount())
print(a2.item_base_price())
print(a2.item_gst_amount())
print(a2.item_pst_amount())
print(a1.get_item_total())
print(a2.get_item_total())"""



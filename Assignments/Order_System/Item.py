class Item:
    __sku = 00000000
    __name = ""
    __price = 0
    __taxable = False
    __item_name_field_length = 25
    __price_field_length = 11

    def __init__(self, sku: int, name: str, price: float, taxable: bool):
        """Instantiating the items"""
        self.__sku = sku
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    @staticmethod
    def get_price_field_length(self):
        """Static method to refer the length of the price field"""
        return Item.__price_field_length

    @staticmethod
    def get_item_name_field_length(self):
        """Static method to refer the length of the item name field"""
        return Item.__item_name_field_length

    def get_item_sku(self):
        """This function returns a SKU."""
        return self.__sku


    def is_taxable():
        """This function returns a Boolean value of True or False depending if the taxable attribute is True or False."""
        return self.__taxable

    def get_item_base_price(self):
        """Returns the price and makes it available to user"""
        return self.__price

    def calculate_gst(self):
        """Returns GST tax amount"""
        if self.__taxable:
            self.__gst_amount = self.__price * .05
        else:
            self.__gst_amount = 0
        return self.__gst_amount

    def calculate_qst(self):
        """Returns PST tax amount"""
        if self.__taxable:
            self.__pst_amount = self.__price * .09975
        else:
            self.__pst_amount = 0
        return self.__pst_amount

    def get_item_total(self):
        """Returns the TOTAL amount to pay, Taxes included"""
        self.__item_total = Item.get_item_base_price(self) + Item.calculate_qst(self) + Item.calculate_gst(self)
        return self.__item_total



    def print_item(self):
        """Returns the formatted description of the item"""
        self.__name_field_fill = "." * (Item.__item_name_field_length - len(self.__name))
        self.__price_field_fill = "." * (Item.__price_field_length - len('{:0,.2f}'.format(self.__price)))
        self.__taxable_field_fill = "T" * self.__taxable + " " * (1 - self.__taxable)

        self.__item_description = ("| {} | {} {} | $ {}{:0,.2f} |  {}  |".format(self.__sku,
                                                                                 self.__name,
                                                                                 self.__name_field_fill,
                                                                                 self.__price_field_fill,
                                                                                 self.__price,
                                                                                 self.__taxable_field_fill))
        return self.__item_description

# Test area

# a1 = Item(12345678, "first item", 2.00, True)# instantiating the first item
# a2 = Item(23456789, "second item", 3.00, False)# instantiating the second item
# a3 = Item(34567891, "third item", 10.00, True)# instantiating the third item
#
# print(a1.print_item())
# print(a2.print_item())
# print(a1.item_base_price())
# print(a1.item_gst_amount())
# print(a1.item_pst_amount())
# print(a2.item_base_price())
# print(a2.item_gst_amount())
# print(a2.item_pst_amount())
# print(a1.get_item_total())
# print(a2.get_item_total())
# print(a3.get_item_total())



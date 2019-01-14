class Item():
    """A class describing the items in orders."""
    __sku = 00000000
    __name = ""
    __price = 0
    __taxable = False
    __item_name_field_length = 25
    __price_field_length = 11

    def __init__(self, sku: int, name: str, price: float, taxable: bool):
        """A method to substantiate each order item."""
        self.__sku = sku
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    @staticmethod
    def get_price field_length:
        """A static method to return the price field length."""
        return Item.__price_field_length


    @staticmethod
    def get_item_field_length:
        """A static method to return the item's name field length."""
        return Item.__item_name_field_length

    def get_item_sku:
        """Makes available the item's SKU."""
        return self.__sku

    def is_taxable:
        """Returns a boolean indicating if the item is taxable."""
        return self.__taxable

    def get_item_base_price(self):
        """Makes available the item's base price."""
        return self.__price

    #def get_item_name:
     #   """Makes available the item's name. """
     #   return self.__name

    def calculate_gst():
        """Calculates the GST amount."""
        if self.taxable
            __gst_amount = self.__price * .05
        else gst_amount = 0
        return gst_amount


    def calculate_qst():
        """Calculates the GST amount."""
        if self.taxable
            __qst_amount = __price * .09975
        else qst_amount = 0
        return qst_amount

    def get_item_total():
        "Calculates the item total amount."
        self.__item_total = get_item_base_price(self) + get_calculate_gst(self) + get_calculate_qst(self)
# why not self.__item_total = self.__price + self.gst_amount + self.qst_amount

    def print item(self):
        self.__name_field_fill





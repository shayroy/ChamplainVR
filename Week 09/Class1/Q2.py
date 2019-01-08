class BankAccount:

    def __init__(self, account_number):
        self.__balance = 0
        self.__account_num = account_number # two underscores make it private to the class.

    def set_balance(self, balance: float): # this is setter, or officially mutator

        self.__balance = balance # sets balance to amount provided

    def get_balance(self): # this is a getter, or offically accessor

        return self.__balance

    # def set_acc_num(self, account_num): # as a business rule, cannot normally change account number.

    #    self.__account_num = account_num

    def get_acc_num(self):

        return self.__account_num

acc1 = BankAccount(123435)

acc1.set_balance(123.12)

print("The balance of the account is " + str(acc1.get_balance()))


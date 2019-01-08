class BankAccount:

    def __init__(self, account_number): # Brendan put : float after account number in his answers but this is wrong.
        self.balance = 0 # have to use self. before balance. Balance alone refers to something else static. Have
        #more control in initiating values. This setup allows people to provide the account number but not make a
        #mistake with account number.
        self.account_num = account_number

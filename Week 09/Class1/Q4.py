class Worker:
    def __init__(self, first, last, acc):

        self.first_name = first
        self.last_name = last
        self.account_name = acc


class Employee(Worker):

    def __init__(self, salary, first, last, acc):
        self.salary =salary
        super().__init__(first, last, acc) # if you make it private, which is not the case here, need to use Super.
    # Instead of using super, could use
        # self.first_name = first
        # self.last_name = last
        # self.account_name = acc

class Contractor(Worker):
    def __init(self, rate, first, last, acc):
        self.rate = rate


emp1 = Employee()

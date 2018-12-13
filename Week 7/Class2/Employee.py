# base class worker: name
# specialized categories
# employee: salary
# contractor: rate
# The above is a review of inheritance
# Below we do it for employee with

class Worker: # always capitalize class name
    """This class represents a worker."""
    def __init__(self, worker_name=""): # upon instantiation
        self.__name = worker_name

    def set_name(self, new_name): # net to give value
        self.__name = new_name

    def get_name(self):
        return self.__name

class Employee(Worker):
    """This class specializes Worker and is salaried."""
    def __init__(self, initial_salary, initial_name):
        self.__salary = initial_salary
        super().__init__(initial_name) # super applies to the super class Worker. Have to set the name from Worker class

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def get_salary(self):
        return self.__salary

e1 = Employee(50000, "Bob")

print(e1.get_name())
print(e1.get_salary())
# can't print (e1.__salary) as salary cannot be accessed directly.
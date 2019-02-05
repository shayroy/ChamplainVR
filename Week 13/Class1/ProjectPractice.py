import datetime

class Worker:
    """This is the super class for workers."""
    # created static variable and counter by moving it out of the init. To do: Add this to employee and contractor
    auto_id = 0

    def __init__(self, first_name: str, last_name: str, hire_date: datetime):

        self.__id = Worker.auto_id + 1
        Worker.auto_id = self.__id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hire_date = hire_date

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_hire_date(self):
        return self.__hire_date

class Employee(Worker):
    """Child class represents employees."""

    def __init__(self, first_name: str, last_name: str, hire_date: datetime, salary: float):
        self.__salary = salary
        super().__init__(first_name, last_name, hire_date)

    def set_salary(self, salary: float):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_hourly_rate(self):
        return self.__salary / 261 / 8

class Contractor(Worker):
    """Child class for contractors."""

    def __init__(self, first_name: str, last_name: str, hire_date: datetime, hourly_rate: float):
        self.__hourly_rate = hourly_rate
        super().__init__(first_name, last_name, hire_date)


    def set_hourly_rate(self, hourly_rate: float):
        self.__hourly_rate = hourly_rate

    def get_hourly_rate(self):
        return self.__hourly_rate




class Task:
    """Class for tasks."""
    def __init__(self, id: int, name: str, description: str, assigned_to: Worker, duration_hours: float):

        self.__id = id
        self.__name = name
        self.__description = description
        self.__assigned_to = assigned_to
        self.__duration_hours = duration_hours
        self.__hours_completed = 0.0

    def set_name(self, name:str):
        self.name = name

    def set_description(self, description: str):
        self.__description = description

    def set_assigned_to(self, assigned_to: Worker):
        self.__assigned_to = assigned_to

    def set_duration_hours(self, duration_hours: float):
        self.__duration_hours = duration_hours

    def get_id(self):
        return self.__id

    def get_name(self): # never provide parameters in a getter
        return self.__name

    def get_description(self):
        return self.__description

    def get_assigned_to(self):
        return self.__assigned_to

    def get_duration_hours(self):
        return self.__duration_hours

    def get_hours_completed(self):
        return self.__hours_completed

    def add_time(self, num_hours: float):
        self.__hours_completed += num_hours



class Project:
    """The Project class represents the main project, which holds between 0 and n tasks."""
    def __init__(self, id: int, name: str, hours_estimated: int):
        self.__id = id
        self.__name = name
        self.__hours_estimated = hours_estimated
        self.__tasks = []

    def set_name(self, name: str):
        self.__name = name

    def set_estimated_hours(self, hours_estimated: float):
        self.__estimated_hours = hours_estimated

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_estimated_hours(self):
        return self.__hours_estimated

    def add_task(self, task: Task):
        self.__tasks.append(task)

# Total cost is created by walking through all the tasks with for loop, calling the getter
    # and calculating the sum from a variable accumulator to holds the increasing value. [task, task, task].
    # task.assigned_to.get_hourly_rate
    # Tasks have duration in hours, say 10, worker's rate, say $45

    def get_project_cost(self):

        total_cost = 0.00

        for task in self.__tasks:

            total_cost += task.get_duration_hours() * task.get_assigned_to().get_hourly_rate()

        return total_cost

    def get_project_elapsed_hours(self):

        total_hours = 0.00
        for task in self.__tasks:
            total_hours += task.get_hours_completed()
        return total_hours

    def get_project_elapsed_cost(self):

        total_elapsed_cost = 0.00
        for task in self.__tasks:
            total_elapsed_cost += task.get_hours_completed() * task.get_assigned_to().get_hourly_rate()
        return total_elapsed_cost





# test
emp = Employee("Brendan", "Wood", None, 75000)
contr = Contractor("Alice", "Smith", None, 78)

task1 = Task(1, "Cook Breakfast", "Cook a great breakfast", emp, 10)
task2 = Task(2, "Make Lunch", "Lunch is important.", contr, 10)
task1.add_time(8)
task2.add_time(9)
proj1 = Project(1, "Project #1", 30)

proj1.add_task(task1)
proj1.add_task(task2)

print("The total estimated cost for project " + proj1.get_name() + " is " + '${:,.2f}'.format(proj1.get_project_cost()))
print("The final cost for project " + proj1.get_name() + " is " + '${:,.2f}'.format(proj1.get_project_elapsed_cost()))


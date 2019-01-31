import datetime

class Worker:
    """Super class for workers."""
    def __init__(self, id: int, first_name: str, last_name: str, hire_date: datetime):
        self.__id = id
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
    """Child class for employees."""

    def __init__(self, id: int, first_name: str, last_name: str, hire_date: datetime, salary: float):
        self.__salary = salary
        super().__init__(id, first_name, last_name, hire_date)

    def set_salary(self, salary: float):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_hourly_rate(self):
        return self.__salary / 261 / 8

class Contractor(Worker):
    """Child class for contractors."""

    def __init__(self, id: int, first_name: str, last_name: str, hire_date: datetime, hourly_rate: float):
        self.__hourly_rate = hourly_rate
        super().__init__(id, first_name, last_name, hire_date)


    def set_hourly_rate(self, hourly_rate: float):
        self.__hourly_rate = hourly_rate

    def get_hourly_rate(self):
        return self.__hourly_rate




class Task:
    """Class for tasks."""
    def __init__(self, id: int, name: str, description: str, assigned_to: Worker, duration_hours: float, worked):

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

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_assigned_to(self):
        return self.__assigned_to

    def get_duration_hours(self, duration_hours: float):
        return self.__duration_hours

    def get_hours_completed(self):
        return self.__hours_completed

    def add_time(self, num_hours: float):
        self.__hours_completed += num_hours

class Project:
    """Class for project."""
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



# test to see if hourly rate is returned for employee.
# emp = Employee(1, "Brendan", "Wood", None, 75000)
#
# print (emp.get_hourly_rate())




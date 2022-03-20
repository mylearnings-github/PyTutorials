"""
    Understanding:
    --------------
    1) Class Methods - cls as first argument
    2) Instance Methods - self as first argument
    3) Static Methods - Just a regular method we included in class because it had some connection with it.
"""

# Definition
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'        
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        ''' Working with class instead of instance '''
        cls.raise_amount = amount
    
    @classmethod    
    def from_string(cls, emp_str):
        """
            This type of usage is commonly called
            'Using class methods as alternative Constructors'

            you can find it's implementation in standard 'datetime.py' module. 
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Instantiation
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

''' Class method utilized '''
Employee.set_raise_amt(1.05) # Properly done
emp_1.set_raise_amt(1.12) # Using class method from instance works, but not the right way.

# Validation
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


"""
    Problem Statement - 1
    ---------------------
    Someone says they will give us the employee detail in the form of string, separated by hyphen.
    And asks us if there is a way we can parse that string and put it as employee class.
"""

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# Done:
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

# But wait, this doesn't seem good. Is there a better way of doing?
''' Surprisingly, yes and below implementation does that!'''
emp_obj_1 = Employee.from_string(emp_str_1)
emp_obj_2 = Employee.from_string(emp_str_2)
emp_obj_3 = Employee.from_string(emp_str_3)

# Validation
emp_obj_2.__dict__



"""
    Problem Statement - 2
    ---------------------

    Find out if a given day is a work day or not!

    This has logical connection with Employee class, so let's have a static method. 
"""

# Verification
import datetime
my_date = datetime.date(2022, 3, 19)
print(Employee.is_workday(my_date))
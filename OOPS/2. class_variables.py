"""
    Difference B/W Class Variable and Instance Variable ? 
    1) 'self' keyword is used for instance variable.    
    2) <ClassName>.Variable is the syntax used while accessing class variable.
    3) Class variable remains constant for all instance of that class. 
    4) Instance variable can be changed.
"""

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        ''' Employee number is not going to change, hence it is made a class variable '''
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        ''' 
            If below comment is enabled, all employees gets the same raise amount 
            i.e) 'self' gives 1st priority to the instance of the class!
        '''
        #self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


print(f'Number of Employees : {Employee.num_of_emps}')
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(f'Number of Employees : {Employee.num_of_emps}')

# By default instance variable does not hold class variable
print(emp_1.__dict__)
print(emp_2.__dict__)

# Instance refers from below class variable, unless if it is explicitly specified
# print(Employee.__dict__)

# I'm explicitly specifying the emp_1 instance to have a good raise amount
emp_1.raise_amount = 1.10
emp_1.apply_raise()
print(emp_1.pay)



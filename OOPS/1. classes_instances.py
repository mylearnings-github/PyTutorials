"""
    Classes and it's Instances
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

''' emp_1 & emp_2 are instances of Employee Class'''
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)



''' 1) Manual Steps below is easily replaced by __init__ method'''
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

''' init replacement '''
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

''' 2) Getting full name is manual, and it can be replaced by function '''
print(f'{emp_1.first} {emp_1.last}')

''' function replacement '''
print(emp_1.fullname())

''' alternative way - call method by class name '''
print(Employee.fullname(emp_1))
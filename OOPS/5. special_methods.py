"""
    Special Methods
    ---------------
    Some people call it Magic/Dunder methods

    Dunder - Nothing but 'Double Underscore' methods which helps developers
    1) __init__
    2) __repr__
    3) __str__
"""

class Employee:
    
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'                

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'
    
    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('New', 'Joiner', 10000)
emp_2 = Employee('New', 'Joiner2', 12000)

print(emp_1) 
# Run this print statement
# without __repr__ 
# with __repr__
# with __str___

'''
    Priority of execution:
    ----------------------
    1) str - good to have
    2) repr - must have
'''

# Alternative Ways to check:
print(repr(emp_1)) 
# or
print(emp_1.__repr__())

print(str(emp_1))
# or 
print(emp_1.__str__())

''' 
    Ever wondered when using '+' symbol, strings are concatenated, and numbers are evaluated?
'''

print(1 + 2)    # Returns 3
print('a'+'b')  # Returns ab

# Magic is again the dunder method (which works behind the scene)
print(int.__add__(1, 2))        # Returns 3
print(str.__add__('a', 'b'))    # Returns ab 


"""
    A strange requirement, but let's say if I add two employee objects, and expect it to give us a total pay of both?

    Yes, it's possible. Please refer dunder add implementation in Employee Class.
"""

# By default __add__ does not support addition of 2 employee objects, hence specified it as dunder add.
print(emp_1 + emp_2)


"""
    Do you know len() is also a dunder method?
"""
print('test'.__len__())
print(len(emp_1)) # Customized the dunder length method for employee use case, to get length of full name

"""
    Food for Thought:
    -----------------
    Real-life implementation of dunder method customization:
    1) In datetime.py module, to add two dates.
"""
"""
    Inheritance Demo
    ----------------
    Using Employee class which has Developer/Manager sub classes
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

class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # good way
        # or
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):    

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# Instantiate Parent/Sub Classes
emp_1 = Employee('New', 'Joiner', 10000)
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'C#')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])


# Validating Developer Class
print(dev_1.email)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(help(Developer))

# Validating Manager Class
print(mgr_1.email)
mgr_1.print_emp()
mgr_1.add_emp(dev_2)
mgr_1.add_emp(emp_1)
mgr_1.remove_emp(emp_1)

''' Additional Tips & Tricks '''
# 1. To validate if the given object is an instance of a given class
print(isinstance(mgr_1, Manager))   # Returns True
print(isinstance(mgr_1, Employee))  # Returns True
print(isinstance(mgr_1, Developer)) # Returns False

# 2. To validate if the given class is a subclass of the parent class specified
print(issubclass(Developer, Employee))  # Returns True
print(issubclass(Manager, Employee))    # Returns True
print(issubclass(Employee, Employee))   # Returns True
print(issubclass(Employee, Developer))  # Returns False

'''
    The sub-class impementation is found in standard 'exceptions.py' module
'''
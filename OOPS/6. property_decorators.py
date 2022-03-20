class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last        
        self.email = first + '.' + last + '@company.com'                

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('New', 'Joiner')

# It's fine up to here:
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

# The moment I update first name:
emp_1.first = 'Jim'
print(emp_1.fullname())     # Updated
print(emp_1.email)          # Not Updated, an issue. 

''' To overcome this issue, we have getter/setter just like other languages have '''
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last        
        #self.email = first + '.' + last + '@company.com'                
    
    @property # Add and remove this line to see the difference
    def email(self):
        return f'{self.first}.{self.last}@company.com'
        
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter # Sets the value for full name
    def fullname(self, name):
        first, last = name.split(' ') # Custom Logic
        self.first = first
        self.last = last

    @fullname.deleter # Deletes the value for full name
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('New', 'Joiner')

print(emp_1.email())    # This works now, it is updating email. 
print(emp_1.email)      # But this is what I really want, hence specified property
print(emp_1.fullname)

emp_1.fullname = 'Experienced Resource' # Can't set attribute error

# Validation
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
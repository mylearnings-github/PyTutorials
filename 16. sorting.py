"""
    Focus is to sort list, tuples, objects
"""

''' 1. Sort vs Sorted in List '''

from typing import List


li = [9,1,6,7,5,8,3,4,2]
s_li = sorted(li) # Returns Sorted List, does not change original
li.sort() # Sorts Original List, does not return
print('Sorted List : \t', s_li)
print('Original List : \t',li)

''' Sorted is a preferred method, as it works on other iterables like tuple '''

''' 2. Sorting Tuple '''

tup = (9,1,6,7,5,8,3,4,2)
s_tup = sorted(tup) # Returns sorted list of that tuple
print('Sorted Tuple : \t',s_tup)

''' 3. Sorting Dictionary '''

di = {'name': 'Corey', 'job':'programming', 'age': None, 'os':'Mac'}
s_di = sorted(di) # Returns sorted list of dictionary key
print('Original Dict : \t',di)
print('Sorted Dict : \t',s_di)

''' 4. Sorting Negative Values '''
li = [-1, -3, -2, -9, 0, 4, 5, 6, 2]
s_li = sorted(li)
print(s_li)

''' what if we have a requirement to sort absolute values from given negative list?
    absolute value of (-1) is 1, to check --> print(abs(-1))
    absolute value of (-5) is 5, to check --> print(abs(-5))
    i.e. a non-negative value
'''

li = [-1, -3, -9, 0, 4, 5, 6, 2, 3, 1]
s_li = sorted(li, key=abs)
print(s_li)


''' 5. Sorting a custom built class, real world example '''

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return f'({self.name}, {self.age}, {self.salary})'

e1 = Employee('Kirubha', 26, 1000000)
e2 = Employee('Pooja', 28, 1300000)
e3 = Employee('Ashwar', 26, 2500000)

employees = [e1, e2, e3]

# Way - 1 (creating custom function to get sort key based on our class structure)
def sort_key(emp):
    return emp.salary

s_employees = sorted(employees, key=sort_key, reverse=True)

# Way - 2 (using lambda functions)
s_employees = sorted(employees, key=lambda e: e.salary)

# Way - 3 (by importing attribute getter)
from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('salary'), reverse=True)

print(s_employees)

"""
Here we see problems between default arguments!
"""

""" 1. Example """
# Carefully see emp_list=[] argument to the add_employee function

def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

add_employee('Corey', emps)

''' It behaves different as it is not initializing to empty every time '''
add_employee('Kirups')
add_employee('Pooja')



"""
    [] is mutable
    None is immutable

    Below solution solves the issue!
"""
def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)



""" 2. Example """
import datetime as dt
import time

''' Wrong way '''
def display_time(time=dt.datetime.now()):    
    print(time.strftime('%B %d, %Y %H:%M:%S'))

''' Corrected way '''
def display_time(time=None):
    if time is None:
        time = dt.datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))

''' Validation '''
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
"""
    Use of functions:
    -----------------
    Allow us to reuse code w/o repeating ourself.
    In other words, it's about keeping code DRY (Don't Repeat Yourself)

    pass keyword - just to pass the function w/o any errors
"""

def hello_func():
    pass

def hello_func():
    print('Hello Function!')

def hello_func():
    return 'Hello Function!'

# Example of chaining functions:
print(hello_func().upper())

print(len('Test'))

# Functions with Arguments
def hello_func(greeting):
    return f'{greeting} Function'

# Functions with Default Arguments
def hello_func(greeting, name = 'You'):
    return f'{greeting}, {name}!'

hello_func('Hello')
hello_func('Hello','Corey')

# Arguments and Keyword arguments

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age= 22)

courses = ['Math','Art']
info = {'name':'John', 'age' : 22}

student_info(courses, info)
student_info(*courses, **info)


"""To understand function better, here is a quick demo program"""

# Number of days per month. First value placeholder for indexing purposes. 
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(days_in_month(2020, 2))
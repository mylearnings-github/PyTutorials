"""
    Different ways we call for loop in python
"""

courses = ['History', 'Math', 'Physics', 'CompSci']

# Way - 1
for course in courses:
    print(course)

# Way - 2 
for index, course in enumerate(courses):
    print(index, course)

# Way - 3
for index, course in enumerate(courses, start=1):
    print(index, course)
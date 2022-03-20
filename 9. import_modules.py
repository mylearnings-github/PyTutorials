courses = ['History', 'Math', 'Physics', 'CompSci']

# Way - 1
import modules.my_module as mm
index = mm.find_index(courses, 'Math')
print(index)


# Way - 2 [Common Way]
from modules.my_module import find_index, test
print(test)
index = find_index(courses, 'Physics')
print(index)


# Way - 3
from modules.my_module import *
print(test)
index = find_index(courses, 'Physics')
print(index)


# Where does python looks for modules to import, in general?
import sys
print(sys.path)

# Not a best way, but this adds modules folder to system path
sys.path.append('/modules')

"""Here are some examples of how to utilize standard libraries in python"""

# Example - 1

import random
random_course = random.choice(courses)
print(random_course)

# Example - 2

import math
rads = math.radians(90)
print(math.sin(rads))

# Example - 3

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2022))

# Example - 4

import os
print(os.getcwd())

"""To find location of any standard module on our file system"""

print(os.__file__)
print(datetime.__file__)
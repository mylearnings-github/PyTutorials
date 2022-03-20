""" 
    We will discuss about issues with Import here.
"""

filename = 'somefile.txt'

# Way - 1
import os
os.rename(filename)

# Way - 2
from os import rename
rename(filename)

# Way - 3 
""" 
    Importing asterisks is always a bad practice 
    Reason:
    -------
    1) Hard to debug
    2) Error prone
"""
from os import *
rename(filename)

# Error Prone - example:
''' both html & glob has escape() function '''
from html import *
from glob import *

print(help(escape))

# Right Ways - for the above example:
''' Way 1 '''
from html import escape as h_escape
from glob import escape as g_escape
print(help(h_escape))
print(help(g_escape))

''' Way 2 '''
import html
import glob
print(help(html.escape()))
print(help(glob.escape()))
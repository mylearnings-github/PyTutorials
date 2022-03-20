"""
    1. Try to keep module name different from standard library modules.
    2. Importing something in pip also has same type of error. 
    3. Variable name & function names has to be different.
"""

from math import radians, sin

rad = radians(90)
print(sin(rad))

radians = radians(90) #variable name equals to function name
print(sin(radians))

# We see this error
rad45 = radians(45)
print(rad45)
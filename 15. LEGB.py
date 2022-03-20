"""
    Sequence of Execution - LEGB:
    -----------------------------
    1) Local       : Variables defined within function, accessible only to it's function
    2) Enclosing   : Variables defined in an enclosing function
    3) Global      : Specific to module
    4) Built-in    : Pre-assigned in Python

"""

x = 'global x'

def test():    
    x = 'local x'
    print(x)

test()
print(x)


''' min is a Built-in Function '''

# To know the list of built-in variables/functions:
import builtins
print(dir(builtins))

# Sample use case of min function:
m = min([1,8,9,0,10])
print(m)

# Caution! - It will be overwritten, if you do so:
def min():
    pass

''' Let's discuss about Enclosing '''
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        # global x # affects globally
        # nonlocal x # affects enclosing function
        x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
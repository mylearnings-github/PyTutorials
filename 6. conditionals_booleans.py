"""
    Comparisions:
    -------------
    Equal:              ==
    Not Equal:          !=
    Greater Than:       >
    Less Than:          <
    Greater or Equal:   >=
    Less or Equal:      <=
    Object Identity:    is

    Boolean:
    --------
    and
    or
    not

    False Values:
    -------------
    False
    None
    Zero of any numeric type
    Any empty sequence. For example, '', (), [].
    Any empty mapping. For example, {}.

"""


# Conditionals

language = 'C#'

if language == 'Python':
    print('Language is Python')
elif language == 'C#':
    print('Language is C#')
else:
    print('No match')

# Boolean

user = 'Admin'
logged_in = False

if user =='Admin' and logged_in:
    print('Admin Page')
elif not logged_in:
    print('Please Log In')
elif logged_in or user =='Admin':
    print('Admin Page')
else:
    print('Bad Creds')

# is Comparison check Memory
a = [1,2,3]
b = [1,2,3] # Try,  b = a and see the id. 
print(a == b)
print(id(a))
print(id(b))
print(a is b) # or simply, print (id(a) == id(b))

# False Values:

condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

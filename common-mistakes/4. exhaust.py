"""
    Changes from Python2 --> Python3
"""

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = zip(names, heroes)

''' Works well in Python 2'''
print(identities)
# Py2 Sample Output: 
# [('Peter Parker', 'Spiderman'), ('Clark Kent', 'Superman'), ('Wade Wilson', 'Deadpool'), ('Bruce Wayne', 'Batman')]

''' To make it work in Python 3, need to write like this. 
    Reason: 
    -------
    Python 3 has got lot of generator like output, which helps to improve performance.
'''
for identity in identities:
    print(f'{identity[0]} is actually {identity[1]}!')

''' Generators are exhausive (values can be accessed only once), List is not! '''
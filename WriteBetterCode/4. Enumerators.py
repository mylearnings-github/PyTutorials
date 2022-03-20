
names = ['Corey', 'Chris', 'Dave', 'Travis']

# Syntax for loop over a list
for name in names:
    print(name)

# Syntax for loop over a list, with index
for index, name in enumerate(names):
    print(index, name)

# Syntax for loop over a list, with index and start value of index specified
for index, name in enumerate(names, start=1):
    print(index, name)
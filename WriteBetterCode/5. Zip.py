names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# Loop over 2 lists at once :
for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# A better way of doing this:
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

# Zip can also be used to merge more than 2 lists, something like this:
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

# We can also get is as tuple
for value in zip(names, heroes, universes):
    print(value)


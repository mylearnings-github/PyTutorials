class Person():
    pass

person = Person()

# We can dynamically assign to a class
person.first = 'Corey'
person.last = 'Schafer'

print(person.first)
print(person.last)

# Instead of assigning dynamically, you can make assignment like this
first_key = 'first'
first_val = 'Kirups'
setattr(person, first_key, first_val)
print(person.first)

first = getattr(person, first_key)
print(first)


''' Real case example, why setattr, getattr may be helpful '''

person_info = {'first': 'Corey', 'last': 'Schafer'} # given input format, a dictionary
person = Person() # expected output format

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))
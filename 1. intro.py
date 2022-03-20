"""
    1. len - length of chars in str
    2. count - count the occurrence of a word
    3. find - find the index of a word, if not found returns -1
    4. replace - find the occurrence of word, and replace with given word
    5. slice - get specific words by specifying start & end index [end index is not counted]
    6. format - placeholders, fString in 3.6 and above
    7. dir - get list of methods supported for the variable
    8. help - get details on how that list of methods can be utilized
    9. type - shows the type of variable
    
"""

greeting = 'Hello'
name = 'Kirubha'
#message = greeting+', '+name + '.Welcome!'

#message = '{}, {}. Welcome!'.format(greeting, name)

message = f'{greeting}, {name.upper()}. Welcome!'

print(dir(name))



print(message)
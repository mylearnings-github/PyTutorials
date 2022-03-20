
''' Tough to read this number - Is it a Million/Billion? '''
num1 = 100000000000
num2 = 100000000

''' 
    Trick - Underscore doesn't affect numbers 
    We can use it for readability
'''
num1 = 100_000_000_000 #100 Billion
num2 = 100_000_000 #100 Million

total = num1 + num2
print(total) # Total is not affected when underscore is present

print(f'{total:,}') # If I had to print it in comma separated form
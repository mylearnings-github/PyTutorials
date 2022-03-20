# Knowingly or unknowingly, we had unpacked a tuple 
''' Tuple Unpacking Example '''
a, b = (1,2)
print(a)
#print(b)

''' 
    After unpacking, if you're surely not going to use the variable 
    Better unpack it with an underscore
'''
a, _ = (1, 2)
print(a)

# Unpacking More values or Lesser values, leads to error
a, b, c = (1, 2) #ValueError: not enough values to unpack
a, b, c = (1, 2, 3, 4, 5) #ValueError: too many values to unpack

# If we have too many values, we can still unpack by using below trick:

a, b, *c = (1, 2, 3, 4, 5) # Club last few values into single variable
print(a, b, c)

a, b, *_ = (1, 2, 3, 4, 5) # Ignore the last few
print(a, b)

a, b, *c, d = (1, 2, 3, 4, 5) # a,b,d - will be filled first based on position, c - will get remaining values
print(a, b, c, d)

a, b, *_, d = (1, 2, 3, 4, 5) # a,b,d - will be filled first based on position, *_ - ignore remaining values
print(a, b, d)

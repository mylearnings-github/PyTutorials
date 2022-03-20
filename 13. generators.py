"""
    A generator is better in performance as it does not hold all the values in memory.    
"""


''' Understanding Generators '''
# Normal Way
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

# Using Generators
def square_numbers(nums):    
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])


''' Generators for list comprehensions '''

# List Comprehension
my_nums = [x*x for x in [1,2,3,4,5]]
print(my_nums)

# Using Generators
my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)

print(list(my_nums)) # Converting generator to list

''' Test your code '''
print(my_nums)

print(next(my_nums))

for num in my_nums:
    print(num)

''' Refer /Hands-On/generator_demo.py for a live demo '''
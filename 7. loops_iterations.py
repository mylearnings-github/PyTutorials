"""
    Loop Keywords:
    --------------
    break       - breaks loop
    continue    - skip to the next iteration

"""

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# Loop inside Loop:
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Definite time:
for i in range(1,11):
    print(i)

# While Loop - executes until certain condition is met

x = 0
while x < 10: # simply putting True means it's an infinite loop.
    if x == 5:
        break
    print(x)
    x += 1

# Caution! - Infinite Loop 
# Press Ctrl + C to terminate
x = 1
while True:
    print(x)
    x += 1

"""
    Key-Value pair
    Key can be string, int or any immutable data type
"""
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['name'] # Returns John
student['phone'] # Returns KeyError
student.get('phone') # Returns None
student.get('phone', 'Not Found') # Returns Not Found

student['phone'] = '555-5555' # Add Phone
student['name'] = 'Jane' # Update Name

# To update multiple things at a time
student.update({'name': 'Julie', 'age': 26, 'phone': '555-5566'})

# Delete
del student['age']
age = student.pop('age') # returns what's removed

# List all Key values
student.keys()
student.values()
student.items()

# Loop through Dict:

# Way - 1:
for key in student:
    print(key)

# Way - 2:
for key, value in student.items():
    print(key, value)
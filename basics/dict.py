# Dictionaries are datastructures store data in key value pairs
student = {
    'name': 'Mohit Gajjar',
    'age': 23,
    'courses': ['Maths', 'Science', 'Computer Science', 'History']
}

# Printing specific values from the dictionary using the key
print(student['name'])

# to get None or default values in the dict
print(student.get('courses', 'Not found'))
print(student.get('phone', 'Not found'))

# adding more key values in a dict
student['phone'] = "1231231230"
print(student.get('phone', 'Not found'))


# updating the values of a specific key
student.update({'name': 'Mohit Rameshbhai Gajjar'})
print(student['name'])

# deleting the keys and its values
del student['phone']
age = student.pop('age')
print(student)
print(age)

# looping through values in a dictionary
print(len(student))
print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, value)
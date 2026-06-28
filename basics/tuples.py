# we cannot modify tuples but we can modify the tuples

# Mutable
courses = [
    "History", 
    "Maths",
    "Computer science",
    "Physics"
]

courses1 = courses

# This changes index zero element to art, because it is same mutable objects.
courses[0] = 'Art'

print(courses)
print(courses1)


# Immutable
courses_tuple = (
    "History", 
    "Maths",
    "Computer science",
    "Physics"
)

courses_tuple1 = courses_tuple

# it will throw error "TypeError: 'tuple' object does not support item assignment"
courses_tuple[0] = 'Art'

print(courses_tuple)
print(courses_tuple1)
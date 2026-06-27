# Sets removes duplicates, they change order with each execution, they are optimised for membership functions, like finding the element in the set
courses = {
    "Maths",
    "History", 
    "Physics",
    "Computer science",
    "Physics"
}

print(courses)

print("Physics" in courses)


art_courses = {
    "Maths",
    "History", 
    "Physics",
    "Design"
}

# printing the comon elements in 2 sets
print(courses.intersection(art_courses))

# prints the uncommon element from courses
print(courses.difference(art_courses))

# prints the uncommon element from art courses
print(art_courses.difference(courses))

# This isnt empty set it's dictionary
empty_set = {} 
print(type(empty_set))

# This it empty set

empty_set = set()
print(type(empty_set))


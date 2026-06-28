courses = [
    "History", 
    "Maths",
    "Computer science",
    "Physics"
]

# prints entire course list
print(courses)

# prints length of list
print(len(courses))

# prints element of that index
print(courses[2])

# prints the element from starting back of the list
print(courses[-1])

# prints the elements starting from index 0 to but including 2
print(courses[0:2])
print(courses[:2])

# prints the elements starting from index 2 to the last
print(courses[2:])

# adding item to the list
courses.append("Art")
print(courses)

# adding the element at the specific location
courses.insert(3, "Politics")

extracurricular = ["Photography", "Sports"]

# adds entire list variable into 2nd position instead of the each element
courses.insert(2, extracurricular)
print(courses)
print(courses[2])

# deleting the element by specifying the element to the list
courses.remove(extracurricular)

# adding multiple values to a existing
courses.extend(extracurricular)
print(courses)

# Remove and return item at index (default last).
popped = courses.pop(3)
print(popped)

# reversing the list
courses.reverse()
print(courses)

# sorting the list
number_list = [2,5,3,4,1,6,7,9,0,8]

number_list.sort()
print(number_list)

# given string it sorts in accending order
courses.sort()
print(courses)

# reversing the sort
courses.sort(reverse=True)
print(courses)

number_list.sort()
print(number_list)

# returns the new sorted list keeping the orignal list as it is
sorted_courses = sorted(courses)
sorted_numbers = sorted(number_list)
print(sorted_courses)
print(sorted_numbers)

# min, max, sum
print(min(number_list))
print(max(number_list))
print(sum(number_list))

# finding values of elements, and indexes

# prints the index of the element passed
print(courses.index('Physics'))

# checking the element is in the list and at what index

print('Math' in courses)
print('Maths' in courses)


# for loop, prints all the elements in the list
for item in courses:
    print(item)

# accessing the index and elements 
for index, course in enumerate(courses):
    print(index, course)
    
for index, course in enumerate(courses, start=1):
    print(index, course)

# return a string from list
course_str = ' ,'.join(courses)
print(course_str)

course_str = '-'.join(courses)
print(course_str)

# getting the course back with courses list from string
new_list = course_str.split('-')
print(new_list)
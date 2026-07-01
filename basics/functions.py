# declaring function only without statements, to be used it later
def hello():
    pass

# executing the function
hello()

# function itself
print(hello)

def hello():
    print("Hello Mohit")
    return "Hello Mohit"

print(hello().upper())


def who_is_good(name):
    return f'{name} is good'

print(who_is_good("Mohit Gajjar"))


# unpack a tuple and dictionary and pass those to the function arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Maths', 'Science', 'Art']
info = {'name': 'Mohit Gajjar', 'age': 23}

student_info(*courses, **info)
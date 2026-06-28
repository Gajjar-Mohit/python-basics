if True:
    print("This will always run")

if False:
    print("This will never run")

lang = 'Typescript'
if lang == 'Python':
    print("Yes, this is python")
else:
    print("Lang is not python")


if lang == 'Python':
    print("Yes, this is python")
elif lang == "Typescript":
    print("Lang is not python, it's Typescipt")


user = "User"
logged_in = True

if user == "Admin" and logged_in:
    print('Admin logged in')
else:
    print('Access Denied')


if not logged_in:
    print("Please login first")
else:
    print("Welcome")


# Object indentity, checks the object if they has same id, same object in memory
a = [1,2,3]
b = [1,2,3]

print(a == b)
# It returns false becauase there are two saperate objects in the memory
print(a is b)
print(id(a))
print(id(b))

b = a
print(a is b)
print(id(a))
print(id(b))


condition = 0
condition1 = 20

if condition:
    print('Condition true')
else:
    print('Condition is false')

if condition1:
    print('Condition true')
else:
    print('Condition is false')


condition = [1,2]
condition1 = {}

if condition:
    print('Condition true')
else:
    print('Condition is false')

if condition1:
    print('Condition true')
else:
    print('Condition is false')

message = "Hello, World!"

#starting with 0 and ending at index 3 (not including index 3)
print(message[0:3])

#will print same as above since starting index is 0
print(message[:3]) 

# starting from index 7 to the end of the string
print(message[7:])

# uppercase the string
print(message.upper())

# lowercase the string
print(message.lower())

# counts the number of times "o" appears in the string
print(message.count("o")) 

# counts the number of times "l" appears in the string from index 0 to 5
print(message.count("l", 0, 5)) 

# returns the index of the first occurrence of "World" in the string
print(message.find("World"))

print(message.find("Python")) # returns -1 since "Python" is not in the string
print(message.find("World")) # returns 7 since "World" starts at index 7

# replaces "World" with "Python" in the string
print(message.replace("World", "Python")) 


greeting = 'Hello'
name = 'Mohit'

# concatenates the strings
message = greeting + ', ' + name + '!' 

# prints "Hello, Mohit!"
print(message) 

# using f-string for string formatting
message = f"{greeting}, {name}!" 

# prints "Hello, Mohit!"
print(message) 

# prints all the methods available to that name variable
print(dir(name))

# prints all the information of the methods do
print(help(str))